---
content_hash: 84630fefca2518cf46f0c7905ef46034e42340fdc4852f36e1b6446d4d339f3a
fetched_at: '2026-06-29T00:09:48.470363+00:00'
page_id: '435105162'
product: rm
source: tdn-rm
title: Calcular Fechamento - Cálculos - Cálculo de Reservas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105162
version: 6
---

Ao executar o processo de **Calcular Fechamento** para o item de **Reservas**, serão gerados registros que irão compor o valor total dos lançamentos referentes ao condomínio. Desta forma, todas as reservas feitas no mesmo período de vigência do Fechamento calculado serão apuradas para a geração dos respectivos lançamentos.  
**OBSERVAÇÃO:** A Partir da Versão 12.1.2410 o processo passa a ser chamado de:***"****Apurar condomínio"***

Para o fácil entendimento do Cálculo de Reservas, vamos ver o seguinte exemplo:   
O Salão de Festas 1 (**Área Comum**) pertencente ao empreendimento Residencial Paris, unidade Torre Sul possui as reservas abaixo:

* Reserva 1: Período do evento: 03/02/2018 - 18:00 até 04/02/2018 - 08:00, onde o ocupante solicitante foi o João do 101 com a taxa de R$ 200,00 e Item de Cobrança A.
* Reserva 2: Período do evento: 10/02/2018 - 20:00 até 11/02/2018 - 08:00, onde o ocupante solicitante foi o Pedro do 403 com a taxa de R$ 100,00 e Item de Cobrança A.
* Reserva 3: Período do evento: 16/02/2018 - 22:00 até 18/02/2018 - 17:00, onde o ocupante solicitante foi o João do 101 com a taxa de R$ 500,00 e Item de Cobrança A.

Para este exemplo, o cadastro de Fechamento para calcular estas reservas deverá ter a competência de 02/2018 informando também o mesmo empreendimento no caso Residencial Paris.  
Após realizar o processo de Calcular Fechamento, serão gerados os seguintes registros originados da Reserva:

* Reserva 1: Empreendimento Residencial Paris, Torre Sul, Solicitante João do 101 no valor de R$ 200,00 e Item de Cobrança A.
* Reserva 2: Empreendimento Residencial Paris, Torre Sul, Solicitante Pedro do 403 no valor de R$ 100,00 e Item de Cobrança A.
* Reserva 3: Empreendimento Residencial Paris, Torre Sul, Solicitante João do 101 no valor de R$ 500,00 e Item de Cobrança A.

Cada linha acima, será um registro no histórico do Fechamento, podendo ser visualizadas em **Condomínio / Fechamento do Condomínio / Histórico de Cálculos**.

ObservaçõesCaso o Item de Cobrança não seja informado no cadastro da Reserva, o sistema irá utilizar o Item de Cobrança informado no cadastro de **Áreas Comuns;**  
Os Itens de Cobrança serão utilizados para compor o valor do lançamento a ser gerado para o ocupante solicitante da reserva, pois os o cadastro de Itens de Cobrança existe um espaço para associar um ou mais **Valores de Integração**. Lembrando que os registros de Valores de Integração tem origem no **TOTVS Gestão Financeira.**

Lembrando que para criar registros de reserva, basta acessar **Menu de Condomínio / Áreas Comuns / Reserva de Áreas Comuns** do **TOTVS Incorporação**.

Veja Também
