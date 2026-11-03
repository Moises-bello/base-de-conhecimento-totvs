---
article_id: 24813044221335
category: PMS - Projetos
content_hash: a73981132847690a67cf5f1fd42c979406dec9c429df9d46550ca0cc48a38a00
fetched_at: '2026-06-28T22:37:14.971255+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Reprogramar Dt.Inc. Prv e
  Dat.Fim.Prv do projeto
type: support-article
updated_at: '2024-07-11T14:31:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24813044221335-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Reprogramar-Dt-Inc-Prv-e-Dat-Fim-Prv-do-projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24813044194583) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como alterar várias Dt.Inc. Prv e Dat.Fim.Prv do projeto de uma só vez?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**1 - Entre no projeto > Selecione a EDT ou Tarefa > 3 - Vá no botão "Outras ações" > Ferramentas > Reprogramar datas previstas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24813005205271)

2 - Defina:

* As EDTs/Tarefas que só alterarão quando tiverem alguma equipe ou recursos inseridos
* Se ignora a atualização em tarefas que já tem apontamento de início gerado ou ainda não
* Se a data quando for reajustada, se será definido a data do fim da previsão e recalculado a data de inicial da previsão ou se será definido a data inicial da previsão e recalculado o fim da previsão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24813044196119)

No exemplo acima, recalcularemos como o novo fim previsto sendo 20 de junho de 2024.

**Antes:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24813044197015)

**Depois (recalculou-se o início a partir da nova data do fim):**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24813044197655)

**OBSERVAÇÃO:** Os intervalos das datas respeitam as horas de cada tarefa trabalhada junto do calendário das EDTs e tarefas (AFC/AF9\_HDURAC e AFC\_AF9\_CALEND) automaticamente.
