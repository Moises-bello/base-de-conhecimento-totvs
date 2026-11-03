---
article_id: 9980741845527
category: Gestão de Transportes (TMS)
content_hash: 7c02671861885ddb435219aa63044f7f9eb5f10556cceeed01e97a2a3dbfabec
fetched_at: '2026-06-28T22:45:32.442382+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Principais parâmetros Viagem
type: support-article
updated_at: '2022-11-03T16:04:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9980741845527-Log%C3%ADstica-Linha-Protheus-TMS-Principais-par%C3%A2metros-Viagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Quais são os principais parâmetros para geração de viagem no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Os principais parâmetros relacionados a geração de viagem são: 

* **MV\_SVCENT**: Código do serviço para carregamento de entrega e reprocesso no ambiente **TOTVS Logística TMS**. Por padrão, o parâmetro é preenchido com o serviço **002**.
* **MV\_GEROPER**: Valida se as operações relacionadas ao serviço operacional deverão ser geradas, automaticamente ou não, ao efetuar o carregamento do transporte:

  + **T (True/Verdadeiro):** ao efetuar o carregamento de transporte, o Sistema gera, automaticamente, as operações do serviço operacional informado no cadastro de serviços x atividades.
  + **F (False/Falso):** o Sistema não gera as operações relacionadas ao serviço operacional informado.
* **MV\_TMSEXP**: Controla modo express. Se necessário, verifique a documentação [TMS0001 - Viagem Modelo Express](https://tdn.totvs.com/display/public/PROT/TMS0001+-+Viagem+Modelo+Express)
* **MV\_PCANOP**: Identifica se na chegada ou saída de viagem, existem operações anteriores em aberto e se estas devem ser canceladas automaticamente:

  + **0 - Cancela automaticamente;**
  + **1 - Pergunta antes de cancelar;**
  + **2 - Não cancela operações anteriores em aberto;**
  + **3 - Apontamento obrigatório das operações anteriores em aberto.**
