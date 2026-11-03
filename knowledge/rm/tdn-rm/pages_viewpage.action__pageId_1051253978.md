---
content_hash: 4f89d352120255f5abd804487e10f3c07acde516fd8cf71c6242bc71191bdf5c
fetched_at: '2026-06-29T00:05:51.559577+00:00'
page_id: '1051253978'
product: rm
source: tdn-rm
title: Grupo de informações dos tributos PIS/COFINS aplicados ao serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1051253978
version: 15
---

### Voltar para [Layout único de integração da NFS-e com o TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=560652116)

| **Nome** | **Pai** | **Tipo Elemento** | **Ocorrência** | **Tipo Dado** | **Campo no RM** | **Descrição** | **Observações** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **piscofins** | **[servico](https://tdn.totvs.com/pages/viewpage.action?pageId=560653807)** | **G** | **0-1** | **--** |  | **Grupo de informações para os Valores de PIS/COFINS** | **Este grupo é gerado apenas com as informações dos tributos PIS/COFINS retidos. (PISRF e COFINSRF)** |
| CST | piscofins | E | 0-1 | Alfanumérico | Tributo do Movimento/Item do Movimento  TTRBMOV.SITTRIBUTARIA | CST da Nota Fiscal  Obs.: CST deve ser igual para todas as linhas do Tributo. |  |
| vBCPisCofins | piscofins | E | 0-1 | Numérico | Tributo do Movimento/Item do Movimento  Se tributo no movimento TTRBMOV.BASEDECALCULO  Senão  somatório dos itens  TTRBMOV.BASEDECALCULO | Base de Cálculo do Tributo |  |
| pAliqPis | piscofins | E | 0-1 | Numérico | Tributo do Movimento/Item do Movimento  TTRBMOV.ALIQUOTA | Alíquota do Tributo PIS |  |
| pAliqCofins | piscofins | E | 0-1 | Numérico | Tributo do Movimento/Item do Movimento  TTRBMOV.ALIQUOTA | Alíquota do Tributo COFINS |  |
| tpRetPisCofins | piscofins | E | 0-1 | Alfanumérico | 0 - PIS/COFINS/CSLL Não Retidos; 1 - PIS/COFINS Retido; 2 - PIS/COFINS Não Retido; 3 - PIS/COFINS/CSLL Retidos; 4 - PIS/COFINS Retidos, CSLL Não Retido; 5 - PIS Retido, COFINS/CSLL Não Retido; 6 - COFINS Retido, PIS/CSLL Não Retido; 7 - PIS Não Retido, COFINS/CSLL Retidos; 8 - PIS/COFINS Não Retidos, CSLL Retido; 9 - COFINS Não Retido, PIS/CSLL Retidos; | O valor da tag será gerado da seguinte forma:  Se não houver os tributos IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | | --- | --- | --- | | **1** | Sim | Sim | | **2** | Não | Não |   Se houver IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | **CSLL Retida?** | | --- | --- | --- | --- | | **0** | Não | Não | Não | | **3** | Sim | Sim | Sim | | **4** | Sim | Sim | Não | | **5** | Sim | Não | Não | | **6** | Não | Sim | Não | | **7** | Não | Sim | Sim | | **8** | Não | Não | Sim | | **9** | Sim | Não | Sim | |  |

## Nota Técnica Nº 007/2026

Caso o município não tenha aderido a NT007 o valor da tag **tpRetPisCofins** pode ser parametrizado para gerar somente com os códigos 1 e 2 mesmo que o IBS/CBS esteja presente no movimento.

É necessário cadastrar uma Rotina Fiscal.

Para isso acesse o módulo de Gestão Fiscal e a aba Obrigações Acessórias.

Cadastre uma nova rotina do tipo "Não se Aplica".

Em seguida no anexo "Parâmetros da Rotina" é necessário cadastrar um novo informando o código IBGE do município no campo chave e o texto NT007 no campo valor.

Imagens

Este cadastro indica que o município não aderiu a NT 007 e, portanto, a tag **tpRetPisCofins** será gerada somente com os valores 1 ou 2 de acordo com as regras descritas na tabela acima.
