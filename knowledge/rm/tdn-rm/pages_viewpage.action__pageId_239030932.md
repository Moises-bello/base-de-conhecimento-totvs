---
content_hash: 83933a1b86bbfeaa8cc2644c8b4a22bb813ecfe4e94fae2bf8757d9d49300511
fetched_at: '2026-06-29T00:08:09.249664+00:00'
page_id: '239030932'
product: rm
source: tdn-rm
title: ER_SAUHRM01-9_Integração_Responsável_X_Cadastro_de_Visitantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239030932
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-8 |
| **Requisito** | SAUHRM01-9 | **Subtarefa** | SAUHRM01-105 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Este documento tem como objetivo especificar o requisito de integração entre o cadastro de responsável e o cadastro de visitantes, onde o sistema deverá possibilitar a exportação dos dados de um responsável para o cadastro de visitantes. 

## Definição da Regra de Negócio

**RN001**

1. Criar uma opção com o texto "Integrar cadastro de visitante", cuja função será responsável por habilitar a realização do cadastro das informações do responsável na tabela de visitantes.

**RN002** 

1. Na tela de registro de internações, aba "Responsável", criar uma janela ao salvar o registro, perguntando se o usuário deseja incluir no cadastro de visitantes o responsável que foi cadastrado.
2. Verificar se já existe um cadastro com aquele número de CPF antes de fazer a inserção na tabela de visitantes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Gerais | [Criação] | [Opções -> Parâmetros -> Parâmetros Gerais] | RN001 |
| Registro de Internações | [Criação] | [Atendimento -> Internação -> Registro de Internações ->  Responsável -> Pesquisa Responsável -> Cadastrar novo responsável ->  Responsável pelo Paciente/Responsável Legal] | RN002 |

**Exemplo de Aplicação:**

1. Acessar o menu "Atendimento > Internação > Registro de Internações";
2. Preencher as informações referentes à internação;
3. Acessar a aba "Responsável";
4. Informar os dados do responsável e clicar no botão "OK";

**Tabelas Utilizadas**

* SZCADVISITANTE - Tabela com as informações dos visitantes.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
