---
article_id: 5849357024791
category: Controle de Auditorias (SIGAQAD)
content_hash: e37f4e1977c743659caa0d9a890138fdfad361a092fa9cc997ba5836aefee616
fetched_at: '2026-06-28T22:42:30.833574+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - Campo QUB_CONCLU da rotina QADA140
type: support-article
updated_at: '2022-05-05T11:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5849357024791-Manufatura-Linha-Protheus-SIGAQAD-Campo-QUB-CONCLU-da-rotina-QADA140
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**O conteúdo inserido no campo **Conclusão** da rotina **QADA140 - Encerramento de Auditorias** é registrado em qual campo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões  
  
**Solução**Quando o encerramento da auditoria é realizada pela rotina **QADA140**, o conteúdo informado no campo **QUB\_CONCLU - Conclusão** é registrado na tabela **SYP - Descrição dos Campos Memo** no campo **YP\_TEXTO - Linha**.  
O relacionamento entre as tabelas **QUB - Auditorias** e **SYP** são pelos campos **QUB\_CHAVE - Chave** e **YP\_CHAVE - Chave**, onde **QUB\_CHAVE** é igual à **YP\_CHAVE**.  
  
**Importante**  
Os campos **QUB\_CONCLU** e **YP\_TEXTO - Linha** precisam ter o mesmo tamanho. No padrão, este tamanho está definido como 80.  
Neste caso, quando a descrição inserida no campo **Conclusão** ultrapassar 80 caracteres, o texto será quebrado e inserindo no máximo 80 caracteres no campo **YP\_TEXTO**, quebrando o texto em várias sequências no campo **YP\_SEQ - Sequência**, mas todas as sequências com a mesma chave **YP\_CHAVE**.
