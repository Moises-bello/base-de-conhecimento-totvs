---
article_id: 20530323713303
category: Materiais - Compras (SIGACOM)
content_hash: 4353e60c772e7df5b62b877b4444d455506b6214d3fa0a5a489131adbfb9647e
fetched_at: '2026-06-28T22:41:24.210633+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais são os principais
  parâmetros na rotina do Importador XML ?
type: support-article
updated_at: '2024-06-11T18:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20530323713303-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-s%C3%A3o-os-principais-par%C3%A2metros-na-rotina-do-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20530314019863) Tempo aproximado para leitura: **00h10 min****Dúvida**Quais são os principais parâmetros na rotina do Importador XML ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Tipo** | **Descrição** | **Observação** |
| MV\_IMPXML | Logico | Indica se utiliza Importador XML |  |
| MV\_XMLCFPC | Caracter | Identifica os CFOPs de venda que serão tratados como bonificação na importação dos XML de NFe. | No caso de necessidade de informar mais de 1 CFOP, separe-os com o caractere barra a direita "/". |
| MV\_XMLCFBN | Caracter | Identifica os CFOPs de venda que serão tratados como beneficiamento na importação dos XML de NFe. | No caso de necessidade de informar mais de 1 CFOP, separe-os com o caractere barra a direita "/". |
| MV\_XMLCFDV | Caracter | Identifica os CFOPs de venda que serão tratados como devolução na importação dos XML de NFe. | No caso de necessidade de informar mais de 1 CFOP, separe-os com o caractere barra a direita "/". |
| MV\_XMLCFND | Caracter | Indica os CFOPS de retorno de Beneficiamento quando o parâmetro MV\_PCNFE = .T. | No caso de necessidade de informar mais de 1 CFOP, separe-os com o caractere barra a direita "/". |
| MV\_XMLCFNO | Caracter | Identifica os CFOP's de retorno de Beneficiamento para entrada com tipo N = Normal no documento. | No caso de necessidade de informar mais de 1 CFOP, separe-os com o caractere barra a direita "/". |
| MV\_CTECLAS | Logico | Define se o Importador XML deve gerar a nota de CT-e já classificada quando o sistema estiver configurado para geração automática de notas. | . |
| MV\_XMLPFCT | Caracter | Identifica o código do produto de frete que será utilizado na geração de documentos de transporte via Importador XML |  |
| MV\_XMLTECT | Caracter | Identifica o tipo de entrada que deve ser utilizado para geração de documentos de transporte via Importador XML. |  |
| MV\_XMLCPCT | Caracter | Identifica o código de condição de pagamento que será utilizada na geração de documentos de transporte via Importador XML. |  |
| MV\_DIVIZER | Logico | Indica se zera a alíquota de imposto quando o valor do imposto for zero na analise de divergências fiscais. |  |
| MV\_COMCOL1 | Numerico | Indica como será processada a geração automática de documentos do Importador XML (0=Não Gera; 1=A Classificar; 2=Classificado). |  |
| MV\_COMCOL2 | Caracter | Indica para quais documentos Importador XML será processada a geração automática (N=Compra; D=Devol.; C=Complemento; O=Bonificação; T=CTe; B=Beneficia.) |  |
| MV\_COMCOL3 | Logico | Indica se devera atualizar a database na geração  da nota fiscal | Valor default .T. |
| MV\_MSGCOL | Numerico | Número máximo de XML’s que podem estar contidos em um e-mail do Importador XML. |  |
| MV\_TCNEW | Caracter | Tipos de documentos transmitidos via Importador XML (0=TODOS;1=NFe;2-CTe;3=NFSe;4=MDe;5=MDfe;6=Recebimento). Exemplo: 6 |  |
| MV\_FILREP | Logico | Define se traz os XML filtrados pelo filial escolhida ou não. (.T. = Filtra filial, .F. = Traz tudo). | Valor default .T. (Filtra Filial) |
| MV\_XMLRATD | Lógico | Rateia o valor do frete sobre devolução de vendas entre os itens da nota de devolução. (.T.) Efetua o rateio;(.F.) Lança o frete no produto MV\_XMLPFCT. | Valor default .T. (Efetua o rateio) |
| MV\_COLEDI | Caracter | Informa qual ou quais código dos arquivos que serão importados | Valor default = "{}"  Ex: {"109","214","273","319"} |
| MV\_COLTEG | Logico | Na "geração do documento", indica se a TES será informada para o D1\_TESACLA (A classificar) ou D1\_TES (Classificado) | Parâmetro verificado quando MV\_COMCOL1 = 0  MV\_COMCOL1 = 1 (Sempre será D1\_TESACLA - A classificar)  MV\_COMCOL2 = 2 (Sempre será D1\_TES - Classificado)  Mais informações: [IX08004 - Importador XML - Regras TES / Condição de pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=546695598) |
| MV\_ERRCTEG | Logico | Indica se ira gerar pre nota ou inconsistência ao não encontrar TES, quando MV\_COLTEG estiver ativo |  |
| MV\_COLVCHV | Logico | habilita a importação da CTE sem NF origem, quando a busca é efetuado pela chave da nota | .T. |
| MV\_COLVDCS | Logico | habilita a importação da CTE sem NF origem, quando a busca é efetuado pelo documento e serie | Valor default .F. (não importa) |
| MV\_VLRCTE | Logico | Indica qual tag será o valor do CTe/CTeOS, F=vRec T=vTPrest | F (Default) |
| MV\_XMLCAUT | Logico | Habilita automação cadastral na integração Importador XML x TOTVS Transmite | T (Default) |
| MV\_OCRXSEL | Lógico | Ao fazer a seleção de todos os registros na tela do Monitor do importador Xml devem ser selecionados os registros com status de E - ("Documento c/ Ocorrência) ? | Valor default .F. (será selecionado todos os registros com status diferente de B ( Docto. Pendente Rev.Cadastral ) e E ( Documento c/ Ocorrência). |

***Saiba Mais:***

[Parâmetros](https://tdn.totvs.com/pages/releaseview.action?pageId=485869217)

[Pontos de Entrada disponíveis nas funções](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
