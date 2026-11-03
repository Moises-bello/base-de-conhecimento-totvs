---
content_hash: 8d60013f3138f39df83c334fe2829d1c74d49e2712d2939f3c8ee5e14edae243
fetched_at: '2026-06-29T00:08:11.359669+00:00'
page_id: '242389772'
product: rm
source: tdn-rm
title: ER_SAUHRM01-324_E-mail_na_Especialidade
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM01-324_E-mail_na_Especialidade
version: 107
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Cadastros |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM01 | **IRM1** | SAUHRM01-322 |
| **Requisito1** | SAUHRM01-324 | **Subtarefa1** | SAUHRM01-331 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 Incluir o campo de e-mail no cadastro de especialidades que será utilizado no PEP 2 para envio de pareceres solicitados à especialidade

### (Obrigatório)

## Definição da Regra de Negócio

**RN01**: Incluir o campo de e-mail no cadastro de especialidades

**RN02**: Preencher no objeto de especialidade (PhysicianSpecialityWrapper) a propriedade email na camada de integração com o PEP 2

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cadastro de Especialidades | [Alteração] | Cadastros -> Uso Geral -> Especialidade | RN01 |
| Objeto PhysicianSpecialityWrapper | [Alteração] | - | RN02 |

***Tabelas Utilizadas***

* *SZESPECIALIDADE - Cadastro de especialidades*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
