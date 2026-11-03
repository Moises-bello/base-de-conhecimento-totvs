---
article_id: 8549802506519
category: Faturamento - Cadastros
content_hash: cdb539d4d39d255997f401ea35ed9add968f9ff9d187301e0b39364e61294bcb
fetched_at: '2026-06-28T22:38:36.495288+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAFAT - Como habilitar a opção
  Complemento do Cliente no cadastro do cliente no botão Outras Ações?
type: support-article
updated_at: '2022-08-31T12:09:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8549802506519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFAT-Como-habilitar-a-op%C3%A7%C3%A3o-Complemento-do-Cliente-no-cadastro-do-cliente-no-bot%C3%A3o-Outras-A%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**

Como habilitar a opção Complemento do Cliente no cadastro do cliente quando vou alterá-lo no botão Outras Ações?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento – Protheus 12+

**Solução**

**Caso esteja em uso a rotina Cadastro de Clientes - CRMA980 (MV\_MVCSA1 = .T.):**

Os complementos do cliente possuem uma nova aba, a "Informações Complementares" que é por lá que será inserido essas e mais informações, não é mostrado no botão "Outras Ações".

**Caso você use a rotina Cadastro de Clientes - MATA030 (MV\_MVCSA1 = .F.):**  
Os complementos do cliente estão em "Outras Ações" quando você **Alterar** e/ou **Visualizar** um cliente:

> ![](https://totvssuporte.zendesk.com/attachments/token/cBQW1YXAcEjTmjBxbRQNsyW3h/?name=image.png)

O fonte chamado no processo é o **MATA030A** e mostra alguns campos da tabela **AI0 - Complementos de Clientes**:

> ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8549613921943/mceclip0.png)

**Sobre Como habilitar a opção Complemento do Cliente​, pode lhe interessar:**

[Documentação Complemento do Cliente: https://tdn.totvs.com/x/tw8NF](https://tdn.totvs.com/x/tw8NF)

**Vídeo HowTo explicando a descontinuação da rotina Cadastro de Clientes - MATA030:**

<https://www.youtube.com/watch?v=aEY_Xk_wnCg>
