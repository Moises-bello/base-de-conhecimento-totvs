---
article_id: 360047840094
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 7587db4dee6887ffb880a9ec05459632db62785acbca901774ca6151563bb714
fetched_at: '2026-06-28T22:40:44.337902+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD registro I052 COMO
  GERAR
type: support-article
updated_at: '2024-04-11T19:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047840094-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-registro-I052-COMO-GERAR
---

**Ocorrência**

Com gerar o registro I052 ?  
  
**Ambiente**  
Microsiga Protheus – Contabilidade  – A partir da versão 11.80  
  
  
**Solução**O registro I052 é gerados para a contas que foram informadas nas visões gerenciais de Balanço e DRE 

Verifique:

* Caso tenha gerado a ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)
* Para gerar o ECD com Centro de Custo é necessário primeiramente, que o Centro de Custo esteja apurado.Veja como realizar a [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)
* Obs: caso esteja gerando com centro de custo, necessário verificar se o centro de custo esta devidamente zerado caso contrario o registro I052 não será gerado
* conta existe no plano de contas
* conta está amarrada ao plano referencial (só é obrigatório , para quem for gerar com plano de contas referencial )
* conta foi informada na visão gerencial

Através da rotina de cadastro de visão gerencial (CTBA161)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070331594)

Veja se os dados foram corretamente informado e caso for gerar com  centro de  [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search) verifique foi informado na visão gerencial

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070331734)

Ao gerar o arquivo informe a visão gerencial de balanço [J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)  e Dre [J150 ​](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-J150-LAYOUT-6?source=search)

* O sistema irá gerar o registro

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070331814)

 Tabelas :

• CTS - Entidade Gerencial  
• CVE - Visão gerencial  
• CVF - Itens da Visão Gerencial  
• CTN - Configuração de Livros Contábeis

Veja :

* se as tabelas estão com o compartilhamento correto
* se a ordem dos campos não foram alteradas
* se todos as tabelas estão populadas corretamente
* caso possua alguma conta que o sistema não gerou o I052 e para outra sim sugiro comparar o cadastro dessas contas   nas tabelas mencionadas anteriormente, para assim identificar a diferença entre elas.

<https://tdn.totvs.com/pages/releaseview.action?pageId=647438980>

Saiba mais

[MP - SIGACTB - ECD registro J150 - 7-VL\_CTA e 2-COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)
