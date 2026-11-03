---
article_id: 4417311484823
category: Faturamento - Integrações
content_hash: b867c99096827f88eec2a69455fab263da88bf4a395e2cc7ac222b75bbb161f2
fetched_at: '2026-06-28T22:38:26.454092+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Valor do parâmetro
  MV_CROSFAT: 0 Incorreto'
type: support-article
updated_at: '2021-12-28T14:08:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417311484823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Valor-do-par%C3%A2metro-MV-CROSFAT-0-Incorreto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**  
Ao tentar importar o XML com o uso do Importador XML, ocorre a mensagem no arquivo Order:

**Valor do parâmetro MV\_CROSFAT: 0 Incorreto, favor informar 1, 2 ou 3!**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417325317783/mceclip0.png)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - a partir da release 12.1.25.  
  
**Solução**

A mensagem ocorre por que o parâmetro **MV\_CROSFAT** está em branco ou recebendo o valor 0.

O parâmetro define se utiliza a **Prog. Entrega ou o Ped. Venda** no **CrossDocking**. 1-Não utiliza, 2-Prog.de Entrega, 3-Pedido Vendas .

Deixe como valor default, **1** e  a mensagem deixa de ocorrer.  
  
**Saiba Mais sobre Importador XML no Faturamento: [Importador XML - Guia de Referência - Faturamento - P12](https://tdn.totvs.com/x/5zzuIw)**
