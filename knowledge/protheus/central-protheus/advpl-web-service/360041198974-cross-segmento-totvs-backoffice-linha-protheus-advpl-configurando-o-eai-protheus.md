---
article_id: 360041198974
category: ADVPL - Web Service
content_hash: 31bc62e72df0e400132cbb125d5fb99063e5574c3afe6bd3ca31e465f67c8ae2
fetched_at: '2026-06-28T22:40:10.383770+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Configurando o EAI
  Protheus para receber e enviar Mensagens REST
type: support-article
updated_at: '2021-12-29T13:02:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041198974-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configurando-o-EAI-Protheus-para-receber-e-enviar-Mensagens-REST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como configurar mensagem padronizada via **REST**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12  
  
**Solução**Para a utilização da porta **REST** nas mensagem padronizadas deve-se seguir estes passos:

1 - Cadastro de Rotas:

A rotina pode ser acessada pelo menu do **SIGACFG**:

![eai1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055675933/eai1.png)

Preencher os campos de produto e aplicação, selecionar o canal de envio como REST, e completar o cadastro com os dados de acesso ao canal:

![eai2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054797134/eai2.png)

2-Configuração do **Adapter**

A rotina pode ser acessada pelo menu do **SIGACFG**:

![eai3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055675893/eai3.png)

Preenchendo os seguintes campos, o Canal de envio nesse cadastro deve ser configurado como PAD. APP (para seguir o que foi cadastrado no registro anterior):

![eai4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055675913/eai4.png)

**Saiba Mais:**[**EAI REST**](https://tdn.totvs.com/display/framework/Mensagem+Padronizada+Via+Rest)
