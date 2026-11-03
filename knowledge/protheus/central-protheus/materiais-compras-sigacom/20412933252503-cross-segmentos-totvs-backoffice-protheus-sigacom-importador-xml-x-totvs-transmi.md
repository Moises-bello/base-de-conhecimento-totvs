---
article_id: 20412933252503
category: Materiais - Compras (SIGACOM)
content_hash: ff38b41929f573b3fc1f308cc0a6a4b88d789eddaad77491fb538701baaf609e
fetched_at: '2026-06-28T22:41:19.951698+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML x TOTVS
  Transmite - Não grava o Número de Série no Documento de Entrada em NFSe
type: support-article
updated_at: '2024-03-28T12:15:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20412933252503-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-x-TOTVS-Transmite-N%C3%A3o-grava-o-N%C3%BAmero-de-S%C3%A9rie-no-Documento-de-Entrada-em-NFSe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20412945055255) Tempo aproximado para leitura: **00h03min****Ocorrência**Não grava o Número de Série no Documento de Entrada em NFSe - Importador XML x TOTVS Transmite  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Causa**Documentos de NFSe **não gravam o Número de Série**, pois, a prefeitura somente envia a numeração do documento.  
  
**Solução**

Quando há integração do Importador XML com o TOTVS Transmite, a "Série" que é apresentada no TOTVS Transmite refere-se ao RPS (Recibo Provisório de Serviços), ou seja, à série do prestador do serviço e não do tomador do serviço. Essa configuração é importante para garantir a correta identificação e registro das informações nos sistemas envolvidos.

Veja nesse ex:

![](https://tdn.totvs.com/download/attachments/819041933/image-2024-1-8_15-13-18.png?version=1&modificationDate=1704737624820&api=v2)

Veja que tem a informação apenas da **"Nota Prefeitura"** que contém apenas o Número do documento.

***Saiba Mais :***

[IX08021 - Importador XML x TOTVS Transmite - Informação da "Serie" em documentos do tipo NFSe (Serviço)](https://tdn.totvs.com/pages/releaseview.action?pageId=819041933)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
