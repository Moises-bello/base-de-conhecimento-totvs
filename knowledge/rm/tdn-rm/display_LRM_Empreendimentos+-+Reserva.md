---
content_hash: d1d646e4685e1cbd80b150cade4ca76b575eba557d9817330a185667d5ac2e8d
fetched_at: '2026-06-29T00:11:06.894694+00:00'
page_id: '636309404'
product: rm
source: tdn-rm
title: Empreendimentos - Reserva
type: documentation
url: https://tdn.totvs.com/display/LRM/Empreendimentos+-+Reserva
version: 8
---

O Portal de Vendas trabalha com o conceito de reservas e fila de reservas. Isto significa que um corretor pode reservar uma unidade de um empreendimento para si, por um prazo definido.

A quantidade de reservas que um corretor pode fazer podem ser definidos em 

Uma reserva está vinculada ao corretor e a uma unidade de um empreendimento. Por padrão o Portal de Imóveis só permite uma proposta ativa por unidade reservada. (vide parâmetros de situação de propostas para determinar quais situações de propostas são consideradas ativas) .

Para realizar uma reserva, o usuário deverá clicar no botão de "Simular Propostas" ou “Mapa de Disponibilidade” e em seguida clicar sobre reservar.

Reserva pelo botão “Simular propostas” Reserva pelo “Mapa de Disponibilidade”Reserva pela “Imagem de Disponibilidade do Empreendimento”

Uma vez o corretor A tenha efetuado uma reserva para a unidade 49, o corretor B também poderá reservar a mesma unidade mas somente o corretor A poderá salvar uma proposta, pois ele é dono da reserva atual. O corretor B será avisado por e-mail caso a reserva dele entre em vigor, devido ao cancelamento ou expiração da reserva do corretor A.

O Portal de Imóveis controla dois tipos de reservas, sendo a primeira somente uma reserva quando um corretor clica no botão de reservas e a segunda quando esta reserva é feita por uma proposta criada. Cada um dos tipos de reservas podem ter prazos (em horas) diferentes por empreendimento. Para isto basta entrar em BACKEND > EMPREENDIMENTOS e definir os prazos de tempo em reservas e propostas.

* Parâmetros em backend > empreendimentos (primeira aba do cadastro de empreendimentos)

Os parâmetros globais para todas as propostas caso o parâmetro do cadastro de empreendimento esteja zerado se encontra em (Backend > parâmetros > Unidades).  

Fila de reserva

Quando uma reserva é feita o sistema demonstra no topo da tela de simulação de propostas a reserva e seu prazo para expirar. Neste momento a unidade reservada tem seu status alterado conforme parâmetro de situação de propostas. Ao final do prazo de validade de uma reserva a unidade voltará para seu status padrão "UNIDADE DISPONÏVEL" caso não exista uma reserva aguardando na fila.

* Uma fila de reservas é quando dois ou mais corretores selecionaram a mesma unidade. O Portal de Imóveis controla a ordem das reservas no momento em que estas foram selecionadas. Caso uma unidade tenha duas reservas, ao expirar a primeira o Portal de Imóveis assume a segunda automaticamente. Antes de uma reserva expirar o Portal envia e-mail ao usuário ativo da reserva informando o prazo que falta para a reserva cair. Quando uma reserva que estava em aguardo é ativada o usuário receberá um e-mail informando que a reserva deste está no ar.

Tela indicativa de reservas numa unidade. Demonstra o total de reservas que existem em uma unidade.

Para verificar todas as reservas existentes em um empreendimento, o Portal de Imóveis demonstra na visão deste empreendimento a existência destas reservas através do card "Reservados" . Ao clicar no hiperlink ou no botão Reservas todas as reservas neste empreendimento e seus respectivos prazos e usuários são demonstrados.

Além disso, dentro desta visão será possível também realizar uma proposta diretamente, dando mais rapidez ao processo.  
Basta clicar no botão de reserva dentro do campo de ações da reserva.

Reserva com nome do prospect 

Uma reserva pode ser realizada solicitando os dados do prospect com o parâmetro **Reservas: informar dados básico do prospect ao reservar unidade ()** habilitado, abrirá a janela abaixo ao clicar em reservar uma unidade para associar as informações do prospect
