---
content_hash: 9f9f6243ee6a5d647d6064eb64ce16ed3132aa23a3ebecaf0dfdc730715844c8
fetched_at: '2026-06-29T00:06:09.710669+00:00'
page_id: '203756425'
product: rm
source: tdn-rm
title: TSTDHW_DT_Cadastro_De_Chefe_Supervisor
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTDHW_DT_Cadastro_De_Chefe_Supervisor
version: 2
---

# CADASTRO DE CHEFE/SUPERVISOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Chefes / Supervisores* |
| **Situação/Requisito:** | *Ao editar alguns cadastros de supervisores, a lookup de Chapa não trazia o nome do funcionário corretamente.* |
| **Solução/Implementação:** | Ao criar a tela de cadastro de Supervisor, foi adicionado um filtro de seção na lookup de funcionários, mas o filtro não pode ser aplicado à edição, pois em caso de um supervisor expirado que existe por questões de histórico, a lookup de funcionário não estava trazendo o funcionário corretamente. O filtro de seção passou a não ser aplicado na lookup de funcionário em caso de edição, para que o funcionário seja encontrado em caso de ele já ter mudado de seção. |
| **Chamados relacionados:** | TSTDHW |
| **Versões/Release:** | *11.82.41* |
