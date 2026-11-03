---
article_id: 39766677923351
category: Gestão de Distribuição (SIGAOMS)
content_hash: 5abd458626e590ab639685692f68d3203735b02bf53933797cc20f0b32066799
fetched_at: '2026-06-28T22:45:49.810312+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE
  com Cliente de Entrega Diferente do Cliente Principal
type: support-article
updated_at: '2026-05-29T17:44:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39766677923351-Log%C3%ADstica-Linha-Protheus-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOL-TRE-com-Cliente-de-Entrega-Diferente-do-Cliente-Principal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39766663964695) Tempo aproximado para leitura: **00:02:24 min**  
  
**Dúvida**  
O TOTVS OMS permite o envio de pedidos para TOL/TRE quando o cliente de entrega é diferente do cliente principal?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
No processo de **Pedidos de Venda - MATA410**, ao informar um **Cliente de Entrega - C5\_CLIENT** diferente do **Cliente Principal - C5\_CLIENTE,** o Sistema passa a considerar automaticamente o cliente de entrega como referência para o endereço de entrega do pedido.

Quando existe um Cliente Principal com múltiplos endereços de entrega, a recomendação padrão no **ERP Protheus** é realizar a duplicação do cadastro do cliente, diferenciando-os pelo campo Loja.

As informações relacionadas ao **Cliente de Retirada ou Cliente de Remessa** não são contempladas na rotina de **Montagem de Carga - OMSA200**, tampouco no processo de integração com **TOL/TRE**.

A rotina de **Envio de Pedidos - OMSXCPL6** segue o mesmo comportamento da **MATA410** quando integrada à **Montagem de Carga**. Ou seja, ao definir um cliente de entrega diferente do cliente principal no pedido de venda, os dados considerados e enviados como endereço de entrega serão sempre os do cliente de entrega informado.

**Exemplo de utilização:**

1. No cadastro de **Clientes - MATA030**, certifique-se de que existem registros duplicados para o mesmo cliente, diferenciados pelo código da Loja, onde cada loja possui o seu respectivo endereço cadastrado (Exemplo: Cliente João da Silva Loja 01 para endereço principal, Loja 02 para o segundo endereço).
2. Na rotina de **Pedido de Venda - MATA410**, informe no campo **Cliente Principal - C5\_CLIENTE** o cadastro correspondente à Loja 01.
3. No campo **Cliente de Entrega - C5\_CLIENT**, informe o cadastro correspondente à loja com o endereço desejado, por exemplo, Loja 02.
4. Com essa configuração, o sistema considerará corretamente o Endereço de Entrega da Loja 02 na integração e o comportamento será mantido de forma consistente entre as rotinas **MATA410**, **OMSXCPL6** e **OMSA200**.

A seguir, apresenta-se um exemplo desse comportamento na rotina de **Montagem de Carga e Envio de Pedidos ao TOL/TRE:**  
  
**Pedido de Venda:**

![PEDIDO_CLIE ENTREGA.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/39774256037527)

**Montagem de Carga:**

![OMSA200_CLIENTE ENTREGA.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/39774256038423)

**Arquivo XML enviado ao TOL/TRE:**

![xml.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/39774270701207)

**Importante**  
Para alterar informações no arquivo **XML** enviado ao **TOL/TRE**, disponibilizamos o Ponto de Entrada [OMSXCPL1](https://tdn.totvs.com/display/public/PROT/DT+PE+OMSXCPL1+-+Permite+alterar+o+XML+antes+do+envio+para+o+TOL)  
  
**Saiba mais**  
Mais informações poderão ser acessadas nos *link's*:   
[Envio de Pedidos de Venda - OMSXCPL6](https://tdn.totvs.com/pages/viewpage.action?pageId=549492947)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003568682-MP-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-Integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
