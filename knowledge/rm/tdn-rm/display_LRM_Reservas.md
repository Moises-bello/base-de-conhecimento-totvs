---
content_hash: a267b2d5596e4adcd25b3b4a433e490192e40c63e90c331bc92e05b90181a908
fetched_at: '2026-06-29T00:11:13.095707+00:00'
page_id: '656317369'
product: rm
source: tdn-rm
title: Reservas
type: documentation
url: https://tdn.totvs.com/display/LRM/Reservas
version: 2
---

#FF9000Introdução

O Portal de Vendas trabalha com o conceito de reservas e fila de reservas. Isto significa que um corretor pode reservar uma unidade de um empreendimento para si, por um prazo definido. A quantidade de reservas que um corretor pode fazer pode ser definido em parâmetros globais  *(backend > parâmetros > Unidade.)*

Ou no grupo do usuário:

E por ultimo no cadastro do usuário.

Desta forma podemos ter um parâmetro global para todos os usuários e um usuário específico que tenha uma possibilidade de reserva diferente dos demais.

Um reserva está vinculada ao corretor e a uma unidade de um empreendimento. Por padrão o Portal de Imóveis só permite uma proposta ativa por unidade reservada. (vide parâmetros de situação de propostas para determinar quais situações de propostas são consideradas ativas).

#FF9000Procedimentos para Utilização

Para realizar uma reserva, o usuário deverá clicar no botão de "Simular Propostas" ou “Mapa de Disponibilidade” e em seguida clicar sobre reservar.

Uma vez o corretor A tenha efetuado uma reserva para a unidade 101, o corretor B também poderá reservar a mesma unidade mas somente o corretor A poderá salvar uma proposta, pois ele é dono da reserva atual. O corretor B será avisado por e-mail caso a reserva dele entre em vigor, devido ao cancelamento ou expiração da reserva do corretor A.

Reserva pelo botão “Simular propostas” 

Reserva pelo “Mapa de Disponibilidade”

Reserva pela “Imagem de Disponibilidade do Empreendimento”

O Portal de Imóveis controla dois tipos de reservas, sendo a primeira somente uma reserva quando um corretor clica no botão de reservas e a segunda quando esta reserva é feita por uma proposta criada. Cada um dos tipos de reservas podem ter prazos (em horas) diferentes por empreendimento. Para isto basta entrar em *BACKEND > EMPREENDIMENTOS* e definir os prazos de tempo em reservas e propostas.

Parâmetro global para todas as propostas caso o parâmetro do cadastro de empreendimento esteja zerado. (Backend > parâmetros > Unidades

Parâmetros em backend > empreendimentos (primeira aba do cadastro de empreendimentos)

Quando uma reserva é feita o sistema demonstra no topo da tela de simulação de propostas a reserva e seu prazo para expirar. Neste momento a unidade reservada tem seu status alterado conforme parâmetro de situação de propostas. Ao final do prazo de validade de uma reserva a unidade voltará para seu status padrão "UNIDADE DISPONÏVEL" caso não exista uma reserva aguardando na fila.

Uma fila de reservas é quando dois ou mais corretores selecionaram a mesma unidade. O Portal de Imóveis controla a ordem das reservas no momento em que estas foram selecionadas. Caso uma unidade tenha duas reservas, ao expirar a primeira o Portal de Imóveis assume a segunda automaticamente. Antes de uma reserva expirar o Portal envia e-mail ao usuário ativo da reserva informando o prazo que falta para a reserva cair. Quando uma reserva que estava em aguardo é ativada o usuário receberá um e-mail informando que a reserva deste está no ar.

Para verificar todas as reservas existentes em um empreendimento, o Portal de Imóveis demonstra na visão deste empreendimento a existência destas reservas através do botão RESERVAS DO EMPREENDIMENTO (botão vermelho da tela abaixo). Ao clicar neste botão todas as reservas neste empreendimento e seus respectivos prazos e usuários são demonstrados.

Botão indicador de que existem reservas no Empreendimento

Após clicar sobre o botão de reservas do empreendimento, é exibida a janela contendo todas as reservas existentes no empreendimento.
