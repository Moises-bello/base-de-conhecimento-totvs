---
content_hash: b875d9d7cdd4aa2287851f52adb3dee8ecc78396c1ae0cb9cdcae46b3ad973c1
fetched_at: '2026-06-29T00:09:35.917090+00:00'
page_id: '425459430'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x TOTVS e-Learning Management SUITE (LMS) - Notas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459430
version: 5
---

---

**Notas**

**Mensagem**  
    
 A mensagem "score" é gerada na integração entre o TOTVS Gestão de Pessoas e o TOTVS LMS. Está mensagem é assíncrona. O TOTVS LMS envia as mensagens "score" via EAI, processando-as e realizando as ações necessárias na sua base de dados. Para saber mais sobre EAI [clique aqui.](http://tdn.totvs.com/pages/releaseview.action?pageId=5264533)  
    
 Dados que devem ser enviados pelo TOTVS LMS na mensagem "score":

* CourseCode
* UserCodeUserInternalId
* ApprovalStatus
* PostTestScore
* PostTestCode

**Cadastro**  
    
 Ao executar o pré-teste e o pós-teste no treinamento, as notas obtidas pelos alunos são enviadas à fila do EAI para serem processadas conforme configurada mensagem **Processar Mensagens do EAI**no menu **Agendamento**. Após processadas, as mensagens são enviadas ao Vitae.
