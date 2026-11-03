---
article_id: 4402311146263
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 3957b861c8f7a06eb4176501c57ab1c99e82563ae37c9549506b9317b32ba12a
fetched_at: '2026-06-28T22:47:29.533882+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH -  Como verificar Versão e Patch da Biblioteca RM e Meu RH
type: support-article
updated_at: '2025-02-11T12:57:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402311146263-RH-RM-Meu-RH-Como-verificar-Vers%C3%A3o-e-Patch-da-Biblioteca-RM-e-Meu-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24078407712023) Tempo aproximado para leitura: 00:01:53 min****Dúvida**Como verificar a versão e patch da Biblioteca RM e MEU RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**Existem duas formas de verificar a versão do RM e Portal.  
  
**1º-** Verificando pelo Painel de Controle do Windows :  
  
Acesse o Painel de controle do Windows | Programas e Recursos  e identifique os instaladores BibliotecaRM e TOTVS RM Portal .

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402317962007)

**2º-** Verificando pelo caminho do instalador:  
  
Acesse o diretório que foi instalado o RM e Portal, para verificar o patch da BibliotecaRM acesse a pasta TOTVS\CorporeRM\RM.Net e localize a DLL | RM.VERSION.DLL | acesse propriedades | detalhes.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402318026647)

Para verificar o patch do MEU RH acesse a pasta TOTVS\CorporeRM\FrameHTML\Bin e localize a DLL | RM.VERSION.DLL | acesse  propriedades | detalhes . 

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402310953751)

**Importante**

- Para o correto funcionamento do **Meu RH, deve está na mesma versão/patch da Biblioteca RM**.

- Quando trabalhar em N camadas, verifique se todos servidores inclusive o servidor do Meu RH, a versão/patch da Biblioteca RM está igual ao Meu RH.
