---
content_hash: f38247fd0d80942939d719127c15112c3a78759d00aebbd321fb102d9434a467
fetched_at: '2026-06-29T00:12:16.432053+00:00'
page_id: '989564275'
product: rm
source: tdn-rm
title: Grupo de Informações do Crédito Presumido - CBS (NFCom)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=989564275
version: 3
---

# gCBSCredPres - Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **gCBSCredPres** | **[gIBSCBS](https://tdn.totvs.com/pages/viewpage.action?pageId=982936968)** | **0-1** | **Grupo** | **Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento**  Este grupo será gerado sempre que o código do Credito presumido estiver preenchido no tributo do Item do Movimento |
| cCredPres | gCBSCredPres | 1-1 | Elemento | TTRBMOV.CODCREDPRESUMIDO  Busca do CBS definido no Item do Movimento |
| pCredPres | gCBSCredPres | 1-1 | Elemento | TTRBMOV.PCCREDPRESUMIDO  Busca do CBS definido no Item do Movimento |
| vCredPres | gCBSCredPres | 1-1 | Elemento de Escolha | TTRBMOV.VALORCREDPRESUMIDO  Busca do CBS definido no Item do Movimento |
| vCredPresCondSus | gCBSCredPres | 1-1 | Não será gerado |
