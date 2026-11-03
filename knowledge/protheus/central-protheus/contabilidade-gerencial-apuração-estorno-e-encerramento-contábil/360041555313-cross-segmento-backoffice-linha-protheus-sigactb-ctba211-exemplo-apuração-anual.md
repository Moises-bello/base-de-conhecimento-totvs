---
article_id: 360041555313
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 3e0cdcce3abd112cc02d29c0536f0e8839b01df5aa46ff0b7341ccef085d5c71
fetched_at: '2026-06-28T22:41:04.970189+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Exemplo -
  Apuração Anual: Apuração Sem conta PONTE'
type: support-article
updated_at: '2025-04-15T12:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE
---

**Dúvida**Como realizar Apuração Anual Sem conta PONTE  
  
**Ambiente**Microsiga Protheus – Contabilidade  – A partir da versão 11.80  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. **Passo**

* Através da rotina de lançamento contábeis (CTBA102) veja os lançamentos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055439473)

2. **Passo**

* Através da rotina de apuração de resultado CTBA211 , realize a apuração seguindo os parâmetros abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054574254)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054574274)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054574294)

* Realize o reprocessamento de saldos
* Sistema realiza o lançamento conforme  demonstrado no razonete abaixo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054574334)

* As Contas de receita e despesas **são zeradas:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054574354)

* Conta 2 Patrimônio Recebe o saldo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055440653)

* Através da [rotina de dados contábeis auxiliares (CTBA007)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024134092-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA007-CTBA211-Chave-de-Apura%C3%A7%C3%A3o-CW0) o sistema gera Registro com Z:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054574394)

Veja como sistema preenche os campos[\_LP e \_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)

* **Apuração de Resultado Anual em Vídeo** (How to):

* Veja se os campos CT2\_DTLP e das tabelas tabelas CQx foram populados pelo sistema
* Tabelas CQx (1, 2, 3, 4, 5, 6, 7, 8 e 9) "CQ0",'CQ2','CQ4','CQ6','CQ8"  possua com o campo CQ2\_LP = 'S' e o campo CQ0\_DTLP = data de apuração

Veja como deve ser realizada a [APURAÇÃO DAS ENTIDADES CENTRO DE CUSTO,ITEM CONTABIL E CLASSE DE VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)   
**Apuração de Resultado Conta e Centro de Custo em Vídeo** (How to):



Veja também:  
[Conceitos apuração e do sistema](https://tdn.totvs.com/pages/releaseview.action?pageId=334338459)

[O SISTEMA NÃO ESTA ZERANDO AS CONTAS DE RECEITA E DESPESA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046954954-MP-SIGACTB-CTBA211-O-SISTEMA-N%C3%83O-ESTA-ZERANDO-AS-CONTAS-DE-RECEITA-E-DESPESA?source=search)
