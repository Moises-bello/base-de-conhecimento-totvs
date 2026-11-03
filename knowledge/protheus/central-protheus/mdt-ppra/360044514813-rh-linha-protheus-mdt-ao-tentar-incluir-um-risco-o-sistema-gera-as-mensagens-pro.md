---
article_id: 360044514813
category: MDT - PPRA
content_hash: 7749895870d21c7b6c3683135a2404f15817a808c0c47725c656ec2151f69ac0
fetched_at: '2026-06-28T22:44:27.249345+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: 'RH - Linha Protheus - MDT - Ao tentar incluir um risco o sistema gera as mensagens. Problema:
  Erro no conteúdo do Inicializador Padrão. Campo: Nome Sub-fase ou TN0_DESSUB. Solução:
  Corrija Inicializador Padrão'
type: support-article
updated_at: '2025-08-14T18:51:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044514813-RH-Linha-Protheus-MDT-Ao-tentar-incluir-um-risco-o-sistema-gera-as-mensagens-Problema-Erro-no-conte%C3%BAdo-do-Inicializador-Padr%C3%A3o-Campo-Nome-Sub-fase-ou-TN0-DESSUB-Solu%C3%A7%C3%A3o-Corrija-Inicializador-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19643791538583)** Tempo aproximado para leitura **00:02:00 min  
  
Ocorrência**Ao tentar incluir um risco o sistema gera as mensagens. **Problema**: Erro no conteúdo do Inicializador Padrão. **Campo**: Nome Sub-fase ou TN0\_DESSUB. **Solução**: Corrija Inicializador Padrão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059591274)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Esse erro pode ocorrer devido a um problema no inicializador padrão, ou por a ordem dos campos estarem incorretas.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Efetue o **backup** completo do sistema antes das alterações a seguir;  
  
**2.** Acesse o modulo configurador (SIGACFG) e acesse a configuração dos campos da tabela **TN0** (Risco);

Caminho SIGACFG: base de dados > base de dados  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207282033431)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207282041367)  
  
**3.** Acesse o campo **TN0\_DESSUB**(Sub-Fase) e verifique o inicializador padrão do campo;  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207320534039)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060487013)  
  
**4.** Caso o inicializador esteja correto verifique a ordem dos campos conforme demonstrado na imagem abaixo;  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207282050071)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207320541591)  
  
**5.** Após realizador todos os procedimentos clique em salvar.  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207282059287)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17207320551191)  
  
**Saiba Mais**[Artigos PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
