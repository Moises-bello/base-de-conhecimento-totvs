---
article_id: 25500824620439
category: TAF - eSocial - Atualização
content_hash: ea4c07f9439133c6446c004ab52aae30d1591bcc64eb0a36d21c88732662e777
fetched_at: '2026-06-28T22:45:13.404943+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - O valor '68' informado na
  tag CodIncIRRF não existe na base de dados.
type: support-article
updated_at: '2024-08-08T17:44:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25500824620439-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-O-valor-68-informado-na-tag-CodIncIRRF-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência**Ao cadastrar uma verba no ERP a mensagem abaixo é apresentada:

**![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25500795071383)**

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF -Todas as versões

**Solução**Para que o código seja criado no TAF será necessário aplicar a expedição contínua e atualizar as autocontidas:

Expedição contínua TAF:

12.1.2310:

<https://suporte.totvs.com/portal/p/10098/download#detail/1126399>

Autocontidas:

[RH - Linha Protheus - TAF - eSocial - Configuração - Como atualizar as tabelas autocontidas no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017826812-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-atualizar-as-tabelas-autocontidas-no-TAF?source=search)

É necessário também que a tabela C8U (tabela de incidência de IRRF) esteja totalmente compartilhada e sem filial, caso contrário, mesmo que o código exista no TAF a integração/geração da verba não será realizada.
