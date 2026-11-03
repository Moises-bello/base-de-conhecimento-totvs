---
article_id: 4411205403927
category: Financeiro - Consultas / Relatórios
content_hash: 4cd7f2b77bf3a1ece14f957a2a21a9445f7ee4d0bd9893c175a9b02490c3cb17
fetched_at: '2026-06-28T22:37:58.406859+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINR130 - Como configurar
  o relatório para que apresente o desconto quando altera o vencimento do título.
type: support-article
updated_at: '2021-10-21T20:38:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411205403927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINR130-Como-configurar-o-relat%C3%B3rio-para-que-apresente-o-desconto-quando-altera-o-vencimento-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Ao alterar o vencimento do título o relatório considera o vencimento original ao invés do novo vencimento.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINR130 - Todas as versões.  
  
**Solução**Para solucionar realize os seguintes passos:No Configurador **(SIGACFG)**, acesse **Ambiente-> Cadastro-> Parâmetro** abra a pasta e selecione o **Parâmetros**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411204439319/mceclip1.png)  
  
Selecione o ícone da lupa  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411204499095/mceclip2.png)  
  
E procure pelo parâmetro **MV\_DTDESCF.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411204587543/mceclip3.png)**Selecione o ícone de **alterar**.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411204603159/mceclip4.png)  
  
Altera o campo para **"****E1\_VENCTO"**ou **"E1\_VENCREA".**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411208454423/mceclip5.png)  
   
**Importante:**Não esqueça de adicionar aspas duplas
