---
article_id: 14873920258327
category: eSocial - Eventos Totalizadores
content_hash: 8c6e6711e77b820f91bc6effe656f0285d7fa7c37450fb2f4c9d3433dcf490a9
fetched_at: '2026-06-28T22:47:07.023773+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP - eSocial - Código de Receita relativo ao Imposto de Renda Retido
  na Fonte sobre rendimentos do trabalho
type: support-article
updated_at: '2025-07-02T13:51:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14873920258327-RH-RM-FOP-eSocial-C%C3%B3digo-de-Receita-relativo-ao-Imposto-de-Renda-Retido-na-Fonte-sobre-rendimentos-do-trabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18491213548183) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como o governo valida o Código da Receita relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.34.263, 12.1.2205.211, 12.1.2209.155 e superiores  
  
**Solução**Com a publicação do leiaute *S-*1.1, o governo começou a retornar o **código de receita** relativo ao IRRF sobre rendimentos do trabalho. A informação é retornada no evento totalizador **S-5002**, após o evento **S-1210** ser enviado e recepcionado pelo governo.

A informação será identificada no XML **S-5002** através da *tag* **CRMen**, conforme consta no leiaute*.*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14873805975831)

O governo irá validar algumas informações para retornar um dos códigos de receita supracitados. Abaixo as validações conforme leiaute.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14874427108503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14873943463703)

Caso o funcionário seja residente no exterior, o governo retornará a informação na tag CRDia com o código abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14964399124759)

**Saiba mais**Para mais informações, acesse:  
     - [Novidades eSocial](https://tdn.totvs.com/display/LRM/Novidades+eSocial+-+Linha+RM)  
     - [Como exportar XML de retorno do Governo no Middleware](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6214979985175-RH-RM-FOP-eSocial-Middleware-Como-exportar-XML-de-retorno-do-Governo-)   
     - [Como acessar a rotina de IRRF por Trabalhador no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037640414-Automa%C3%A7%C3%A3o-Fiscal-Totalizadores-S-5002-Como-acessar-a-rotina-de-IRRF-por-Trabalhador)   
     - [Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432-RH-RM-FOP-eSocial-Contato-com-o-Governo-para-d%C3%BAvidas-sobre-os-eventos-do-eSocial#:~:text=O%20telefone%20da%20Central%20de%20Atendimento%20%C3%A9%200800%2D730%2D0888)
