---
article_id: 23512656735255
category: Originação de Grãos (OG)
content_hash: db872c41eac9d59b5fcd3ea546c7e98d18268ca9317040e855bd1e6f25b1fdc5
fetched_at: '2026-06-28T22:45:44.962419+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Tabela de Controle de Contratos por Qtd Física
  ou Fiscal no OGA250
type: support-article
updated_at: '2025-06-24T20:44:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23512656735255-Agro-Linha-Protheus-AGR-Tabela-de-Controle-de-Contratos-por-Qtd-F%C3%ADsica-ou-Fiscal-no-OGA250
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23512630270999) Tempo aproximado para leitura: **00:01:****25 min** **Dúvida**  
O que é que indica a estrutura de uma tabela de **Controle de Contratos por Qtd Física ou Fiscal** no Romaneio **OGA250**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**

**Controle de Contratos por Qtd Física ou Fiscal:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus® |
| **Segmento:** | Gestão Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s)** | **Nome Técnico** | | OGA250 | Romaneios com pesagem | | OGA290 | Contratos de Venda | | OGR253 | Relatório Classificações por romaneio | | OGC003 | Movimento Romaneio | | OGR250 | Impressão romaneio c\ pesagem | | OGA260 | Controle depto de 3 | | OGA270 | Controle depto Em 3 | |
| **Parâmetros** | ``` MV_AGOCLAS ``` |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [DAGROGAP-383\DAGROGAP-382](http://jiraproducao.totvs.com.br/browse/DAGROGAP-383) |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | Todos |
| **Tabelas Utilizadas:** | NJJ, NJK, NJR |
| **Sistema(s) Operacional(is):** | Windows® / Linux® |

  

**Descrição:**

Este projeto tem por finalidade permitir o controle de qualidade dos produtos na origem e no destino do romaneio.
