---
article_id: 360025350934
category: Controle de Não Conformidades (SIGAQNC)
content_hash: c9fb2aa4b3af127fcf82bed5dcb6516adc99ce128f8c07205bc819eccc7ea294
fetched_at: '2026-06-28T22:42:28.053896+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Sequência para baixa de pendências
type: support-article
updated_at: '2021-09-08T12:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025350934-Manufatura-Linha-Protheus-SIGAQNC-Sequ%C3%AAncia-para-baixa-de-pend%C3%AAncias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Por que ao incluir as etapas na rotina **Plano de Ação - QNCA030**, o Sistema gera apenas a primeira pendência da sequência de etapas?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**Para gerar todas as pendências do plano de ação simultaneamente para todos os responsáveis, o parâmetro **MV\_QNCBALE - Indica se a baixa das etapas é realizada aleatoriamente ou seqüencialmente** deve ser configurado igual a **1 = Sim** para que a baixa das etapas seja realizada aleatoriamente.   
  
**Importante**  
Esta configuração será válida apenas para as **próximas** pendências geradas após alteração do parâmetro. Para as pendências atuais, será necessário aguardar a liberação de cada pendência para o Sistema gerar a próxima pendência.
