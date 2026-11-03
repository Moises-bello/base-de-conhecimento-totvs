---
article_id: 20324530948119
category: Materiais - Compras (SIGACOM)
content_hash: f0e7c7d22345ce74d3491caa518b9b20906069b7fde82f2023a8d998be56fc47
fetched_at: '2026-06-28T22:41:13.014389+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Importador XML - Existe
  algum parâmetro como Data Corte associado à Data de Início da integração entre o
  Importador XML e o TOTVS Transmite?
type: support-article
updated_at: '2024-04-03T12:30:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20324530948119-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Existe-algum-par%C3%A2metro-como-Data-Corte-associado-%C3%A0-Data-de-In%C3%ADcio-da-integra%C3%A7%C3%A3o-entre-o-Importador-XML-e-o-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20324574253079) Tempo aproximado para leitura: **00h01min** **Dúvida**Existe algum parâmetro como Data Corte associado à data de início da integração entre o Importador XML e o TOTVS Transmite?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12

**Solução**

O Parâmetro tem a finalidade de informar a Data de Início da Integração entre o Importador XML e o TOTVS Transmite. O processo associado a esse Parâmetro é o seguinte:

* Ao informar documentos na CKOCOL, se a data do documento for anterior à data definida no parâmetro, esses documentos serão ajustados (CKO\_STRAN = '0'). Isso significa que eles não serão submetidos a tentativas de atualização de status no TOTVS Transmite.

* Por outro lado, os documentos cuja data seja igual ou posterior à data definida no parâmetro serão analisados para garantir que sejam corretamente atualizados no TOTVS Transmite.

* Este processo visa garantir que apenas documentos recentes sejam considerados para atualização no sistema externo, otimizando assim o fluxo de integração e evitando a tentativa de atualização de documentos mais antigos.

**Obs:** Se não informar será solicitado TODOS documentos no TOTVS Transmite, caso tenha informado, somente a partir da data será selecionado documentos no TOTVS Transmite.

***Saiba Mais :***

[IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195#Funcionalidades-Par%C3%A2metros)

[IX08013 - Importador XML x Totvs Transmite - Performance](https://tdn.totvs.com/display/public/PROT/IX08013+-+Importador+XML+x+Totvs+Transmite+-+Performance)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
