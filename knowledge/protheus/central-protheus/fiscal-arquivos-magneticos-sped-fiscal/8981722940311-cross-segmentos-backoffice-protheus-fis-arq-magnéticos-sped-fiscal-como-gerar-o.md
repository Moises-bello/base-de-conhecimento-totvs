---
article_id: 8981722940311
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 43932c5691a8b1d2738fa964378934a367dda287d2deb68a6e11b7fd8aaed8e4
fetched_at: '2026-06-28T22:42:01.233759+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Como gerar o registro E115 de forma manual pelo MATA017?
type: support-article
updated_at: '2022-09-19T17:39:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8981722940311-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-registro-E115-de-forma-manual-pelo-MATA017
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida** Como gerar o **registro E115** de forma manual pelo **MATA017**?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**

**Solução**

1. Acesse a rotina **FISA156**, inclua um novo conteúdo informando o **código de ajuste** conforme sua operação para alimentar a tabela **CDY**.

2. Ao efetuar a inclusão, acesse a rotina **MATA017** e realize uma inclusão para alimentar a tabela **CDV**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8981292222615/mceclip0.png)

3. Acesse a rotina **FISA072** e faça a configuração do **código de reflexo** que irá utilizar na sua **TES**.

4. Após esses processos, acesse a **TES** que irá utilizar no processo de escrituração e inclua conteúdo nos campos **CC7\_CLANAP, CC7\_IFCOMP, CC7\_CODREF e CC7\_CLANC**.

5. Ao acessar a rotina **MATA953** identifique se o código de ajuste que utilizou foi gerado na **apuração** de forma automática, alimentando a tabela **CDH e processe a Apuração.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8981401927959/mceclip2.png)

6. Verifique se as tabelas **CDH** e **CDV** foram geradas corretamente.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8981396138903/mceclip1.png)

Atenção: Período apurado na *wizard* seguindo o padrão do conteúdo do campo **CDH\_DTINI e CDH\_DTFIM**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8981549679255/mceclip3.png)

7. Gere o arquivo txt do **Sped Fiscal** e verifique o registro **E115** gerado:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8981504606871/mceclip4.png)
