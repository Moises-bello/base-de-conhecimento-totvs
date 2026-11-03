---
content_hash: fb8d96e4170d52aca8abb28180764078d83f48cd07ddca8bdae9dabb20f8880d
fetched_at: '2026-06-28T21:35:30.535354+00:00'
page_id: '857583857'
product: fluig
source: tdn-fluig
title: Desabilitando a integração da plataforma com o Identity
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=857583857
version: 18
---

# Pré-requisitos

---

* Possuir o TOTVS Fluig Plataforma em **atualização 1.6.x ou superior** instalado e configurado conforme as orientações do [Guia de Instalação fluig](https://tdn.totvs.com/x/zAJbDw).
* Possuir um contexto criado no TOTVS Identity, conforme as orientações da página [Criação de Conta no Identity](https://tdn.totvs.com/x/sAzMCg).
* Ter uma empresa cadastrada no Fluig e integrada com o Identity, de acordo com a documentação .

# Acessar o wcmadmin com a plataforma integrada ao Identity

---

**01.** Quando realizada a integração TOTVS Fluig Plataforma com o TOTVS Identity, toda tentativa de acesso à tela de login do Fluig será direcionado para a tela do Identity.

**02.** Para acessar com o wcmadmin é necessário usar a seguinte URL:

* **http://[endereco]:[porta]/portal/home?wcmadmin=true**

Exemplos:

* <https://fluig.suaempresa.com/portal/home?wcmadmin=true>
* <http://10.80.80.219:8080/portal/home?wcmadmin=true>

# Desabilitar a integração com o Identity

---

**01.** De posse dos dados de acesso do usuário **wcmadmin** do Fluig, é possível desabilitar a integração com o Identity.

identificaridentificarPasso 1

* Acessar o Fluig com o usuário **wcmadmin**.
* Acessar o **Painel de Controle** → agrupador **WCM** → **Empresas**.
* Assinalar a empresa desejada e acionar **Editar**.

identificarPasso 2

* Acessar a aba **Autenticação**.
* Assinalar **NÃO** na opção**"**Deseja habilitar o acesso com Identity?**"**.
* Clicar em **Salvar**.

identificarPasso 3

* Uma notificação push será exibida em tela informando que a autenticação via Identity foi desabilitada e sugerindo executar o processo de recuperação de senha para todos os usuários.
* Marque a opção **Sim**.

identificarPasso 4

* Deverá aparecer um push na cor **verde** indicando que o processo de recuperação de senha foi realizado com sucesso.
