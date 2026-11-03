---
article_id: 360028375752
category: Gestão de Transportes (TMS)
content_hash: 7657afadb6e1292315deeec0be971e54eb38e15e7d442ad93dd752e6d714099d
fetched_at: '2026-06-28T22:45:27.243782+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Alteração da descrição do documento de transporte
type: support-article
updated_at: '2022-05-31T19:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028375752-Log%C3%ADstica-Linha-Protheus-TMS-Altera%C3%A7%C3%A3o-da-descri%C3%A7%C3%A3o-do-documento-de-transporte
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)  Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como proceder para alterar a descrição do documento de transporte?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**É permitido a alteração da descrição dos documentos de transporte do tipo apoio - **B, C, H, I, N e O**.  
  
Para alteração dos tipos permitidos, é necessário configurar o parâmetro **MV\_TMSDOC** **- Define a descrição dos documentos de transporte** via **Configurador - SIGACFG/Base de dados/Dicionário/Base de dados/Parâmetros**.  
  
Neste parâmetro, deve ser informado o código do documento de transporte e a descrição desejada, conforme exemplo abaixo:  
  
**B=ACT;C=teste**  
  
Após, ao acessar a rotina **Configuração de Documentos - Atualizações/Documentos e Regras**, no campo **Docto.Transp. - DUI\_DOCTMS** já estará listando o documento em questão com a nova descrição.

![Capturar1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360029091031/Capturar1.PNG)
