---
article_id: 360041554693
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 63d92afb90ce445a1fc166d589ffaffc31805fdd81857dddc788f1480cc85252
fetched_at: '2026-06-28T22:41:05.000944+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Exemplo -
  Apuração Trimestral: Apuração Sem conta PONTE'
type: support-article
updated_at: '2025-04-15T12:32:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE
---

**Dúvida**

Como realizar Apuração **Sem** conta **PONTE,** zerando as contas de receita e despesa  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial - Versão 12

**Requisitos**

Caso a apuração já tenha sido realizada, é necessário efetuar o estorno:

* Através da rotina **CTBA215**, realize o estorno da apuração, um trimestre de cada vez. Consulte o material: [ECF - Como realizar estorno de apuração de resultados L/P?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search)
* Acesse a [rotina **CTBA007**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) e verifique se o registro de apuração foi excluído.
* Acesse a rotina **CTBA102** e confirme se os lançamentos contábeis foram excluídos.
* Emita os relatórios de Razão e Balancete para verificar se os lançamentos retornaram para as contas de receita e despesa.
* Ao emitir o relatório, configure a pergunta abaixo como "**Não**".  
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082615853)​

* Verifique se os campos **CT2\_DTLP**, **CQ0\_DTLP** e **CQ1\_LP** foram limpos pelo sistema.

Durante a apuração de resultados, avalie os seguintes pontos:

* Realize a apuração de resultados.
* Acesse a rotina **CTBA007** e verifique se foi gerado o registro de apuração.
* Acesse a rotina **CTBA102** e confirme se os lançamentos contábeis foram gerados.
* Verifique se os campos **CT2\_DTLP**, **CQ0\_DTLP** e **CQ1\_LP** foram preenchidos pelo sistema.

**Solução**

**1. Passo**  
Através da rotina de lançamentos contábeis **CTBA102**, verifique os lançamentos realizados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572794)

**2. Passo**  
Através da rotina de apuração de resultados **CTBA211**, realize a apuração seguindo os parâmetros abaixo:

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438613)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437873)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437913)

* Realize o reprocessamento de saldos.
* O sistema reliza os lançamentos conforme demonstrado no razonete:

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438573)

* A conta **2 – Patrimônio Líquido** recebe o saldo total.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572854)

* As contas de receita e despesa são zeradas.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437993)

* Através da [rotina de dados contábeis auxiliares (**CTBA007**),](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera o registro com "Z".

![blobid0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438013)

3. **Passo**

**![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438553)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437873)**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572874)**

* Realize o reprocessamento de saldos.
* O sistema reliza os lançamentos conforme demonstrado no razonete:

**![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438513)**

* A conta **2 – Patrimônio Líquido** recebe o saldo total.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438093)

* As contas de receita e despesa são zeradas.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438113)

* Através da [rotina de dados contábeis auxiliares (**CTBA007**),](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera o registro com "Z".

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438173)

4. **Passo**

**![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438473)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437873)**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438293)**

* Realize o reprocessamento de saldos.
* O sistema reliza os lançamentos conforme demonstrado no razonete:![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573214)

* A conta **2 – Patrimônio Líquido** recebe o saldo total.

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573374)

* As contas de receita e despesa são zeradas.

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573554)

* Através da [rotina de dados contábeis auxiliares (**CTBA007**)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0), o sistema gera o registro com "Z".

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438733)

5. **Passo**

**![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573614)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437873)**

**![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573634)**

* Realize o reprocessamento de saldos.
* O sistema reliza os lançamentos conforme demonstrado no razonete:

**![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573694)**

* A conta **2 – Patrimônio Líquido** recebe o saldo total.

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054573754)

* As contas de receita e despesa são zeradas.

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055438893)

* Através da [rotina de dados contábeis auxiliares (**CTBA007**),](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera o registro com "Z".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054580414)

Veja como sistema preenche os campos[\_LP e \_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)

* Veja se os campos CT2\_DTLP e das tabelas tabelas CQx foram populados pelo sistema
* Tabelas CQx (1, 2, 3, 4, 5, 6, 7, 8 e 9) "CQ0",'CQ2','CQ4','CQ6','CQ8"  possua com o campo CQ2\_LP = 'S' e o campo CQ0\_DTLP = data de apuração

Veja como deve ser realizada a [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)

Veja também :[Conceitos apuração e do sistema](https://tdn.totvs.com/pages/releaseview.action?pageId=334338459)

[O SISTEMA NÃO ESTA ZERANDO AS CONTAS DE RECEITA E DESPESA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046954954-MP-SIGACTB-CTBA211-O-SISTEMA-N%C3%83O-ESTA-ZERANDO-AS-CONTAS-DE-RECEITA-E-DESPESA?source=search)
