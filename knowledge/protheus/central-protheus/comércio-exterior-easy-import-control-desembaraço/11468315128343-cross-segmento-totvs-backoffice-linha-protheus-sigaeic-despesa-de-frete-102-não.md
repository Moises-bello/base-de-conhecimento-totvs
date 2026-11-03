---
article_id: 11468315128343
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 4dc2bfe0b6b6847d978d24bf125a8278e9ef13459b90980a7116b63ffe117846
fetched_at: '2026-06-28T22:39:51.328995+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Despesa de Frete
  (102) não atualiza na Integração com o Despachante
type: support-article
updated_at: '2023-01-05T20:43:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11468315128343-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Despesa-de-Frete-102-n%C3%A3o-atualiza-na-Integra%C3%A7%C3%A3o-com-o-Despachante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **03:00 min** **Dúvida**Ao efetuarmos a integração conforme o layout do arquivo de **dados de recebimento de Despesas de Importação**, o sistema não está respeitando o que está informado na **linha** **"DE"** do arquivo txt, posição 50 e 51, referente a despesa **102-Frete,** "**A****diantado-SIM**" e "**pago por** "**Despachante**"".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão P12.1.27  
  
**Solução**As despesas de **Frete** e **Seguro** são despesas Internacionais do processo e seus valores são definidos na integração pela **"Capa das Despesas",** identificadas por **linha "DI"**, onde é possível informar a **Moeda do Frete** (Posição 084-086)**,** o **valor do frete** (Posição 087-101) e a **taxa do frete** (posição 102-116).

Estas despesas não tem sua integração efetivada quando informadas na linha do itens, identificadas por "**DE"**.

Desta forma, a integração deverá ser realizada utilizando o layout do arquivo de **integração dados da Solicitação de Numerário** ou pela Capa de Integração na linha "**DI**" do layout de **integração de** **dados de recebimento de Despesas de Importação**.  
  
**Observação**Os dados de Seguro também devem seguir a mesma linha, apenas observando as posições corretas no layout.  
  
**Saiba mais**  
[Layout de Integração de dados da Solicitação de Numerário](https://tdn.totvs.com/pages/releaseview.action?pageId=394220463)  
[Layout de integração de dados de recebimento de Despesas de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=394220339)  
[Integração com Despachante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028440511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-com-Despachante)  
[Como efetuar a integração com o Despachante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040571214-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-efetuar-a-integra%C3%A7%C3%A3o-do-arquivo-despachante)
