---
content_hash: 8c1eae006c58c8a697288d0420ff4b1e08c3ab1c669bab5b1fa5a89acb487fd1
fetched_at: '2026-06-29T00:12:03.589332+00:00'
page_id: '911862412'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Cálculos - Reserva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911862412
version: 2
---

Ao executar o processo de **Apurar Condomínio** para o item de **Reservas**, serão gerados registros que irão compor o valor total dos lançamentos referentes ao condomínio. Desta forma, todas as reservas feitas no mesmo período de vigência do Fechamento calculado para determinada subunidade, serão apuradas para a geração dos respectivos lançamentos.

Para o fácil entendimento do Cálculo de Reservas, vamos ver o seguinte exemplo:   
O Salão de Eventos (**Área Comum**) pertencente ao Empreendimento X, Unidade A possui as reservas abaixo:

* Reserva 1: Período do evento: 03/02/2018 - 18:00 até 04/02/2018 - 08:00, onde o ocupante solicitante foi a Loja X da LUC1 com a taxa de R$ 200,00 e Item de Cobrança A.
* Reserva 2: Período do evento: 10/02/2018 - 20:00 até 11/02/2018 - 08:00, onde o ocupante solicitante foi a Loja Y da LUC2 com a taxa de R$ 100,00 e Item de Cobrança A.
* Reserva 3: Período do evento: 16/02/2018 - 22:00 até 18/02/2018 - 17:00, onde o ocupante solicitante foi a Loja Z da LUC3 com a taxa de R$ 500,00 e Item de Cobrança A.

Para este exemplo, o cadastro de Fechamento para calcular estas reservas deverá ter a competência de 02/2018 informando também o mesmo empreendimento no caso Empreendimento X  
Após realizar o processo de **Apurar Condomínio**, selecionando as LUC's acima (Subunidades), serão gerados os seguintes registros originados da Reserva:

* Reserva 1: Empreendimento X, Unidade A, Solicitante Loja X da LUC1 no valor de R$ 200,00 e Item de Cobrança A.
* Reserva 2: Empreendimento X, Unidade A, Solicitante Loja Y da LUC2 no valor de R$ 100,00 e Item de Cobrança A.
* Reserva 3: Empreendimento X, Unidade A, Solicitante Loja Z da LUC3 no valor de R$ 500,00 e Item de Cobrança A.

Cada linha acima, será um registro referente a cada subunidade, podendo ser visualizadas no anexo de Apurações do Condomínio no Processo de Reserva.

ObservaçõesCaso o Item de Cobrança não seja informado no cadastro da Reserva, o sistema irá utilizar o Item de Cobrança informado no cadastro de **Áreas Comuns;**  
Os Itens de Cobrança serão utilizados para compor o valor do lançamento a ser gerado para o ocupante solicitante da reserva****.****

Lembrando que para criar registros de reserva, basta acessar ***Menu de Condomínio / Áreas Comuns / Reserva de Áreas Comuns** do **TOTVS Incorporação**.*

Veja Também
