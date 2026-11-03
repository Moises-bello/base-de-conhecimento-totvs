---
article_id: 37340103242903
category: SIGAACD - Automação e Coleta de Dados
content_hash: bffaf7c6b8ebfff522625ff42a220a69f35a7f7bac85e34e9d3f065ab3521808
fetched_at: '2026-06-28T22:39:12.673707+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Criação de Mestre
  de Inventário por Endereço, contagem com divergência como corrigir?
type: support-article
updated_at: '2025-12-30T13:37:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37340103242903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Cria%C3%A7%C3%A3o-de-Mestre-de-Invent%C3%A1rio-por-Endere%C3%A7o-contagem-com-diverg%C3%AAncia-como-corrigir
---

O artigo explica como corrigir divergências em contagens no mestre de inventário por endereço com duas contagens no TOTVS Protheus. O procedimento envolve criar o mestre, realizar a primeira contagem via emulador Tera Term, monitorar as quantidades, continuar com um segundo operador para a segunda contagem e finalizar com uma terceira contagem para ajustar as divergências. Links adicionais sobre inventário e automação são fornecidos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103236247) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como corrigir uma contagem com divergência, no mestre de inventário por endereço gerando duas contagens?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para criar um  Mestre de Inventário por Endereço, com duas contagens e a mesma ficar com divergência, como devemos corrigir essa tratativa, nesse caso é realizado o procedimento abaixo:

1. Criação do Mestre de Inventário por Endereço com duas contagens;![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103237015)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089992983)
2. Acessar o emulador do Tera Term na opção de inventário, realizando a primeira contagem;![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089993623)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103237655)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089994519)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103238679)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103239959)
3. Clico em outras ações Monitor e apresenta duas quantidades da primeira contagem;![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103240087)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103240215)
4. Volto no emulador, com outro operador para dar andamento na contagem na segunda contagem com a terceira contagem, para finalizar o mestre.![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089998103)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340103240343)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089999127)

   As contagens ficou divergente de cada operador, acessando novamente o Monitor.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089999383)
5. Continuando a contagem com o segundo operador, informo mais uma contagem de quantidade um, para ficar iguais as contagens no Monitor;![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089999127)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340089999639)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340196707863)
6. Para finalizar o mestre de inventário, é necessário uma terceira contagem, para bater as contagens;![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340171830423)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37340196712343)

Segue um boletim explicando o conceito das contagens batidas:

[Inventário por Produto (ACDV035-SIGAACD)](https://tdn.totvs.com/pages/releaseview.action?pageId=780791398)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
