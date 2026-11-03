---
article_id: 360047560593
category: RH - MANAD
content_hash: fdad60a6efaf7cb94b4f8a10ced5a2e24027e22352a853189e11a348c755eafa
fetched_at: '2026-06-28T22:43:33.825132+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: RH - Linha Protheus - GPE - Geração do arquivo, MANAD não grava o arquivo .txt
  na pasta especificada
type: support-article
updated_at: '2021-04-06T20:21:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047560593-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-do-arquivo-MANAD-n%C3%A3o-grava-o-arquivo-txt-na-pasta-especificada
---

**Ocorrência**MP - GPE - Geração do arquivo, MANAD não grava o arquivo .txt na pasta especificada.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois nos parâmetros de perguntas da rotina, no campo Diretório não foi incluída uma "/".   
  
**Solução**

Na gravação do arquivo é  necessário incluir uma **\** ao final do diretório selecionado para gravar o arquivo. Isso ocorre pois a geração do  arquivo MANAD criará uma nova pasta no diretório selecionado.  
  
Segue exemplo, utilizando o diretório C:\RELATORIO\  :  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067871694/mceclip0.png)  
  
**Saiba Mais**[Artigos sobre Manad](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360008157193-RH-MANAD)
