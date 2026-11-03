---
content_hash: c2d3ed1bb422060636568bf54707f272dbb50c4ad23c07b703353019944ba744
fetched_at: '2026-06-29T00:06:01.063586+00:00'
page_id: '198935528'
product: rm
source: tdn-rm
title: TSVQP4_DT_Habilitar_Entrada_Dados_Tomador_Centro_Custo_Conforme_Parametrizacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVQP4_DT_Habilitar_Entrada_Dados_Tomador_Centro_Custo_Conforme_Parametrizacao
version: 2
---

# Entrada de Dados

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Menu Entrada de Dados por Tomador*  *Menu Entrada de Dados por Centro de Custo* |
| **Situação/Requisito:** | O Labore na nova MDI não está controlando a visibilidade dos módulos de entrada de dados por centro de custo e por tomador, de acordo com a parametrização do usuário. Estes módulos estão sempre visíveis independentemente do valor informado nos parâmetros: "Utiliza Cálculo por Centro de Custo", "Utiliza tomador de serviço" com "Distribuição de eventos por tomador via entrada de dados". |
| **Solução/Implementação:** | O Labore na nova MDI Respeitará os parâmetros  "Utiliza Cálculo por Centro de Custo", "Utiliza tomador de serviço" com "Distribuição de eventos por tomador via entrada de dados", a fim visualizar os módulos de Entrada de Dados por Centros de Custo e por Tomador somente se estes parâmetros estiverem marcados. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSVQP4* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.6* |
