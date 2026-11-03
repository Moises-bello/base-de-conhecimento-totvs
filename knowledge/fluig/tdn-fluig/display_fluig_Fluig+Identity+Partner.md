---
content_hash: c76277b970eb8fa966000e516dd2fccfac47663e6b847e9607f0f837676f1636
fetched_at: '2026-06-28T21:35:25.332691+00:00'
page_id: '281141190'
product: fluig
source: tdn-fluig
title: Fluig Identity Partner
type: documentation
url: https://tdn.totvs.com/display/fluig/Fluig+Identity+Partner
version: 10
---

# Índice

4true.\*ndicenone

# Objetivo

---

O objetivo deste guia é mostrar como configurar o licenciamento controlado pelo Identity. O Fluig Identity Partner é um modelo de licenciamento que utiliza o TOTVS Identity na nuvem para controlar o acesso a plataforma TOTVS Fluig.

# Pré-requisitos

---

Este recurso é disponibilizado apenas para clientes que são **parceiros TOTVS**.

Para utilizar este licenciamento não é preciso ter a plataforma Fluig integrada com o Identity.

# Configuração na plataforma

---

Para realizar a configuração do licenciamento controlado pelo Identity, siga os passos abaixo:

0.5falsefluigfadetrue1Passo 1

* Acesse a plataforma com um usuário que contenha perfil de administrador;

2Passo 2

* Clique sobre o menu em **Painel de Controle** e localize a opção **Identity Partner Admin**.

3Passo 3

* Acesse o Identity e obtenha o License ID, Client ID e Cliente Secret para preencher nos campos solicitados na página de configuração do Identity Partner Admin. Caso tiver dúvidas em como realizar este procedimento no Identity .
* Se este ambiente for de homologação, a opção "Utilizar ambiente de homologação" deve ser ativada.
* Finalizado a inclusão dos IDs, clique em **Ativar**.

4Passo 4

* Caso a plataforma esteja utilizando o License Server, será necessário desativá-lo no painel administrativo da plataforma. Dúvidas em realizar este procedimento, .

identity

# Obter Credenciais e Licença no Identity

---

Siga os passos abaixo para obter as informações solicitadas na plataforma para configuração do Identity Partner Admin.

0.5falseidentityfadetrue1Passo 1

* Acesse o Identity com um usuário que contenha perfil de administrador;
* Acione o menu **Aplicativos**;
* Pesquise pelo aplicativo do Fluig;
* Clique sobre o aplicativo Fluig que deseja configurar o Identity Partner Admin;

2Passo 2

* Acesse a aba **Credenciais OAuth 2.0**.
* Clique sobre o botão **Gerar Nova Credencial;**

* Informe uma descrição;
* Clique em **Salvar**.

* Copie o Client ID e Client Secret e cole na tela de configuração do Identity Partner Admin no Fluig.

3Passo 3

* Acesse a aba **Licenças** para copiar o ID da Licença gerada pelo seu parceiro TOTVS.
* Basta clicar no ícone de copiar () localizado ao lado do ID.
* Cole o ID na tela de configuração do Identity Partner Admin no Fluig.

ls

# Desativar License Server da plataforma

---

Atenção!

Clientes hospedados em Cloud TOTVS deverão abrir um ticket para a Equipe de Atendimento Cloud solicitando a desativação do License Server.

Para realizar este procedimento, acesse a plataforma com o usuário 'wcmadmin' e siga os passos abaixo:

0.5falsewcmadminfadetrue1Passo 1

* Clique sobre o menu **Painel de Controle** e acione a opção **Configurações do Sistema**;
* Acesse a aba **Parâmetros da Plataforma** onde estão localizados os parâmetros de configuração da plataforma;
2Passo 2

* Localize na página o item Servidor de Licença;
* Clique sobre o botão **Habilitar License Server** para Desativá-lo;

3Passo 3

* No topo da página clique em Salvar para desativar o License Server. Para que a desativação seja reconhecida pela plataforma será necessário reiniciar os serviços do Fluig.

4Passo 4

* Reinicie os serviços do Fluig na ordem correta.

**Parar**: fluig, fluig\_RealTime, luig\_Indexer e fluig\_MemCached (caso utilizar).  
**Iniciar**: fluig\_MemCached (caso utilizar), fluig\_Indexer, fluig\_RealTime e fluig.

 ]]>
