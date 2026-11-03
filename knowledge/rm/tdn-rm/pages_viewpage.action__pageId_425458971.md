---
content_hash: 84cb7a351519bc6757e7af5ad330d61d44d2e0041424d5e317ad94d78d4017e0
fetched_at: '2026-06-29T00:09:33.320318+00:00'
page_id: '425458971'
product: rm
source: tdn-rm
title: TOTVS Gestão de Pessoas x Fluig LMS - Elearning - Matrícula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458971
version: 5
---

**Matrícula**

---

**Mensagem**

A mensagem "enrollment" é gerada na integração de matrículas entre o Gestão de Pessoas x Fluig LMS – E-Learning. O Fluig recebe as mensagens "enrollment" via EAI, processando-as e realizando as ações necessárias na sua base de dados.

Dados que devem ser enviados pelo TOTVS Gestão de Pessoas na mensagem "enrollment":

* **Cod. Coligada**
* **Cod. Matrícula**
* **Data Matrícula**
* **Cod. E-Learning**
* **Cod. Pessoa**
* **Status**
* **Score Pré-Teste**
* **Score Pós Teste**

Junto com a mensagem de Matrícula, é enviado a mensagem de usuários que pode ser vista [aqui.](http://tdn.totvs.com/x/E-1bGQ)  
     
 **Matrícula**

As matrículas dessa integração ocorrem somente no TOTVS Gestão de Pessoas e são replicadas para o Fluig. Ao receber a solicitação de matrícula, o Fluig matricula automaticamente o Usuário no treinamento. Quando matriculado, o Usuário tem acesso à turma através do Portal em Painel de Aprendizagem.

Para matricular um Funcionário acesse **Portal | Recursos Humanos | Painel de Aprendizagem.**

• A matrícula ocorrerá do mesmo modo que acontece atualmente através das matrículas do Painel de Aprendizagem.
