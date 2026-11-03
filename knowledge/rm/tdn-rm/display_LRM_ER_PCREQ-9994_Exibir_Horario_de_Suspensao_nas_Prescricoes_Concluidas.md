---
content_hash: 26c36f89c07bf6a449414d090106f5700b174313cd40a6b3f345791cc3070824
fetched_at: '2026-06-29T00:06:27.338953+00:00'
page_id: '232819819'
product: rm
source: tdn-rm
title: ER_PCREQ-9994_Exibir_Horario_de_Suspensao_nas_Prescricoes_Concluidas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9994_Exibir_Horario_de_Suspensao_nas_Prescricoes_Concluidas
version: 117
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Exibição do Horário de Suspensão do Item nas Prescrições Concluídas

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Prontuário |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-9991 |
| **Requisito1** | PCREQ-9994 | **Subtarefa1** | SAU\_DEV-4200 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Exibir o horário de suspensão do medicamento na grid de Prescrições concluídas e na página de Enfermagem, sub-aba Check de Medicamentos

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Prescrições Concluídas | [Alteração] | Prontuário | Incluir a coluna de Horário da Suspensão na grid das Prescrições Concluídas. No momento em que o botão de Suspender item for clicado, deve-se gravar nas colunas RECMODIFIEDON e RECMODIFIELDBY a data/hora e o usuário que está suspendendo. |
| Check de Medicamentos | [Alteração] | Prontuário | Incluir a coluna de Horário da Suspensão na grid de Check de Medicamentos. |

**Tabelas Utilizadas**

* SZITEMPRESCRICAO - Itens da prescrição
* SZAPRAZAMENTO – Horários do aprazamento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
