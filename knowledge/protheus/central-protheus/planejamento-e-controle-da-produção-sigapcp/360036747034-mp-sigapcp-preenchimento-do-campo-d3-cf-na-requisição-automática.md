---
article_id: 360036747034
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7168ffac8e752eb5276d49e6b590b14ebf750b962cbde81126c32d860a326269
fetched_at: '2026-06-28T22:42:48.082680+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Preenchimento do campo D3_CF na requisição automática
type: support-article
updated_at: '2019-12-27T11:40:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036747034-MP-SIGAPCP-Preenchimento-do-campo-D3-CF-na-requisi%C3%A7%C3%A3o-autom%C3%A1tica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quais são os possíveis conteúdos para o campo **D3\_CF - Tipo RE/DE** na requisição automática, quando ocorre o apontamento de produção?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**O campo **D3\_CF** pode ter os conteúdos **RE1**, quando o produto não for de apropriação indireta, **RE2**, para produtos de apropriação indireta ou **RE9** para produto que não é de apropriação indireta porém está configurado para não custear a **OP - Ordem de produção**, de acordo com o conteúdo do campo **B1\_AGREGCU - Custeio OP**, ou o tipo de movimento do apontamento está configurado para não custear a **OP**, de acordo com o campo **F5\_AGREGCU - Custeio OP**.
