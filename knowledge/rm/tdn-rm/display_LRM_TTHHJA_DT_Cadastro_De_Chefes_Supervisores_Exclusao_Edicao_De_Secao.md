---
content_hash: 5dc51c735c05e65718f9f443cfffc0a23ec2fbe39f8d99626aea1265c346cccc
fetched_at: '2026-06-29T00:06:09.714349+00:00'
page_id: '203756508'
product: rm
source: tdn-rm
title: TTHHJA_DT_Cadastro_De_Chefes_Supervisores_Exclusao_Edicao_De_Secao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHHJA_DT_Cadastro_De_Chefes_Supervisores_Exclusao_Edicao_De_Secao
version: 4
---

# CADASTRO DE CHEFE/SUPERVISOR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Chefes / Supervisores* |
| **Situação/Requisito:** | *Ao editar alguns cadastros de supervisores, a lookup de Chapa não   trazia o nome do funcionário corretamente e ao tentar excluir ou editar uma   seção as informações não eram corretas.* |
| **Solução/Implementação:** | *Ao criar a tela de cadastro de Supervisor, foi adicionado um filtro de   seção na lookup de funcionários, mas o filtro não pode ser aplicado à edição,   pois em caso de um supervisor expirado que existe por questões de histórico,   a lookup de funcionário não estava trazendo o funcionário corretamente. O   filtro de seção passou a não ser aplicado na lookup de funcionário em caso de   edição, para que o funcionário seja encontrado em caso de ele já ter mudado   de seção. Adicionado uma mensagem quando tentar excluir ou editar uma   seção pela tela de Chefe e Supervisores* |
| **Chamados   relacionados:** | *TTHHJA* |
| **Versões/Release:** | *12.1.8* |
