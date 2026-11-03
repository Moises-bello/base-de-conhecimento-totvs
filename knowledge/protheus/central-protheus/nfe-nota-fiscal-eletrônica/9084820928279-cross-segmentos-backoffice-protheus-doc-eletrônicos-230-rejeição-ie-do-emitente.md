---
article_id: 9084820928279
category: NFe - Nota Fiscal Eletrônica
content_hash: 7ccff2c8bd3fee044ccce809a5e50e6b770df0e23da9108e10d6d8b672bf30ff
fetched_at: '2026-06-28T22:40:03.778677+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 230 Rejeição: IE
  do emitente não cadastrada'
type: support-article
updated_at: '2025-06-13T12:12:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9084820928279-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-230-Rejei%C3%A7%C3%A3o-IE-do-emitente-n%C3%A3o-cadastrada
---

**Dúvida**Como corrigir a 230 Rejeição: IE do emitente não cadastrada ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar a  **rotina de transmissão SPEDNFE;**

![nfesefaz.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16691114322711)

2. Clique em **Outras ações -> Monitor -> faixa ->** Digite o número e série da nota;

**![monitor_faixa.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16691121131927)**

3. Clique no**botão Schema; Copie e Cole o conteúdo completo do XML.**

![545_rej_monitor.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16691121133847)

4. Verifique ***a TAG emit se o conteúdo da TAG CNPJ e IE estão corretos.***

5. Se informada IE do Emitente:  
– Acessar ***Cadastro de Contribuinte da UF (Chave: IE Emitente)***  
– IE Emitente ***não cadastrada***

A rejeição é um retorno da **Sefaz**, quando gera a rejeição 230 é necessário consultar a inscrição estadual do emitente

**6. O correto para** Sefaz é consultar o CCC:

Verificação se a IE do destinatário existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização (SEFAZ Autorizadora ou SEFAZ Virtual);

**7. Acesse o Cadastro** Centralizado de Contribuinte (CCC):

<https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc>

![ccc.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11548430797079)

**8. Se a rejeição persistir mesmo com IE válido em homologação e produção** entrar em contato junto a Sefaz.
