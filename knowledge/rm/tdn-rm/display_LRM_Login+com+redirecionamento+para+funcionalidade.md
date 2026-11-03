---
content_hash: 2a75946b046cea1252e7f603f01c32fb286856ef0c7b2f5d461f76bf407e64fb
fetched_at: '2026-06-29T00:08:50.898703+00:00'
page_id: '334345338'
product: rm
source: tdn-rm
title: Login com redirecionamento para funcionalidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Login+com+redirecionamento+para+funcionalidade
version: 15
---

O login com redirecionamento para funcionalidade do portal do aluno, tem como objetivo otimizar para uma funcionalidade específica através do path do menus após login no portal do aluno.

Funcionalidade não disponível para login com aplicativo externo

Esta funcionalidade **não está disponível** para login com aplicativo externo.

O redirecionamento ocorrerá apenas para a rota da funcionalidade, se a página possuir detalhamentos como por exemplo "Faltas" que possui a opção de "Faltas por etapa" e "Faltas por aula", o usuário será redirecionado para a página principal exatamente como se tivesse clicado na funcionalidade pelo menu.

## **01. ACESSO A FUNCIONALIDADE**

Existem duas possibilidades de URL que redirecionará o usuário para uma funcionalidade.

* **Pode ser utilizada a URL direta da funcionalidade:**Exemplo: http://SERVIDOR/web\_src/app/edu/PortalEducacional/#/grade-curricular
* **Utilizar o parâmetro redirect na tela de login, passando a rota desejada**: Exemplo: http://SERVIDOR/web\_src/app/edu/PortalEducacional/login/?redirect=calendario

Resultado: após efetuar o login, o usuário será redirecionando para o menu: Atividades Curriculares.
