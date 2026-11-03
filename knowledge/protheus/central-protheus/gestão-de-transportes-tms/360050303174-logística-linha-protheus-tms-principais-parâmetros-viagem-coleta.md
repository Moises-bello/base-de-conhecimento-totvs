---
article_id: 360050303174
category: Gestão de Transportes (TMS)
content_hash: 6dc689da929ba886ef8745b9c2641316c2c752c247536012d035749e6ad2a6ae
fetched_at: '2026-06-28T22:45:32.445965+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Principais parâmetros Viagem Coleta
type: support-article
updated_at: '2021-10-06T17:05:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050303174-Log%C3%ADstica-Linha-Protheus-TMS-Principais-par%C3%A2metros-Viagem-Coleta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min****Dúvida**Quais são os principais parâmetros utilizados na Viagem Coleta?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Os principais parâmetros relacionados a Viagem de Coleta são:

* **MV\_OCORCOL -**informar uma ocorrência de encerramento de processo de coleta e ativar o parâmetro **MV\_ENCVIAG**. Quando realizar a entrada de documento a**tualizações/Recebimento/Entrada Documento- TMSA050**, se a viagem estiver com o **STATUS** em **TRÂNSITO** a viagem será encerrada de forma automática.
* **MV\_COLSOCO** - Gera Contrato de Carreteiro para Viagens de  Coleta sem registro de Ocorrência (DUA)?
* **MV\_OCORCOL** - Define a ocorrência de coleta utilizado no apontamento automático de ocorrência na geração da nota
* **MV\_OCORCAN** - Define a ocorrência de cancelamento automático utilizado na Viagem de Coleta do tipo Planejada
* **MV\_ROTGCOL** - Rota genérica para coleta
* **MV\_TMSOCOL** - Permite informar a ocorrência do documento em outra filial
* **MV\_TMSPCOL** - Define se deverá incluir regiões coligadas para cálculo do prazo de entrega (default .T).
* **MV\_UMOVCOL** - Ocorrências de coleta. 1=Ocorrência para finalizar processo de coleta, 2= Ocorrência para informar documentos não coletados
* **MV\_TMSDCOL** -  Desconsidera filial de origem da solicitação de coleta.
