---
content_hash: 2a1886f6e643d4dd2313d0562eaeb182b32e4d171c2faa533feec17fd12c25ec
fetched_at: '2026-06-29T00:05:51.674142+00:00'
page_id: '1052750483'
product: rm
source: tdn-rm
title: Contrato de Locação - Anexo - Controle de Acesso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1052750483
version: 6
---

## 1. Visão Geral

O módulo de **Controle de Acesso** é a funcionalidade central para a governança de permissões no Portal do Lojista. Ele permite vincular usuários específicos a contratos de locação ativos, habilitando a execução de atendimentos diretamente pelo portal.

## 2. Pré-requisitos e Dependências

Antes de realizar a associação ao contrato, certifique-se de que os seguintes critérios foram atendidos:

1. **Cadastro de Usuário:** O usuário deve estar previamente cadastrado no sistema base.
2. **Perfil de Acesso:** O perfil vinculado ao usuário deve possuir permissões específicas para a "Gestão de Contratos de Aluguel". Sem essa atribuição, o acesso ao portal será negado ou limitado.
3. **URL de Acesso:** O acesso ao portal é realizado através do endereço: `http://site:porta/portal-imobiliario/#/auth/login`.

> **Para mais detalhes sobre a criação de usuários, consulte: [Manutenção de Usuários](https://tdn.totvs.com/pages/viewpage.action?pageId=435105178)  
> Para mais detalhes sobre o Portal do Lojista acesse:**

## 3. Procedimento de Configuração (Associação de Contrato)

Siga o fluxo abaixo para conceder acesso a um colaborador no contexto de um contrato de locação:

1. Acesse o módulo de **Locação**.
2. Selecione o contrato desejado.
3. Navegue até o menu **Anexos** > **Controle de Acesso**.
4. Clique em **Incluir/Novo** e preencha os campos obrigatórios:

   * **Código do Usuário:** Selecione o usuário previamente cadastrado.
   * **Função na Estrutura:** Defina a responsabilidade do usuário no contexto da loja (Ex: Gerente, Funcionário, Proprietário).

## 4. Operações Disponíveis no Portal

Após a configuração bem-sucedida, o usuário estará apto a realizar as seguintes rotinas operacionais:

4.1 Gestão de Atendimento

Interface para comunicação direta entre o lojista e a administradora, permitindo o registro de solicitações e anexação de documentos.

* **Referência Técnica:** [Manual de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=904060317)
