---
content_hash: 8a486ffe371fdddb193b4a5335403f927fd9cc9c20c1f9ac2814ac27d1d9b144
fetched_at: '2026-06-29T00:09:33.302942+00:00'
page_id: '425458963'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x Fluig LMS - E-learning - Cadastro de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458963
version: 7
---

**Cadastro de Usuários**

**Mensagem**

A mensagem "User 4.003" é gerada na integração Gestão de Pessoas x Fluig LMS – E-Learning nos processos de matricula no TOTVS Gestão de pessoas, sendo uma mensagem síncrona. Esta mensagem é enviada apenas quando é realizado uma matricula. Ela pode mandar um novo usuário, e pode também alterar um usuário já existente no FLUIG.

O Fluig recebe as mensagens "User 4.003" via EAI, processando-as e realizando as ações necessárias na sua base de dados.

Dados que devem ser enviados pelo TOTVS Gestão de Pessoas na mensagem "user":

**• Cod. Coligada**  
**• Nome completo**   
**• Cod. Pessoa**   
**• E-mail**   
**• Cod. Usuário**   
**• Papel**

**Observações:**

Usuários cadastrados diretamente no Fluig não são integrados ao TOTVS Gestão de Pessoas
