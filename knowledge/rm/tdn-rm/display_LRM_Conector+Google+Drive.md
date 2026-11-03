---
content_hash: 90d60da70ec90d8612e21de0520225279b19ff51edd92b50feb165cfd190bdb8
fetched_at: '2026-06-29T00:12:15.359726+00:00'
page_id: '977177612'
product: rm
source: tdn-rm
title: Conector Google Drive
type: documentation
url: https://tdn.totvs.com/display/LRM/Conector+Google+Drive
version: 5
---

## **01. VISÃO GERAL**

O RM permite que o **Google Drive** seja utilizado como repositório de arquivos para armazenar e gerenciar documentos eletrônicos.

## **02. Pré-Requisitos**

Para utilizar a integração com o Google Drive no TOTVS RM por meio do FileRepo, é necessário criar um **projeto no Google Cloud**.  
Dentro desse projeto, será preciso **gerar credenciais** que permitam o acesso ao Google Drive.

Anteriormente, era possível utilizar **contas de serviço** (Service Accounts) para autenticação. Contudo, **o Google não aceita mais contas de serviço para essa integração**, exigindo o uso do fluxo **OAuth**, no qual o usuário final concede permissão de acesso ao RM ao repositório de arquivos da conta que foi utilizada para criar o projeto.

Portanto, sugerimos que criação das credenciais deve seguir o modelo **OAuth**, garantindo conformidade com as políticas mais recentes do Google.

#### **Passo 1: Crie um Projeto no Google Cloud Platform**

1. Acesse o [Google Cloud Platform Console](https://console.cloud.google.com/) e faça login utilizando uma conta de Gmail.
2. Se esta for a primeira vez que você faz login no console, **aceite os Termos de Serviço**.

   Demonstração
3. Na barra de pesquisa, digite "**Criar Projeto**" e insira o nome do projeto e outros detalhes.

   Demonstração de como criar um projeto.

#### **Passo 2: Habilite a API do Google Drive**

1. No painel de navegação esquerdo, clique em "**APIs & Services**" e depois em "**APIs e serviços ativados.**"
2. No canto superior da tela, clique em "**ATIVAR APIs E SERVIÇOS**".
3. Na barra de pesquisa, digite "**Google Drive API**" e clique no resultado correspondente.
4. Clique no botão "**Ativar**" para habilitar a API do Google Drive para o seu projeto.

    Demonstração de como habilitar a API do Google

1. Se esta for a primeira vez que você faz login no console, **aceite os Termos de Serviço**.

   Demonstração
2. Na barra de pesquisa, digite "**Criar Projeto**" e insira o nome do projeto e outros detalhes.

   Demonstração de como criar um projeto.

#### **Passo 3: Como gerar as credenciais**

Acesse as páginas filhas para criar as credenciais
