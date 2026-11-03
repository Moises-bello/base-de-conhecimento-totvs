---
content_hash: d59acaad69be70817bcfe28588156d3ee5e4f6208555786bbc6103cdc4a8a5a1
fetched_at: '2026-06-28T21:35:24.223763+00:00'
page_id: '269067666'
product: fluig
source: tdn-fluig
title: ARQ - Como faço a migração da pasta 'volume' de um servidor Linux para Windows?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269067666
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Nossa plataforma está instalada em sistema operacional Linux e estamos migrando para ambiente Windows. Precisamos apontar a pasta "Volume" para o servidor com Windows portanto, qual é o procedimento que devemos realizar?

# Solução

0.5falseSamplefadetrue1Passo 1

* Criar uma nova pasta de "Volume" no servidor com Windows.
2Passo 2

* Acesse a plataforma do Servidor Windows logando com o usuário 'wcmadmin'.

3Passo 3

* Navegue até o Painel de Controle → Gerais → Volumes.

4Passo 4

* Selecione a opção *Default* e clique em Editar.

5Passo 5

* Altere o campo **Diretório físico** para o novo diretório da pasta 'Volume' do servidor Windows e clique em **Salvar**.

6Passo 6

* Copie as sub-pastas do 'Volume' contido no servidor Linux para a nova pasta de 'Volume' criada no servidor Windows.
