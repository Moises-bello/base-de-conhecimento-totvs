---
content_hash: 13451dbd65bb73f358277ffbbb283ee646eaa9b5c2216af8c16db60c6998a849
fetched_at: '2026-06-29T00:05:52.078371+00:00'
page_id: '1056144705'
product: rm
source: tdn-rm
title: Totais das informações dos tributos PIS/COFINS (valores)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144705
version: 6
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| piscofins | [valores](https://tdn.totvs.com/pages/viewpage.action?pageId=560653837) | G | 1-1 | Totais das informações dos tributos PIS/COFINS |  | Este grupo é gerado apenas com as informações dos tributos PIS/COFINS retidos. (PISRF e COFINSRF) |
| CST | piscofins | E | 1-1 | CST PIS/COFINS. | TTRBMOV.SITTRIBUTARIA |  |
| vBCPisCofins | piscofins | E | 1-1 | Base Cálculo PIS/COFINS. | TTRBMOV.BASEDECALCULO |  |
| pAliqPis | piscofins | E | 1-1 | Alíquota PIS | TTRBMOV.ALIQUOTA |  |
| pAliqCofins | piscofins | E | 1-1 | Alíquota COFINS. | TTRBMOV.ALIQUOTA |  |
| tpRetPisCofins | piscofins | E | 1-1 | Tipo Retenção. |  | O valor da tag será gerado da seguinte forma:  Se não houver os tributos IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | | --- | --- | --- | | **1** | Sim | Sim | | **2** | Não | Não |     Se houver IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | **CSLL Retida?** | | --- | --- | --- | --- | | **0** | Não | Não | Não | | **3** | Sim | Sim | Sim | | **4** | Sim | Sim | Não | | **5** | Sim | Não | Não | | **6** | Não | Sim | Não | | **7** | Não | Sim | Sim | | **8** | Não | Não | Sim | | **9** | Sim | Não | Sim | |
| vSumCSLL | piscofins | E | 1-1 | Valor Somado do Pis, Cofins e CSLL | TTRBMOV.VALOR |  |

## Nota Técnica Nº 007/2026

Caso o município não tenha aderido a NT007 o valor da tag **tpRetPisCofins** pode ser parametrizado para gerar somente com os códigos 1 e 2 mesmo que o IBS/CBS esteja presente no movimento.

É necessário cadastrar uma Rotina Fiscal.

Para isso acesse o módulo de Gestão Fiscal e a aba Obrigações Acessórias.

Cadastre uma nova rotina do tipo "Não se Aplica".

Em seguida no anexo "Parâmetros da Rotina" é necessário cadastrar um novo informando o código IBGE do município no campo chave e o texto NT007 no campo valor.

Imagens

Este cadastro indica que o município não aderiu a NT 007 e, portanto, a tag **tpRetPisCofins** será gerada somente com os valores 1 ou 2 de acordo com as regras descritas na tabela acima.
