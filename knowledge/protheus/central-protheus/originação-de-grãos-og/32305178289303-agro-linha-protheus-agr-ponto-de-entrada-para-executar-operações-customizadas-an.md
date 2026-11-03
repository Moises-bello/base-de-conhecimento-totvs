---
article_id: 32305178289303
category: Originação de Grãos (OG)
content_hash: 7fcc00d3516e1d5eaf2ab595bc9a79bd9c84fabe0251212b07e871de408d7059
fetched_at: '2026-06-28T22:45:42.926617+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Executar Operações Customizadas
  antes de Cancelar a Liquidação
type: support-article
updated_at: '2025-08-27T13:06:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32305178289303-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Executar-Opera%C3%A7%C3%B5es-Customizadas-antes-de-Cancelar-a-Liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32305192890903) Tempo aproximado para leitura: **00:02:30 min**  
  
**Dúvida**  
Como confirmar um **Ponto de Entrada para Executar Operações Customizadas antes de Cancelar a Liquidação**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA360LIQ | Rotina de Romaneio de Compra utilizada para entradas de cargas. Na emissão do documento do romaneio é obrigatório. | |
| **Pontos de Entrada:** | F565CANC, F565E5, FIN565E2 |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.16 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite executar operações customizadas antes do cancelamento de liquidação, decidindo se os registros a serem processados no cancelamento serão realizados. |
| **Localização:** | Rotina de Cancelamento de Liquidação |
| **Programa Fonte:** | OGA360LIQ |
| **Função:** | F565CANC |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **nOpct** | Numérico | Se retornado o valor 1, é realizado o cancelamento.  Sem parâmetros | NÃO | |

**Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function F565CANC()

     Local nOpct := 1  
     Alert("Exemplo de Alerta anteriormente ao cancelamento de liquidação.")  
      
    Return

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite executar operações customizadas após o cancelamento de liquidação. |
| **Localização:** | Rotina de Cancelamento de Liquidação |
| **Programa Fonte:** | OGA360LIQ |
| **Função:** | FIN565E2 |

**Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function FIN565E2()

     Alert("Exemplo de Alerta para tratamento do titulo gerado pela liquidação após o cancelamento")  
      
    Return
