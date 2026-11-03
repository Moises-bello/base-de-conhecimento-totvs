---
content_hash: 2c90fb43f294ad3d0fb8a013ae30ffee81dd3c4653af96caa7f11d8afddbcca0
fetched_at: '2026-06-29T00:08:57.263640+00:00'
page_id: '353286739'
product: rm
source: tdn-rm
title: DT Cadastro de Produto - Unidade Tributável Interna
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353286739
version: 9
---

# PRODUTO / NF-e PREENCHIMENTO DAS TAGS cEAN e cEANTrib NO XML DA NF-e

### Características do Requisito

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| ****Segmento Executor:**** | Construção & Projetos | | |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Produto | EstPrdAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | FisNFeEnvioAction | Envio de NF-e | | | |
| ****Tickets relacionados**:** | Não se aplica. | | |
| **Requisito (ISSUE):** | MATESTCNTFTOF01-2018*.* | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Banco(s) de Dados:** | SQL Server e Oracle. | | |
| **Tabelas Utilizadas:** | TPRODUTODEF - Definições dos Produtos. | | |
| **Sistema(s) Operacional(is):** | Windows. | | |
| **Outros:** |  | | |

## Objetivo

 

Permitir que o usuário defina a Unidade Tributável Interna e o Fator de Conversão Tributável Interna no cadastro de Produtos para ser utilizado na NF-e.

## Definição da Regra de Negócio

Este documento visa complementar o que foi desenvolvido para atender à Nota Técnica 2016/001 - Unidade Tributável no Comércio Exterior (consultar link acima). 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Produto | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Produto | Na pasta Controle de Estoque alterar a descrição dos campos:   * Unidade Tributável para Unidade Tributável Exterior * Fator de Conversão Tributável para Fator de Conversão Tributável Exterior |
| Produto | Criação | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Produto | Criar na pasta Controle de Estoque os campos:   * Unidade Tributável * Fator de Conversão Tributável |
| Unidades de Medida | Alteração | RM \ BackOffice \ Gestão de Estoque, Compras e Faturamento \ Cadastros \ Mais \ Tabelas Auxiliares \ Unidade | - |

**Cadastro de Unidades de Medida**

Alterar a descrição do campo Unidade Tributável Comércio Exterior para **Unidade Tributável**.

**Cadastro de Produto**

Para atender esta implementação da Unidade Tributável Interna e o Fator de Conversão Tributável Interna serão necessário realizar as seguintes alterações no cadastro de Produto pasta Controle de Estoque:

Alterar a descrição dos campos existentes:

* Unidade Tributável para **Unidade Tributável Exterior.**
* Fator de Conversão Tributável para **Fator de Conversão Tributável Exterior**

Criar os campos:

* **Unidade Tributável:**campo do tipo lookup que deverá apresentar apenas as unidades de medida que estão configuradas como Tributável, ou seja, apenas aquelas que no cadastro de **Unidades de Medida** estão com o campo **Cód. Unidade Tributável** preenchido.
* **Fator de Conversão Tributável.**

**Consistências:**

No momento da gravação do registro do Produto o sistema irá verificar, e caso a unidade base da Unidade Tributária informada seja diferente da unidade base da Unidade de Controle do produto, o sistema não permitirá, sendo exibida a seguinte mensagem: "Produto X: A Unidade Tributável não está compatível com a Unidade de Controle."

**Tabelas Utilizadas**

* TPRODUTODEF – Definições dos Produtos.

## Procedimento para Utilização

1. Acesse **Cadatros | Mais | Tabelas Auxiliares | Unidade;**

Defina a Unidade de Medida como Tributável:

2. Acesse **Cadastros | Produto |** **Controle Estoque**;

Preencha os campos **Unidade Tributável** e ****Fator de Conversão Tributável.****

## Procedimento para Configuração

Para utilizar este recurso será necessário baixar na central de downloads o último patch da Biblioteca RM e solicitar ao Suporte o script que cria os campos no cadastro de Produto.

Versões disponíveis:

* Biblioteca RM versão 12.1.18.222 ou superior
* Biblioteca RM versão 12.1.19.183 ou superior
* Biblioteca RM versão 12.1.20.123 ou superior
* Biblioteca RM versão 12.1.21

## Dicionário de Dados

**Código do Script:** /\*$Versao=NU.2018.04\_03\*/

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | CODUNDTRIBUTAVELINT |
| **Tipo** | VARCHAR |
| **Tamanho** | 5 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Código Unidade Tributável Interno no Produto. |
| **Título** | Unidade Tributável |
| **Help de Campo** | Informar a Unidade Tributável. Serão apresentadas apenas as unidades de medida que estão configuradas como Tributável. |

|  |  |
| --- | --- |
| **Tabela** | TPRODUTODEF |
| **Campo** | FATORCONVERSAOTRIBUTAVELINT |
| **Tipo** | NUMERIC |
| **Tamanho** | 21,10 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não ( x ) |
| **Descrição** | Fator de Conversão Tributável Interno. |
| **Título** | Fator de Conversão Tributável. |
| **Help de Campo** | Informar o Fator de Conversão Tributável. |
