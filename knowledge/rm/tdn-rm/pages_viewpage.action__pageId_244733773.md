---
content_hash: 18a8f9c1f4c2eae606371bf8589198fba9c30fa80d4fe89911b24966a963326c
fetched_at: '2026-06-29T00:08:15.423520+00:00'
page_id: '244733773'
product: rm
source: tdn-rm
title: ER_SAUHRM01-548_Toten_Registro_Atendimento_Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244733773
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-391 |
| **Requisito** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-396 | **Subtarefa** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-548 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Este documento tem como objetivo especificar o requisito de criação de um Toten, onde este irá ler a carteirinha e ao encontrar o paciente irá registrar automaticamente o atendimento e emitir a senha para o atendimento.

## Definição da Regra de Negócio

    **RN001**

1. No painel de senhas será incluída uma rotina que irá ler a carteirinha do paciente.
2. Ao encontrar o paciente pela matrícula, serão geradas perguntas de segurança como **Data de Nascimento** e **Nome da Mãe.**
3. Com as perguntas respondidas corretamente será registrado o atendimento do paciente automaticamente.
4. Após o registro do atendimento será emitida a senha para o paciente aguardar na fila de espera.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Toten de Pronto Atendimento | Envolvida | Atendimento -> Pronto Atendimento / Ambulatório / Toten de Pronto Atendimento | **RN001** |

**Exemplo de Aplicação**

1. Acesse o RM Saude.
2. Acessar o menu **Cadastro -> Uso Geral -> Unidades de Atendimento.**
3. Parametrize a Unidade de Atendimento que deseja-se utilizar o registro de atendimento automática via Toten.
4. Acessar o menu **Atendimento -> Pronto Atendimento / Ambulatório / Toten de Pronto Atendimento.**
5. Informe a Unidade de Atendimento a ser usada no Toten.
6. Informe a matrícula.
7. Selecione a data de nascimento do paciente.
8. Selecione o nome da mãe do paciente.
9. Retire a senha ao final do registro de atendimento.

         **\*Se durante o processamento da rotina ocorrer qualquer inconsistência, ou alguma informação for respondida errada, o sistema retomará o curso antigo da rotina e o paciente terá seu registro de atendimento feito manualmente por um operador.**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
