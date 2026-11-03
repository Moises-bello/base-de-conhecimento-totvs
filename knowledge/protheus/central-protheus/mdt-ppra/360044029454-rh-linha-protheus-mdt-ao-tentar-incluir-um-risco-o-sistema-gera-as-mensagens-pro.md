---
article_id: 360044029454
category: MDT - PPRA
content_hash: fab909f6189626fe0e0ea1350a81b2b34b3f6160d5783dcfcb5b8525942d502f
fetched_at: '2026-06-28T22:44:27.244567+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: 'RH - Linha Protheus - MDT - Ao tentar incluir um risco o sistema gera as mensagens. Problema:
  Erro no conteúdo do Inicializador Padrão. Campo: Nome Fase ou TN0_DESFAS. Solução:
  Corrija Inicializador Padrão'
type: support-article
updated_at: '2025-07-31T14:28:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044029454-RH-Linha-Protheus-MDT-Ao-tentar-incluir-um-risco-o-sistema-gera-as-mensagens-Problema-Erro-no-conte%C3%BAdo-do-Inicializador-Padr%C3%A3o-Campo-Nome-Fase-ou-TN0-DESFAS-Solu%C3%A7%C3%A3o-Corrija-Inicializador-Padr%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20003028960407)** Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar incluir um risco o sistema gera as mensagens. **Problema**: Erro no conteúdo do Inicializador Padrão. **Campo**: Nome Fase ou TN0\_DESFAS. **Solução**: Corrija Inicializador Padrão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060480793)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Esse erro pode ocorrer devido a um problema no inicializador padrão, ou por a ordem dos campos estarem incorretas.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Efetue o **backup** completo do sistema antes das alterações a seguir;  
  
**2.** Acesse o modulo configurador (SIGACFG) e acesse a configuração dos campos da tabela **TN0** (Risco);

Caminho SIGACFG: base de dados > base de dados  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060482533)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059589374)  
  
**3.** Acesse o campo **TN0\_DESFAS** (Nome Fase) e verifique o inicializador padrão do campo:  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059590414)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059590054)  
  
**4.** Caso o inicializador esteja correto verifique a ordem dos campos conforme demonstrado na imagem abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060482093)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059588954)  
  
**5.** Após realizador todos os procedimentos clique em salvar.  
  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060483713)  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059590534)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
