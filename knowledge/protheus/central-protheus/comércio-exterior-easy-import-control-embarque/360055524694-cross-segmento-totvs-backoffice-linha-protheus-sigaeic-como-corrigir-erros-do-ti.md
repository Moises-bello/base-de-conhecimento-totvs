---
article_id: 360055524694
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 828c7b4e1471a927f83187050f16908b8fc643376b6bd5e997fabc051db9aa74
fetched_at: '2026-06-28T22:39:48.679929+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -  Como Corrigir
  erros do Tipo RUP na migração de Release
type: support-article
updated_at: '2021-08-11T13:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055524694-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-Corrigir-erros-do-Tipo-RUP-na-migra%C3%A7%C3%A3o-de-Release
---

**Dúvida**Como Corrigir erros do Tipo RUP na migração de Release - InterFunctionCall: cannot find function ENGHLP127?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Erros do tipo *RUP* ocorre quando utiliza-se repositório (RPO) da versão Protheus superior a 12.1.23, porém o *cRelFinish*, que é o release para qual está migrando, está desatualizado.

Esse erro ocorre ao executar o *UPDDISTR* com ambiente Protheus versão superior a 12.1.23 porém o SDF encontra-se antigo, provavelmente por falta de atualização do arquivo.

Neste caso, deve baixar o dicionário SDF para versão atualizada do Protheus (exemplo: 12.1.27) e extrair na pasta *Systemload* , após execute o *UPDDISTR* novamente.

Segue boletim explicando como funciona esta função *RUP*: <https://tdn.totvs.com/pages/releaseview.action?pageId=286729822>
