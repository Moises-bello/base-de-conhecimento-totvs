---
article_id: 4403478266775
category: NFe - Nota Fiscal Eletrônica
content_hash: d87cddf04d1511c2ef13608cd9fade6f47f931e531e31ded7d369b291e6792f7
fetched_at: '2026-06-28T22:40:03.862392+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 307 Emitente bloqueado
  pela UF de destino em operação com consumidor final
type: support-article
updated_at: '2024-08-09T17:26:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403478266775-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-307-Emitente-bloqueado-pela-UF-de-destino-em-opera%C3%A7%C3%A3o-com-consumidor-final
---

**Dúvida**Como solucionar a rejeição 307 Emitente bloqueado pela UF de destino, em operação com consumidor final.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se operação de saída interestadual (tpNF=1 e idDest=2) e operação com  
Consumidor Final (indFinal=1) e indIEDest=9:

Acessar Cadastro Centralizado de Contribuinte (Chave: UF do Destinatário,  
CNPJ do Emitente, cSitCNPJ=10)

1 - Verifique se realmente a nota é de **consumidor final, caso não seja altere no pedido de vendas** no campo**Tipo Cliente "C5\_TIPOCLI" = L, R, S e X**

![C5_TIPOCLI.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4403478983319)

2 - Após isso, **exclua a nota** e gere novamente.

3 - Caso o destinatário **seja Consumidor final, verifique se realmente é não contribuinte:**

* **Cadastro de Cliente:**

**Contribuinte**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25533856310679)**

1- Preencha a inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25533870138775)

**Isento**  
​  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25533870141463)

1- Deixe em branco ou Preencha com literal Isento o campo de inscrição estadual no campo  Ins. Estad. **"A1\_INSCR"**

![](https://totvssuporte.zendesk.com/attachments/token/F28rwEzItrBoQEVD6unisbVWf/?name=inline2138881771.png)​

2- Preencha o campo Destaca IE **"A1\_IECONT"**  em branco

![](https://totvssuporte.zendesk.com/attachments/token/mL279biwk84pyy9o3nV2hwcwc/?name=inline135028164.png)

3- Preencha o campo Contribuinte **"A1\_CONTRIB"**  1- Sim

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25533870138775)

4 - Caso a nota seja nota realmente nota de **consumidor final e não contribuinte:**

Assim, se uma empresa que estiver em situação regular emitir uma NF-e, mas informar nos dados do emitente ou destinatário uma Inscrição Estadual baixada, então essa nota está sujeita a ser rejeitada. Nesse caso, o emitente pode corrigir os dados do destinatário e emitir uma nova nota.

**O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

**Cadastro Centralizado de Contribuinte (CCC):**

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

Para regularizar a situação entre em contato junto a Sefaz.

**Validação da Sefaz:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25533870144407)
