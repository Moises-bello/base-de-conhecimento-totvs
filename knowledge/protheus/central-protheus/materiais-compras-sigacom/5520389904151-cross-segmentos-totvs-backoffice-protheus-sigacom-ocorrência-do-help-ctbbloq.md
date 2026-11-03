---
article_id: 5520389904151
category: Materiais - Compras (SIGACOM)
content_hash: 708a1d98685943e508834f9f1c9eb41ba9ac37084305c54e20360cbaf12955bd
fetched_at: '2026-06-28T22:41:22.019651+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ocorrência do help
  CTBBLOQ
type: support-article
updated_at: '2024-01-04T14:46:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5520389904151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ocorr%C3%AAncia-do-help-CTBBLOQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20315894068247) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quais ocorrências do help CTBBLOQ ?  
Qual a Data que o sistema verifica quando o Calendário Contábil está bloqueado e apresenta o Help CTBBLOQ no Estorno da Classificação da Pré - Nota?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Protheus Compras - Todas as versões  
  
**Solução**

**1ª ocorrência: Estorno da Classificação da Pré - Nota**

Qual a Data que o sistema verifica quando o Calendário Contábil está bloqueado e apresenta o Help CTBBLOQ no Estorno da Classificação da Pré - Nota?

 O sistema considera a Data do campo de Digitação da Nota F1\_DTDIGIT (ele inicialmente é preenchido com a data de inclusão da Pré-nota no sistema e posteriormente é atualizado quando é realizada a classificação da Pré-nota)  e verifica se o Calendário Contabil está bloqueado nesse período, caso esteja bloqueado e  tente estornar uma nota independente da Data que esteja logada no sistema  será apresentado o Help CTBBLOQ no estorno da Classificação da Nota.

**Exemplo.**

**Data de Digitação na Inclusão da Pré-Nota = 01/12/2021**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519163483159)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519181281943)

**Data da Classificação da Pré-Nota = 02/12/2021**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519252674327)

Observe que o campo F1\_DTDIGIT foi atualizado com a Data = **02/12/2021**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519293499799)

Após Classificar a Pré-Nota em 02/12/2021 , acessei a rotina CTBA010 e Bloquiei o Calendário Contabil para o período de Dez de 2021 e Bloqueio por Processos no módulo de Compras.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519331700759)

Bloqueio por Processo Compras período 01/12/2021  a 31/12/2021.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519386386327)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519394989975)

Acessei o sistema em 01/04/2022 e ao tentar estornar a Classificar da Pré - Nota (MATA140) apresentou o Help CTBBLOQ , pois, o sistema considera a data do campo F1\_DTDIGIT para o Bloqueio do Calendário Contábil.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519459235735)

**2ª ocorrência: Classificação da pré-nota**

Ao classificar uma pré-nota de data de emissão 23/11/2023 com bloqueio por processos do compras no calendário contábil do mês 11, o sistema gera o help abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20316283989527)

![](https://totvssuporte.zendesk.com/attachments/token/tsSFnx3g7JCh1bv9IVxb0RMTO/?name=image.png)

Isso ocorre pois o parâmetro **MV\_CTBDTBL**está com o conteúdo igual a 1. Caso deseje que o sistema permita essa classificação sem gerar help, será necessário alterar o conteúdo do parâmetro para 2.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20316283997975)

Para maiores informações referente ao parâmetro, verifique documentação abaixo.

https://tdn.totvs.com/pages/releaseview.action?pageId=754953489

**Saiba Mais:**

* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA010 - Como funciona a funcionalidade - Bloqueio por Processo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035066073-MP-SIGACTB-CTBA010-Como-funciona-a-funcionalidade-Bloqueio-por-Processo-?source=search)
* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como o Documento de Entrada verifica o Parâmetro MV\_DATAFIN ?](Cross%20Segmento%20-%20TOTVS%20Backoffice%20(Linha%20Protheus)%20-%20SIGACOM%20-%20Como%20o%20Documento%20de%20Entrada%20verifica%20o%20Par%C3%A2metro%20MV_DATAFIN%20?)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Tdn do parâmetro **MV\_CTBDTBL**](https://tdn.totvs.com/pages/releaseview.action?pageId=754953489)
