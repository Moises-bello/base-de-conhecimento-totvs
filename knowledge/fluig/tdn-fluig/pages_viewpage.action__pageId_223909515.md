---
content_hash: 3757045cb4fed25c4db8c0fafe3153ba1ce198fa9f6d1420087dbfa2be6e8bdd
fetched_at: '2026-06-28T21:35:19.787696+00:00'
page_id: '223909515'
product: fluig
source: tdn-fluig
title: BPM 016 - É possível cancelar várias solicitações de um processo ao mesmo tempo?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223909515
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

É possível cancelar várias solicitações de um processo ao mesmo tempo?

# Solução

Através do sistema é possível cancelar mais de uma solicitação ao mesmo tempo, utilizando a rotina de [Cancelamento em Bloco](http://tdn.totvs.com/pages/viewpage.action?pageId=233763398#Minhassolicita%C3%A7%C3%B5es-Cancelarsolicita%C3%A7%C3%B5esembloco). Após as solicitações terem sido canceladas, é possível também eliminar várias ao mesmo tempo.

Temos também a alternativa de utilização de um *web service* capaz de realizar cancelamentos em massa.

É possível utilizar o método cancelInstance do *web service* WorkflowEngineService para o cancelamento de solicitações. Neste método é necessário retornar o número da solicitação e a matrícula de um usuário que tenha permissão de cancelamento da solicitação.

Desta forma, o ideal seria desenvolver uma rotina que faça a consulta destas solicitações **antes** da rotina de cancelamento. Esta consulta pode ser feita via dataset. Para obter mais informações, acesse a documentação de *web services* em Utilização de *Webservices*, e de datasets em [.](http://tdn.totvs.com/x/eitbB)

[Os parâmetros do método cancelInstance são:](http://tdn.totvs.com/x/eitbB)

**user:** *login* do colaborador  
**password:** senha do colaborador  
**companyId:** código da empresa  
**processInstanceId:** número da solicitação  
**userId:** matrícula do usuário  
**cancelText:** comentários do cancelamento  
  
Os parâmetros *user* e *password* referem-se a um usuário e senha de administrador, não necessita ser o usuário que tenha permissão de cancelamento. Já userID precisa ser a matrícula de um usuário com permissão de cancelamento da solicitação.
