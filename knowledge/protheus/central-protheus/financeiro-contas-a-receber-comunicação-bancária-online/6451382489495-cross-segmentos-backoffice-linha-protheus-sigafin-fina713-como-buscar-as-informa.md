---
article_id: 6451382489495
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: ec281763a7f8a37e658a842d1caad584df76f5ab98622bf04852e7e22e0c1efc
fetched_at: '2026-06-28T22:37:49.211859+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como buscar
  as informações do Json após executar o schedule
type: support-article
updated_at: '2026-01-07T18:27:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451382489495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-buscar-as-informa%C3%A7%C3%B5es-do-Json-ap%C3%B3s-executar-o-schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32389452347031) Tempo aproximado para leitura: **00:02 min**  
  
**Dúvida**  
Como buscar as informações do Json após executar o schedule?  
  
**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - FINA710 - A partir da versão 12.1.33.  
  
**Solução**  
Após executar o schedule **FINA713**, na tabela **SEA,** conseguirá as informações do **Json** no campo **EA\_APIMSG.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6451156256919)

Para converter as informações, pode utilizar o **Notepad++,** adicionando a extensão **JSTool.**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6451126288663)**

O JSON contém as informações da requisição da API na tag 'response', em que é possível avaliar o retorno recebido do banco.
