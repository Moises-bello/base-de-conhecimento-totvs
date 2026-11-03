---
article_id: 4412782071831
category: NFe - Nota Fiscal Eletrônica
content_hash: 5049333dae6317e33a102da3277dc7f12f74035bb19dec2a1b9a4e5e3d401318
fetched_at: '2026-06-28T22:40:00.247060+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  554 Rejeição:
  IE do Emitente informada como ISENTO indevidamente '
type: support-article
updated_at: '2023-05-16T17:50:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412782071831--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-554-Rejei%C3%A7%C3%A3o-IE-do-Emitente-informada-como-ISENTO-indevidamente
---

**Dúvida**Como solucionar a rejeição abaixo:

554 Rejeição: IE do Emitente informada como ISENTO indevidamente ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se IE informada **com “ISENTO”:** - Se modelo = 65 **ou Série difere da faixa 890-919**

* **O correto para Sefaz é consultar o CCC:**

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

* **Cadastro Centralizado de Contribuinte (CCC):**

*<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>*

1. Entre no ***SIGACFG (Configurador),*** geralmente o acesso é restrito ao administrador do sistema;

2. Acesse o caminho: ***Ambiente> Empresas> Grupo de Empresas.*** Nesse caminho poderá ser visualizado a estrutura do cadastro de empresas (SIGAMAT).

3. Informar a Inscrição estadual da empresa conforme consta no cadastro ***centralizado de** **contribuinte da Sefaz;***

4. Após isso, ***exclua a nota e gere novamente.***

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412775522839/mceclip0.png)
