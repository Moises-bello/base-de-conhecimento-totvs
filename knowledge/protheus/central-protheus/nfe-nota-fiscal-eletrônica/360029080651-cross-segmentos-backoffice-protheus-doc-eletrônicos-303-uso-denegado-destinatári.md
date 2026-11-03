---
article_id: 360029080651
category: NFe - Nota Fiscal Eletrônica
content_hash: c9ddaddce7b2573f91b87205e7e4888212f701f36606b981aa79b337b5990cff
fetched_at: '2026-06-28T22:40:00.225134+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  303 Uso Denegado
  : Destinatário não habilitado a operar na UF'
type: support-article
updated_at: '2026-01-07T21:57:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029080651--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-303-Uso-Denegado-Destinat%C3%A1rio-n%C3%A3o-habilitado-a-operar-na-UF
---

**Dúvida**Como corrigir o retorno da Sefaz abaixo ?

303 Uso Denegado : Destinatário não habilitado a operar na UF  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Uma NF-e pode ser denegada por irregularidade fiscal do destinatário.

Assim, se uma empresa que estiver em situação regular emitir uma NF-e, mas informar nos dados do destinatário uma Inscrição Estadual baixada, então essa nota está sujeita a ser denegada.

Nesse caso, o emitente pode corrigir os dados do destinatário e emitir uma nova nota.

Lembrando que a denegação é diferente da rejeição. Uma nota que foi rejeitada pode ser corrigida e retransmitida com o mesmo número.

**Uma nota que foi denegada não pode ser retransmitida com o mesmo número**.

O que o emitente pode fazer é corrigir os dados do destinatário e emitir uma nova nota com uma nova numeração.

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029097411/mceclip0.png)

* **Cadastro de Cliente:**

**Contribuinte**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972554/mceclip4.png)**

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972034/mceclip2.png)

**Isento**  
​  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972074/mceclip3.png)

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059972034/mceclip2.png)

**Não Contribuinte**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059971394/mceclip0.png)

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059973634/mceclip5.png)

* **Cadastro de Fornecedor:**

     ![](https://totvssuporte.zendesk.com/attachments/token/vdmTfl5OB3RUjr1rT0c64YNuH/?name=inline1744640135.png)​  
  
     ![](https://totvssuporte.zendesk.com/attachments/token/gCLm5Rzelye7tNYi0CLltK6Is/?name=inline1704168182.png)​  
  
     ![](https://totvssuporte.zendesk.com/attachments/token/qlU80Sd0pYPmGSIucDKavVmvy/?name=inline-365322687.png)​

* **CNPJ Cliente:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360029030912/mceclip3.png)

* **CNPJ Fornecedor:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360029030431/mceclip4.png)**

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030033232/mceclip0.png)

* **Processo:**

No sistema **Protheus** a nota Denegada deve ser excluídas para que o sistema estorne as movimentações da nota (estoque, financeiro, contabilização, entre outros processos).

Com essa ação não levará valores para outras obrigações acessórias, como Apurações de ICMS e IPI ou arquivos magnéticos como Sped Fiscal, EFD Contribuições, entre outros.

No Livro Fiscal existe tratamento para que a nota fique como denegada, pois essa numeração não pode ser utilizada por já constar na base da SEFAZ. Dessa forma, esse número não pode ser mais utilizado, cancelado ou inutilizado.

Com isso, essa nota ficará com situação de **“Denegada”**.

No Livro Fiscal existe tratamento para que esta nota fique como denegada, no campo**F3\_CODRSEF** que verifica se o código de retorno foi o citado acima, então retorna a mensagem para o livro (MATR930).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029992531/mceclip0.png)

<http://tdn.totvs.com/pages/viewpage.action?pageId=134152528>
