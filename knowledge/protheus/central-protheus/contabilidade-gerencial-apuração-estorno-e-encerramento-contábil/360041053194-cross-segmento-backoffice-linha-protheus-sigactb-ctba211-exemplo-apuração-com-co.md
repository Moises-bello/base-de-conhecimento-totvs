---
article_id: 360041053194
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 0f5f689bbf34445361d6fb5397576ba31541df822695ad013fc882da2c29df21
fetched_at: '2026-06-28T22:41:04.979224+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Exemplo -
  Apuração Com Conta PONTE, Contas de Resultados e Encerramento
type: support-article
updated_at: '2025-04-15T12:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-de-Resultados-e-Encerramento
---

**Dúvida**

Como realizar Apuração com Conta Ponte, Contas de Resultados e Encerramento, para controle gerencial

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Causa**

" As contas de patrimônio líquido podem receber todos os saldos das contas de resultados ou somente o saldo do resultado do período?"

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572674)

Para atender [**Lei nº. 11.638/07** ao art. 178 (alínea d) da Lei nº. 6.404/76](https://tdn.totvs.com/pages/releaseview.action?pageId=525020345) , deve seguir o procedimento abaixo 

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. **Passo**

* Através da rotina de lançamento contábeis (CTBA102) veja os lançamentos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055436913)

2. **Passo**

* Através da rotina de apuração de resultado CTBA211 , realize a apuração seguindo os parâmetros abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055436953)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054571034)

* Sistema realiza lançamento, conforme razonete abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572234)

* Veja que a conta 5.01 Ponte recebeu o saldo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572254)

* Conta 2 Patrimônio Liquido recebe o saldo total:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437153)

* Conta de receita e despesa não são zeradas:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437213)

* Através da [rotina de dados contábeis auxiliares (CTBA007)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera Registro com P

![blobid0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437253)

3. **Passo**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572274)**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437273)**

* O sistema realiza o lançamento de zeramento:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054572294)

* Apos apuração as contas de Receita e Despesa são zeradas

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437313)

* Conta 5.01 Ponte é zerada:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437333)

* Conta 5.02 é zerada:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437353)

* Através da [rotina de dados contábeis auxiliares (CTBA007)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera Registro com Z

![blobid1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055437373)

**Saiba Mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=334338459>

[MP - SIGACTB CTBA211 - APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)
