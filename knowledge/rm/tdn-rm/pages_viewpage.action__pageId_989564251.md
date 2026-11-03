---
content_hash: 192e2fccc5a8ebcb6de0d0c16dd578dae85689b1975c849482c0b408a4bb7448
fetched_at: '2026-06-29T00:12:16.428417+00:00'
page_id: '989564251'
product: rm
source: tdn-rm
title: Grupo de Informações do Crédito Presumido - IBS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564251
version: 3
---

# gIBSCredPres - Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gIBSCredPres** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **0-1** | **Grupo** | **Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento**  Este grupo será gerado sempre que o código do Credito presumido estiver preenchido no tributo do Item do Movimento |
| cCredPres | gIBSCredPres | 1-1 | Elemento | TTRBMOV.CODCREDPRESUMIDO  Busca do IBS definido no Item do Movimento |
| pCredPres | gIBSCredPres | 1-1 | Elemento | TTRBMOV.PCCREDPRESUMIDO  Busca do IBS definido no Item do Movimento |
| vCredPres | gIBSCredPres | 1-1 | Elemento de Escolha | TTRBMOV.VALORCREDPRESUMIDO  Busca do IBS definido no Item do Movimento |
| vCredPresCondSus | gIBSCredPres | 1-1 | Não será gerado |
