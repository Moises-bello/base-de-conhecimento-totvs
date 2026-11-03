---
content_hash: bc3059c44616543355bd1d3e53a81666e66b31847efc53bdbddc094140d2d78e
fetched_at: '2026-06-29T00:06:26.689618+00:00'
page_id: '226527400'
product: rm
source: tdn-rm
title: ER_PCREQ-9992_Velocidade_de_Infusao_para_a_enfermagem
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9992_Velocidade_de_Infusao_para_a_enfermagem
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

# Velocidade de Infusão disponível para a Enfermagem

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** |  |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-9991 |
| **Requisito1** | PCREQ-9992 | **Subtarefa1** | SAU\_DEV-4194 |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Disponibilizar a informação da velocidade/tempo de infusão informada na prescrição médica para os locais em que o setor de enfermagem tem acesso, ou seja, nas prescrições concluídas, na aba Enfermagem/Check de medicamentos

### (Obrigatório)

## Definição da Regra de Negócio

Prontuário

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Prontuário Eletrônico | Alteração | Prontuário | - |
| Prescrições Concluídas | Alteração | Prontuário | Inclusão na grid das colunas Velocidade de infusão e tipo |
| Check de medicamentos | Alteração | Prontuário | Inclusão na grid da coluna tipo de velocidade/tempo |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
