---
content_hash: cfb5bb516b4b3889093b969fc7ad5b4654e69d2a44705f7c5d88fb6f5e3a39b2
fetched_at: '2026-06-29T00:10:50.805338+00:00'
page_id: '563431291'
product: rm
source: tdn-rm
title: 9794822 FISCAL01-13942 DT ECF - Relacionamento - Tabela dinâmica 8.13 Adições
  por Doação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563431291
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Gerar arquivo ECF |
| Ticket: | 9794822 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13942 |

## **02. SITUAÇÃO/REQUISITO**

Ao validar a ECF foi apresentado a seguinte mensagem:

A adição ao lucro real desta linha deve ter relacionamento com a conta contábil somente.

       Registro M300 - Campo Valor;

       A inconsistência ocorre pois foi gerado na linha o relacionamento 4 - Lançamento manual, porém no sistema está parametrizado como Contábil, e nesse caso deveria gerar o       relacionamento 2-Contábil;

## **03. SOLUÇÃO**

Foi implementado um parâmetro no layout para sinalizar que não terá mudanças de Origem e Tipo para geração do M300 do grupo de Adições por Doação.
