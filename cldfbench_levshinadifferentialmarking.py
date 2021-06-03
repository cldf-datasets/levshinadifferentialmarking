import pathlib
import collections

from pybtex.database import parse_string
from clldutils.misc import slug
from cldfbench import Dataset as BaseDataset, CLDFSpec

CODES = {
    'Marking_Type': {
        'none': None,
        'differential': None,
        'stable overt': None,
    },
    'Local_or_Global': {
        'local': 'the use or omission of the marker depends only on the properties of the argument itself',
        'global': 'the use of the marker also or solely depends on the properties of the other argument.',
    },
    'Marking_Contrast': {
        'zero_nonzero': 'when differential marking in a given language is privative, i.e. there is zero expression vs. non-zero (audible) expression',
        'marker_length': 'when the differential marking pertains to different markers rather than zero expression vs. non-zero expression',
        'stem_length': 'when the case forms differ in stem length (e.g. as in Ik)',
    },
    'Split_or_Fluid': {
        'split': 'when Marking_Probability is >90%/<10%',
        'fluid': 'when Marking_Probability is >50%, 50%, <50%, <, or >',
        'split-fluid': 'when both split and fluid marking occurs in a given language',
    },
    'TAM_DM': {'yes': None, 'no': None},
    'WO_DM': {'yes': None, 'no': None},
    'Other_DM': {'yes': None, 'no': None},
}


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "levshinadifferentialmarking"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(module='StructureDataset', dir=self.cldf_dir)

    def cmd_download(self, args):
        pass

    def _read(self, what):
        return [
            {k.strip(): v.strip() for k, v in d.items()} for d in
            self.raw_dir.read_csv('{}.txt'.format(what), dicts=True, delimiter='\t')]

    def cmd_makecldf(self, args):
        legend = {(r['Spreadsheet'], r['Column']): r['Meaning'] for r in self._read('Legend')}
        notes = '\n'.join([k[0] for k in legend if k[0].startswith('Note')])

        cldf = args.writer.cldf
        cldf.add_component('LanguageTable')
        cldf.add_component(
            'ExampleTable',
            {
                'name': 'Source',
                'separator': ';',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#source',
            }
        )
        t = cldf.add_component(
            'ParameterTable',
            {
                'name': 'Argument',
                'datatype': {'base': 'string', 'format': 'A|P'},
                'dc:description': 'A (role that expresses the prototypical Agent) or P '
                                  '(grammatical role that expresses the prototypical Patient)'
            }
        )
        cldf.add_columns(
            'ValueTable',
            'Usages',
            {
                'name': 'Type',
                'dc:description': 'For values of the "* Marker" parameter: {}'.format(
                    legend['Markers', 'Type']),
            },
            {
                'name': 'Condition',
                'dc:description': 'For values of the "* Marker" parameter: {}'.format(
                    legend['Markers', 'Condition']),
            },
            {
                'name': 'Examples',
                'separator': ';',
                'dc:description': 'For values of the "* Marker" parameter: {}'.format(
                    'Links to examples of usages of the marker'),
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#exampleReference',
            },
        )
        cldf['ValueTable', 'Value'].null = ['NotApplicable']
        cldf.add_component('CodeTable')
        t = cldf.add_table(
            'usages.csv',
            'ID',
            'Marker_ID',
            {
                'name': 'TAM_Conditions',
                'separator': ' ; ',
                'dc:description': legend['Usages', 'TAM_Conditions'],
            },
            {
                'name': 'WordOrder_Conditions',
                'separator': ' ; ',
                'dc:description': legend['Usages', 'WordOrder_Conditions'],
            },
            {
                'name': 'Other_Conditions',
                'separator': ' ; ',
                'dc:description': legend['Usages', 'Other_Conditions'],
            },
            {
                'name': 'Host',
                'separator': ' ; ',
                'dc:description': legend['Usages', 'Host'],
            },
            {
                'name': 'Marking_Probability',
                'dc:description': legend['Usages', 'Marking_Probability'],
            },
            {
                'name': 'Examples',
                'separator': ';',
                'dc:description': 'Links to examples of this usage of a marker',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#exampleReference',
            },
        )
        t.tableSchema.primaryKey = ['ID']
        cldf.add_foreign_key('usages.csv', 'Marker_ID', 'ValueTable', 'ID')
        t.common_props['dc:description'] = "Usage restrictions for markers"
        # t = cldf.add_table(
        #    'conditions.csv',
        #    'ID',
        #    'Type',
        #    'Name',
        # )
        # t.tableSchema.primaryKey = ['ID']

        sources = parse_string(self.raw_dir.read('Bibliography.bib'), 'bibtex')
        args.writer.cldf.add_sources(sources)

        for arg in ['A', 'P']:
            for (sheet, col), desc in legend.items():
                if col.endswith('Scale'):
                    desc += '\n\n' + notes
                    CODES[col] = dict(fit=None, viol=None, none=None)
                if sheet == 'Languages' and (col not in ['Language', 'Argument']):
                    args.writer.objects['ParameterTable'].append(dict(
                        ID='{}_{}'.format(arg, col),
                        Name='{} {}'.format(arg, col.replace('_', ' ')),
                        Description=desc,
                        Argument=arg,
                    ))
                if col in CODES:
                    for code, desc in CODES[col].items():
                        args.writer.objects['CodeTable'].append(dict(
                            ID='{}_{}-{}'.format(arg, col, slug(code)),
                            Parameter_ID='{}_{}'.format(arg, col),
                            Name=code,
                            Description=desc,
                        ))
            col = 'Marker'
            args.writer.objects['ParameterTable'].append(dict(
                ID='{}_{}'.format(arg, col),
                Name='{} {}'.format(arg, col.replace('_', ' ')),
                Argument=arg,
            ))

        lang_map = {r['ISO']: r['Name'] for r in self.etc_dir.read_csv('languages.csv', dicts=True)}
        for glang in args.glottolog.api.languoids():
            if glang.iso in lang_map:
                args.writer.objects['LanguageTable'].append(dict(
                    ID=glang.iso,
                    Name=lang_map[glang.iso],
                    Glottocode=glang.id,
                    Latitude=glang.latitude,
                    Longitude=glang.longitude,
                    Macroarea=glang.macroareas[0].name,
                    ISO639P3code=glang.iso,
                ))
        lang_map = {v: k for k, v in lang_map.items()}
        for lang in self._read('Languages'):
            assert lang['Language'] in lang_map
            for k, v in lang.items():
                if k == 'Local_or_global':
                    k = 'Local_or_Global'
                if k not in ['Language', 'Argument']:
                    val = None if v == 'NotApplicable' else v
                    assert val != ''
                    pid = '{}_{}'.format(lang['Argument'], k)
                    lid = lang_map[lang['Language']]
                    for i, vval in enumerate(val.split(';') if val else [val], start=1):
                        vval = vval.strip() if vval else vval
                        args.writer.objects['ValueTable'].append(dict(
                            ID='{}-{}-{}'.format(lid, pid, i),
                            Language_ID=lid,
                            Parameter_ID=pid,
                            Value=vval,
                            Code_ID='{}-{}'.format(pid, slug(vval)) if k in CODES and vval else None,
                        ))

        markers = self._read('Markers')
        for m in markers:
            if m['Marker_ID'].startswith('grj'):
                m['Marker_ID'] = m['Marker_ID'].replace('grj', 'gjr')

        m2l = {r['Marker_ID']: lang_map[r['Language']] for r in markers}
        # FIXME: Example_ID is many! -> separator = '; '
        e2m = {}
        conditions = collections.defaultdict(set)
        for i, r in enumerate(self._read('Usages'), start=1):
            eids = []
            for eid in r['Example_ID'].split('; '):
                if eid != 'NotAvailable':
                    e2m[eid] = r['Marker_ID']
                    eids.append(eid)
            kw = dict(ID=str(i), Marker_ID=r['Marker_ID'], Examples=eids, Marking_Probability=r['Marking_Probability'])
            for k in ['TAM_Conditions', 'WordOrder_Conditions', 'Other_Conditions', 'Host']:
                v = r[k]
                if v == 'all':
                    v = []
                else:
                    v = [vv.strip() for vv in v.split(';')]
                conditions[k] = conditions[k].union(v)
                kw[k] = v
            args.writer.objects['usages.csv'].append(kw)
        e2l = {k: m2l[v] for k, v in e2m.items()}
        e2s = {}

        # i = 0
        # for k, v in sorted(conditions.items()):
        #    for vv in sorted(v):
        #        i += 1
        #        args.writer.objects['conditions.csv'].append(dict(ID=str(i), Type=k, Name=vv))

        for r in self._read('Examples'):
            e2s[r['Example_ID']] = '{}[{}]'.format(r['Reference_ID'], r['Page'])
            args.writer.objects['ExampleTable'].append(dict(
                ID=r['Example_ID'],
                Language_ID=e2l[r['Example_ID']],
                Primary_Text=r['SourceText'],
                Analyzed_Word=r['SourceText'].split(),
                Gloss=r['Gloss'].split(),
                Translated_Text=r['Translation'],
                Comment=r['Glossing_Comments'],
                Source=['{}[{}]'.format(r['Reference_ID'], r['Page'])],
            ))

        for marker in markers:
            eids = [k for k, v in e2m.items() if v == marker['Marker_ID']]
            args.writer.objects['ValueTable'].append(dict(
                ID=marker['Marker_ID'],
                Language_ID=lang_map[marker['Language']],
                Parameter_ID='{}_Marker'.format(marker['Argument']),
                Value=marker['Form'],
                Type=marker['Type'],
                Condition=marker['Condition'],
                Examples=eids,
                Source=[e2s[eid] for eid in eids],
            ))
