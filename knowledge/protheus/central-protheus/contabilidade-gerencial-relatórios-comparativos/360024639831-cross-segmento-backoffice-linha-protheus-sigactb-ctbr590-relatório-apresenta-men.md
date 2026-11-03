---
article_id: 360024639831
category: Contabilidade Gerencial - Relatórios Comparativos
content_hash: b29e2b4b08a2fbbaa650337e513259f0bde65e8bac043d4977d2a4186b4804f7
fetched_at: '2026-06-28T22:40:37.200108+00:00'
product: protheus
section_id: 1500001548922
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: CTBR590 RELATÓRIO APRESENTA
  MENSAGEM  HELP: CTBENTR590'
type: support-article
updated_at: '2022-06-20T19:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024639831-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR590-RELAT%C3%93RIO-APRESENTA-MENSAGEM-HELP-CTBENTR590
---

**Dúvida**

 Ao tentar acessar o relatório CTBR590 o sistema apresenta mensagem

Help : CTBENTR590  
Problema : Relatório não disponível para utilizar com as entidades adicionais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022872012/mceclip0.png)  
   
 **Ambiente**  
Microsiga Protheus  – Contabilidade gerencial – A partir da versão 11.80

**Causa:**

Situação é apresentada pois o parâmetro está habilitado para utilizar cubo de entidades contábeis

MV\_CTBCUBE = 1  
  
   
**Solução**

Para que a situação não seja apresentada o parâmetro deve ser configurado para não Utilizar as entidades contábeis

MV\_CTBCUBE

Este parâmetro deve ser ativado, quando utilizado o [wizard de configuração de Entidades Contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=311066123).

Utiliza cubo de entidades contábeis?

0 - Não;

1 - Sim.
