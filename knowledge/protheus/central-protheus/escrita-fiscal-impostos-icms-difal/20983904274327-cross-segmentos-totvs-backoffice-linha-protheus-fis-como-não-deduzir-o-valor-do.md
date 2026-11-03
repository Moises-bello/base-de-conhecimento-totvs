---
article_id: 20983904274327
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: ae3c4da9ac844753a59ad944ec91e665b550ce339c974bc92e5790ae9b0462c5
fetched_at: '2026-06-28T22:39:19.284674+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como não deduzir
  o valor do ICMS da base dupla do DIFAL ST?
type: support-article
updated_at: '2025-01-15T13:45:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20983904274327-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-n%C3%A3o-deduzir-o-valor-do-ICMS-da-base-dupla-do-DIFAL-ST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20983879842583) Tempo aproximado para leitura: **00:05:00 min****Dúvida**

Como não deduzir o valor do ICMS da base dupla do DIFAL ST?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**Para que o valor de ICMS não seja deduzido da base dupla do DIFAL ST, deve seguir a seguinte a configuração.

obs: a UF utilizado como exemplo é AL, porém pode ser configurado para os demais estados.

**Parâmetros:**  
MV\_UFBSTGO = AL  
MV\_UFBDST = AL  
   
**TES**

* **Calcula ICMS**(F4\_ICM) = Sim
* **L. FISC. ICMS** (F4\_LFICM) = Tributado ou Outros Ou Isento
* **Calc Dif ICM**. (F4\_COMPL) = NÃO
* **MATL CONSUMO** (F4\_CONSUMO) = SIM
* **AGREGA SOLID.** (F4\_INCSOL) = SIM
* **MKP.ICM.COMP** (F4\_MKPCMP) = NÃO
* **MARG. SOLID.** (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)
* **Ded.ICM.ST (F4\_ICMSTMT)** = 1-Sim ou  2-Não

**Produto ou Exceção Fiscal:**  
Informe no **Cadastro do Produto Campo:**Solid. Saída ( B1\_PICMRET) ou da **Exceção Fiscal**Campo: Margem de Lucro (F7\_MARGEM)  o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial.

Primeiro destaco a memória de cálculo dessa configuração que será a seguinte.

Base dupla DIFAL ST = Base de cálculo ICMS interestadual / ((100 - alíquota destino)/100)

Base Dupla DIFAL ST = 1000 / ((100 - 19)/100)

Base Dupla DIFAL ST = 1000 / 0,81 = **1.234,57**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20983879845399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20983904235415)

A memória da cálculo da base dupla do DIFAL ST padrão, onde ocorre a dedução do ICMS é a seguinte:

Base dupla Difal ST = ( Base de cálculo ICMS interestadual - Valor de ICMS) / ((100 - alíquota destino)/100)

Base Dupla DIFAL ST = (1000 - 70,00) / ((100 - 19)/100)

Base Dupla DIFAL ST = 930,00 / 0,81 = **1.148,15**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20983904239127)**
