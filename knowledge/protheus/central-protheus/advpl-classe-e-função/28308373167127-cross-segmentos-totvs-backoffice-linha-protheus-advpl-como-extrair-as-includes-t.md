---
article_id: 28308373167127
category: ADVPL - Classe e Função
content_hash: 30c5169a24fdfc73219316b905dda95ce3318fd459a2a222d67431a8c8741d11
fetched_at: '2026-06-28T22:40:21.586013+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Como extrair as
  includes TLPP?
type: support-article
updated_at: '2024-12-05T19:07:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28308373167127-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-extrair-as-includes-TLPP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28308373139863)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como extrair as includes TLPP?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – até a versão 12.1.2410  
  
**Solução**Para desenvolver programas em TLPP é necessário possuir as Includes TLPP, as includes ficam dentro do tlpp.rpo.

Como os includes fazem parte do RPO (tlpp.rpo), basta executar a função tlpp.environment.getIncludesTLPP para extraí-los.

**Execução**

Abrir o SmartClient e digitar na tela:

Programa inicial: tlpp.environment.getIncludesTLPP

Comunicação no cliente: [seu serviço]

Ambiente no servidor: [seu ambiente]

![teste_gif.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28308373142807)

Após executar esta função os includes serão extraídos dentro do diretório do "RootPath" do seu ambiente, em um diretório chamado "includes".

**Saiba mais:**

[Ambiente de compilação do TLPP](https://tdn.totvs.com/pages/viewpage.action?pageId=555860439)

[TLPP](https://tdn.totvs.com/display/tec/TLPP)
