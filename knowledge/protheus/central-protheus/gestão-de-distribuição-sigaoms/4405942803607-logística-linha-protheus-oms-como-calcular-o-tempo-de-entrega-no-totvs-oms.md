---
article_id: 4405942803607
category: Gestão de Distribuição (SIGAOMS)
content_hash: 1022d5520cc7998bcf4ea87104203db92fdf6be69587202b94ac73c363358b26
fetched_at: '2026-06-28T22:45:49.629956+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Como calcular o tempo de entrega no TOTVS
  OMS '
type: support-article
updated_at: '2021-08-23T17:23:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405942803607-Log%C3%ADstica-Linha-Protheus-OMS-Como-calcular-o-tempo-de-entrega-no-TOTVS-OMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:36 min****Dúvida**Como calcular o **tempo de entrega** no **TOTVS OMS - **Ord**er Management System**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Na **Montagem de Carga - OMSA200**, é possível visualizar a **sequencia de entrega**, onde o usuário poderá verificar se o pedido irá atender a regra de entrega do **cliente ou das rotas**.  
De acordo com os tempos médios de deslocamento informados nos cadastros de **Zonas - OMSA070**, **Setores por Zona - OMSA080**,  e **Rotas - OMSA090**,  o Sistema efetua o cálculo da hora de chegada prevista no cliente.  
  
Abaixo descrevemos exemplos que poderão ser configurados:  
 **Cenário 1**:  
 **Cadastro Zonas - OMSA070:** Zona código 01, com tempo de 04:00 - campo **DA5\_TEMPO****Cadastro** **Setores por Zona - OMSA080:**  
Setor código 1, com tempo de 00:50 - campo **DA6\_TEMPO**  
Setor código 2, com tempo de 00:30 - campo **DA6\_TEMPO****Cadastro Pontos por Zona e Setor - OMSA090:**Cliente 004585 - **SETOR 1**   
Cliente PFISIC - **SETOR 1**   
Cliente CLI002 - **SETOR 1**   
Cliente 003959 - **SETOR 2**   
  
**Cadastro** **Rotas - OMSA100:**Rota código 01, com tempo de 02:00 - campo **DA8\_TEMPO**  
Nesse exemplo, estamos utilizando os Pedidos de venda abaixo:  
Pedido **000194 - Cliente 004585**  
Pedido **000195 - Cliente PFISIC**  
Pedido **000196 - Cliente CLI002**  
Pedido **000197 - Cliente 003959**  
  
Considerando horário inicial para as entregas a partir das 08:00, temos o resultado abaixo:

* **Cliente 004585:** entrega programada para às **10:00**.Está considerando o tempo informado na rota de 2 Horas.
* **Cliente PFISIC:** entrega programada para às **10:50**.Está considerando o horário da entrega anterior às 10:00, acrescentando **00:50** informado no Setores por Zona, campo **DA6\_TEMPO** para **SETOR 1**.
* **Cliente CLI002:** entrega programada para às **11:40**.Está considerando o horário da entrega anterior às 10:50, acrescentando **00:50** informado no Setores por Zona, campo **DA6\_TEMPO** para **SETOR 1**.
* **Cliente 003959:** entrega programada para às **17:40**.Está considerando o horário da entrega anterior às 11:40, acrescentando **04:00** informado na Zona, campo **DA5\_TEMPO +**  02:00 informado na Zona, campo **DA8\_TEMPO.**

**Exemplo dos cadastros descritos acima, localizados em Atualizações/Roteirização:**

![CADASTROS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405967245847/CADASTROS.png)

**Exemplo de como ficará a Montagem de Carga, Rota, Zona e Setores por Zona, localizado em Atualizações/Cargas:**

**![MONTAGEM_CARGA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405967284631/MONTAGEM_CARGA.png)**

**Exemplo de como ficará a Montagem de Carga/Outras Ações/Sequencia de Entrega - OMSA200, localizado em Atualizações/Cargas:**

**![SEQUENCIA_ENTREGA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405967300119/SEQUENCIA_ENTREGA.png)**

**Exemplo de como ficará a Simulação de Carga - OMSA220, localizado em Atualizações/Cargas:**

**![SIMULACAO_ENTREGA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405958831127/SIMULACAO_ENTREGA.png)**

**Importante**  
O campo **DA5\_TEMPO,** será considerado quando existir pedidos de venda em SETORES DIFERENTES, onde o Sistema realiza o recalculo do valor total do tempo de entrega para todos os níveis: Rota + Zona + Setores. Os resultados apresentados na rotina de **Simulação de Carga - OMSA220** é um espelho da rotina **Montagem de Carga - OMSA200**.  
  
**Cenário 2:**Considerando os mesmos cadastros utilizados no Cenário 1  
  
**Cadastro Zonas - OMSA070:** Zona código 01, com tempo de 04:00 - campo **DA5\_TEMPO** **Cadastro** **Setores por Zona - OMSA080:**  
Setor código 1, com tempo de 00:50 - campo **DA6\_TEMPO**  
Setor código 2, com tempo de 00:30 - campo **DA6\_TEMPO****Cadastro Pontos por Zona e Setor - OMSA090:**Cliente 004585 - **SETOR 1**   
Cliente PFISIC - **SETOR 1**   
Cliente CLI002 - **SETOR 1**   
  
**Cadastro Rotas - OMSA100:**Rota código 01, com tempo de 02:00 - campo **DA8\_TEMPO**  
Nesse exemplo, estamos utilizando os Pedidos de venda abaixo:  
Pedido **000194 - Cliente 004585**  
Pedido **000195 - Cliente PFISIC**  
Pedido **000196 - Cliente CLI002**Considerando horário inicial para as entregas a partir das 08:00, temos o resultado abaixo:

* **Cliente 004585:** entrega programada para às **10:00**.Está considerando o tempo informado na rota de 2 Horas.
* **Cliente PFISIC:** entrega programada para às **10:50**.Está considerando o horário da entrega anterior às 10:00, acrescentando **00:50** informado no Setores por Zona, campo **DA6\_TEMPO** para **SETOR 1**.
* **Cliente CLI002:** entrega programada para às **11:40**.Está considerando o horário da entrega anterior às 10:50, acrescentando **00:50** informado no Setores por Zona, campo **DA6\_TEMPO** para **SETOR 1**.

**Exemplo de como ficará a Montagem de Carga - OMSA200, localizado em Atualizações/Cargas:**

**![MONTAGEM_CARGA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405967284631/MONTAGEM_CARGA.png)**

**Exemplo de como ficará a Montagem de Carga/Outras Ações/Sequencia de Entrega - OMSA200, localizado em Atualizações/Cargas:**

**![SEQUENCIA_ENTREGA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405967300119/SEQUENCIA_ENTREGA.png)**

**Exemplo de como ficará a Simulação de Carga - OMSA220, localizado em Atualizações/Cargas:**

**![SEQUENCIA_ENTREGA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405967300119/SEQUENCIA_ENTREGA.png)**

**Importante**Nesse cenário **todos os clientes** estão para o **mesmo SETOR 1**, onde está sendo considerado o tempo informado no campo **DA6\_TEMPO**. Esse campo será considerado apenas quando na carga existirem pedidos de vendas para vários clientes. O tempo informado no campo **DA6\_TEMPO** será considerado como transição de um cliente para outro.  
  
**Saiba mais**Mais informações poderão ser acessadas no *link's*:  
[Logística - Linha Protheus - OMS - Cadastros Básicos para utilização do TOTVS OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021897892-MP-OMS-Cadastros-B%C3%A1sicos-para-utiliza%C3%A7%C3%A3o-do-SIGAOMS)[Logística - Linha Protheus - OMS - Busca do CEP a ser considerado na Montagem de Carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027564691-MP-OMS-Busca-do-CEP-a-ser-considerado-na-Montagem-de-Carga)[Logística - Linha Protheus - OMS - Como determinar a sequencia entrega na Montagem da Carga](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008651541-Log%C3%ADstica-Linha-Protheus-OMS-Como-determinar-a-sequencia-entrega-na-Montagem-da-Carga)  
[Simulação de Entrega - OMSA220](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=572021874#Simula%C3%A7%C3%A3odeEntrega(OMSA220-SIGAOMS)-SimularaEntrega)   
[Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)
