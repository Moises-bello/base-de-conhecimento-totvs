---
content_hash: 8be2134bd3e09909a1b16b06a03f1828423dd302fab321d5651fcde248cd4860
fetched_at: '2026-06-29T00:12:10.279112+00:00'
page_id: '953000693'
product: rm
source: tdn-rm
title: Grupo I01 - Produtos e Serviços / Declaração de Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000693
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo I01 - Produtos e Serviços / Declaração de Importação** | | | | | | | | | | | | |
| **#** | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo da Aplicação** | **Mais Informações** |
| 117 | I18 | DI | Declaração de Importação | G | I01 |  | 0-100 | - | Informar dados da importação |  |  |  |
| 118 | I19 | nDI | Número do Documento de Importação (DI, DSI, DIRE, ...) | E | I18 | C | 1-1 | 1-12 | (NT 2011/004) | TMOVFISCAL.DECLARACAOIMPORTACAO | Núm. Declaração de Exportação | No movimento, pasta Informações Adicionais | aba Importação. |
| 119 | I20 | dDI | Data de Registro do documento | E | I18 | D | 1-1 |  | Formato: “AAAA-MM-DD” | TMOVFISCAL.DATADI | Data Declaração de Importação | No movimento, pasta Informações Adicionais | aba Importação. |
| 120 | I21 | xLocDesemb | Local de desembaraço | E | I18 | C | 1-1 | 1-60 | - | TMOVFISCAL.LOCALDESEMBARACO | Local de Desembaraço/Embarque | No movimento, pasta Informações Adicionais | aba Importação. |
| 121 | I22 | UFDesemb | Sigla da UF onde ocorreu o Desembaraço Aduaneiro | E | I18 | C | 1-1 | 2 | - | TMOVFISCAL.UFDESEMBARACO | UF do Desembaraço/Embarque | No movimento, pasta Informações Adicionais | Importação. |
| 122 | I23 | dDesemb | Data do Desembaraço Aduaneiro | E | I18 | D | 1-1 |  | Formato: “AAAA-MM-DD” | TMOVFISCAL.DATADESEMBARACO | Data do Desembaraço Aduaneiro | No movimento, pasta Informações Adicionais | Importação. |
| 122a | I23a | tpViaTransp | Via de transporte internacional informada na Declaração de Importação (DI) | E | I18 | N | 1-1 | 2 | 1=Marítima; 2=Fluvial; 3=Lacustre; 4=Aérea; 5=Postal 6=Ferroviária; 7=Rodoviária; 8=Conduto / Rede Transmissão; 9=Meios Próprios; 10=Entrada / Saída ficta. 11=Courier; 12=Handcarry. (NT 2013/005 v 1.10). 13=Por reboque (NT2020.005) | TMOV.CODVIATRANSPORTE | Via de transporte | No movimento, pasta Transporte | Transportadora. |
| 122b | I23b | vAFRMM | Valor da AFRMM - Adicional ao Frete para Renovação da Marinha Mercante | E | I18 | N | 0-1 | 13v2 | A tag deve ser informada no caso da via de transporte marítima. | Criar um campo complementar no item do movimento com o nome vAFRMM. | Campo complementar | Produto selecionado no item do movimento, pasta Itens | aba Cabeçalho | agrupador Movimentação.  Criar um campo complementar no item do movimento com o nome vAFRMM. |
| 122c | I23c | tpIntermedio | Forma de importação quanto a intermediação | E | I18 | N | 0-1 | 1 | 1=Importação por conta própria; 2=Importação por conta e ordem; 3=Importação por encomenda; |  | Será levado Fixo 1, os valores 2 e 3 não serão gerados | - |
| 122d | I23d | CNPJ | CNPJ do adquirente ou do encomendante | E | I18 | N | 0-1 | 14 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos |  | - | NÃO SERÁ GERADO |
| 122e | I23e | UFTerceiro | Sigla da UF do adquirente ou do encomendante | E | I18 | C | 0-1 | 2 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Não aceita o valor "EX". |  | - | NÃO SERÁ GERADO |
| 123 | I24 | cExportador | Código do Exportador | E | I18 | C | 1-1 | 1-60 | Código do Exportador, usado nos sistemas internos de informação do emitente da NF-e | TMOVFISCAL.CODCFONATUREZA | Código Cliente/Fornecedor | No movimento, pasta Integrações | aba Fiscal. |
| 124 | I25 | adi | Adições | G | I18 |  | 1-100 |  | (NT 2011/004) |  | - | - |
| 125 | I26 | nAdicao | Numero da Adição | E | I25 | N | 1-1 | 1-3 | - | TITMMOVFISCAL.NROADICAO | Número da Adição | No item do movimento, pasta Identificação | aba cabeçalho. |
| 126 | I27 | nSeqAdic | Numero sequencial do item dentro da Adição | E | I25 | N | 1-1 | 1-3 | - | TITMMOVFISCAL.NROITEM | Número do Item na Adição | No item do movimento, pasta Identificação | aba cabeçalho. |
| 127 | I28 | cFabricante | Código do fabricante estrangeiro | E | I25 | C | 1-1 | 1-60 | Código do fabricante estrangeiro, usado nos sistemas internos de informação do emitente da NF-e | TPRODUTODEF.CODFAB | Código do Fabricantes | Produto selecionado no item do movimento, pasta Identificação | agrupador Identificação do Fabricante. |
| 128 | I29 | vDescDI | Valor do desconto do item da DI – Adição | E | I25 | N | 0-1 | 13v2 | - | TITMMOVFISCAL.VALORDESC | Valor do Desconto da DI | No item do movimento, pasta Identificação | aba cabeçalho. |
| 128.01 | I29a | nDraw | Número do ato concessório de Drawback | E | I25 | C | 0-1 | 1-20 | O número do Ato Concessório de Suspensão deve ser preenchido com 11 dígitos (AAAANNNNNND) e o número do Ato Concessório de Drawback Isenção deve ser preenchido com 9 dígitos (AANNNNNND). (Observação incluída na NT 2013/005 v. 1.10) | TMOVFISCAL.DRAWBACK | Número Ato Concess. Regime Drawback | No movimento, pasta Integrações | aba Fiscal. |
