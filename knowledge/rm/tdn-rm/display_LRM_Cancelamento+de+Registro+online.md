---
content_hash: 6a3fb915ba0f747636af208e154443d31d7205ba2a329d8b47417bb5ffdca8f7
fetched_at: '2026-06-29T00:11:39.229473+00:00'
page_id: '788621873'
product: rm
source: tdn-rm
title: Cancelamento de Registro online
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelamento+de+Registro+online
version: 15
---

O processo de cancelamento do registro online tem como objetivo efetuar o cancelamento do registro online, via comunicação direta com o serviço do banco, de um grande volume de boletos através da tela padrão de filtro\* do RM, sem a necessidade do usuário acessar a visão de boletos.

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco. O TOTVS Gestão Financeira disponibiliza dois modelos de cancelamento de registro:

Cards2Modelo de Registro Online v1

Processo disponível atualmente apenas para o (s) seguinte (s) banco (s):

* AutBank (Crefisa/b.Uni) a partir do release 2506

**Importante**: A opção de Modelo de Registro Online do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845) deve ser selecionada como API 'v1'. 

3Modelo de Registro Online v2

Processo disponível atualmente apenas para os seguintes bancos:

* Itaú
* SICOOB
* Banco do Brasil.  Obs: O cancelamento do registro poderá ser realizado após 30min do registro do boleto junto ao Banco. Caso tente cancelar antes deste prazo, o Banco poderá retornar uma mensagem com este aviso.
* Santander
* Bradesco (a partir do release 2410)
* Sicredi (a partir do release 2502)

**Importante**: A opção de Modelo de Registro Online do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845) deve ser selecionada como API 'v2'. 

4Modelo de Registro Online v3

Processo disponível atualmente apenas para o (s) seguinte (s) banco (s):

* SICOOB

**Importante**: A opção de Modelo de Registro Online do [Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845) deve ser selecionada como API 'v3'. 

**\*Filtro**

A definição do filtro é essencial no processo para contemplar os boletos que serão submetidos ao processo de cancelamento do registro online. Vale ressaltar que não é possível utilizar a opção de filtro de datas dinâmicas ("$hoje", "$Hoje - 1", "$NaSemana", etc) **em conjunto** com filtro de variáveis de parâmetro de usuário ("Status da remessa = Pendente Remessa", por exemplo). Além disso, apenas boletos com os status CNAB 'Registrado Online', 'Registrado' ou 'Pendente Remessa' serão submetidos a este processo.

O processo não será interrompido caso algum boleto apresente divergência, exibindo ao final da execução o Log para os devidos ajustes.

Há também a opção de realizar o processo agendado e de forma recorrente, através do menu Movimentações Bancárias | Integração Bancária | Processos em Lote | [Cancelamento de Registro Online Por Filtro](https://tdn.totvs.com/display/LRM/Cancelamento+de+Registro+Online+Por+Filtro).
