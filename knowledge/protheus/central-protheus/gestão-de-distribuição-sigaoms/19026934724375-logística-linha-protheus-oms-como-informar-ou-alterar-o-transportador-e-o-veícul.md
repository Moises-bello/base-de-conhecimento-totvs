---
article_id: 19026934724375
category: Gestão de Distribuição (SIGAOMS)
content_hash: c5614c35fa2d47fe9dc6323033bdf1409f2766ba86e571c47bee589ba01889cc
fetched_at: '2026-06-28T22:45:49.712123+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como informar ou alterar o Transportador
  e o Veículo na Montagem de Carga?
type: support-article
updated_at: '2024-02-29T13:59:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19026934724375-Log%C3%ADstica-Linha-Protheus-OMS-Como-informar-ou-alterar-o-Transportador-e-o-Ve%C3%ADculo-na-Montagem-de-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19026945540247) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como informar ou alterar Transportador e o Veículo no **OMSA200 -** **Montagem de Carga**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**A rotina **OMSA200 -** **Montagem de Carga**, permite informar ou alterar o Transportador e o Veículo na criação da Carga ou após a sua criação.Exemplos de Utilização:

1. Menu **SIGAOMS**;
2. Atualizações;
3. Cargas;
4. Carregamento;
5. Montagem de Carga

Na inclusão de uma nova carga, após selecionar os pedidos que irão compor a carga, acesse o botão de Outras Ações > Veículo e ou Transp.:

**![kcs 1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/20989119694871)**

Salve a inclusão da carga, em seguida será criada  a carga com os dados do Veículo e Transportador.

![kcs2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21005548401943)

**Outra forma de utilização:**

1. Menu **SIGAOMS**;
2. Atualizações;
3. Cargas;
4. Carregamento;
5. Associar Veiculo

Na tela de **Associação de Veiculo** é possível alterar ou incluir os dados de Veículo ou Transportador**:**

**![kcs3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/21005517321623)**

O Pedido de Venda pode conter informações de Veículo e Transportador, caso na carga for informado outro Transportador ou Veículo, ou seja, diferente do que está no Pedido de Venda, automaticamente os campos **Veic. Transp -** **C5\_VEICULO** e **Transp. - C5\_TRANSP** serão atualizados. Esse tipo de alteração é utilizada na carga quando por algum motivo o Transportador ou Veículo não irá mais atender a carga em questão.Para atualizar o **Veic. Transp - C5\_VEICULO**, dependerá do parâmetro informado no **F12** da rotina **OMSA200**. Segue o parâmetro:

![kcs4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21005548442519)

Com a carga Faturada, no produto padrão é possível informar ou alterar o Transportador. Essa manutenção na carga irá atualizar o campo **Transp. -** **F2\_TRANSP**.  
Caso desejar bloquear essa ação, dispomos os **Pontos de Entradas** abaixo:

* **OS200ASS - Associar veículos nas cargas**
* **OM200VEI - Validação de Veículo**
* **OS200MNT - Associação do Veículo na Carga**

**Importante**Ao estornar uma carga, cuja o Pedido de venda esteja com Transportador informado no campo **Transp. - C5\_TRANSP** e não exista Transportador vinculado a carga no campo **Código da Transportadora -  DAK\_TRANSP**, o Sistema manterá os dados do Transportador no Pedido de Venda.  
  
Caso seja informado um Transportador na Montagem de Carga, este será assumido para todos os Pedidos de Venda envolvidos na Carga. E no caso de estorno desta carga o campo **Transp. - C5\_TRANSP** será limpo automaticamente.   
 **Saiba mais**Mais informações sobre a rotina **OMSA200** e seus **Pontos de Entradas** estão disponíveis nos *links* abaixo:[Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000900021-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-OMSA200)
