---
content_hash: 6e9e78ef7bdab07e615ec0e5e51fdc24f963e7d1a77eaf2b9e5fdc0d3ae168a1
fetched_at: '2026-06-29T00:09:39.474226+00:00'
page_id: '431671679'
product: rm
source: tdn-rm
title: DT Portal TOP - Gerar um novo Pedido de Material
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Portal+TOP+-+Gerar+um+novo+Pedido+de+Material
version: 6
---

# GERAR PEDIDO DE MATERIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Obras e Projetos. |
| **Função:** | Portal TOTVS Obras e Projetos - Pedido de Material. |
| **Situação/Requisito:** | Criar uma página web para gerar um novo pedido de material através do portal do TOP.  É necessário criar a funcionalidade de acordo com os protótipos:  <http://jiraproducao.totvs.com.br/browse/CPAPP01-364> |
| **Solução/Implementação:** | Foi desenvolvido o formulário para gerar um novo pedido de material de forma responsiva para os dispositivos: mobile, tablet e desktop.   * A escolha da origem dos dados é feita com base nos parâmetros de projeto para verificar se utiliza planilha de serviços e também faz a verificação se está integrado com o Protheus ou EMS. * Os tipos de requisição são exibidos de acordo com a definição de utilização e nomes nos parâmetros de projeto. * O pedido de material pode ser gerado escolhendo um intervalo de tarefas ou tarefa por tarefa. * Os insumos são filtrados pelas tarefas, períodos, planilha, tipo de requisição e grupos de custos. * Serão feitas as mesmas validações de geração do pedido de material em função do histograma estar calculado, existência de máscara de pedido ou necessidade do cálculo do projeto.   A tela possui um botão para cancelar o novo pedido e ser redirecionado para a página de listagem dos pedido de material. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | [TOPORCAPLAN001-5177](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-5177). [TOPORCAPLAN001-5327](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-5327). TOPORCAPLAN001-6520 |
| **Requisito:** | [TOPORCAPLAN001-5162](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-5162). [TOPORCAPLAN001-5288](http://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-5288). |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
