---
article_id: 10845024720663
category: Faturamento - Cadastros
content_hash: 2d6edc31c2106b74883cc5e956e6fa73a70d14927f1956b45371ab56f5faeb45
fetched_at: '2026-06-28T22:38:35.336842+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Restrição de
  rotina do menu, para cadastro de Cliente (CRMA980)
type: support-article
updated_at: '2022-12-09T19:03:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10845024720663-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Restri%C3%A7%C3%A3o-de-rotina-do-menu-para-cadastro-de-Cliente-CRMA980
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a restrição de rotina do menu(SIGACFG), para o cadastro de Cliente (CRMA980);  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Somente na Release 12.1.033;  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Para o sistema validar a restrição para o cadastro de Cliente "CRMA980", é necessário realizar a inclusão desta rotina no Menu do Faturamento;

1. Realize a criação de um novo menu com a chamada do CRMA980 para o Faturamento;

[MP - FRAME - Personalização de Menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000575567-MP-FRAME-Personaliza%C3%A7%C3%A3o-de-Menus)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844424257943)

2. Após Configuração do Menu, acessar o cadastro do Usuário / Grupo e atribuir o novo Menu;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844578784791)

3. Ir em Outra ações e selecionar a opção **Restrição de Rotina do Menu**, localizar a rotina CRMA980 e fazer os bloqueios;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844778225687)

**Observe que foi desabilitada a opção do MATA030;**

Resultado da configuração da restrição para o CRMA980;

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10844873629463)**
