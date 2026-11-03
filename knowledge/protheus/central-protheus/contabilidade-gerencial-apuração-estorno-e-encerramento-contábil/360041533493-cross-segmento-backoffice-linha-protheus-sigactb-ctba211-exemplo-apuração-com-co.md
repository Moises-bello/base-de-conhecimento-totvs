---
article_id: 360041533493
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 357fd3a80db726b80713c2ce8d06b5b1844c31655b186a9a8867725304074ea1
fetched_at: '2026-06-28T22:41:04.987170+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Exemplo -
  Apuração Com Conta PONTE, Contas Transitórias e Encerramento
type: support-article
updated_at: '2025-04-15T12:35:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Com-Conta-PONTE-Contas-Transit%C3%B3rias-e-Encerramento
---

**Dúvida**

Como realizar Apuração com Conta  ponte , Contas Transitórias  e Encerramento, para controle gerencial   
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. **Passo**

* Através da rotina de lançamento contábeis (CTBA102) veja os lançamentos

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054526614)  
  
2. **Passo**

* A través da rotina de apuração de resultado CTBA211 , realize a apuração seguindo os parâmetros abaixo

 ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054526894)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054526914)

* Sistema realiza o lançamento conforme  demonstrado no razonete abaixo

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054526974)

* A conta 5.01 Ponte recebe somente o saldo

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054527234)

* A conta 5.02 Ponte recebe somente o saldo

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054527294)

* As Contas de receita e despesas não são zeradas

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055397613)

* Através da [rotina de dados contábeis auxiliares(CTBA007)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera Registro com P

![blobid1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055397673)

3. **Passo**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055397753)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054527574)

* O sistema realiza o lançamento de zeramento

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055397793)

* Apos apuração as contas de Receita e Despesa são zeradas

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055397853)

* Conta 5.01 Ponte é zerada

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055397953)

* Conta 5.02 é zerada

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054527714)

* Conta 2 Patrimônio Recebe o saldo

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054527734)

* Através da rotina de dados [contábeis auxiliares(CTBA007](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-MP-SIGACTB-CTBA007-CTBA211-CHAVE-DE-APURA%C3%87%C3%83O-CW0-?source=search)) o sistema gera Registro com Z

![blobid2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055398073)

**Saiba Mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=334338459>
