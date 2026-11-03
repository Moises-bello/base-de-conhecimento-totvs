---
article_id: 31177033788183
category: Originação de Grãos (OG)
content_hash: 4f5271608b0cfcad313474838afa97ea3639d8eccdeb2da12b9d7f7babf04ada
fetched_at: '2026-06-28T22:45:42.945965+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para incluir novos itens no
  menu das Ações Relacionadas
type: support-article
updated_at: '2025-07-10T19:47:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31177033788183-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-incluir-novos-itens-no-menu-das-A%C3%A7%C3%B5es-Relacionadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31176989565975) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**O que indica a tabela **Ponto de Entrada para incluir novos itens no menu das Ações Relacionadas**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA035D | Cadastro de Tabelas de Descontos Agrícolas | |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.19 |

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA035 | Cadastro de Tabela de Classificação Agrícola | |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.19 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Definição de Menu |
| **Programa Fonte:** | AGRA035D |
| **Função:** | Permite incluir novos itens no menu "Ações Relacionadas". |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | AG35DMNU | Variedade | Não envie parâmetros. | NÃO | |

****Exemplo:****

#Incluir ' [Protheus.ch](http://protheus.ch/) '  
#incluir " [fwmvcdef.ch](http://fwmvcdef.ch/) "

Função do usuário AG35DMNU ()  
Local aRotina := {}  
aAdd( aRotina, { "TESTE PNT ENT.", " AG35DMNU ", 0, 4, 0, Nil } )  
Retorno (aRotina)

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Definição de Menu |
| **Programa Fonte:** | AGRA035 |
| **Função:** | Permite incluir novos itens no menu "Ações Relacionadas". |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | AGR35MNU | Variedade | Não envie parâmetros. | NÃO | |

****Exemplo:****

#Incluir ' [Protheus.ch](http://protheus.ch/) '  
#incluir " [fwmvcdef.ch](http://fwmvcdef.ch/) "

Função de usuário AGR35MNU ()  
Local aRotina := {}  
aAdd( aRotina, { "TESTE PNT ENT.", " AGR35MNU ", 0, 4, 0, Nil } )  
Retornar (aRotina)
