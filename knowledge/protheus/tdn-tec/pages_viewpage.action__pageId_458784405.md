---
content_hash: 156cf31f4cef421fca08a27c6c20c670a902439d8e29a765656012f2d3822d89
fetched_at: '2026-07-02T19:24:24.155816+00:00'
page_id: '458784405'
product: protheus
source: tdn-tec
title: Correção - TGrid não exibe campos em edição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458784405
version: 3
---

Correção - TGrid não exibe campos em edição

|  |  |
| --- | --- |
| Situação | Quando o componente TGrid possui campos nas colunas que estão parcialmente visíveis ou além do limite de visualização horizontal (que só podem ser acessados através da barra de rolagem) e, em algumas circunstâncias recebem a ação de edição, eles permanecem ocultos (ou parcialmente ocultos) não sendo possível visualizar o conteúdo inserido na edição. |
| Ocorrência | É possível verificar o problema de duas formas:   1. Se um campo parcialmente oculto pelo limite horizontal recebe a ação de duplo-clique, ele entra no modo de edição porém a área editável se sobrepõe a qualquer componente visual a direita e uma nova barra de rolagem é exibida. 2. Utilizando somente o teclado, após o preenchimento de um campo, o próximo é automaticamente selecionado. Quando o limite de visualização horizontal é alcançado, o próximo campo que está oculto entra em modo de edição mas não é possível visualizá-lo. |
| Correção | Foi aplicada uma correção para que campos ocultos ou parcialmente ocultos sejam automaticamente exibidos ao receber a ação de edição, seja por duplo clique ou pelo foco automático que ocorre após finalização da edição do campo anterior. |
| Informações adicionais | * Referente ao chamado: 4555779 * Referente à ocorrência: MTEC-2419 * Disponível em builds iguais ou superiores a 13.2.3.39 |
