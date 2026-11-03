---
content_hash: 21949be66e5c4a9a71366c4c0c0e071eb66949ccb8fdbd90d4f85d098938e010
fetched_at: '2026-06-29T00:09:38.019960+00:00'
page_id: '425459675'
product: rm
source: tdn-rm
title: Tipo de usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459675
version: 2
---

A entidade "Tipo de Usuário" é essencial na configuração das Regras de Empréstimo juntamente com a entidade "Tipo de Publicação" a associação destas entidades e configuração de parâmetros vai estabelecer as regras de empréstimo a serem seguidas pelos usuários do sistema.  
  
 Um exemplo disso é que ao cadastrar um novo tipo de usuário e associá-lo a um usuário em questão o mesmo não poderá realizar empréstimos até que seja configurada uma regra de empréstimo para este tipo de usuário.  
  
 O sistema exibe alerta informando: "Para este tipo de usuário ainda não foi definido uma regra de empréstimo".  
  
 Os parâmetros disponíveis no cadastro/edição dos tipos de usuário são:

* **Verificar validade do usuário:** usuários associados à este tipo de usuário não poderão realizar empréstimo se estiverem com a data de validade vencida.
* **Consistir empréstimo pela grade do usuário:** utilizado para criação de tipos de usuário a serem utilizados por alunos cadastrados nos sistemas TOTVS Educacional e RM Classis e importados para o TOTVS Gestão Bibliotecária.
* **Consistir empréstimo pelo tipo de publicação:** configura a quantidade de empréstimo permitido levando em conta os tipos de publicação, a utilização deste parâmetro obriga que sejam cadastrados limites de empréstimo para cada tipo de publicação.

**Observação: O número máximo de empréstimo para um tipo de publicação não poderá ser maior que o número máximo de empréstimos geral.**
