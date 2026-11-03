---
article_id: 360019546991
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: d25c52549bb5d1b84c60b336c6308c71e782cccb003967c949b6052ea08fe353
fetched_at: '2026-06-28T22:47:29.584482+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: 'RH - RM - Meu RH - Erro HTTP Error 403.1 - Forbidden: Execute access is denied.'
type: support-article
updated_at: '2025-02-10T18:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019546991-RH-RM-Meu-RH-Erro-HTTP-Error-403-1-Forbidden-Execute-access-is-denied
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:15 min  
  
Ocorrência**Ao acessar o Meu RH via desktop ocorre o seguinte erro: *HTTP Error 403.1 - Forbidden: Execute access is denied.***Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.17  
  
**Causa**O incidente ocorre, pois alguns recursos que são utilizados pelo Meu RH estão desabilitados no Gerenciador do Serviços de Informações da Internet (IIS).  
  
**Solução**Para solucionar essa ocorrência, realize os passos abaixo:  
  
**01.** No *Windows*, acesse o Iniciar e o procure pelo Gerenciador do Serviço de Informações da Internet IIS. É possível informar o nome e pesquisar no menu iniciar;  
 **02.** Ao acessar o Gerenciador IIS, selecione o site FrameHTML;  
 **03.** Na exibição Recursos, clique duas vezes em Mapeamentos de Manipulador;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015260731/mceclip0.png)  
  
**04.** Após acesso, clique em Editar Permissões de Recurso, à direita no painel Ações;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015260831/mceclip1.png)  
  
**05.** Será aberta uma janela com algumas opções. Marque a opção *Script*. Assim será habilitado todos os recursos necessários para o acesso via *desktop.*  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015213812/mceclip2.png)
