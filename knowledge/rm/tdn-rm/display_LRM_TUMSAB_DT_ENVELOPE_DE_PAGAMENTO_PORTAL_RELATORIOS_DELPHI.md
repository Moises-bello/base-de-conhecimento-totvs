---
content_hash: 8f956c4f52c5dc90dfe87a2a05ef5859b658b12ab7077cec5f2bb3fe313361be
fetched_at: '2026-06-29T00:08:04.676656+00:00'
page_id: '235576228'
product: rm
source: tdn-rm
title: TUMSAB_DT_ENVELOPE_DE_PAGAMENTO_PORTAL_RELATORIOS_DELPHI
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMSAB_DT_ENVELOPE_DE_PAGAMENTO_PORTAL_RELATORIOS_DELPHI
version: 115
---

# ENVELOPE DE PAGAMENTO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope de Pagamento do Portal* |
| **Situação/Requisito:** | Ao gerar um envelope de pagamento no portal selecionando um relatório Delphi e utilizando o servidor do RMLabore.exe, o relatório nunca era exibido pois o job era criado com o código da coligada do contexto e o resultado era buscado com o código de coligada do relatório. |
| **Solução/Implementação:** | *Foi tratada a busca do job finalizado para localizar corretamente o envelope.* |
| **Chamados relacionados:** | TUMSAB |

divs
