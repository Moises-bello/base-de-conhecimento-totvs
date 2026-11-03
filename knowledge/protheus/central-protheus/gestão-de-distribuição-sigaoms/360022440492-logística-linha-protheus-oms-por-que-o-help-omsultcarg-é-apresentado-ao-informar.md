---
article_id: 360022440492
category: Gestão de Distribuição (SIGAOMS)
content_hash: a78b2509fdd4cdc328f10f56fd42f3a26b362836b68aeedcd2814509ce002f4c
fetched_at: '2026-06-28T22:45:50.060342+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Por que o help OMSULTCARG é apresentado
  ao informar o veículo na Montagem de Carga - OMSA200
type: support-article
updated_at: '2021-12-21T19:28:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022440492-Log%C3%ADstica-Linha-Protheus-OMS-Por-que-o-help-OMSULTCARG-%C3%A9-apresentado-ao-informar-o-ve%C3%ADculo-na-Montagem-de-Carga-OMSA200
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:54min  
  
Dúvida**Por que o **help OMSULTCARG - Veículo não comporta a capacidade da carga** é apresentado ao informar o **veículo na Montagem de Carga - OMSA200**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Para que o **help** **OMSULTCARG**, seja apresentado, o Sistema verifica o parâmetro **Consid. Restrição?** na montagem da carga, após selecionar os pedidos e informar o veículo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013809702/mceclip1.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013815022/mceclip3.png)

Se o parâmetro **Consid. Restrição?** estiver preenchido como **Sim**, serão avaliados os itens abaixo em conjunto:  
  
O preenchimento do parâmetro **MV\_OMSCAPA**, irá definir de qual campo será considerado o **Peso Total do Veiculo**.

* Parâmetro preenchido for igual a **1** a **capacidade do veiculo** será considerada com o campo **DA3\_CAPACN - Capacidade Nominal do veículo** do **Cadastro de Veiculo - OMSA060**.
* Parâmetro preenchido for igual a **2** a **capacidade do veiculo** será considerada com o campo **DA3\_CAPACM - Capacidade Máxima do veículo** do **Cadastro de Veiculo - OMSA060**.

Após a definição do **Peso Total do Veiculo** **é necessário preencher os itens abaixo**:

* **Cadastro do Produto - MATA010**, definir o **Peso** no campo **B1\_PESO - Peso Liquido**.
* **Cadastro do veiculo - OMSA060**, informar o **Volume Máximo do veiculo** no campo **DA3\_VOLMAX - Vol.****Máximo**.
* **Cadastro do veiculo - OMSA060**, informar a **quantidade de Limite máximo de pontos de venda que o veículo pode atender**, no campo **DA3\_LIMMAX - Max.Ptos.Ven**.

Os itens destacados acima, são os parâmetros para realizar o calculo de restrição na rotina de **Montagem de Carga - OMSA200.****Importante**Caso utilize o parâmetro **Consid. Restrição?** como **Não**, o Sistema não irá realizar as verificações descritas acima.
