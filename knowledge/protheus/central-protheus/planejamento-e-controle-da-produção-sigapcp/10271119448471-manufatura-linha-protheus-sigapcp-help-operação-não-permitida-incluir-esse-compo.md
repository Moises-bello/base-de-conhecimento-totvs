---
article_id: 10271119448471
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b107a34f5a288dab7e16cf45e7baf1af8605e02cd043641d28f89ba37492bfe8
fetched_at: '2026-06-28T22:42:43.371819+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - HELP: Operação não permitida. Incluir
  esse componente causará recursividade na estrutura'
type: support-article
updated_at: '2023-11-30T19:38:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10271119448471-Manufatura-Linha-Protheus-SIGAPCP-HELP-Opera%C3%A7%C3%A3o-n%C3%A3o-permitida-Incluir-esse-componente-causar%C3%A1-recursividade-na-estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19461209270295) Tempo aproximado para leitura: **00:00:27 min****Ocorrência**Ao tentar incluir um componente na estrutura no **PCPA200 - Estrutura** é apresenta a mensagem **Operação não permitida. Incluir esse componente causará recursividade na estrutura**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10271035888663)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Incluindo um produto numa estrutura onde o mesmo já é Pai do componente.  
  
**Solução**Avaliar o componente informado, pois não pode ter o componente igual ao produto pai independente do nível e revisão.  
  
**Exemplo:**  
Estrutura cadastrada:  
PRODUTO00013  
            |  
PRODUTO00014  
            |  
PRODUTO00015  
  
Selecionar o produto PRODUTO00014, clicar em **Alterar**.  
Ao tentar incluir o produto PRODUTO00013 abaixo no produto PRODUTO00015 a mensagem será apresentada.
