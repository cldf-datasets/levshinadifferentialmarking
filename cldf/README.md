<a name="ds-structuredatasetmetadatajson"> </a>

# StructureDataset Cross-linguistic differential and optional marking database

**CLDF Metadata**: [StructureDataset-metadata.json](./StructureDataset-metadata.json)

**Sources**: [sources.bib](./sources.bib)

This database contains information about differential and optional marking of A and P, including individual case markers and diverse conditions for their usage. It also shows whether a particular language fits or violates different referential scales, as far as the use of markers is concerned. Both global and local marking patterns are included.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF StructureDataset](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/cldf-datasets/levshinadifferentialmarking
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/cldf-datasets/levshinadifferentialmarking/tree/07a260a">cldf-datasets/levshinadifferentialmarking 07a260a</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.4">Glottolog v4.4</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.5</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | levshinadifferentialmarking
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-valuescsv"></a>Table [values.csv](./values.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable)
[dc:extent](http://purl.org/dc/terms/extent) | 683


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) | `string` | References [codes.csv::ID](#table-codescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Usages` | `string` | 
`Type` | `string` | For values of the "* Marker" parameter: Type of marker (suffix, prefix, enclitic, proclitic, preposition or adposition)
`Condition` | `string` | For values of the "* Marker" parameter: Conditions when the marker can be used potentially (phonology, nominal number, etc.)
[Examples](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) | list of `string` (separated by `;`) | For values of the "* Marker" parameter: Links to examples of usages of the marker<br>References [examples.csv::ID](#table-examplescsv)

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 27


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 96


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | 
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | 
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | 
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | 
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 24


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
`Argument` | `string` | A (role that expresses the prototypical Agent) or P (grammatical role that expresses the prototypical Patient)

## <a name="table-codescsv"></a>Table [codes.csv](./codes.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF CodeTable](http://cldf.clld.org/v1.0/terms.rdf#CodeTable)
[dc:extent](http://purl.org/dc/terms/extent) | 58


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 

## <a name="table-usagescsv"></a>Table [usages.csv](./usages.csv)

Usage restrictions for markers

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 220


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`ID` | `string` | Primary key
`Marker_ID` | `string` | References [values.csv::ID](#table-valuescsv)
`TAM_Conditions` | list of `string` (separated by ` ; `) | IMPER = imperative; NONFIN = embedded non-finite clause; MAIN = main clause; SUB = subordinate clause; CON = conditional; FUT = future tense; CONT = continuative aspect; EPISTEMIC = epistemic modality; DEONTIC = deontic modality; SEQ = sequential clause
`WordOrder_Conditions` | list of `string` (separated by ` ; `) | SOV, SVO, etc.; LR_DISLOCATION = left/right dislocation;
`Other_Conditions` | list of `string` (separated by ` ; `) | Other conditions that influence the (dis)use of markers, e.g. fast speech; SUBJ = grammatical subject; OBJ = grammatical object; TYPICAL_SCENARIO = a typical configuration of A, P and verb, e.g. a dog bites a man; NO_TYPICAL_SCENARIO =lack of a typical configuration; OTHER_HIGHER = the other argument is higher on the prominence scales; OTHER_LOWER = the other argument is lower on the prominence scales.  See other abbreviations in the column Host.
`Host` | list of `string` (separated by ` ; `) | ALL = all nominals; PRON = pronoun; DEM = demonstrative; PROPER = proper noun; KIN = kinship term; HUMAN = human noun; SPEC = specific; ANIMAL = animal noun; NOUN = common noun; DEF = definite; INDEF = indefinite; 1P = 1st person; 2P = 2nd person; 3P = 3rd person; PROX = proximate (e.g. 3rd person); EMPH = emphatic; NONEMPH: non-emphatic; LIGHT_VERB = light verb as the head; FOCUS = focus; NONFOCUS = not focus; BABY  = baby; NONBABY = not baby; ADJACENT = adjacent to the verb; NONADJACENT = not adjacent to the verb; LIGHT = syntactically and/or morphologically 'light'; HEAVY = syntactically and/or morphologically 'heavy'; ANIMATE = animate; INANIMATE = inanimate; ANTHROPOMORPH = anthropomorphic (human-like, e.g. animals in a story or mythological beings); PROMINENT = prominent in the narrative; AFFECTED = affected by the action expressed by the verb; DAYS_WEEK = days of the week; INSTITUTION = institution;  POSS = possessive; REFL = reflexive; +REL = modified by relative clause; -REL = not modified by relative clause, PARTITIVE = partitive constructions (e.g. 'two of the girls'); PREDICTABLE_VERB = predictable from the verb
`Marking_Probability` | `string` | >90% = always or nearly always marked; >50% = more frequently marked than unmarked; <50% = less frequently marked than unmarked; 50% = optionally marked, or no precise information about any biases; ">" = more frequently marked than in other situations, "<" = less frequently marked than in other situations
[Examples](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) | list of `string` (separated by `;`) | Links to examples of this usage of a marker<br>References [examples.csv::ID](#table-examplescsv)

