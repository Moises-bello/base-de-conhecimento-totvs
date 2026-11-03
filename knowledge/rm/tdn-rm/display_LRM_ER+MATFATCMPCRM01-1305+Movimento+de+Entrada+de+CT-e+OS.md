---
content_hash: 1f57e632ac4c0394937cbc70ad79a29ff9f5878555e44b3578b8796e2d21bb27
fetched_at: '2026-06-29T00:08:42.222227+00:00'
page_id: '287062437'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-1305 Movimento de Entrada de CT-e OS
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+MATFATCMPCRM01-1305+Movimento+de+Entrada+de+CT-e+OS
version: 103
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-1305 |
| **Requisito/Story/Issue1** | MATFATCMPCRM01-1602 | **Subtarefa1** | NA |
| **País** | ( x ) Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Descrever as alterações que deverão ser implementadas no sistema para que seja possível a inclusão de movimentos de entrada de CT-e OS, permitindo assim o correto tratamento das integrações financeira, contábil e fiscal desse documento no ERP.

## 

## Definição da Regra de Negócio

Para que um movimento seja considerado de entrada de CT-e OS, é necessário que nos parâmetros do Tipo de Movimento, na etapa Fis - Escrituração 1/2, em **Tipo Documento Escrituração**, o campo **Código Default** ou em **Outros Códigos** esteja informado um Tipo de Documento que tenha o campo **Código do Modelo do Documento** preenchido com o valor **67** e na etapa Fis - Conhecimento de Transporte, o campo **Tipo de Operação do Conhecimento de Transporte** esteja selecionada a opção Cadastrar CTRC/CTE.

Na edição de movimento, se em Integrações | Fiscal, no campo **Tipo de Documento** estiver informado um Tipo de Documento que tenha o campo **Código do Modelo do Documento** preenchido com o valor **67**, no menu**Integrações**deverá ser exibida a opção **CT-e Transporte**, que exibirá a tela CT-e Transporte em que é exibido o campo Chave de Acesso do CT-e. Nesse campo deverá ser informada a chave de acesso do CT-e OS que está sendo recebido pelo cliente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |

**Tabelas Utilizadas**

* TMOV - Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
