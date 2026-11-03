---
content_hash: e803abad93b4b21f2d7930eed5caa49727e756082bbe76f42e9e0560ca576d16
fetched_at: '2026-06-29T00:11:55.798580+00:00'
page_id: '864328740'
product: rm
source: tdn-rm
title: Gestão de Leitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864328740
version: 24
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Permissões de acesso**
3. **Visão da Gestão de Leitos**
4. **Detalhamento dos Pacientes**
5. **Reserva de Leito**
6. **Transferência de Paciente**
7. **Internação**
8. **Mapa de Ocupação de Leitos**

itensVisão Geral

## **01. VISÃO GERAL**

Este módulo tem como objetivo, permitir o usuário gerenciar os leitos do hospital ou clínica de forma facilitada e intuitiva, permitindo utilizar vários filtros e com alguns processos de manipulação do leito, como ocupar o mesmo vinculando este leito ao seu módulo, como atendimentos ou agendamento.

Permissões de acesso

## **02. PERMISSÕES DE ACESSO**

As permissões de acesso ficam localizadas no botão de seleção de módulos > Serviços Globais.

Aba Segurança > Perfis, editar seu perfil, então aba Acesso a Menus, e navegar em Hospitais e Clinicas > Atendimento > Internação > Gestão de leitos.

Neste módulo podemos visualizar as permissões:

* Reservar Leito - Permite selecionar um leito para reservar para o paciente.
* Ocupar Leito - Permite alterar o status de um leito para ocupado, quando o paciente possuir registro de atendimento ativo.
* Desfazer Ocupação - Permite desfazer a ocupação de um leito, se esta ocupação foi efetuada em menos de 60 minutos.
* Transferências e Internações - Permite visualizar os registros de transferências e internações do PEP.
Visão da Gestão de Leitos

## **03. VISÃO DA GESTÃO DE LEITOS**

O módulo de gestão de leitos está localizado em Atendimento > Internação > Gestão de Leitos.

Nesta visão é possível visualizar na lateral esquerda, informações sobre os módulos em que os pacientes estão associados, exibindo informações como a data da solicitação, reserva, cirurgia, leito, paciente, procedimento, etc...

Os módulos dos pacientes estão dividiso em duas abas "Aguardando" e "Agendados".

Na aba Aguardando são exibidos todos os registros de Transferência e Internação ativos lançados no PEP, é possível aplicar um filtro para determinar um período.  
Na aba Agendados são exibidos todos os registros de Cirurgias Agendadas e Pré-Registro de Internação. Para estes há um filtro para determinar um período, além de informar se é uma reserva e suas quantidades.

Na parte central visualizamos os leitos com informações básicas, como número do leito, unidade, gênero e status.

Os leitos exibidos são destacados com cores diferentes para cada situação do leito, como azul para ocupado ou verde para livre.  
Os card exibem no seu cabeçalho o número do leito e a situação.  
Dentro do card tem algumas informações básicas, como o gênero do leito, o tipo de acomodação, dias de ocupação e previsão de alta (a previsão de alta é destacada em vermelho caso a data da previsão da alta seja igual ou superior a data atual).

Acima dos leitos há um painel de filtros, onde os principais estão sempre sendo exibidos, e é possível expandir este painel para filtros avançados.

O Status Aguardando Supervisão somente irá aparecer no Mapa de Leitos caso o parâmetro **Utilizar status "Aguardando Supervisão" na Gestão de Leitos**estiver marcado, conforme documentação da .

Detalhamento dos Pacientes

## **04. DETALHAMENTO DOS PACIENTES**

Ao clicar no ícone de informações dos cards dos módulos dos pacientes, será exibido o detalhamento deste item.

Este detalhamento exibirá as informações do paciente, como nome, idade e gênero, e outras informações de acordo com o módulo, como dados de reservas, leitos, solicitante.

O detalhamento é diferente de acordo com o card de paciente, segue um exemplo para transferências:

Alguns campos, como a "Indicação Clínica" do detalhamento das Cirurgias Agendadas, pode conter um valor muito grande para ser exibido, com isso o conteúdo será "cortado" e adicionados três pontos demonstrando que há mais conteúdo, e exibirá uma opção "Ver Mais".

Ao clicar na opção "Ver Mais", a opção será alterada para "Ver Menos" e exibirá todo o conteúdo do campo.

Caso o paciente tenha reserva as seguintes informações serão mostradas:

Se havia uma reserva, porém ela foi cancelada, será informado quem realizou o cancelamento e a data/hora:

Reserva de Leito

## **05. RESERVA DE LEITO**

ReservaReservar

Ao clicar no ícone de informações no leito, serão exibidas algumas opções, onde uma delas é o "Reserva de Leito".

Clicando nesta opção, será exibida uma tela com as reservas atuais para este leito, permitindo adicionar novas reservas ou deletar as existentes.

Caso o leito esteja ocupado, além das informações de reserva, terá a opção "Informações", que exibe informações do leito selecionado, como nome, idade e gênero do paciente, convênio, plano e subplano, e dados do leito.

Esta tela possui um botão "Salvar", onde salvará a data de previsão de alta do paciente ocupando este leito.

Quando o leito possui reserva(s), é exibido um ícone no card do leito, e ao clicar no mesmo é exibida uma mensagem informando o paciente e a data da reserva do leito.

Cancelamento de Reserva

Ao clicar para excluir uma reserva no botão de ação da tabela de Reservas:

Será necessário informar **obrigatoriamente** o motivo do cancelamento e opcionalmente a observação do cancelamento.

Cadastro de Motivo

## **CADASTRO DE MOTIVO DE RESERVA / CANCELAMENTO**

Nesta tela é realizado o cadastro dos motivos, sendo eles do tipo Reserva, Cancelamento ou Ambos.

Transferência de Paciente

## **06. TRANSFERÊNCIA DE PACIENTE**

Ao clicar no ícone de informações no leito também é exibida a opção "Transferência de Paciente".

Esta opção abrirá uma tela para que seja identificado um paciente do módulo de Transferência, o motivo da transferência, data...

Ao clicar em "Salvar" será efetuada a transferência do paciente de um leito para outro.

Se a opção "Desocupar leito atual", o leito que o paciente está no momento será desocupado.

Se o parâmetro "**Executar o processo de Mudança de unidade de atendimento do paciente ao realizar a transferência de leito**" estiver ativo a unidade de atendimento do registro de atendimento será igual ao do Leito novo

Caso existam reservas para este leito no dia em questão para outros pacientes, será exibida uma mensagem de confirmação, onde só processará se o usuário confirmar.

Nesta tela há uma segunda aba "Histórico", que exibe o histórico de transferências de leito do paciente.

Internação

## **07. INTERNAÇÃO**

Ao clicar no ícone de informações no leito também é exibida a opção "Internação".

Esta opção abrirá uma tela para que seja identificado um paciente do módulo de Internações, o tipo de atendimento, observações e previsão de alta.

Ao clicar em "Salvar" será efetuada a transferência do tipo de paciente de "Externo" para "Interno".

Caso existam reservas para este leito no dia em questão para outros pacientes, será exibida uma mensagem de confirmação, onde só processará se o usuário confirmar.

O campo "Data Previsão Alta" é preenchido automaticamente ao selecionar o paciente, calculando a data de solicitação mais a quantidade de diárias.

Se ao selecionar o paciente não seja possível calcular uma data válida, como por exemplo uma data inferior a hoje, será exibida uma mensagem.

Mapa de Ocupação de Leitos

## **08. MAPA DE OCUPAÇÃO DE LEITOS**

O módulo de mapa de ocupação de leitos está localizado em Atendimento > Internação > Mapa de Ocupação de Leitos.

Esta opção exibirá todos os leitos, porém com informações míminas, assim dando melhor visibilidade a todos os leitos.  
Cada card exibe apenas o número do leito e sua situação atual.

No topo da tela há uma breve legenda de cada situação.

O Status Aguardando Supervisão somente irá aparecer no Mapa de Leitos caso o parâmetro **Utilizar status "Aguardando Supervisão" na Gestão de Leitos**estiver marcado, conforme documentação da .
