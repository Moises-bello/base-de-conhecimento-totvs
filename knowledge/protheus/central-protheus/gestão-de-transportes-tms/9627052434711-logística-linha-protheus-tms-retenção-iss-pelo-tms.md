---
article_id: 9627052434711
category: Gestão de Transportes (TMS)
content_hash: 2fed395af08849b5527b6b11dcb1fe83331d50ac5047ffb64991e436488cab39
fetched_at: '2026-06-28T22:45:33.353502+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Retenção ISS pelo TMS
type: support-article
updated_at: '2024-11-22T17:21:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9627052434711-Log%C3%ADstica-Linha-Protheus-TMS-Reten%C3%A7%C3%A3o-ISS-pelo-TMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27997651002263) Tempo aproximado para leitura: **00:01:45 min** **Dúvida**Como funciona a retenção de **ISS - Imposto sobre Serviço** de documentos gerados pelo **TOTVS Logística TMS**?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O **TOTVS Logística TMS** acata as regras de retenção de **ISS** definidas pelo **Fiscal**, considerando os cadastros e parâmetros detalhados na documentação [Retenção de ISS](https://tdn.totvs.com/pages/releaseview.action;jsessionid=163663615DA6E59328255635614C696F?pageId=6076798).  
  
Para documentos gerados a partir do **TMS**, há dois cenários para a retenção de **ISS**:

* **Quando o tomador recolhe o ISS:**Se o tomador recolhe o **ISS**, o cadastro do cliente deve estar cadastrado com o campo **A1\_RECISS = 1 - Sim**. Com isso, o Sistema irá gerar dois títulos, um com o  valor total da fatura e outro com o valor do **ISS**, para que este valor seja abatido na baixa do titulo no **Contas a Receber**.
* **Quando a transportadora recolhe o ISS:**Se a transportadora recolhe o **ISS**, o cadastro do cliente  deve estar cadastrado como o campo **A1\_RECISS = 2 - Não**. Com isso, o Sistema irá gerar o titulo com o valor total da fatura, e o **ISS** não será abatido, visto que a transportadora quem irá recolher o **ISS**.

Em ambos os casos, o valor líquido que deseja só será definido na baixa do título, afim de garantir que o  **Financeiro** tenha a visão de quem irá reter o **ISS**.  
  
**Anexo**Exemplo da baixa de títulos para os cenários descritos**.**
