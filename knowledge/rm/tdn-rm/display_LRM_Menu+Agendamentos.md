---
content_hash: 1ee09c7e1701bc7cece8f3714872d09ce7ae3365175a48b3ed8d489e5f81167a
fetched_at: '2026-06-29T00:11:13.124512+00:00'
page_id: '656327205'
product: rm
source: tdn-rm
title: Menu Agendamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Menu+Agendamentos
version: 2
---

#FF9000Procedimentos para utilização

Neste menu podemos visualizar agendamentos para eventos criados nas propostas. Estes devem ser eventos relacionados a situação de uma proposta, exemplo: Uma proposta está na situação “Contrato em Assinatura” e nesta situação devemos solicitar o agendamento da assinatura do contrato e quem executa esta atividade é o usuário “Mestre TOTVS”, então criaremos um evento chamado ASSINATURA DO CONTRATO, associaremos este evento a situação da proposta “Contrato em Assinatura, para que toda proposta nesta situação, permita que seja agendado o evento.  Também devemos determinar qual grupo de usuários pode ter este evento associado, ou seja, quem será o responsável por esta ação.

Para realizar a parametrização acima vamos acessar *Backend > Globais > Eventos da agenda.* Ao inserir um novo registro será solicitado no nome deste evento e a quais situações de proposta este evento estará associado, ou seja, em quais situações de proposta eu consigo gerar um agendamento para este evento criado

Feita esta parametrização agora vamos determinar quais usuários podem ser associados ao evento de Assinatura de Contrato, ou seja, quem serão os usuários para quem vamos associar estes eventos quando estes forem definidos nas propostas. Para isto acesse Backend > Usuários > Grupos, edite o grupo desejado, role a tela deste grupo até o final. Aparecerá a opção “Mapa de Eventos da Agenda Autorizados para o Grupo”

Marque os eventos que este grupo de usuário é responsável e salve. A partir de agora, em todas as propostas que estão na situação de CONTRATO EM ASSINATURA aparecerá no menu de PROPOSTAS ou CONTRATOS uma opção chamada “Agendamento”, possibilitando a criação do evento de Assinatura do Contrato para a proposta selecionada, definindo um responsável por esta ação.

Ao clicar em agendamento podemos criar a agenda para o evento criado anteriormente.

Este evento, após salvo, aparecerá no menu AGENDAMENTOS no frontend do PVI. Portanto este menu será somente leitura, exemplificando os eventos já criados e disponíveis.
