---
article_id: 7971693787287
category: Financeiro - Contas a Receber
content_hash: 325261bd33564d000e986b43e12dff1a273c32ca8ef8e80ec7c943682afe79ff
fetched_at: '2026-06-28T22:38:13.983178+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA151 - HELP REGNOIS
  ao cadastrar instrução de cobrança '
type: support-article
updated_at: '2022-08-08T14:55:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7971693787287-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA151-HELP-REGNOIS-ao-cadastrar-instru%C3%A7%C3%A3o-de-cobran%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar o cadastro de instrução de Cobrança na alteração do titulo enviado ao banco, ocorre o **HELP REGNOIS Não existe registro relacionado a chave informada no alias SEB, ordenação 1.**

![fina151.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7971213309207/fina151.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o titulo não está em Borderô para a cobrança.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Incluir o titulo no Borderô via **FINA590 Manutenção de Borderô** ou cadastrar um novo na rotina **FINA060 - Transferência**  
2. Com o titulo em Bordero, efetuar a alteração e cadastrar novamente a instrução de Cobrança

**Saiba mais**   
<https://tdn.totvs.com/pages/releaseview.action?pageId=312165259>  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019906471>
