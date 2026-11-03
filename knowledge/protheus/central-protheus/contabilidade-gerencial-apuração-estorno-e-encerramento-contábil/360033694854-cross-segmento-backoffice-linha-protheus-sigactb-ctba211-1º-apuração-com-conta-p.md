---
article_id: 360033694854
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: 181130a51c24b59e6ccfe2e6c3b4fd71071163ac0b930596401e7f9b1b7e22ec
fetched_at: '2026-06-28T22:41:05.048839+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA211 - 1º Apuração  com
  Conta ponte e 2º  sem Conta Ponte: Não é permitido duas apurações para o mesmo período'
type: support-article
updated_at: '2025-01-22T22:26:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033694854-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA211-1%C2%BA-Apura%C3%A7%C3%A3o-com-Conta-ponte-e-2%C2%BA-sem-Conta-Ponte-N%C3%A3o-%C3%A9-permitido-duas-apura%C3%A7%C3%B5es-para-o-mesmo-per%C3%ADodo
---

**Ocorrência:**

Ao realizar duas apurações **1º**por **conta Ponte** para os 12 meses o sistema apurou normalmente, porém ao realizar a **2º** apuração (**sem conta ponte**) o sistema apresentou a mensagem **"Não é permitida duas apurações para o mesmo período"**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043363914)  
  
**Ambiente**Microsiga Protheus– Contabilidade – A partir da versão 11.80  
  
**Causa**

A situação ocorre quando alguma das tabelas **CQx** (1, 2, 3, 4, 5, 6, 7, 8 e 9) — como **"CQ0", "CQ2", "CQ4", "CQ6" e "CQ8"** — possui o campo **CQ2\_LP** marcado como **'S'** e o campo **CQ0\_DTLP** preenchido com a data de apuração.

Nesse caso, o sistema não permite a execução da apuração de resultados, pois entende que o processo já foi concluído.

💡️ Situação pode ter sido ocasionada devido alguma interrupção na apuração de resultados.

**Observação ⚠️:**

* "\_LP = 'S' "  será gerado nos lotes normais que foram apurados
* "\_LP = 'Z' " será gerado nos lotes de apuração

**Exemplo 🚩️:**

Incluso o lançamento através da rotina **CTBA102**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043767694)

Após apuração, realizada validação através da rotina **CTBA211**

Veja que o campo "\_LP =S"

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044636593)

O lote de apuração é gerado com o campos "\_LP=Z"

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043767894)

**Solução**

Caso identifique que a(s) tabela(s) possuem os campos "\_LP" e "\_DTLP" já preenchido para o período que esta tentando realizar a apuração de resultado, é necessário ajuste de base por um analista de sua confiança.

Saiba Mais:

* [Tabela Processadas na execução da apuração de resultado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009345312-MP-SIGACTB-CTBA211-Tabela-Processadas-na-execu%C3%A7%C3%A3o-da-apura%C3%A7%C3%A3o-de-resultado?source=search)
* [PREENCHIMENTO DOS CAMPOS CQ0\_LP e CQ0\_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)veja que ao realizar o estorno da apuração o sistema [limpa os campos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010708171-MP-SIGACTB-ECF-Como-realizar-estorno-de-apura%C3%A7%C3%A3o-de-resultados-L-P-?source=search)

Caso os procedimentos anteriores tenham sido revisados, mas o erro continue sendo apresentado, aplique o patch abaixo conforme a versão utilizada:

1. Verifique se os fontes estão atualizados com as seguintes datas ou superiores:
   * **CFGX019.PRW**: 19/06/2019 08:32:42
   * **CTBA211.PRW**: 14/02/2020 11:03:33
2. Veja se está realizando apuração corretamente:

* [Exemplo - Apuração Com Conta PONTE, Contas de Resultados e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041053194--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-com-Conta-Ponte-Contas-de-Resultados-e-Encerramento?source=search)
* [Exemplo - Apuração Com Conta PONTE, Contas Transitórias e Encerramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041533493--MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-com-Conta-Ponte-Contas-Transit%C3%B3rias-e-Encerramento?source=search)
