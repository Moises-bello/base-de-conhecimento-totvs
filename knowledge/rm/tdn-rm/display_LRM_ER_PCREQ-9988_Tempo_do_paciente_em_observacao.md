---
content_hash: 5fa7dfbb773e599bf89973f1f986887de47cc1aebfdcfb71936398fac178627f
fetched_at: '2026-06-29T00:06:27.220446+00:00'
page_id: '231899799'
product: rm
source: tdn-rm
title: ER_PCREQ-9988_Tempo_do_paciente_em_observacao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9988_Tempo_do_paciente_em_observacao
version: 119
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Tempo em Observação do paciente na Classificação de Risco

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Atendimento |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-9983 |
| **Requisito1** | PCREQ-9988 | **Subtarefa1** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Para pacientes em observação, a coluna "Espera" ficava em branco. Incluir o tempo em que o paciente está em observação a partir da data/hora que o mesmo foi transferido para observação (aba de "Atendimento Médico")

### (Obrigatório)

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Painel de Classificação de Risco | [Alteração] | Atendimento -> Pronto Atendimento -> Painel de Classificação de Risco | Cálculo do tempo em que o paciente encontra-se em observação na página "Atendimento Médico".   O cálculo deve pegar a data/hora/minutos/segundos atual e calcular o tempo de observação a partir da mudança de status de "Em atendimento" para "Em observação" |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
