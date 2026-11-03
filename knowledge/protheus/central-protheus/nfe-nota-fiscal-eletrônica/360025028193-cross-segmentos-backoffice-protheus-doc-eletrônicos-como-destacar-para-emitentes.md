---
article_id: 360025028193
category: NFe - Nota Fiscal Eletrônica
content_hash: dfd0a5d0106ed8356073efb85b74cdb201243f4ae2bae7d610d895ebc448c555
fetched_at: '2026-06-28T22:40:03.499239+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como destacar para
  emitentes do Simples Nacional Base de cálculo do ICMS e Valor do ICMS
type: support-article
updated_at: '2024-10-22T18:21:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025028193-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-destacar-para-emitentes-do-Simples-Nacional-Base-de-c%C3%A1lculo-do-ICMS-e-Valor-do-ICMS
---

**Dúvida**

Como destacar para emitentes do Simples Nacional Base de cálculo do ICMS e Valor do ICMS ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Será destacado o ICMS **no  Danfe em cálculo do imposto** nos campos ***Base de cálculo do ICMS e Valor do ICMS.***

1. Caso sua empresa seja do regime Simples Nacional devera acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** e alterar o parâmetro **MV\_CODREG = 1**

2.  Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros e alterar o parâmetro  MV\_IMPSIMP=.T.** 

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061240273)**

 3. Para haver o destaque o ICMS deve ser calculado e além disso, no TES o campo  **F4\_CSOSN "Campo Cod. Sit. SN" deve estar como 101, 202 ou 900.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26136438301335)

4. Para destacar no Danfe os campos na SF3 **(SF3->F3\_BASEICM e SF3->F3\_VALICM)** devem estar preenchidos. Para isso no **TES** deixar L. fiscal ICMS = **Tributado**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061239653)**

* **Saiba mais:**

 Atualmente o ICMS e o ICMS-ST são destacados quando a empresa é optante pelo simples nacional apenas no **cabeçalho da Nfe** se o parâmetro estiver habilitado.  
  
Nos itens do Danfe já foi aberto chamado **para a nossa consultoria tributária**  e a mesma informou que **nos itens não devem ser destacados a base de cálculo do ICMS e o valor do ICMS.**  
  
Para **sair em Dados do produto e serviço deve ser realizada uma consulta formal junto** a Sefaz e abrir um ticket no suporte.

* **Importante:**

Caso sua empresa seja do regime normal e esteja realizando uma devolução de um fornecedor do simples nacional utilizando CSOSN 101**para não seja apresentado os valores de ICMS basta preencher o campo da TES *Calcula ICMS = N - Não*.**

**Somente com CSOSN 900 gera as tags vBC e vICMS na linha do item, pois para esse CSOSN a Sefaz liberou essas tags.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26136635957271)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26136635962903)**
