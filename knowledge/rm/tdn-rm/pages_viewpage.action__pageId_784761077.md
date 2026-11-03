---
content_hash: 61a5bef30eb399f57fe4c40c002f37bd6deadfb481ef1d5a0e455ae3fb894489
fetched_at: '2026-06-29T00:11:38.327158+00:00'
page_id: '784761077'
product: rm
source: tdn-rm
title: Como criar uma conta de serviço do Google para acessar e usar o Google Drive
  através do RM com o FileRepo.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784761077
version: 14
---

ATENÇÃO

Novas contas de serviço Google, não são mais compatíveis com esta forma de integração. Documentação apenas para histórico ou quem usa contas de serviços antigas.

Clique aqui para ver o novo formato que está compatível e funcionando: [Como criar credenciais Utilizando Oauth](https://tdn.totvs.com.br/display/LRM/Como+criar+credenciais+Utilizando+Oauth)

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

#### **Passo 3: Crie uma Conta de Serviço**

1. No painel de navegação esquerdo, clique em "**IAM & Admin**" e depois em "**Contas de serviço**".
2. Clique no botão "**Criar conta de serviço**".
3. Preencha os campos "**Nome**", "**Descrição**" e selecione um papel.   
   O papel depende das permissões necessárias; você pode começar com acesso Básico e papel "**Editor**".   
   Para mais detalhes sobre papéis, confira a [documentação oficial](https://cloud.google.com/iam/docs/understanding-roles?hl=pt-br).
4. Clique em "**Continue**" e depois em "**Concluir**".

    Demonstração de como criar uma Conta de Serviço

#### **Passo 4: Baixe as Credenciais**

1. Na lista de contas de serviço, clique no ícone de três pontos (opções) ao lado da conta de serviço que você acabou de criar.
2. Clique em "**Gerenciar chaves**".
3. Na tela seguinte, clique em "Adicionar chave" e selecione "**Criar nova chave**".
4. Selecione o formato "**JSON**" e clique em "**Criar**". O arquivo JSON das credenciais será baixado.

   Demonstração de como baixar as Credenciais
