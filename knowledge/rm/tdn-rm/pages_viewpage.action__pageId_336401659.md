---
content_hash: e1cf7e8ec95fa8735d78bc534ba5ce04ea762ad454cc53489d4c66069338662e
fetched_at: '2026-06-29T00:08:51.059690+00:00'
page_id: '336401659'
product: rm
source: tdn-rm
title: RMSAU-2375 DT Campos de justificativa antimicrobiano, restrito e não padronizado
  por unidade de atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336401659
version: 4
---

# Campos de justificativa antimicrobiano, restrito e não padronizado por unidade de atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | PEP - Prescrição Médica | |
| **Cadastros Iniciais:** | Unidade de Atendimento e Produto |
| **Parâmetro(s):** | Justifica medicamentos Antimicrobianos  Justifica Fármacos Restritos  Justifica Itens não padronizados |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Removido parâmetro "Solicita/Justifica antimicrobianos e fármacos restritos ou não padronizados" presente anteriormente nos parâmetros gerais para os novos parâmetros criados por Unidade de Atendimento, dessa forma pode-se escolher se em uma determinada unidade será ou não realizada a Justificativa de itens antimicrobianos, restritos ou não padronizados.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **TOTVS Gestão Hospitalar (RM Saúde)**, acesse **Cadastros/Uso Geral/Unidades de Atendimento**. Na aba parâmetros da prescrição, configure os parâmetros a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Justifica medicamentos Antimicrobianos  Justifica Fármacos Restritos  Justifica Itens não padronizados |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | Recebe por padrão o que estava marcado no parâmetro geral "Solicita/Justifica antimicrobianos e fármacos restritos ou não padronizados". |

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (RM Saúde), Cadastros > Uso Geral > Unidades de atendimento e marque os parâmetros conforme a imagem

       2.            Acesse PEP / Prescrição Médica

Prescreva um medicamento do tipo não padronizado para que a tela de justificativa seja apresentada
