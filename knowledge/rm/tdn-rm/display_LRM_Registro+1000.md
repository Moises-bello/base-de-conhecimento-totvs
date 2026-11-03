---
content_hash: e26726e33749a46445a49d1ea9b325b1ba0984d5e81b032af89e3ffe15970275
fetched_at: '2026-06-29T00:10:45.975996+00:00'
page_id: '553905971'
product: rm
source: tdn-rm
title: Registro 1000
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+1000
version: 12
---

**Registro analítico do produto**

Este registro contém todas as características que identificam a mercadoria.

Este registro apresenta os produtos relacionados nos Itens das Notas Fiscais que saíram nos registros filhos.

| Nº | Campo | Descrição | Origem dos Dados |
| --- | --- | --- | --- |
| B01 | REG | Registro 1000 | Texto fixo contendo 1000 |
| B02 | IND\_FECOP | Indicador de produto sujeito ao Fundo de Combate à Pobreza:  0 – Produto não está sujeito ao FECOP 1 – Produto está sujeito ao FECOP | Se o percentual do FECP informado no Anexo Dados Fiscais (PR) for **igual** a zero gera o campo com "0"..  Se for **maior** que zero, gera com a opção "1"  TPRDCODFISCAL.PERFECP |
| B03 | COD\_ITEM | Informar o código de identificação da mercadoria utilizado na aquisição e na comercialização do produto. | Preenchido com o Código do Produto  TPRODUTO.CODIGOPRD |
| B04 | COD\_BARRAS | Código GTIN/EAN Tributável da menor unidade do produto | Código de Barras do Produto (TPRDCODIGO.CODIGO) para a unidade de Controle |
| B05 | COD\_ANP | Código do produto conforme tabela da Agência Nacional de Petróleo - ANP | Código na ANP informado no Cadastro do Produto em Anexos | Dados Fiscais do Produto | pasta Tributação.  TPRDFISCAL.CODIGOANP |
| B06 | NCM | Informar a NCM da mercadoria com 8 dígitos | Código NCM informado no Cadastro do produto, na pata Detalhes | aba Outros Dados | agrupador Nomeclatura Comun do Mercosul (NCM).  TPRD.NUMEROCCF |
| B07 | CEST | Informar o código CEST específico para cada item de mercadoria comercializada sujeita à substituição tributária | TPRDFISCAL.CODIGOCEST |
| B08 | DESCR\_ITEM | Descrição do item | Nome Fantasia do Produto  TPRD.NOMEFANTASIA |
| B09 | UNID\_ITEM | Informar a unidade de medida utilizada na quantificação do estoque | Recebe a Unidade de Controle informada no Cadastro do Produto, pasta Controle Estoque  TPRODUTODEF.CODUNDCONTROLE |
| B10 | ALIQ\_ICMS\_ITEM | Alíquota do ICMS aplicável ao item nas operações internas, incluído o FECOP. Caso a mercadoria seja beneficiada com redução da base de cálculo, adotar a carga tributária efetiva | Receberá a alíquota interna do ICMS informada no Anexo Dados Fiscais por UF  TPRDCODFISCAL.ALIQINTICMS |
| B11 | ALIQ\_FECOP | Informar o percentual da aliquota do ICMS destinada ao FECOP | Receberá a alíquota do FECP informada no Anexo Dados Fiscais por UF  TPRDCODFISCAL.PERFECP.  Quando não há alíquota ou quando não há ou ela é zerada, o campo será gerado em branco. |
| B12 | QTD\_TOT\_ENTRADA | Quantidade total do item adquirido no período. Informar o mesmo valor do campo D02 do registro 1100 | Gerado com o valor do campo D02 do Registro 1100 |
| B13 | QTD\_TOT\_SAIDA | Quantidade total de saídas do item no período. Somatória da quantidade das operações de saídas do item declaradas nos campos F02, H02, J02, L02 | Gerado com o somatório dos campos F02 + H02 + J02 + L02 dos registros 1200, 1300, 1400 e 1500, respectivamente. |
