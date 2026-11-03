---
content_hash: 8c3e6c337bae2df2fab39a129d1722539017cb5c257e39d9154bf1d6581595e9
fetched_at: '2026-06-29T00:09:34.677645+00:00'
page_id: '425459218'
product: rm
source: tdn-rm
title: Importação padrão MARC21
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459218
version: 12
---

Este processo permite a importação de registros bibliográficos e catalográficos via padrão MARC21.

Segue a relação de tags contempladas pelo TOTVS Gestão Bibliotecária:

|  |  |  |  |
| --- | --- | --- | --- |
| **Tag** | **Descrição** | **Repetível?** | **Obervação** |
| 005 | Data e hora da última operação | Não |  |
| 008 | Informações gerais | Não |  |
| 020 | ISBN | Sim | Utilizada somente para livros |
| 022 | ISSN | Sim | Utilizada somente para publicações seriadas (periódicos) |
| 035 | Número de controle do sistema | Sim |  |
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

**Informações**  
   
**1 -** A coluna repetível indica que a tag pode aparecer mais de uma vez no registro MARC.  
**2** - A TAG 008 é utilizada para fornecer informações gerais codificadas sobre o registro como um todo. Este campo compreende 40 posições, não contém indicadores e subcampos.  
**3 -** A TAG 005 também não contém indicadores e subcampos.  
**4 -** O registro líder (LDR) não será exibido na visualização.  
**5 -** A importação tratará as tags a partir da 020, dessa forma, as demais serão ignoradas e não poderão contar como tags inválidas.

**Informações Complementares**

Relação de valores para os indicadores das tags

Relação de subcampos e seus valores

**Observação**

Nas tags 100 e 650 (correspondentes aos itens de autores e assuntos), o separador padrão de texto é o hífen (-). Por esse motivo, no texto de importação de autores e assuntos, **NÃO** **deve ser utilizado hifens (-)**, pois o sistema irá tratar como um separador. Sugerimos nesse caso, o uso da barra oblíqua (/).
