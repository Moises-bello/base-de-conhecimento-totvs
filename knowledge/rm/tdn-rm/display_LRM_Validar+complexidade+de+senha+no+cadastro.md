---
content_hash: f35e044f01a2984fd4161d14831026fcd3e76fd0052f1390cb80f3450883e77e
fetched_at: '2026-06-29T00:11:56.404182+00:00'
page_id: '865418181'
product: rm
source: tdn-rm
title: Validar complexidade de senha no cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/Validar+complexidade+de+senha+no+cadastro
version: 10
---

**CONTEÚDO**

* Visão Geral

#### **01. VISÃO GERAL**

* O Parâmetro global "**Validar complexidade de senha no cadastro**" altera o comportamento da rotina de **criação e edição\*** de usuários do sistema.

* Caso a opção esteja **marcada** ao incluir ou editar um usuário no sistema a senha digitada será verificada se a mesma respeita as configurações de complexidade de senha, caso não esteja de acordo, um erro será exibido no sistema.

  Atenção

  **Este parâmetro tem efeito nas rotinas que utilizam o DataServer de usuário (Tela de cadastro de Usuários, Api´s de usuário) e** Rotinas de **produtos** que **Incluem** usuários.

  **Edição\***: A senha só será validada na edição caso a mesma esteja sendo trocada, seguindo informações acima.

Atenção

A complexidade de senha sempre será validada quando a troca de senha for disparada através das funcionalidades abaixo

**Alterar a senha no Próximo Login**  
**Expiração da senha**
