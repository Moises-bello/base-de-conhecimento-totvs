---
content_hash: 3d9eb1442370c8d68ae7651aa04e2ef2c43960a34dbd662ab00b8909f17cac86
fetched_at: '2026-06-29T00:08:30.382818+00:00'
page_id: '272428623'
product: rm
source: tdn-rm
title: 647073 MRH-9152 DT Coluna Usuario Rescisao Transferencia
type: documentation
url: https://tdn.totvs.com/display/LRM/647073+MRH-9152+DT+Coluna+Usuario+Rescisao+Transferencia
version: 111
---

# PREENCHIMENTO CORRETO DA COLUNA DE USUÁRIO NA RESCISÃO POR TRANSFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | Na rescisão por transferência, ao incluir o registro da nova chapa na PFUNC, as colunas RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY, RECMODIFIEDON estão sendo preenchidas com o mesmo conteúdo da chapa transferida.  O correto é preencher as informações com os dados atuais. |
| **Solução/Implementação:** | Ajuste na rescisão por transferência para preencher as colunas RECCREATEDBY, RECCREATEDON, RECMODIFIEDBY e RECMODIFIEDON com o usuário corrente e data do dia, no registro da nova chapa na PFUNC. |
| **Tickets relacionados:** | MRH-9152 |

divs
