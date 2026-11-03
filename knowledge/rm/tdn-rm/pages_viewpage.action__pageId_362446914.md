---
content_hash: d99126af34f5bb5c99e2df89a80caa638171134111db4eacbaf6184f9f920c0a
fetched_at: '2026-06-29T00:08:58.934834+00:00'
page_id: '362446914'
product: rm
source: tdn-rm
title: 2811365 FOPCALCULO01-3693 DT SEFIP Com Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362446914
version: 5
---

# Geração SEFIP / Lançamento Financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Geração SEFIP / Lançamento Financeiro |
| **Situação/Requisito:** | Ao processar a Geração de SEFIP com a opção gerar Lançamentos financeiro marcada e selecionando funcionários na situação V - Aviso Prévio, o sistema apresenta a mensagem que nenhum funcionário atende a seleção e não realiza o lançamento. |
| **Solução/Implementação:** | Ajustado a rotina de Geração SEFIP para efetuar o lançamento financeiro de valores FGTS mês anterior que não foram recolhidos na GRFC (parâmetro "FGTS mês anterior será recolhido na GRFC" desmarcado no processo de rescisão) e funcionário na situação "V". |
| **Tickets relacionados:** | 2811365 |
