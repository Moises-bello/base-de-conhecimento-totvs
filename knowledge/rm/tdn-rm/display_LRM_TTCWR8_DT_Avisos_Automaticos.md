---
content_hash: 8fde0a8226adc96bde1fa3b9234f48c93fdee75767a632e8b416fd3b27e23d91
fetched_at: '2026-06-29T00:06:05.719726+00:00'
page_id: '201726643'
product: rm
source: tdn-rm
title: TTCWR8_DT_Avisos_Automaticos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCWR8_DT_Avisos_Automaticos
version: 1
---

# Avisos Automáticos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Totvs Folha de Pagamento* |
| **Função:** | *Avisos Automáticos* |
| **Situação/Requisito:** | *Erro ao enviar Avisos Automáticos agrupados por Seção* |
| **Solução/Implementação:** | Alterada sentença de agrupamento por seção, que chamava a sentença de agrupamento por supervisor.  Agora o agrupamento por seção chama a sentença de agrupamento de chefes como help informa e não mais o agrupamento de supervisor. Passagem de parâmetros para agrupamento por chefes e seção |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTCWR8* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
