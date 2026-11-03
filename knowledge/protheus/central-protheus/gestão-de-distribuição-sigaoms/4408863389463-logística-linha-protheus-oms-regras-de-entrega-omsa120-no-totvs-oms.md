---
article_id: 4408863389463
category: Gestão de Distribuição (SIGAOMS)
content_hash: e40e3da689a01f66efc41a80c8ff5a3fe76ca27cf6b31e8001c02df1b5fab2be
fetched_at: '2026-06-28T22:45:50.124015+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Regras de Entrega - OMSA120 no TOTVS OMS
type: support-article
updated_at: '2022-12-01T11:11:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408863389463-Log%C3%ADstica-Linha-Protheus-OMS-Regras-de-Entrega-OMSA120-no-TOTVS-OMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como utilizar o cadastro de **Regras de Entrega - OMSA120** no **TOTVS OMS - Order Management System**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**A  rotina **Regras de Entrega - OMSA120,** permite configurar **regras** e **exceções de entrega** para um determinado **Cliente** ou **Grupo de Clientes**.  
  
Com as **Regras de Entrega** cadastradas, na rotina de **Montagem de Carga - OMSA200**, selecione os **pedidos que irão compor a carga**, utilize o botão **Seq. Ent.** para realizar o **sequenciamento de entregas**, nesse momento permite visualizar as **restrições cadastradas**.  
  
O Sistema disponibiliza a **visualização dos Pedidos com restrição** por meio do *status* da **entrega**, podendo ser:

* **Verde**: Entrega liberada. Indica que não existe regra de entrega ou a mesma foi atendida.
* **Amarelo**: Restrição por horário.
* **Vermelho**: Restrição por calendário. A entrega esta prevista para um determinado dia da semana ou mês em que o cliente não recebe entregas, de acordo com o cadastro de Calendários associado à regra do cliente.
* **Cinza**: Restrição por veículo. De acordo com a regra estabelecida, o cliente não aceita a entrega com o veículo designado para a mesma.

Exemplo:  
  
Na rotina **Regras de Entrega - OMSA120**, configurar que o **Cliente TOTSP** receberá apenas **veículo TRUCK 01** das **08:00 às 10:00** horas de **segundas e quartas-feiras**, conforme definido no **Calendário - OMSA350.**

**![CADASTRO_REGRAS1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4409019484311/CADASTRO_REGRAS1.JPG)**

![seq_entrega_1_verde.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4409020260503/seq_entrega_1_verde.JPG)

O resultado do exemplo acima foi atualizado com *status* igual a **verde**, pois a regra de entrega foi atendida.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *link's*:  
[Cadastro de Regras de Entregas - OMSA120](https://tdn.totvs.com/pages/viewpage.action?pageId=572494254)  
[Logística - Linha Protheus - OMS - Cadastro de Janela de Entregas - OMSA350](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408150146071-Log%C3%ADstica-Linha-Protheus-OMS-Cadastro-de-Janela-de-Entregas-OMSA350-)  
[Logística - Linha Protheus - OMS - Como determinar a sequencia entrega na Montagem da Carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008651541-Log%C3%ADstica-Linha-Protheus-OMS-Como-determinar-a-sequencia-entrega-na-Montagem-da-Carga)
