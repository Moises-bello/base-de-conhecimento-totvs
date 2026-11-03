---
content_hash: 45a9259e80dde9a98898056fde472073e8eed2fba2bfa000d5453a3b18ab30b2
fetched_at: '2026-06-29T00:09:00.544758+00:00'
page_id: '369626768'
product: rm
source: tdn-rm
title: 2618807 FISCAL01-4509 NF-e com item de serviço tributado pelo ICMS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=369626768
version: 1
---

# Integração RM X TAF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio de Nota Fiscal Eletrônica |
| **Situação/Requisito:** | Ao enviar uma NF-e é apresentado a mensagem:  Enviar NF-e: Erro no envio da NF-e.  TSS - Erro na validação desta nota. Motivo:Campo: PIS': This element is not expected. Expected is one of (  {<http://www.portalfiscal.inf.br/nfe>}  ICMS,  {<http://www.portalfiscal.inf.br/nfe>}  IPI,  {<http://www.portalfiscal.inf.br/nfe>}  ISSQN . Campo: PIS': This element is not expected. Expected is one of (  {<http://www.portalfiscal.inf.br/nfe>}  ICMS,  {<http://www.portalfiscal.inf.br/nfe>}  IPI,  {<http://www.portalfiscal.inf.br/nfe>}  ISSQN . |
| **Solução/Implementação:** | Ajustado a condição na geração das tags de ICMS para passar a considerar itens do Tipo Serviço que são tributados pelo ICMS |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | 2618807 |
| **Requisito:** | Não se Aplica |
| **Documento de Referência:** | Não se Aplica |
