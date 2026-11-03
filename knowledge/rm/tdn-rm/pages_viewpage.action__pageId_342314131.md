---
content_hash: 3a1218d1ec11c8d500fd5cdc6f73b850dc96787ca40c54cb332a6522ee9cdc0f
fetched_at: '2026-06-29T00:08:53.104860+00:00'
page_id: '342314131'
product: rm
source: tdn-rm
title: 2135352 FISCAL01-3925 DT NF-e 4.00 Tag obrigatória não validada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342314131
version: 1
---

# Envio NF-e 4.00

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Envio NF-e 4.00 |
| **Situação/Requisito:** | Ao emitir nota fiscal 4.00 estava ocorrendo a seguinte mensagem:  Motivo:Campo: CNPJFab': This element is not expected. Expected is one of (  {<http://www.portalfiscal.inf.br/nfe>}  NVE,  {<http://www.portalfiscal.inf.br/nfe>}  CEST,  {<http://www.portalfiscal.inf.br/nfe>}  cBenef,  {<http://www.portalfiscal.inf.br/nfe>}  EXTIPI,  {<http://www.portalfiscal.inf.br/nfe>}  CFOP . Campo: IPINT': This element is not expected. Expected is one of (  {<http://www.portalfiscal.inf.br/nfe>}  cSelo,  {<http://www.portalfiscal.inf.br/nfe>}  qSelo,  {<http://www.portalfiscal.inf.br/nfe>}  cEnq .  Foi verificado que tal erro no envio estava ocorrendo pois a tag CEST que antes era opcional na NF-e 3.10 passou a ser obrigatória na 4.00 e este tratamento não era feito pelo sistema. |
| **Solução/Implementação:** | Implementada melhoria na geração da tag CEST para sistema tratar corretamente sua obrigatoriedade no envio da NF-e 4.00. O  comportamento como tag opcional permanece na versão 3.10. |
