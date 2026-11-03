---
article_id: 360050499433
category: Controle de Documentos (SIGAQDO)
content_hash: 8fef5ee3f933d8340f9711cddcd2271c6885276e1c93dac53af2aebbf2d48b40
fetched_at: '2026-06-28T22:42:28.974723+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Como identificar o usuário que fez
  o cancelamento de um documento
type: support-article
updated_at: '2021-05-11T19:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050499433-Manufatura-Linha-Protheus-SIGAQDO-Como-identificar-o-usu%C3%A1rio-que-fez-o-cancelamento-de-um-documento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Como identificar qual usuário fez o cancelamento de um documento na rotina **QDOA050 - Cadastro de Documentos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Quando um documento é cancelado, uma nova revisão deste documento é gerada.  
Nesta nova revisão é possível identificar qual usuário fez este cancelamento por meio da tabela **QDH - Documentos**, onde é registrado no campo **QDH\_MAT - Cod Usr Dig** a matrícula do usuário que fez o cancelamento e no campo **QDH\_DEPTOD - Cod Dep Dist** o código do departamento deste usuário. Essas informações são com base no cadastro do usuário registrado na rotina **QAXA010 - Cadastro de Usuários**, armazenadas na tabela **QAA - Usuários**.
