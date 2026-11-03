---
article_id: 23126498803735
category: eSocial - Middleware
content_hash: 8b939e586f0f0553c5d3bbfbcfb5e558c128cd8505aad29130c09faa34f4b0b4
fetched_at: '2026-06-28T22:47:05.519439+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware - Erro código 609: Código inválido'
type: support-article
updated_at: '2025-07-03T18:00:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23126498803735-RH-RM-FOP-eSocial-Middleware-Erro-c%C3%B3digo-609-C%C3%B3digo-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23126498773655) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao integrar os eventos ao eSocial é apresentado a rejeição Erro código 609: Código inválido..  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - eSocial - Todas as versões  
  
**Causa**Esse incidente ocorre no momento de gerar o ID do evento, gerando um ID incorreto  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Configurações | Parametrizador | eSocial | Integração Middleware**, aba **Certificado Digital**;

2. Clique em **Atualizar Certificado TSS**;

3. Avance até o final para salvar o Wizard;

4. Reinicie os serviços do TAF/TSS;

5. Gere novamente o XML e integre ao eSocial.

**Importante**

Caso as orientações acima foram seguidas e o erro persiste, validar a natureza jurídica informada em **eSocial | Informações do Empregador**, campo Natureza Jurídica, verificar se foi informado **indevidamente** as naturezas 101-5, 104-0, 107-4, 116-3 ou 134-1, visto que essas naturezas mudam a geração do ID do evento e podem ocasionar no erro supracitado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33235338688663)
