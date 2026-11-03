---
article_id: 360061630273
category: SIGAEST - INVENTÁRIO
content_hash: c4413a91ca9ebab11965e776dc7230452db30ceeb93eff23aeffc5d4a74ee2bb
fetched_at: '2026-06-28T22:38:50.378464+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - MV_CONTINV
  múltiplas contagens de inventário por seleção de contagem
type: support-article
updated_at: '2025-12-04T18:01:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061630273-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-MV-CONTINV-m%C3%BAltiplas-contagens-de-invent%C3%A1rio-por-sele%C3%A7%C3%A3o-de-contagem
---

**Dúvida**  
Como efetuar múltiplas contagens de inventário no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

***Sugestão*****:** Assista também o ***Webinar sobre o processo padrão de inventário*** no Protheus, [***clique aqui***](https://www.youtube.com/watch?v=x-UMZkr8ukA).  
  
**Exemplo de utilização:**  
Opção de digitação do inventário em várias contagens. Poderá ser selecionada qual contagem  
escolhida para processar o acerto. Ou seja, mais de um usuário efetua a contagem do inventário para que sejam comparadas.

Com o parâmetro desabilitado (MV\_CONTINV = .F.) , todas as contagens são somadas, nesse caso ver o outro artigo sobre [o inventário padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-MP-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque?source=search).

**1.** **Habilitar o parâmetro MV\_CONTINV = .T.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001240502)

**2.** **Na rotina digitação do inventário (MATA270) digitar a primeira contagem para o produto, Armazém e data informados;**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100147774)![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100147754)

**3.** **Ainda na rotina digitação do inventário (MATA270) digitar a segunda contagem para o produto, Armazém e data informados;**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001241262)![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100147874)

**4.** **Na rotina digitação de inventario (MATA270), observe que a legenda esta vermelha, indicando que não foram selecionadas contagens. Selecionar a linha com algum dos documentos digitados, clicar em Outras Ações, e "Sel. contagem".**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100162934)

**5.** **Na tela de seleção de contagem, clicar no Checkbox indicando qual a quantidade correta para ajustes, em seguida clicar no botão Seleciona.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001329441)

**6.** **Após a seleção da contagem a legenda na tela inicial é alterada.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001258702)

**7.** **Em seguida na rotina PROCESSAMENTO DE INVENTÁRIO (MATA340), o sistema considerará somente a contagem selecionada considerando a data que foi informada no processamento.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001259002)

**Observações importantes:**

**1 -** Após o processamento de inventário, todas as contagens de um mesmo documento(B7\_DOC) e com mesma data(B7\_DATA), terão o campo **B7\_STATUS atualizado para 2- Processado**. (A atualização na SB2 ocorrerá somente para a contagem selecionada).

**2 -** Para os casos em que tenha diversas contagens, pode utilizar o relatório de DIVERGÊNCIAS DE CONTAGENS (MATR287) para facilitar a conferência das contagens em quais devem ser selecionadas para ajustes.

**3 -** Quando habilitado o parâmetro MV\_CONTINV não é possível utilizar o relatório MATR285, somente o MATR287;

**4 -** O relatório de DIVERGÊNCIAS DE INVENTÁRIO, exibe dados, apenas quando duas contagens forem diferentes, por exemplo. Contagem 001 quantidade 100 e Contagem 002 quantidade 200. Nesse caso, deve-se avaliar pela rotina MATA270 as contagens que **não** estão divergentes, é necessário revisar pela rotina MATA270 e selecionar item a item.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001334741)![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102347573)

**Saiba mais:**

[*Veja mais informações sobre inventário*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)
