---
article_id: 360049118353
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 41b95b13e0d4e2d689a6cd3f2ac41dacad1361542afd273d6c2cf7f7989191ae
fetched_at: '2026-06-28T22:42:27.913018+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Campo QI2_MEMO1 da rotina QNCA040
type: support-article
updated_at: '2021-05-10T20:13:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049118353-Manufatura-Linha-Protheus-SIGAQNC-Campo-QI2-MEMO1-da-rotina-QNCA040
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**A informação inserida no campo **Descr.Detalh** da rotina **QNCA040 - Cadastro de Não Conformidades**é registrada em qual campo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Solução**A informação inserida no campo **Descr.Detalh** será registrada em duas tabelas: **QI2 - Não Conformidades** e **SYP - Descrições dos Campos Memo**.  
O campo **Descr.Detalh** da rotina **QNCA040** refere-se ao campo **QI2\_MEMO1 -** **Descr.Detalh**, que por sua vez, registra uma chave no campo **QI2\_DDETA - Descr.Detalh** .  
Esta chave é utilizada como relacionamento entre as tabelas **QI2** e **SYP**, por meio do campo **YP\_CHAVE - Chave**.   
Os campos **QI2\_MEMO1** e **SYP\_TEXTO - Linha** precisam ter o mesmo tamanho. No padrão, este tamanho está definido como 80.  
Neste caso, quando a descrição inserida no campo **Descr.Detalh** ultrapassar 80 caracteres, o texto será quebrado e inserindo no máximo 80 caracteres no campo **SYP\_TEXTO**, quebrando o texto em várias sequências no campo **YP\_SEQ - Sequência**, mas todas as sequências com a mesma chave **YP\_CHAVE**.
