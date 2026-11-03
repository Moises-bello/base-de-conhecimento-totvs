---
content_hash: dc77eeb2564b9f5bb258e4683a25bbec9822e2e0481385475f973857c9a95879
fetched_at: '2026-06-29T00:06:20.812476+00:00'
page_id: '223156021'
product: rm
source: tdn-rm
title: TTVYZ1_DT_TRCT_CAMPO_25_Data_Aviso_Previo_26_Data_Afastamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVYZ1_DT_TRCT_CAMPO_25_Data_Aviso_Previo_26_Data_Afastamento
version: 1
---

# TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Emissão TRCT* |
| **Situação/Requisito:** | *Não estava sendo considerado o parâmetro "Data Aviso Prévio Indenizado igual à Data de Demissão" para demissão em que o campo "Desconta Aviso Prévio" estava marcado.* |
| **Solução/Implementação:** | O TRCT passa a igualar as datas dos campos 25 Data do Aviso Prévio e 26 Data de Afastamento se o parâmetro "Data Aviso Prévio Indenizado igual à Data de Demissão" estiver marcado e se no cadastro de rescisão do funcionário estiver marcado ou um ou outro dos campos: "Tem Aviso Prévio Indenizado" ou "Desconta Aviso Prévio". |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTMFCL |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
