---
content_hash: c8ca44da59115fe55e2bd0f76913859066fc31695c19b13f22f2871a02c47eb2
fetched_at: '2026-06-29T00:09:01.511595+00:00'
page_id: '372559978'
product: rm
source: tdn-rm
title: DT Aditivo de Contrato - Data Início de Vigência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372559978
version: 1
---

# CONTRATO / ITEM DE CONTRATO / ADITIVO

### Características do Requisito

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Construção & Projetos | | |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Contrato | CtrCntAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | CtrItmAditivoCntAction | Aditivo do Item de Contrato | | | |
| ****Tickets relacionados**:** | Não se aplica. | | |
| **Requisito (ISSUE):** | MATESTCNTFTOF01-2035 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Banco(s) de Dados:** | SQL Server e Oracle. | | |
| **Tabelas Utilizadas:** | TITMCNTADITIVO - Aditivos de Contrato | | |
| **Sistema(s) Operacional(is):** | Windows. | | |
| **Outros:** |  | | |

## Objetivo

 

Permitir que o usuário defina a data de início de vigência do aditivo do contrato.

## Definição da Regra de Negócio

Este documento visa complementar o que foi desenvolvido para atender à inclusão da informação de início de vigência do aditivo do contrato.. 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Aditivo do item de contrato | Criação | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Manutenção de Contrato \ Item de Contrato \ Aditivo do Item de Contrato | Criar na Aditivo do Item de Contrato os campos:   * Data de Início de Vigência do Aditivo |
|  |  |  |  |

**Cadastro do Aditivo do Item de Contrato**

Criar os campos:

* **Data de início de vigência do aditivo:**campo do tipo data, visível apenas na visão do aditivo do item de contrato, somente informativo, não interfere no aditivo.

**Consistências:**

Nenhuma consistência relacionada ao campo "Data de início de vigência do aditivo".

**Tabelas Utilizadas**

* TITMCNTADITIVO – Aditivos de Contrato.

## Procedimento para Utilização

1. Acesse **Contratos| Item de Contrato| Página Aditivos ;**

Na visão de aditivos do item de contrato defina a visibilidade da coluna "Data de início de vigência do aditivo" e preencha o valor do campo na visão.

## Procedimento para Configuração

Para utilizar este recurso será necessário baixar na central de downloads o último patch da Biblioteca RM

* Biblioteca RM versão 12.1.21 - Criação de campo no conversor.

Solicitar ao Suporte o script que cria os campos no aditivo de contrato.

Versões disponíveis:

* Biblioteca RM versão 12.1.18.304 ou superior
* Biblioteca RM versão 12.1.19.306 ou superior
* Biblioteca RM versão 12.1.20.305 ou superior

## Dicionário de Dados

**Código do Script:** /\*$Versao=NU.2018.06\_01\*/

|  |  |
| --- | --- |
| **Tabela** | TITMCNTADITIVO |
| **Campo** | DATAINICIOVIGENCIA |
| **Tipo** | DATETIME2 |
| **Tamanho** | 8 |
| **Valor Inicial** | NULL |
| **Descrição** | Data de início da vigência do aditivo |
| **Título** | Data de início da vigência do aditivo |
