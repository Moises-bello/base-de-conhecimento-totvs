---
article_id: 40824212177815
category: SIGAACD - Automação e Coleta de Dados
content_hash: e5ddf4cd90c37795d7ef43942216493819f68123a552d8ab0b17dba266a8f6e7
fetched_at: '2026-06-28T22:39:12.772415+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Menu da consulta da
  etiqueta não aparece no aplicativo meu coletor de dados
type: support-article
updated_at: '2026-05-29T14:57:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40824212177815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Menu-da-consulta-da-etiqueta-n%C3%A3o-aparece-no-aplicativo-meu-coletor-de-dados
---

O menu de consulta da etiqueta no aplicativo Meu Coletor de Dados pode não aparecer se o fonte ACDM010 não estiver atualizado. Para corrigir, é necessário aplicar o pacote de atualização correspondente à versão do sistema (12.1.2310, 12.1.2410 ou 12.1.2510) em ambiente de homologação, após realizar backup do RPO.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40824212165271) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O menu da consulta da etiqueta, no aplicativo meu coletor de dados não aparece, como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para que o menu da consulta de etiqueta seja exibido, é necessária a atualização do fonte ACDM010. Segue o pacote para aplicação em sua base de homologação.

12.1.2310:<https://r.totvs.io/p/1250075>

12.1.2410:<https://r.totvs.io/p/1250076>

12.1.2510:<https://r.totvs.io/p/1250077>

Antes da aplicação do pacote de correção, realizar o backup do seu RPO, e aplicar em base de homologação.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
