---
article_id: 360024630411
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: b96fd131f7acb42821c22b033f3f1cfc5a6d38798b9729d601295df6102f1cb8
fetched_at: '2026-06-28T22:41:05.072005+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - Preenchimento
  do campo CQ0_LP e CQ0_DTLP
type: support-article
updated_at: '2025-01-22T22:09:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-Preenchimento-do-campo-CQ0-LP-e-CQ0-DTLP
---

**Dúvida**

Preenchimento do campo **CQ0\_LP** - Flag Saldo Lucros Perdas e **CQ0\_DTLP** - Data da apuração  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Os campo \_LP e \_DTLP são  preenchidas quando a apuração de resultado é executada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022886651) ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022853392)

**Observação ⚠️:**

* "\_LP = 'N' " será gerado ao incluir lançamento contabil através da rotina CTBA101/CTBA102
* "\_LP = 'S' "  será gerado nos lotes normais  que foram apurados
* "\_LP = 'Z' " será gerado nos lotes de apuração

**Exemplo 🚩️:**

1º Ao incluir o lançamento contábil rotina CTBA102/CTBA101 

* **Lote 8850** = Incluir lançamento contábil com a conta  **3201020002** no **crédito****,** o sistema grava  o campo **"\_LP = 'N'**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29432461478167)

2º Após apuração realizada através da rotina **CTBA211**

a) O sistema grava no lançamento contábil

* **Lote 8850** = Conta  **3201020002** que foi apurada permanece no **crédito,** o sistema só muda o campo **"\_LP =S"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29432461480087)

b) Sistema inclui um novo **lote contábil de apuração**  

* **Lote APU001** = é gerado um lote para a conta  **3201020002** no **Débito** para zeramento, o com o campo **"\_LP =Z"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097251393)

Demais tabelas também são alimentadas

CQx (1, 2, 3, 4, 5, 6, 7, 8 e 9) "CQ0",'CQ2','CQ4','CQ6','CQ8" 

CQ0\_LP = 'S' e o campo CQ0\_DTLP = data de apuração

**Saiba Mais :**

[SIGACTB - CTBA211 Não é permitida duas apurações para o mesmo período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033694854-MP-SIGACTB-CTBA211-N%C3%A3o-%C3%A9-permitida-duas-apura%C3%A7%C3%B5es-para-o-mesmo-per%C3%ADodo?source=search)

* [Tabela Processadas na execução da apuração de resultado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009345312-MP-SIGACTB-CTBA211-Tabela-Processadas-na-execu%C3%A7%C3%A3o-da-apura%C3%A7%C3%A3o-de-resultado?source=search)
* Veja que ao realizar o estorno da apuração o sistema [limpa os campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search)
