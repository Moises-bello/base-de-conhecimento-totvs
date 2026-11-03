---
content_hash: 66252e401a66339f9e06b7807a0962729f5b3b4d030436135e1c30d416967d22
fetched_at: '2026-06-29T00:10:46.654349+00:00'
page_id: '555273397'
product: rm
source: tdn-rm
title: Cadastro Cliente/Fornecedor (Integração RM TCGI x Backoffice Protheus - EAI2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555273397
version: 13
---

Os Processos descritos a seguir tem como objetivo orientar nos Cadastros de Clientes e Fornecedores para a Integração no Totvs Construção Gestão de Imóveis x Backoffice Protheus - EAI2.

**Aviso**  
Antes de seguir os passos para cadastro de um cliente e/ou fornecedor é recomendado que seja verificado as configurações de parametrização de integração.  
 entrar na aba "Cadastro de Adapter" que se encontra no link, os adapters utilizados para Cliente (CUSTOMERVENDOR - MATA020) e Fornecedor (CUSTOMERVENDOR - MATA030)

Aviso Importante : <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044416033-MP-FAT-Cadastro-de-Cliente-no-Papel-de-Trabalho>

Cadastro de Cliente no Papel de Trabalho

**Ambiente**Microsiga Protheus - a partir da versão 12

# **CLIENTE - FORNECEDOR**

Quando estivermos cadastrando um Cliente/Fornecedor Estrangeiro vindo do Protheus para o RM, ***deverá existir um estado 'EX' cadastrado na tabela 'GETD' do RM com o valor de País não informado e com a opção nacional desmarcada.***

Caso o cadastro seja do RM para o Protheus para manter a compatibilidade deverá manter obrigatoriamente o estado como EX no RM.  
[SIGACOM - MATA020 Como Cadastrar Fornecedor Estrangeiro no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019752011-MP-SIGACOM-MATA020-COMO-CADASTRAR-FORNECEDOR-ESTRANGEIRO-NO-PROTHEUS)

**Atenção**: Feito um cadastro de Fornecedor você poderá associar no cadastro de Cliente o Fornecedor que poderá ser utilizado na geração de parcelas a Pagar em : Integrações | Integração Protheus | Vincular o Fornecedor ao cadastro do Cliente.

## **CLIENTE**

Poderá ser efetuado o cadastro de cliente tanto no Protheus quanto no RM ou no Portal de Imóvel.

Protheus:   
RM: 

No RM possui uma única visão para se cadastrar Cliente/Fornecedor, sendo assim, o Cliente/Fornecedor tem a opção de campo para marcar que o cadastro seria "Ambos". No entanto - Não é permitido o cadastro como "Ambos" quando se utiliza integrado ao Protheus.

IMPORTANTE

A partir de **04/04/2022** a rotina "Cadastro de Cliente" (**MATA030**) será descontinuada e será obrigatório o uso da rotina "Cadastro de Cliente" (**CRMA980**).  
O configurador de Integração já irá criar o no adpter de Cliente com a nova Rotina e irá preencher o Parâmetro MV\_MVCSA1 Para .T.

**Causa**Isso ocorrerá devido à uma evolução no Produto, a rotina de Cadastro de Clientes (**CRMA980**).

## **FORNECEDOR**

Poderá ser efetuado o cadastro de fornecedor tanto no Protheus quanto no RM ou no Portal de Imóvel

Protheus:   
RM: 

No RM possui uma única visão para se cadastrar Cliente/Fornecedor, sendo assim, o Cliente/Fornecedor tem a opção de campo para marcar que o cadastro seria "Ambos". No entanto - Não é permitido o cadastro como "Ambos" quando se utiliza integrado ao Protheus.
