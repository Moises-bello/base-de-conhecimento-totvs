---
content_hash: 27d6f0493636076e1d362e0b999e2aa8bd0fafafd13fd1b1210def87b9fe4327
fetched_at: '2026-06-29T00:08:23.967158+00:00'
page_id: '270099915'
product: rm
source: tdn-rm
title: ER_SAUHRM02-330_Taxa_Oxigenio_Litros
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM02-330_Taxa_Oxigenio_Litros
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-346 |
| **Requisito** | SAUHRM02-330 | **Subtarefa** | SAUHRM02-444 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

 

### Objetivo

*Este documento tem como objetivo especificar o requisito de utilização de cobrança de taxa de oxigênio na unidade de medida litros.*

### Definição da Regra de Negócio

**RN001 -**  Criar parâmetro nas condições contratuais, para configurar a cobrança de oxigênio em litros

**RN002 -**  Configurar a unidade de medida litros na rotina "Tabela de Procedimentos e Serviços"

**RN003 -**  Criar nas rotina "Elaboração de contas" e aba "Enfermagem" do Prontuário Eletrônico a opção de lançamento de taxas e serviços em litros. 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Condições Contratuais] | [Alteração] | [Cadastro-> Faturamento->Condições Contratuais com Convênios] | RN001 |
| [Tabela de Procedimentos e Serviços] | [Alteração] | [Cadastros -> Faturamento-> Tabela de Procedimentos e Serviços] | RN002 |
| [Elaboração de Conta] | [Alteração] | [Lançamentos na Conta do Paciente] | RN003 |
| Prontuário | [Alteração] | [Prontuário] | RN003 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
