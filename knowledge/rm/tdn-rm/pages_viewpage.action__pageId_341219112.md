---
content_hash: 3c9c72053b3e120838ba4813915baaa7619038b053fd6571ee961d7b1492c226
fetched_at: '2026-06-29T00:08:52.545330+00:00'
page_id: '341219112'
product: rm
source: tdn-rm
title: NFE_Rejeição_461_Informado_percentual_de_Gás_Natural_na_mistura_para_produto_diferente_de_GLP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341219112
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.17 |
| **Ocorrência:** | Rejeição 461: Informado percentual de Gás Natural na mistura para produto diferente de GLP |
| **Passo a passo:** | **Causas:**  A rejeição ocorre quando foi gerada a TAG cProdANP com valor diferente do esperado pela **SEFAZ** (Secretaria da Fazenda). Esta TAG é gerada no bloco de informações específicas para combustível no XML.  Para produto **GLP** (gás liquefeito de petróleo), obrigatoriamente o código do produto gerado na TAG cProdANP deve ser '210203001'.  Veja a regra da SEFAZ:    **Verificações para solução:**  Se o produto é**GLP**, deve estar com o código que a **SEFAZ** espera. Este código é informado no cadastro do Produto | Anexos | Dados Fiscais do Produto | Aba Tributação:    Caso não se trate de produto **GLP**, não deve ser informado nenhum código no campo.  No XML será gerado o bloco abaixo para o produto **GLP**:    Fonte:  Manual de Orientação ao Contribuinte - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=af0MhVeqltw=> |
