---
content_hash: 03463b51f41d67fd111c0b5452b002327bcd1ff38de9bae48c74ede05a3071a0
fetched_at: '2026-06-29T00:12:16.254995+00:00'
page_id: '982936968'
product: rm
source: tdn-rm
title: Grupo de informações da Tributação IBS/CBS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=982936968
version: 15
---

# IBSCBS - Grupo de informações da Tributação IBS/CBS

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **IBSCBS** | **[imposto](https://tdn.totvs.com/pages/viewpage.action?pageId=901954459)** | **0-1** | **Grupo de Escolha** | **Grupo de informações da Tributação IBS/CBS**  Este Grupo será gerado sempre que os tributos IBS e CBS estiverem preenchidos no Item do Movimento |
| CST | IBSCBS | 1-1 | Elemento | TTRBMOV.SITTRIBUTARIA  Definido no Item do Movimento |
| cClassTrib | IBSCBS | 1-1 | Elemento | TTRBMOV.CLASSTRIB  Definido no Item do Movimento |
| indDoacao | IBSCBS | 0-1 | Elemento | **Será gerado sob demanda** |
| **gIBSCBS** | **IBSCBS** | **0-1** | **Grupo** | **Grupo de informações específicas do IBS/CBS**  Este grupo é gerado quando o CST informado tiver a opção "IndIBSCBS" marcada.  Para mais informações consulte a documentação do cadastro de |
| vBC | gIBSCBS | 1-1 | Elemento | TTRBMOV.BASEDECALCULO  Valor da Base de cálculo comum a IBS/CBS |
| **gIBSUF** | **gIBSCBS** | **1-1** | **Grupo** |  |
| **gIBSMun** | **gIBSCBS** | **1-1** | **Grupo** |  |
| vIBS | gIBSCBS | 1-1 | Elemento | Valor do IBS (soma de vIBSUF e vIBSMun) |
| **gCBS** | **gIBSCBS** | **1-1** | **Grupo** |  |
| **gTribRegular** | **gIBSCBS** | **0-1** | **Grupo** |  |
| **gTribCompraGov** | **gIBSCBS** | **0-1** | **Grupo** | O **grupo é gerado** nos seguintes cenários:   * + CST informado tiver a opção "IndIBSCBS" marcada;   + Este grupo será gerado sempre que o grupo ide.gCompraGov for gerado; |

Exemploxml

000
000001

1000.00

0.10
1.00

0.00
0.00
1.00

0.90
9.00
]]>
