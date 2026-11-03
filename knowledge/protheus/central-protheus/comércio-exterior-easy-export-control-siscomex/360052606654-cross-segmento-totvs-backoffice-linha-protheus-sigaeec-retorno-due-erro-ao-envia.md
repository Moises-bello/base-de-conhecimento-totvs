---
article_id: 360052606654
category: Comércio Exterior - Easy Export Control - Siscomex
content_hash: ea12e9ea8d2d234a03596484c76bc181387f10bf4130d3fd049bcc1ad5ea7c84
fetched_at: '2026-06-28T22:37:00.551787+00:00'
product: protheus
section_id: 1500001538121
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Retorno DUE:
  Erro ao enviar NF-E para o Gateway'
type: support-article
updated_at: '2022-06-14T18:43:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052606654-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Retorno-DUE-Erro-ao-enviar-NF-E-para-o-Gateway
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Envio a DUE retorna a mensagem: **ERROR 217/[DUEX-LNHXJA2865] Ocorreu um erro ao enviar NFE para o Gateway. Rejeição: NF-e não consta na base de dados da SEFAZ [GATE]**, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control*  – A partir da versão 12.1.17  
  
**Solução**Para envio do registro da DUE, mesmo em ambiente teste deve ser informado uma chave da nota do ambiente de Produção da SEFAZ, a mesma deve constar com o status autorizado.   
Sendo a chave da Nota fiscal de produção, há um *delay* entre o Portal da Nota Fiscal e o Portal Único Siscomex. Para alguns exportadores a simples consulta no site da Sefaz sincroniza as informações.
