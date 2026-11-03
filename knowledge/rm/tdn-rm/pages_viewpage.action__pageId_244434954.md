---
content_hash: efa3b8773d1035b5bcc61d87611a29a068f7ef02251b61ab74487907053ff530
fetched_at: '2026-06-29T00:08:13.965384+00:00'
page_id: '244434954'
product: rm
source: tdn-rm
title: ER_SAUHRM01-510_Ajustes_divisão_de_honorário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244434954
version: 118
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | * [SAUHRM01](http://jiraproducao.totvs.com.br/browse/SAUHRM01) | **IRM** | * [SAUHRM01-402](http://jiraproducao.totvs.com.br/browse/SAUHRM01-402) |
| **Requisito** | * [SAUHRM01-401](http://jiraproducao.totvs.com.br/browse/SAUHRM01-401) | **Subtarefa** | * [SAUHRM01-510](http://jiraproducao.totvs.com.br/browse/SAUHRM01-510) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Este documento tem como objetivo especificar o requisito de ajustes na funcionalidade de divisão de cobranças.

## Definição da Regra de Negócio

 **RN001**

1. Quando o atendimento for retorno, sistema deve validar se existe divisão de cobranças antes de realizar o lançamento, caso seja, o registro deve ser incluído como fora da conta.

**RN002**

1. Quando um lançamento com regra de divisão for realizado, sistema não deve efetuar o lançamento referente ao adicional por horas extras.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Elaboração de Contas | Alteração | Faturamento / Particular e Convênios / Lançamentos na Conta do Paciente | **RN001** |

**Exemplo de Aplicação:**

1. Acesse o menu "**Cadastros / Faturamento / Condições Contratuais com Convênios**" e selecione o convênio que será utilizado no teste;
2. Acesse o menu "**Anexos / Divisão de Cobranças**" e realize a configuração para o profissional desejado, conforme documento contido em:
3. Acesse o menu  "**Atendimento / Pronto Atendimento/Ambulatório / Registro de Atendimentos Externos**";
4. Efetue um novo registro de atendimento, selecionando como prestador responsável o mesmo para o qual foi configurada a regra de divisão;
5. Acesse a elaboração de contas do atendimento;
6. Inclua o lançamento (Honorário ou SADT), para o qual foi configurada a regra de divisão;
7. Sistema deverá efetuar dois lançamentos na conta, sendo um para o prestador responsável e outro para o prestador principal da unidade de faturamento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
