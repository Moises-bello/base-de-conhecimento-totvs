---
content_hash: 5dee3ec8990ecbff1c4b040845537dd3d91037c6e8cba071f4b257d4af34523b
fetched_at: '2026-06-29T00:06:21.804203+00:00'
page_id: '223181888'
product: rm
source: tdn-rm
title: ER_PCREQ-8817_Copiar_Endereco_Empresa_Para_Funcionario
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8817_Copiar_Endereco_Empresa_Para_Funcionario
version: 3
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | PCREQ-6493 |
| **Requisito1** | PCREQ-8817 | **Subtarefa1** | PDR\_EDU\_EDU016-26 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

O objetivo dessa implementação é permitir que no momento do cadastro do endereço do funcionário da empresa, nas rotinas da Central de Estágio, seja possível que o usuário copie o mesmo endereço da empresa para o funcionário.

## Definição da Regra de Negócio

No momento em que o usuário estiver cadastrando um funcionário para uma empresa na central de estágios, esse usuário deverá ter a opção de atribuir ao endereço do funcionário que está sendo cadastrado o mesmo endereço da empresa à qual ele pertence. Essa regra vale tanto para a tela de cadastro de funcionário da empresa no Sistema quanto para a tela Web disponível no Fluig.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Funcionários da Empresa (Sistema) | [Alteração] | [TOTVS Educacional -> Atividades Acadêmicas -> Empresas -> Anexos -> Funcionários da empresa] | - |
| Cadastro de Funcionários da Empresa | [Alteração] | Fluig | - |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
