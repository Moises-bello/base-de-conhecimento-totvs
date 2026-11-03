---
content_hash: 78d03657d6bbe25397cb0dcf87666490c315824c7c7e7fc76e6b785fac033880
fetched_at: '2026-06-29T00:08:54.732312+00:00'
page_id: '345545427'
product: rm
source: tdn-rm
title: RMFIN-1630 Controle de glosas - Baixa de contas não recebidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=345545427
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Faturamento > Fatura de Convenio |
| **Situação/Requisito:** | Ao importar um arquivo XML de RMS o sistema estava fechando as contas que não estão presentes no arquivo de remessa como se fossem pagamentos integrais. |
| **Solução/Implementação:** | Adicionado um filtro no processo para que sejam processadas apenas as contas do arquivo e não alterar o status da contas que não estão presentes naquele arquivo. |
