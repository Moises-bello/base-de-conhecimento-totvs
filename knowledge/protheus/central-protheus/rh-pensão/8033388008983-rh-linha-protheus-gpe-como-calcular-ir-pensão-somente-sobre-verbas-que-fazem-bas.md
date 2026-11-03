---
article_id: 8033388008983
category: RH - Pensão
content_hash: 243b39b88468735222b26a9f10ec6c5f12bf938c287e2a50f19d89b348eb3157
fetched_at: '2026-06-28T22:43:35.133073+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular IR pensão somente sobre verbas que
  fazem base para pensão (MV_PENSIR)
type: support-article
updated_at: '2025-04-16T14:34:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8033388008983-RH-Linha-Protheus-GPE-Como-calcular-IR-pens%C3%A3o-somente-sobre-verbas-que-fazem-base-para-pens%C3%A3o-MV-PENSIR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15686975850775) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como calcular IR de pensão somente sobre verbas que fazem base para a pensão - MV\_PENSIR?  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Deverá ser criado o parâmetro **MV\_PENSIR** via configurador SIGACF conforme informações abaixo:

|  |  |
| --- | --- |
| **Parâmetro** | MV\_PENSIR |
| **Descrição** | Indica se deve calcular a Base de I.R. separada de outras verbas que são Base de Cálculo de IRRF porém não são base de Cálculo de Pensão |
| **Tipo** | Lógico |
| **Conteúdo Padrão** | .F. |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24830142550807)

Para que o cálculo da pensão considere apenas as verbas que fazem base para a pensão, o conteúdo dele deverá ficar com **.T.**

**Saiba mais**

[RH - Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004995674-RH-Pens%C3%A3o)

[Pensão alimentícia - base de IR com pagamento de bônus](https://tdn.totvs.com/pages/releaseview.action?pageId=701678020)
