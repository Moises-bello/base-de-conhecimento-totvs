---
article_id: 14112737215639
category: Financeiro - Conciliação de Vendas
content_hash: d4cdc4b8eee040c5aaa27365e5ab25bdfad376730fed8ea6a21d7a8970d24248
fetched_at: '2026-06-28T22:37:26.279350+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA918 Conciliação
  Pagamentos - Como funciona o pergunte "Tolerância em %"
type: support-article
updated_at: '2026-02-04T13:23:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14112737215639-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA918-Concilia%C3%A7%C3%A3o-Pagamentos-Como-funciona-o-pergunte-Toler%C3%A2ncia-em
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38158352216599) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
Como funciona o pergunte "Tolerância em %"?

Exemplo:

Ao ter um título a receber no valor de R$ 1.000,00.

[![1_SE1_titulos.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14112307630871)](https://centraldeatendimento.totvs.com/hc/article_attachments/14112307630871)

E ao efetuar a importação do arquivo da administradora, é possível verificar na rotina FINA918 - conciliação de pagamentos, que o registro está com o valor de R$ 900,00.

Em nosso exemplo fictício, a administradora cobrou uma taxa de 10%.

[![2_FIF_titulos.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317242135)](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317242135)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**

Nas perguntas parâmetros, ao utilizar o conteúdo, pergunte "**Tolerância em %**" = 9%.

[![4_parametros_9porc.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317165335)](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317165335)

Veja que o registro será apresentado na aba "**Conciliados Parcialmente**", pois o conteúdo colocado no parâmetro não alcançou o valor mínimo de **taxa descontada** pela administradora.

[![6_conc_parcialmente.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317101335)](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317101335)

Nas perguntas parâmetros, ao utilizar o conteúdo, pergunte "**Tolerância em %**" = 10%.

[![3_parametros_10porc.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317233047)](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317233047)

Veja que o registro será apresentado na aba "**Conciliados**", pois o conteúdo colocado no parâmetro alcançou o valor mínimo de taxa descontada pela administradora.

[![7_conc.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317099927)](https://centraldeatendimento.totvs.com/hc/article_attachments/14112317099927)

**Importante:**   
O pergunte não terá efeito quando o cenário for contrário.

**Exemplo:** Um título de R$ 900,00 (tabela **SE1**), onde a administradora pagou a maior R$ 1.000,00 (tabela **FIF**), neste caso, independente do conteúdo da pergunta "**Tolerância em %**", o registro sempre irá ser apresentado na aba "**Conciliados**".

**Sabia mais**

[Finalidade do parâmetro MV\_LJGERTX](https://tdn.totvs.com.br/pages/releaseview.action?pageId=203764928)

[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877#Abas-1)
