---
article_id: 10082516030231
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: bb500acdf0260fcc2518bd9694261d99904fc30fbec23e4fa1bf0d04d2f35bda
fetched_at: '2026-06-28T22:39:48.874916+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Como corrigir
  o erro: EYZ010: SetOrder - Index not found. on H_EICPO151(EICPO151.APH) ?'
type: support-article
updated_at: '2023-01-02T17:43:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10082516030231-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-corrigir-o-erro-EYZ010-SetOrder-Index-not-found-on-H-EICPO151-EICPO151-APH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como corrigir o erro: **EYZ010: SetOrder - Index not found. on H\_EICPO151(EICPO151.APH)**?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) -*Easy Import Control*- Todas as versões  
  
**Solução**Deve ser verificado se constam os índices referente o dicionário EYZ, conforme padrão abaixo, se não, deve ser incluído via configurador.

![](https://totvssuporte.zendesk.com/attachments/token/WrbnMTceb52IgrtwleysZDlcw/?name=image.png)  
  
1. Acesse o módulo SIGACFG em Base de Dados, selecione Dicionário / Base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025329791/mceclip0.png)  
  
2. Selecione Dicionário de Dados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025309112/mceclip2.png)  
  
3. Selecione a lupa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025330191/mceclip3.png)  
  
4. Selecione Procurar Por e informe a tabela EYZ, após selecione Buscar.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10082327894807)  
  
5 - Selecione editar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10082329611927)

6 - Selecione a opção índices.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10082330866455)  
  
7 - Vá na opção incluir e inclua o índice.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10082332685719)  
  
8 - Inclua o índice que não consta no ambiente e selecione o Salvar.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10082307102615)
