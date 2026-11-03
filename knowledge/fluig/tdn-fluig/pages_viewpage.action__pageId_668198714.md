---
content_hash: 85b7b385bdd3685ba4513467764c3ecbfefd15802d55cf2444485aa1dede2e5e
fetched_at: '2026-06-28T21:35:28.663830+00:00'
page_id: '668198714'
product: fluig
source: tdn-fluig
title: Personalização de formulários - Nova versão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668198714
version: 5
---

# Índice

true.\*ndicenone

Objetivo

---

O objetivo deste guia é descrever algumas personalizações no desenvolvimento de formulários avançados no fluig, abordando conteúdos como a configuração de máscaras dos campos, utilização de campos *combo* e *zoom*, utilização de serviços de dados e utilização de regras de formulário.

# Pré-requisitos

---

Antes de iniciar, é importante que já tenha visto a documentação de [Desenvolvimento de Formulários](https://tdn.totvs.com/pages/viewpage.action?pageId=181962950).

Serviços de Dados

---

O fluig possui integração com dois tipos de serviços de dados, são eles: Dataset e Serviços Externos. Ambos podem ser usados em todos os eventos disponíveis para customização de definição de formulário.

Importante

Ao construir formulários utilizando a antiga técnica (formulário avançado) onde se faz o uso de datasets, é necessário atenção quanto aos dados incluídos no mesmo, pois ao marcar o formulário como **Documento público** o dataset respeitará a condição do formulário se **tornando público também**.

Com isso, orientamos o uso da nova técnica de construção de formulário, muito mais prática e dinâmica facilitando o uso e a construção dos formulários. Confira nossa documentação sobre a nova técnica de [construção de formulário](http://tdn.totvs.com/x/2CicG).

### Dataset

É um serviço de dados que fornece acesso às informações, independente da origem dos dados. O fluig fornece  que permitem acesso as entidades, como Usuários, Grupos de Usuários, entre outros.

Nota

Os exemplos abaixo utilizam a função getDatasetValues, disponível somente para os Datasets de entidade e definição de formulário(quando informado o número da definição de formulário). Para a utilização de Datasets customizados consulte o Guia de Referência Customização de Datasets.

Na função getDatasetValues, NÃO são retornados os valores de todos os campos por questões de segurança. Para obter todos os dados é utilizado o DatasetFactory, exemplificado em .

Por exemplo, para acessar o Dataset de usuários do fluig no evento *displayFields* de uma definição de formulário:

html/xml

Também é possível fazer uma chamada aos Datasets dentro da definição de formulário através de funções JavaScript.

O acesso aos Datasets também pode ser realizado diretamente no formulário da definição de formulário. Por exemplo, para acessar o Dataset de usuário e inserir os valores nos campos do HTML:

html/xml

Teste XMLRPC

 **Nome do Usuário:** 

  
  
 **Matricula do Usuário:** 

  
  
**Login do Usuário:**

  
  
  
 **Ramal do Usuário:** 

  
  
 **Grupo do Usuário:** 

  
  
 **E-mail do Usuário:**
