---
content_hash: 87e1c451414e1ad0386ce6ae9c6ee6d6cfd8dec4c700185e1851f8a185266155
fetched_at: '2026-06-29T00:12:10.260808+00:00'
page_id: '953000672'
product: rm
source: tdn-rm
title: Grupo I – Produtos e serviços da NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953000672
version: 7
---

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Grupo I – Produtos e serviços da NF-e** | | | | | | |
| **ID** | **Campo** | **Ele** | **Pai** | **Ocorrência** | **Campo de Origem** | **Mais Informações** |
| I01 | prod | G | H01 | 1-1 |  |  |
| I02 | cProd | E | I01 | 1-1 | Código do produto. TPRODUTO.CODIGOPRD | No item do movimento, pasta Itens | aba Itens | pasta Identificação | aba Cabeçalho.  **Nota**: Se o Produto for referente ao RECOPI (vide campo Z05), este campo será gerado com o NCM da mercadoria. |
| I03 | cEAN | E | I01 | 1-1 | Código de barras do produto. TPRDCODIGO.CODIGO | Aba Código de Barras do cadastro do Produto selecionado no item do movimento.  Tipo de código de barras: GTIN.  Passo a passo de como gerar a tag disponível no link:   [Geração das tags cEAN, cEANTrib e uTrib- Código de Barras e Unidade e Medida](https://tdn.totvs.com/pages/viewpage.action?pageId=949425241) |
| 103 | cBarra | E | I01 | 0-1 | Código de barras do produto. TPRDCODIGO.CODIGO | Aba Código de Barras do cadastro do Produto selecionado no item do movimento.  Tipo de código de barras: Interno.  Disponível a partir do dia 01/09/2021. |
| I04 | xProd | E | I01 | 1-1 | Descrição do código do produto. TPRODUTO.NOMEFANTASIA ou TPRODUTO.DESCRICAO ou TPRODUTO.DESCRICAOAUX | Produto selecionado no item do movimento pasta Itens | aba Itens | pasta Identificação | aba Cabeçalho. |
| I05 | NCM | E | I01 | 1-1 | Código NCM. TPRD.NUMEROCCF | Cadastro do produto, na pasta Detalhes | aba Outros Dados | agrupador: Nomenclatura Comum do Mercosul (NCM).  A partir da versão 2502:   ... | aba Outros dados | agrupador: Classificação Fiscal de Bens e Serviço | Campo Número NCM cadastrado para o registro. No caso de item do tipo "Serviço", caso o campo esteja vazio, será enviado com default o valor "00" |
| I5a | NVE | E | I01 | 0-8 | NÃO SERÁ GERADO. |  |
| I05b | -x- | G | I01 | 0-1 |  |  |
| I05c | CEST | E | I05b | 1-1 | CEST - Código Especificador da Substituição Tributária. TPRDFISCAL.CODIGOCEST |  |
| I05d | indEscala | E | I05b | 0-1 | Indicador de Produção em escala relevante. TPRODUTO.INDPRODUCAOESCALARELEVANTE |  |
| I05e | CNPJFab | E | I05b | 0-1 | CNPJ do Fabricante. TFAB.CGC | Cadastro do produto, na pasta Identificação | aba Identificação do Fabricante. |
| I05f | cBenef | E | I01 | 0-1 | Código Fiscal. TPRDCODFISCAL.CODFISCAL ou DCFOPCODAJUSTE ou DPRDBENEFICIOFISCAL. | O sistema tem 3 opções de busca para preenchimento conforme Link abaixo: [Hierarquia de preenchimento da tag.](https://tdn.totvs.com/pages/viewpage.action?pageId=874201275)  Obs: Importante verificar qual a opção mais adequada para a operação. |
| I06 | EXTIPI | E | I01 | 0-1 | Código EX. TPRODUTO.CODIGOEX | Cadastro do produto, pasta Detalhes | aba Outros Dados. |
| I08 | CFOP | E | I01 | 1-1 | Código da Natureza de Operação. TMOV.IDNAT | CFOP, No item do movimento pasta Integrações | aba Fiscal. |
| I09 | uCom | E | I01 | 1-1 | Unidade. TITMMOV.CODUND | No item do movimento | pasta Identificação | aba Cabeçalho | agrupador Movimentação. |
| I10 | qCom | E | I01 | 1-1 | Quantidade. TITMMOV.QUANTIDADE | No item do movimento | pasta Identificação | aba Cabeçalho | agrupador Movimentação. |
| I10a | vUnCom | E | I01 | 1-1 | Preço Unitário. TITMMOV.PRECOUNITARIO | No item do movimento | pasta Identificação | aba Cabeçalho | agrupador Movimentação. |
| I11 | vProd | E | I01 | 1-1 | Valor total do produto / serviço. Se parâmetro "EditaPrecoTotalItem" estiver marcado e valor total do item > 0 então TITMMOV.VALORTOTALITEM senão (TITMMOV.QUANTIDADE \* TITMMOV.PRECOUNITARIO) | A opção “Editar Preço Total” estando habilitada no Tipo de Movimento, será considerado o campo Preço Total | pasta Identificação | aba Cabeçalho | agrupador Movimentação do item. Caso o parâmetro esteja desabilitado será considerado Quantidade (\*) Preço Unitário. |
| I12 | cEANTrib | E | I01 | 1-1 | Código de barras do produto. TPRDCODIGO.CODIGO | Cadastro do produto, pasta Código de barras.  Tipo de código de barras: GTIN.  Passo a passo de como gerar a tag disponível no link:  [Geração das tags cEAN, cEANTrib e uTrib- Código de Barras e Unidade e Medida](https://tdn.totvs.com/pages/viewpage.action?pageId=949425241) |
| I12a | cBarraTrib | E | I01 | 0-1 | Código de barras do produto. TPRDCODIGO.CODIGO | Cadastro do produto, pasta Código de barras.  Tipo de código de barras: Interno.  Disponível a partir do dia 01/09/2021. |
| I13 | uTrib | E | I01 | 1-6 | Unidade Tributável. TPRODUTODEF.CODUNDTRIBUTAVELINT  **SE** flag "TRIBUTAVEL" estiver marcada na unidade do item de movimento **ENTÃO** ela é a unidade tributável. | Considera a Unidade Tributável do cadastro do Produto | pasta Controle Estoque.  [Geração das tags cEAN, cEANTrib e uTrib- Código de Barras e Unidade e Medida](https://tdn.totvs.com/pages/viewpage.action?pageId=949425241) |
| I14 | qTrib | E | I01 | 1-1 | Quantidade. TITMMOV.QUANTIDADETRIBUTAVEL ou TITMMOV.QUANTIDADE | Se a unidade de medida utilizada no item de movimento não for uma unidade base, então será quantidade do produto (\*) Fator de conversão. Ao contrário, será levado o valor unitário do item. |
| I14a | vUnTrib | E | I01 | 1-1 | Preço Unitário. TITMMOV.PRECOUNITARIO | No item do movimento | pasta Identificação | aba Cabeçalho | agrupador Movimentação. |
| I15 | vFrete | E | I01 | 0-1 | Frete. TITMMOV.RATEIOFRETE | Item do movimento, pasta Tributos e Valores | aba Valores do agrupador "Rateio de Valores Financeiros do Movimento".". |
| I16 | vSeg | E | I01 | 0-1 | Seguro. TITMMOV.RATEIOSEGURO | Item do movimento, pasta Tributos e Valores | aba Valores do agrupador "Rateio de Valores Financeiros do Movimento". |
| I17 | vDesc | E | I01 | 0-1 | Desconto. (TITMMOV.RATEIODESC + TITMMOV.VALORDESC) + TITMMOV.VALORDESCCONDICONALITM | Item do movimento, pasta Tributos e Valores | aba Valores do agrupador "Rateio de Valores Financeiros do Movimento". |
| l17a | vOutro | E | I01 | 0-1 | Despesa. TITMMOV.RATEIODESP+ TITMMOV.VALORDESP | Item do movimento, pasta Tributos e Valores | aba Valores do agrupador "Rateio de Valores Financeiros do Movimento". |
| l17b | indTot | E | I01 | 1-1 | Se o campo "Tributação ICMS SEM Valor Contábil", da Regra de ICMS vinculada ao CFOP selecionado no movimento, a tag será gerada com valor = 1. Caso o CFOP selecionado no item do movimento não seja Fiscal, então a tag será preenchida com valor = 0.  Se DREGRAICMS.TIPOICMSNCONTABIL = 0 Então: 1 Se DREGRAICMS.TIPOICMSNCONTABIL = 1 ou Natureza Não Fiscal (DCFOP.FISCAL = 0) Então: 0 | **Valor = 1** Regra vinculada ao CFOP selecionado no item do movimento, aba Outros Dados.  **Valor = 0** Cadastro do CFOP selecionado no item do movimento com a flag "Fiscal" da aba Identificação desmarcada. |
| I17c | indBemMovelUsado | E | I01 | 0-1 | NÃO SERÁ GERADO. | **[Incluído pela NT 2025.002-RTC](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YFz9is%20R6tw=)** |
