---
content_hash: 06be51ae022ce088502dff18636bf4701f96502f9ffe4b8cd40f078dbe4ef536
fetched_at: '2026-06-29T00:08:06.129505+00:00'
page_id: '236585081'
product: rm
source: tdn-rm
title: ER_PCREQ-10857_Utilitario_para_exportacao_dados_PEP_RM
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10857_Utilitario_para_exportacao_dados_PEP_RM
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Utilitário para exportação dos dados do PEP RM

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Utilitários |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | R\_SAU\_RM\_V12\_1516 | **IRM1** | PCREQ-10856 |
| **Requisito1** | PCREQ-10857 | **Subtarefa1** | SAU\_DEV-4692 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 

O objetivo do utilitário é exportar os dados do prontuário da linha RM através do RM Reports para a central de documentos do PEP 2.0

### (Obrigatório)

## Definição da Regra de Negócio

O utilitário deverá disponibilizar as opções de gerar os relatório por paciente e por atendimento. Por paciente, será gerado um documento contendo as informações de todos os atendimento. Já por atendimento, será gerado um documento para cada atendimento de cada paciente.

Além do tipo, deve-se selecionar o relatório correspondente e a pasta onde os documentos serão armazenados na central de documentos do PEP 2.0

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Assistente de exportação de dados para a Central de Documentos (PEP 2.0) | [Criação] | Utilitários -> Utilitários do RM Saúde | - |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
