---
content_hash: 7a6844b0a794a82578246de7e67bd9e91bcef4609f8aa3520b16e4514d0ae69e
fetched_at: '2026-06-29T00:12:02.548709+00:00'
page_id: '901958204'
product: rm
source: tdn-rm
title: 2- Acesso ao login unificado dos portais
type: documentation
url: https://tdn.totvs.com/display/LRM/2-+Acesso+ao+login+unificado+dos+portais
version: 23
---

O acesso ao login unificado dos portais para acessar os portais do **Aluno**, **Professor**e **Gestão Educacional.**

O link para acessar é: [http://Nome\_do\_Servidor/FrameHTML/web/app/edu/loginportais/#/login](http://localhost/FrameHTML/web/app/edu/loginportais/#/login).

Acessar utilizando a conta do RM

Ao acessar o login unificado dos portais, será necessário informar o **usuário e senha do RM** e clicar no botão "**Entrar"**

Acesso utilizando uma conta de provedor externo (SAML) - Exemplo do Microsoft Azure 

Ao acessar o login unificado dos portais, será apresentado a opção que foi configurada do provedor externo. Nesse caso o Microsoft Azure, e posteriormente deve-se informar o usuário e senha correspondente do **Azure Microsoft.**

Primeiro acesso

Para o primeiro acesso, o usuário deverá informar e-mail e senha no portal Azure Microsoft.

Após efetuar o login com o usuário e senha, será a apresentação a opção de acesso:

* Se o usuário logado tiver apenas o acesso à um portal, isso é, ser apenas uma persona o usuário será redirecionando diretamente para o portal de destino;
* Se o usuário logado tiver mais de uma persona associado ao seu usuário (exemplo professor e responsável acadêmico/financeiro), será apresentado a opção de acesso conforme o perfil do usuário;

Os portais que estarão disponíveis dependerão das características do usuário que está fazendo login:

* **Portal do Aluno**:
  + Se for aluno, o usuário deve estar vinculado à persona "Aluno" (SALUNO)
  + Se for pais (pai e mãe), responsáveis (acadêmico/financeiro),os mesmos deverão estar associado ao cadastro do aluno.
* **Portal do Professor**: o usuário deve estar vinculado à persona "Professor" (SPROFESSOR).
* **Portal Gestão Educacional**: o usuário deve ter algum perfil de acesso às funcionalidades existentes no PGE e às filiais.
