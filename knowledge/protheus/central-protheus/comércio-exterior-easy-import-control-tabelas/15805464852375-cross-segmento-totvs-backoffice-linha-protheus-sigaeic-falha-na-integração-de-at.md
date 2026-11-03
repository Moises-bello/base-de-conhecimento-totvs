---
article_id: 15805464852375
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 5df8c6bb40ee35c4d9a93b77245278a7eac773b6a624537ca99a9d02e927b8a8
fetched_at: '2026-06-28T22:39:47.750081+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Falha Na Integração
  De Atributos. Falha De Download No Portal Único
type: support-article
updated_at: '2023-07-06T10:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15805464852375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Falha-Na-Integra%C3%A7%C3%A3o-De-Atributos-Falha-De-Download-No-Portal-%C3%9Anico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15805445745815) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Ao integrar a rotina de atributos **(EICAT400)** do módulo do SIGAEIC esta ocorrendo um erro de integração **"Falha na integração de atributos.Falha no download do arqivo no portal único: Can´t find end central directory: is this a zip file ? If it isee** [**https://stuk.github.io/jszip/documentation/howto/read\_zip.html" .**](https://stuk.github.io/jszip/documentation/howto/read_zip.html")

O que preciso fazer para que a integração seja feita sem que ocorra o erro?

![MENSAGEM](https://centraldeatendimento.totvs.com/hc/article_attachments/15805473190295)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**

Este erro ocorre pois o endereço informado do portal único esta errado.  Verifique como estão os conteúdos dos parâmetro **MV\_EIC0072** e **MV\_EIC0073.** O endereço da ***URL*** tem que esta informada conforme tabela abaixo:

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo** |
| MV\_EIC0072 | URL do Endpoint de Integração do Portal Único em Produção (URL principal das APIs de integração para a produção | https://portalunico.siscomex.gov.br |
| MV\_EIC0073 | URL do Endpoint de Integração do Portal Único em Treinamento (URL principal das APIs de integração para treinamento | https://val.portalunico.siscomex.gov.br |
| MV\_EIC0074 | Ambiente de Integração com o Portal Único | 1=Produção, 2=Treinamento |

E o parâmetro **MV\_EIC0074** é o responsável em habilitar se em que ambiente será integrado se é no ambiente de produção ou treinamento. Se atentar em qual ambiente que esta ocorrendo para que seja ajustado o endereço.
