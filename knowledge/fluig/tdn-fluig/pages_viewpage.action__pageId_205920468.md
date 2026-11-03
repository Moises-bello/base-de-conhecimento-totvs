---
content_hash: 7e6ff9c678414f1be8df8c37e7e2e9b19516fd0d25214fe1b845bfaa2a768e80
fetched_at: '2026-06-28T21:35:19.462183+00:00'
page_id: '205920468'
product: fluig
source: tdn-fluig
title: IDE - Como desabilitar a integração entre a plataforma e o Identity?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=205920468
version: 16
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.5.0 ou superior

# Ocorrência

Como desabilitar a integração entre a plataforma (1.5 ou superior) e o Identity?

# Solução

Clientes cujo ambiente esteja hospedado no Cloud TOTVS, devem abrir um ticket solicitando a desativação da integração.

Já clientes on-premises devem seguir os procedimentos abaixo:

falsedesativar\_identityPasso 1

* Acessar a plataforma com o usuário WCMADMIN, conforme detalhado na FAQ .

Passo 2

* Acessar a tela de , localizada na seção WCM do Painel de Controle.

Passo 3

* Na lista de empresas cadastradas, localizar a empresa na qual a integração com o Identity deve ser desabilitada
* Marcar o *checkbox* disponível ao lado do código da empresa. A coluna Identity irá exibir o status Habilitado quando a integração estiver ativa.

* Acionar **Editar**.

Passo 4

* Na aba **Autenticação**, desmarcar a opção **Acessar com Identity**.

* Acionar **Salvar** para concluir a alteração.

Dica

Após a desabilitar a integração, a autenticação dos usuários passa a ocorrer diretamente na plataforma Fluig. Para entender como deve ser feito o login a partir dessa mudança, acesse
