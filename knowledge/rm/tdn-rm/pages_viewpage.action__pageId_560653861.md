---
content_hash: 2d80419efe2b7cfc0a77b3b6b4d50e426db6ea2f8e26cec0b3f1ad372db73d15
fetched_at: '2026-06-29T00:10:47.794701+00:00'
page_id: '560653861'
product: rm
source: tdn-rm
title: Deduções legais da base de cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560653861
version: 11
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| deducoes | [rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143227) | G | 0-1 | Tag raiz que agrupará as deduções do documento. |  |  |
| desccond | deducoes | E | 1-1 | Valor do desconto condicional do documento. | TMOV.VALORDESCCONDICIONAL |  |
| descincond | deducoes | E | 1-1 | Valor do desconto incondicional do documento. | TMOV.VALORDESC |  |
| deducao | deducoes | G | 0-N | Tag raiz que conterá as informações sobre uma dedução do documento. |  | Será gerado se o tipo de Movimento estiver parametrizado para utilizar Dedução por item e se o valor estiver preenchido no movimento ou se percentual estiver preenchido no item de movimento |
| tipo | deducao | E | 1-1 | Tipo de dedução. Os conteúdos possíveis são: •  1 – Por percentual; •  2 – Por valor. |  | Gerado conforme a parametrização do Tipo de Movimento |
| modal | deducao | E | 1-1 | Modalidade da dedução. Os conteúdos possíveis são: •  1 – Despesas com materiais; •  2 – Despesas com sub-empreitada. |  | Quando for utilizado dedução como percentual, será gerado sempre com valor 1 Quando for utilizado o valor de dedução, será gerado conforme o preenchimento do Movimento (Campo Materiais ou Sub Empreitada) |
| codobra | deducao | E | 0-1 | Código da obra da dedução. |  | Não será Gerado |
| codart | deducao | E | 0-1 | Código ART relacionado a dedução. |  | Não será Gerado |
| cpfcnpj | deducao | E | 0-1 | CPF/CNPJ do fornecedor/prestador do serviço. |  | Não será Gerado |
| numeronf | deducao | E | 0-1 | Número da nota fiscal de referência. |  | Não será Gerado |
| totalnf | deducao | E | 1-1 | Valor total da nota fiscal de referência. |  | Não será Gerado |
| percentual | deducao | E | 1-1 | Percentual a ser deduzido. |  | Percentual de dedução preenchido no Item do Movimento (TITMMOV.PERCENTUALDEDUCAO)  [Saiba Mais](https://tdn.totvs.com/pages/viewpage.action?pageId=593743223) |
| valor | deducao | E | 1-1 | Valor a ser deduzido. |  | Quando o parâmetro estiver "Por Valor" ou "Ambos" e o valor da dedução estiver preenchido no campo referente ao valor da Sub Empreitada ou do Material então será preenchido com este valor  Quando o parâmetro estiver "Por Percentual" ou "Ambos" e o percentual estiver preenchido no Item do Movimento, será calculado com o **valor do Item do movimento \* percentual de dedução**  [Saiba Mais](https://tdn.totvs.com/pages/viewpage.action?pageId=593743223) |
| deducaopor | deducao | E | 0-1 | Dedução por:  Valor Percentual |  | Não será Gerado |
| tipodeducao | deducao | E | 0-1 | Tipo Dedução:  Despesas com Materiais Despesas com Subempreitada Despesas com Mercadorias Servicos de Veiculacao e Divulgacao Servicos Mapa de Const. Civil |  | Não será Gerado |
| cpfcnpjreferencia | deducao | E | 0-1 | CNPJ/CPF referencia |  | Não será Gerado |
| numeronfreferencia | deducao | E | 0-1 | Número NF referencia |  | Não será Gerado |
| valortotalreferencia | deducao | E | 0-1 | Valor total referencia |  | Não será Gerado |
| percentualdeduzir | deducao | E | 0-1 | Percentual deduzir. |  | Não será Gerado |
| valordeduzir | deducao | E | 0-1 | Valor deduzir. |  | Não será Gerado |
| documentos | deducao | E | 0-1 |  |  |  |

Campo Dedução por Material ou Sub Empreitada
