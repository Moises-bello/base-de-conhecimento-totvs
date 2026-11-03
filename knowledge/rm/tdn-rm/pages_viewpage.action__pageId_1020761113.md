---
content_hash: 9608b9acc7ee8721fda06bee0648b8cd314965c3a31551e51fbc252b6445abe9
fetched_at: '2026-06-29T00:05:47.991963+00:00'
page_id: '1020761113'
product: rm
source: tdn-rm
title: infDPS/IBSCBS/valores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1020761113
version: 4
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **gReeRepRes** | **valores** | **Não** | **Grupo** | **Grupo de informações relativas a valores incluídos neste documento**  **OBS: Não é gerado nesse momento** |
| **trib** | **valores** | **Sim** | **Grupo** | **Grupo de informações relacionados aos tributos IBS e CBS** |
| **gIBSCBS** | **trib** | **Sim** | **Grupo** | **Grupo de informações relacionadas ao IBS e à CBS** |
| CST | gIBSCBS | Sim | CST do tributo do item | Código de situação tributária do IBS e da CBS |
| cClassTrib | gIBSCBS | Sim | Classificação tributária do tributo do item | Código da classificação tributária do IBS e da CBS |
| cCredPres | gIBSCBS | Não | Código do crédito presumido do tributo do item | Código e a classificação do crédito presumido do IBS e da CBS  O campo é gerado no XML com **zero à esquerda** sempre que o código possuir apenas **1 caractere**.  **Exemplo:**   * Valor informado: `4` * Valor gerado no XML: `04` |
| gTribRegular | gIBSCBS | Não | Grupo. Será gerado caso a regra tributária vinculada ao item do movimento esteja preenchida com a regra tributária regular | Grupo de informações da Tributação Regular |
| **gTribRegular** | **gIBSCBS** | **Não** | **Grupo** | **Grupo de informações da Tributação Regular** |
| CSTReg | gTribRegular | Sim | CST da regra tributária regular | Código de situação tributária do IBS e da CBS de tributação regular |
| cClassTribReg | gTribRegular | Sim | Classificação tributária da regra tributária regular | Código da classificação tributária do IBS e da CBS de tributação regular |
| **gDif** | **gIBSCBS** | **Não** | **Grupo** | **Grupo de informações relacionadas ao diferimento para IBS e CBS** |
| pDifUF | gDif | Sim | Percentual de diferimento do IBS/UF | Percentual de diferimento para o IBS estadual |
| pDifMun | gDif | Sim | Percentual de diferimento do IBS/Mun | Percentual de diferimento para o IBS municipal |
| pDifCBS | gDif | Sim | Percentual de diferimento da CBS | Percentual de diferimento para a CBS |
