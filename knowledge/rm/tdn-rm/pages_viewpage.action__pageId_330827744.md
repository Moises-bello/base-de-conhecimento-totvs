---
content_hash: bb31b185c799db8e503573cb47652456689482382a17b6f5e12367c11ac51d53
fetched_at: '2026-06-29T00:08:49.404555+00:00'
page_id: '330827744'
product: rm
source: tdn-rm
title: 1937880 RMSAU-2113 Geração do arquivo em HD para faturamento com problema no
  convênio Ipasgo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330827744
version: 2
---

# Faturamento de convênios - Convênio Ipasgo

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Função:** | Ajustar exportação de arquivo de faturamento |
| **Situação:** | Ao gerar arquivo para faturamento do convênio Ipasgo, quando o prestador não era credenciado diretamente no convênio, os procedimentos de mesma via não estavam sendo listados. |
| **Solução:** | Foi removido o trecho da query que ignorava os itens de prestador indireto. |
