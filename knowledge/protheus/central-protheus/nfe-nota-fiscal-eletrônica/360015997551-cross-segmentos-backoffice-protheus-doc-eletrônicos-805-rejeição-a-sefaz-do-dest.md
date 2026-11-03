---
article_id: 360015997551
category: NFe - Nota Fiscal Eletrônica
content_hash: 7fdd9bb965ca26607700e002921ed5b98819efebb34e1ab45e64b76bc17f0b1e
fetched_at: '2026-06-28T22:40:05.302817+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 805 Rejeição :
  A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual'
type: support-article
updated_at: '2025-10-09T13:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015997551-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-805-Rejei%C3%A7%C3%A3o-A-SEFAZ-do-destinat%C3%A1rio-n%C3%A3o-permite-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual
---

**Dúvida**Como solucionar a rejeição abaixo ?

805 Rejeição : A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Causa**

Informado destinatário como Contribuinte Isento de Inscrição Estadual (indIEDest=2-  
ISENTO) em UF que não permite esta situação nas operações internas e interestaduais  
(idDest=1 ou 2), conforme segue: AL, AM, BA, CE, DF, GO, MG, MS, MT, PB, PE, RN, RS, SE, SP.

**Solução**

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15523209933975)

Se gerado no XML um destinatário  **ISENTO** e utilizar um **CST do ICMS tributado** na nota causa a rejeição 805:

* **Exemplo o XML gerou conforme abaixo:**

![](https://totvssuporte.zendesk.com/attachments/token/99aV3woNVo7wRHkrOrK95Pf3M/?name=inline820693705.png)​

![](https://totvssuporte.zendesk.com/attachments/token/iblHHd5KmHVnEc5bkq6STHzYV/?name=inline-1917401952.png)​

1- Verifique se a situação tributária do ICMS pode ser alterada:

Altere a situação tributaria do ICMS  no **TES** no campo **Sit. trib. ICMS** **(F4\_SITTRIB) para 40 ou 41.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15523225251735)

2- Após isso **exclua a nota e gere novamente** se for utilizar o mesmo **pedido de vendas digite o TES** novamente para alterar no pedido a situação tributária do ICMS.

3- Se a situação tributaria da nota estiver correta:

* **Cadastro de Cliente:**

**Contribuinte  indIEDest = 1**

1- Preencha a inscrição estadual no campo  **Ins. Estad. A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Deixo o conteúdo campo **Destaca IE** - ***A1\_IENCONT*** em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo **Contribuinte****A1\_CONTRIB****1- Sim**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15523225267351)

**Não Contribuinte indIEDest = 9**

1- Preencha a inscrição estadual no campo  Ins. Estad. **A1\_INSCR**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE***A1\_IENCONT*** 1- Sim

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte**A1\_CONTRIB** 2 - Não

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15523209942039)

* **Conforme a Nota técnica há também as seguintes exceções:**

Observação 1: Regra de validação conforme configuração da UF do Destinatário  
(permite ou não permite Contribuinte Isento de Inscrição Estadual).

Observação 2: No caso das operações internas, a implantação da RV em produção foi  
adiada para **13/10/25.**

**Exceção 1**: Esta regra de validação não se aplica quando houver destaque do ICMS-ST  
(campo vICMSST) em pelo menos um item da NF-e.  
**Exceção 2**: Esta regra de validação não se aplica quando houver informação do ICMSST retido anteriormente (campo vICMSSTRet) em pelo menos um item da NF-e.  
**Exceção 3**: A regra de validação não se aplica, em produção, para Nota Fiscal com data  
de emissão anterior a 01/07/2016.  
**Exceção 4**: Esta regra de validação não se aplica nas operações isentas (**CST=40-Isenta**  
**ou CSOSN=103-Isento), imunes ou não tributadas (CST=41-Não tributada, ou**  
**CSOSN=300-Imune, ou CSOSN=400-Não tributada pelo Simples Nacional).**

* **Validação da Sefaz NT2025.001 V1.02:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34675095471639)
