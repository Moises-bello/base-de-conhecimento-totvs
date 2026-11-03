---
content_hash: 82fc844e045b354313042437d4c2990eabce8052a6a3238f9768950855e3a2e5
fetched_at: '2026-06-29T00:11:44.145666+00:00'
page_id: '80971006'
product: rm
source: tdn-rm
title: RMBIB00001_Importação MARC 21
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=80971006
version: 6
---

O padrão MARC21 é um formato para o intercâmbio de registros bibliográficos e catalográficos e serve de base para a definição de formatos de entrada entre as instituições que o utilizam. O processo de importação MARC21 tem o objetivo de realizar a importação  de dados bibliográficos neste formato.

É preciso informar qual será o delimitador de subcampos, o tipo de publicação, grupo de publicação e escrever/colar as informações do acervo a ser importada. Após esta etapa o assistente irá validar e informar quais as tags conhecidas e não reconhecidas pelo sistema. Ao final da execução do processo a publicação será importada para acervo da biblioteca.

Segue a relação de tags contempladas pelo TOTVS Gestão Bibliotecária:

|  |  |  |  |
| --- | --- | --- | --- |
| **Formato Marc 21** | | | |
| **Relação de tags contempladas pelo RM Biblios** | | | |
| **Tag** | **Descrição** | **Repetível?** | **Obervação** |
| 005 | Data e hora da última operação | Não |  |
| 008 | Informações gerais | Não |  |
| 020 | ISBN | Sim | Utilizada somente para livros |
| 022 | ISSN | Sim | Utilizada somente para publicações seriadas (periódicos) |
| 035 | Número de controle do sistema | Sim |  |
| 040 | Fonte de catalogação | Não |  |
| 041 | Código do idioma | Sim |  |
| 080 | Número CDU | Sim | Utilizada quando o tipo de classificação for CDU |
| 082 | Número CDD | Sim | Utilizada quando o tipo de classificação for CDD |
| 084 | Outros número de classificação | Sim | Utilizada para tipos de classificação diferentes de CDD e CDU |
| 090 | Número de chamada local | Não |  |
| 100 | Entrada principal - Nome pessoal | Não |  |
| 110 | Entrada principal - Entidade coletiva | Não |  |
| 130 | Título uniforme | Não |  |
| 240 | Título uniforme | Não |  |
| 245 | Título principal da obra | Não |  |
| 246 | Formas variantes do título | Sim | Utilizada quando a publicação tiver título equivalente cadastrado |
| 250 | Edição | Não |  |
| 256 | Características do arquivo de computador | Não | Utilizada para publicações do tipo arquivo digital |
| 260 | Publicação, distribuição, etc. | Sim |  |
| 300 | Descrição física | Sim |  |
| 310 | Última periodicidade | Não | Utilizada somente para publicações seriadas (periódicos) |
| 326 | Datas de publicação e/ou designação sequencial | Sim | Utilizada somente para publicações seriadas (periódicos) |
| 500 | Notas gerais | Sim |  |
| 502 | Notas de dissertação ou tese | Sim |  |
| 504 | Notas de bibliografia | Sim |  |
| 505 | Notas de conteúdo | Sim |  |
| 520 | Nota de resumo | Sim |  |
| 440 | Título de série | Sim |  |
| 650 | Assunto | Sim |  |
| 700 | Entrada secundária - Nome pessoal | Sim |  |
| 710 | Entrada secundária - Entidade coletiva | Sim |  |
| 856 | Localização e acesso eletrônico | Sim | Utilizada para publicações do tipo arquivo digital |
|  | | | |
| Informações: | | | |
| 1 - A coluna repetível indica que A tag pode aparecer mais de uma vez no registro MARC. | | | |
| 2 - A tag 008 é utilizada para fornecer informações gerais codificadas sobre o registro como um todo. Este campo compreende 40 posições, não contém indicadores e subcampos. | | | |
| 3 - A tag 005 também não contém indicadores e subcampos. | | | |
| 4 - O registro líder (LDR) não será exibido na visualização | | | |
| 5 - A importação tratará as tags a partir da 020, dessa forma, as demais serão ignoradas e não poderão contar como tags inválidas | | | |
