---
content_hash: f4b57800183b0994efb654366e3f24a2739b4a4d1fe150154a7c7cacf725a292
fetched_at: '2026-06-29T00:10:52.188100+00:00'
page_id: '570382565'
product: rm
source: tdn-rm
title: FISCAL01-14030 DT REINF R-2060 Tag tipoAjuste de Lançamento de Entrada CPRB
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570382565
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração dos Eventos REINF R-2060 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14030 |

## **02. SITUAÇÃO/REQUISITO**

Os valores de exclusões da receita que foram apurados na CPRB também devem ser gerados na Reinf.  Iremos alterar o R-2060 para gerar os valores de exclusão no grupo tipoCod campo vlrExcRecBruta, o campo vlrRecBrutaAtiv hoje é preenchido com o valor  da Base de Cálculo e passará a ser gerado com o Valor da Receita da Atividade.

Devido a uma restrição da Reinf, os valores gerados no campo vlrExcRecBruta provenientes de Lançamentos Fiscais também devem gerar valores do grupo de ajuste

## **03. SOLUÇÃO**

Os lançamentos fiscais de Entrada utilizados para exclusão da base de cálculo na apuração da CPRB serão apresentados no registro R-2060 na tag tipoAjuste.

O campo Código da Contribuição Social do tributo dos itens do lançamento fiscal será apresentado também para o tributo CPRB.

O campo tpAjuste será sempre preenchido com 0;  
O campo codAjuste será preenchido com a informação apresentada no campo DTRBITEM.CODCONTRIBSOCIAL "Código da Contribuição Social";  
O campo vlrAjuste será preenchido com DTRBITEM.BASETRB "Base de Cálculo do Tributo CPRB";  
O campo descAjuste será preenchido com DLAF.DOCINI "Número do Documento";  
O campo dtAjuste será preenchido com o Mês/Ano do Lançamento Fiscal;
