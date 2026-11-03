---
content_hash: 9c19f987ecec3414648de74987efd448eea0cc8789c2f8f0df02fe63b57ef8b7
fetched_at: '2026-06-29T00:05:45.022508+00:00'
page_id: '1001616047'
product: rm
source: tdn-rm
title: Portal de Imóveis - Permissão de Usuário na Proposta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1001616047
version: 7
---

Este documento tem por objetivo demonstrar a configuração de usuário e perfil minima para permissão de criação de uma proposta em clientes que utilizam base PI unificada.  
Considerando que os usuários do PI já começam a ter algumas consistências de segurança provenientes de configuração do TCGI.

# Documento de Configuração de Perfil

**Perfil:** `PI_VENDAMIN – PI Permissão Mínima Venda CRUD`

## 1. Objetivo

Este documento tem como objetivo descrever a criação e configuração do perfil **PI\_VENDAMIN**, desenvolvido para controlar o acesso de usuários vinculados a fornecedores que possuem cadastros tanto no **PI** quanto no **TCGI** utilizando o mesmo CPF/CNPJ.

O perfil foi estruturado para fornecer somente as permissões mínimas necessárias, permitindo ao corretor executar operações de **CRUD** (*Criar, Ler/Visualizar, Atualizar e Excluir*) sobre contratos e documentos, sem conceder acessos adicionais que possam comprometer a segurança ou ampliar as funções além do necessário.

## 2. Escopo

O perfil **PI\_VENDAMIN** deve ser associado exclusivamente aos usuários que necessitam realizar operações básicas de gestão de contratos de venda.

Este perfil **não concede** permissões para processos administrativos, relatórios, parametrizações ou integrações.

## 3. Configuração do Perfil

### 3.1 Identificação

Na tela de identificação do perfil, foram definidos os seguintes parâmetros:

* **Código do Perfil:** `PI_VENDAMIN`
* **Identificação:** `PI Permissão Mínima Venda CRUD`
* **Identificador:** `PI_VENDAMIN`
* **Status:** Ativo

### 3.2 Permissões Liberadas

As permissões liberadas estão relacionadas à gestão de **contratos de venda** e **documentos**, garantindo o ciclo CRUD.

#### [01.01.01] Contratos de Venda

* **[01.01.01.01] Contratos: Incluir**
* **[01.01.01.02] Contratos: Excluir**
* **[01.01.01.03] Contratos: Editar**

#### [01.01.02] Contratos de Venda - Parte 2

* **[01.01.02.02] Contratos: Gerar Plano De Financiamento**
* **[01.01.02.03] Contratos: Excluir Plano Financiamento**
* **[01.01.02.04] Contratos: Documentos - Visualizar**
* **[01.01.02.05] Contratos: Documentos - Editar**
* **[01.01.02.06] Contratos: Documentos - Incluir**
* **[01.01.02.07] Contratos: Documentos - Excluir**
* **........**
* **[01.01.02.15] Contratos: Condições de Financiamento- Visualizar**
* **[01.01.02.16] Contratos: Condições de Financiamento- Incluir**
* **[01.01.02.17] Contratos: Condições de Financiamento- Editar**
* **[01.01.02.18] Contratos: Condições de Financiamento- Excluir**

## 4. Considerações Finais do Perfil

* O perfil garante que o corretor terá **apenas as permissões essenciais** relacionadas ao processo de vendas.
* A configuração atende ao princípio do **menor privilégio**, reduzindo riscos de acesso indevido.
* Qualquer nova necessidade de acesso deverá ser formalmente solicitada e analisada pela equipe responsável pela gestão de perfis.

# 5. Associação do Perfil a Usuários e CLI/FOR

Após a criação do perfil **PI\_VENDAMIN**, o próximo passo é associá-lo corretamente a um usuário do sistema e, em seguida, vinculá-lo ao respectivo **Cliente/Fornecedor (CLI/FOR)**, garantindo a unicidade pelo CPF.

## 5.1 Criação do Usuário

O primeiro passo é criar o cadastro do usuário que utilizará o perfil.

Na **Imagem 4**, temos o exemplo do usuário **Victor Thiago da Luz**, criado com os seguintes dados:

* **Usuário:** 29546010006
* **Nome:** Victor Thiago da Luz
* **Status:** Ativo
* **Validade:** Sempre válido

📌 **Imagem 4 – Criação do Usuário**

## 5.2 Associação do Perfil ao Usuário

Após a criação, o usuário deve receber o perfil **PI\_VENDAMIN**.

Na **Imagem 5**, vemos a tela de associação, onde foi feita a busca pelo perfil e a seleção da opção **PI\_VENDAMIN**, garantindo que o usuário terá apenas as permissões mínimas de CRUD definidas anteriormente.  
  
  
📌 **Imagem 5 – Associação do Perfil ao Usuário**

## 5.3 Associação do Usuário ao CLI/FOR

Por fim, é necessário vincular o usuário ao seu respectivo **Cliente/Fornecedor**, respeitando a unicidade pelo **CPF**.

Na **Imagem 6**, observamos que o usuário **29546010006 – Victor Thiago da Luz** foi associado ao registro de Cliente/Fornecedor correspondente. Isso garante que o acesso será validado sempre pelo **CPF único** do usuário.  
  
  
📌 **Imagem 6 – Associação do Usuário ao CLI/FOR**

## 6. Considerações Finais - Segurança Criada

* A ordem correta do processo é: **criar usuário → associar perfil → vincular ao CLI/FOR**.
* A unicidade do CPF é fundamental para evitar inconsistências entre cadastros no **PI** e no **TCGI**.
* Um mesmo CPF não deve estar vinculado a mais de um usuário.
* Alterações de perfil devem ser solicitadas formalmente à equipe de TI.
