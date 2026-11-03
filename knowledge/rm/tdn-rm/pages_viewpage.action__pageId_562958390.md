---
content_hash: c2fa2a0c034b18cdbc03b837325e97a6f95e1585b384bccd59529410fdbc2af8
fetched_at: '2026-06-29T00:10:50.706779+00:00'
page_id: '562958390'
product: rm
source: tdn-rm
title: 9465566 FISCAL01-13837 - DT EFD - Gerar Valores para Notas Sem Direito a Crédito
  (PIS/COFINS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562958390
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| Ticket: | 9465566;8208115 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13837;FISCAL01-12651 |

## **02. SITUAÇÃO/REQUISITO**

O sistema está levando para o arquivo do EFD Contribuições os lançamentos com CST 49, mesmo marcando a opção NÃO no parâmetro "Gerar Valores para Notas Sem Direito a Crédito (PIS/COFINS)", quando o correto é não levar, visto que são operações sem receita e não precisam ser informados na EFD-Contribuições.  
Documentos que não se refiram a operações geradoras de receitas ou de créditos de PIS/Pasep e de COFINS.  
O sistema não está levando a base de calculo dos lançamentos com CST 06.  
E para o CST 04, levou a base de calculo para alguns lançamentos e para outros não.  
O correto é levar a base de cálculo do PIS e da COFINS de todos os lançamentos com CST 04 e 06.

## **03. SOLUÇÃO**

Retirado os parâmetros :

**Gerar Valores para Notas Sem Direito a Crédito (PIS/COFINS)**

**Gerar Operações Sem Direito a Crédito (PIS/COFINS)**

Adicionado dois parâmetros de texto para que o usuário possa informar os CST's Sem Direito a Crédito e Sem Direito a Debito a ser considerado na Rotina.

**CST - Não Gerar Valores para Notas Sem Direito a Crédito (PIS/COFINS)**

**CST - Não Gerar Operações Sem Direito a Crédito (PIS/COFINS)**

Caso seja informado mais de um CST, é necessário separar os mesmo por  **;**  conforme exemplo abaixo e sem espaços entre os mesmos:

**06;49;08**

Este novo comportamento está disponível a partir da versão 12.1.27 e Layout mais recente da EFD (Patch  e Layout mais recentes após publicação desta documentação)
