---
content_hash: 62cd273642a24b7d99bb09b48143820dde1d25537a9f461e21678c865b72a867
fetched_at: '2026-06-29T00:10:59.038370+00:00'
page_id: '611006083'
product: rm
source: tdn-rm
title: 11146630 FISCAL01-15221 - DT Notas de Serviço \ Uso e Consumo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611006083
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | CAT42 |
| Ticket: | 11146630 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15221 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a CAT 42 está sendo considerado, para o Registro 0200, itens que não atendem às consistências de geração do mesmo.

## **03. SOLUÇÃO**

Foi adicionado filtro no layout gerador da rotina da CAT-42 que verifica se os produtos dos lançamentos fiscais são tributados pelo ICMSST para o Estado (UF) e período de início da tributação do tributo em questão.
