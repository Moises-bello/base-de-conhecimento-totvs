---
content_hash: a7ef3a398b547db2453c8b1b72ef1f5354d98888ee55623bbb8ba605dd9821f8
fetched_at: '2026-06-29T00:09:33.378814+00:00'
page_id: '425459004'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x Fluig LMS - Elearning - Notas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459004
version: 3
---

**Notas**

---

**Mensagem**

A mensagem "score" é gerada na integração Gestão de Pessoas x Fluig LMS – E-Learning. Está mensagem é assíncrona. O Fluig envia as mensagens "score" via EAI que vai processar e realizar as ações necessárias na sua base de dados.

Dados que devem ser enviados pelo TOTVS LMS na mensagem "score":

**• Cod. Coligada**   
**• Cod. Matricula E-Learning**   
**• Data Matricula**   
**• Cod. E-Learning**   
**• Cod. Pessoa**   
**• Status**   
**• Score Pré Teste**   
**• Score Pós Teste**

**Cadastro**

Ao executar o pré-teste e o pós-teste no treinamento, as notas obtidas pelos Usuários são enviadas à fila do EAI para serem processadas. Após processadas, as mensagens são enviadas ao Vitae.
