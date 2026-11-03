---
article_id: 33258726403735
category: RH - Folha de Pagamento
content_hash: ccf07d7d3917442e255d752a3f234f544e2b952b1ad7dcaed2abe1cff1d17358
fetched_at: '2026-06-28T22:44:13.485533+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como fazer pra que na versão 2410 seja apresentada
  a pergunta "imprime relatório personalizável"
type: support-article
updated_at: '2025-07-10T14:32:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33258726403735-RH-Linha-Protheus-GPE-Como-fazer-pra-que-na-vers%C3%A3o-2410-seja-apresentada-a-pergunta-imprime-relat%C3%B3rio-personaliz%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33258726392599) Tempo aproximado para leitura: **00:02:00min**

**Dúvida**  
Como fazer pra que na versão 2410 seja apresentada a pergunta "imprime relatório personalizável"   
  
**Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 2410  
  
**Solução**  
**Ao acessar a rotina GPER040 - Folha de pagamento, apesar do parâmetro MV\_TREPORT estar configurado com 3 (pergunta se utiliza), o sistema não apresenta a pergunta;**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258726393111)**

Para solucionar essa dúvida, realize os seguintes passos:  
Na versão 12.1.2410 é necessário que o WebAgent esteja habilitado para que o sistema apresente essa pergunta.

Para Habilitar, acesse a engrenagem de configuração que é apresentada na tela Inicial TOTVS SMARTCLIENT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258726393367)

Após isso, vá até **Agente Local** e Habilite

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258726393751)

Acesse o sistema novamente e quando acessar a rotina de folha de pagamento, a pergunta será apresentada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33258726394007)

**Saiba Mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
