---
content_hash: fc0a081057f69052edd93ad2089f80de239f0312dec95bc18cd873786a837647
fetched_at: '2026-06-29T00:12:15.292407+00:00'
page_id: '975769386'
product: rm
source: tdn-rm
title: Acelerador de Implantação PDC - Endereço Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=975769386
version: 4
---

## Esta tela apresenta a **lista de portais já cadastrados** no sistema, exibindo informações básicas como **Endereço do Portal**, **Título** e **Descrição**.

Aqui, o usuário deve **selecionar o portal** que deseja configurar utilizando o botão de seleção (círculo à esquerda).

Atenção

Todas as etapas de configuração seguintes serão aplicadas **apenas ao portal selecionado** nesta tela.

Isso significa que:

* Cada portal possui **suas próprias configurações** independentes.
* Para configurar um **novo portal**, selecione-o na lista e clique em **Próximo** para avançar.
* Caso seja necessário configurar outro portal, retorne a esta tela, selecione o novo portal e avance novamente para suas configurações específicas.

Também é possível:

* **Cadastrar um novo portal** clicando em **+ Novo**.
* **Editar** ou **excluir** um portal já existente usando o menu de ações (ícone “...”).

## **Acelerador de Implantação PDC – Cadastro/Edição**

Esta tela é usada para **criar** ou **editar** um portal. O registro criado aqui aparecerá na listagem anterior e servirá como **contexto** para as próximas etapas do acelerador (ou seja, tudo que você configurar em seguida valerá para **este** portal).

## Campos

### 1) Endereço do Portal

Informe a **URL base** pela qual o usuário acessa o Portal do Cliente.

**Exemplo:**exemplo.com.br

**Boas práticas**

* Use a **URL pública final** (a mesma que o usuário usa), não o endereço interno do servidor.
* Evite rotas de páginas específicas (ex.: `/login`, `/home`). Informe **apenas a base** do portal.

### 2) Título

Nome amigável para identificar o portal na lista

**Exemplo:**Portal Exemplo

### 3) Descrição

Campo livre para observações e descrições sobre o portal.

**Exemplo:**Portal do Cliente de vendas
