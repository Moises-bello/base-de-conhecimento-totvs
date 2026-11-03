---
article_id: 360050516294
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 1913a4011a10f5fc0d6adb5a4884bf8bde290c74fdf924a47437b711b48e73a2
fetched_at: '2026-06-28T22:42:27.918967+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Campo QI3_MEMO1 da rotina QNCA030
type: support-article
updated_at: '2021-05-10T21:03:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050516294-Manufatura-Linha-Protheus-SIGAQNC-Campo-QI3-MEMO1-da-rotina-QNCA030
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**A informação inserida no campo **Descr.Detalh**da rotina**QNCA030 - Cadastro de Plano de Ação**é registrada em qual campo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**A informação inserida no campo **Descr.Detalh** será registrada em duas tabelas: **QI3 - Cadastro de Plano de Ação** e **SYP - Descrições dos Campos Memo**.  
O campo **Descr.Detalh** da rotina **QNCA030** refere-se ao campo **QI3\_MEMO1 -** **Descr.Detalh**, que por sua vez, registra uma chave no campo **QI3\_PROBLE - Descr.Detalh** .  
Esta chave é utilizada como relacionamento entre as tabelas **QI3** e **SYP**, por meio do campo **YP\_CHAVE - Chave**.   
Os campos **QI3\_MEMO1** e **SYP\_TEXTO - Linha** precisam ter o mesmo tamanho. No padrão, este tamanho está definido como 80.  
Neste caso, quando a descrição inserida no campo **Descr.Detalh** ultrapassar 80 caracteres, o texto será quebrado e inserindo no máximo 80 caracteres no campo **SYP\_TEXTO**, quebrando o texto em várias sequências no campo **YP\_SEQ - Sequência**, mas todas as sequências com a mesma chave **YP\_CHAVE**.
