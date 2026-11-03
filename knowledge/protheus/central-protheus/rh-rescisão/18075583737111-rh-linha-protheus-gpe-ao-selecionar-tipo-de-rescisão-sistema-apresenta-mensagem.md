---
article_id: 18075583737111
category: RH - Rescisão
content_hash: d8180b967742153ab79369f7f857d8fb8747112327ba183b8c141cb16656254c
fetched_at: '2026-06-28T22:43:51.098129+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao selecionar tipo de rescisão, sistema apresenta
  mensagem: FWRULES - Problema: Regra de dependência não respeitada (Aviso Prévio
  \ RG_TIPORES)'
type: support-article
updated_at: '2024-10-04T14:43:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18075583737111-RH-Linha-Protheus-GPE-Ao-selecionar-tipo-de-rescis%C3%A3o-sistema-apresenta-mensagem-FWRULES-Problema-Regra-de-depend%C3%AAncia-n%C3%A3o-respeitada-Aviso-Pr%C3%A9vio-RG-TIPORES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18075613662231) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que ao selecionar tipo de rescisão, sistema apresenta mensagem: FWRULES - Problema: Regra de dependência não respeitada (Aviso Prévio \ RG\_TIPORES)?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18075411416855)  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**A rotina emite mensagem devido ao cadastro tipo de rescisão em tabela S043 estar sem código informado na coluna Tipo Rescisão.

O campo Tipo Rescisão deve ser informado manualmente, sendo o campo Sequência gerado automaticamente.

**Exemplo**

**S043**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18075364797719)**

**Saiba mais**Para adquirir maior conhecimento acesse os *links* abaixo:

[RH - Linha Protheus - GPE - Como parametrizar a tabela S043 para cadastrar um novo tipo de rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004395831-RH-Linha-Protheus-GPE-Como-parametrizar-a-tabela-S043-para-cadastrar-um-novo-tipo-de-rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE -Sistema não permite deixar o campo COD. HOMOLOGNET em branco na tabela S043 quando a rescisão é por acordo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026397573-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-permite-deixar-o-campo-COD-HOMOLOGNET-em-branco-na-tabela-S043-quando-a-rescis%C3%A3o-%C3%A9-por-acordo)
