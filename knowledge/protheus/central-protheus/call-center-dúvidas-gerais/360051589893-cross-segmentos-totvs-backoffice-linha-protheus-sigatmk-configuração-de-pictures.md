---
article_id: 360051589893
category: Call Center - Dúvidas Gerais
content_hash: 9bbb95d76262aa8ea7845392cb7314d457eb357fc07b08cd96b2cf86ad64b3a5
fetched_at: '2026-06-28T22:41:26.987017+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: 'Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK- Configuração
  de Pictures nas rotinas de Atendimento Call Center '
type: support-article
updated_at: '2022-06-17T19:20:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051589893-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Configura%C3%A7%C3%A3o-de-Pictures-nas-rotinas-de-Atendimento-Call-Center
---

**Dúvida**  
Configuração de Pictures nas rotinas de Atendimento Call Center   
  
**Ambiente**  
Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK - a partir da versão 11

**Solução**  
1 - No padrão as numerações dos campos **ACF\_CODIGO**, **UA\_NUM** e **UC\_CODIGO** são configurados como "**Numéricos**"![Atendimento_Telemarketing.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360078687114/Atendimento_Telemarketing.PNG)

2 - Os campos de atendimentos no modulo de Call Center, são configurados como **Formato** "**999999**"

![SUC.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360078687134/SUC.PNG)

3 - Caso a **numeração** dos atendimentos seja Alfa-Numérico "**AAAA01**", para o sistema respeita o código corretamente, deverá **alterar** a **Picture** para @N dos campos que deseja.

![aaa.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360079820133/aaa.PNG)

**Observação:**

Este procedimento poderá ser consultado no link da documentação abaixo:

[Picture dos Campos - Dicionário de Dados](https://tdn.totvs.com/pages/viewpage.action?pageId=22479526)

Caso tenha duvidas sobre o procedimento, poderá verificar diretamente com a equipe de **Framework**.

**Alteração de Picture é valida para qualquer modulo do sistema.**
