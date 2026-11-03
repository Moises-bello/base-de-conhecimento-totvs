---
article_id: 11954595205783
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 455f9ed0af8a709159fbc1cee5b9a2cab238918aae282e02830609d1cd14444c
fetched_at: '2026-06-28T22:42:43.368074+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - HELP: O produto não está disponível
  para uso'
type: support-article
updated_at: '2023-02-24T13:10:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11954595205783-Manufatura-Linha-Protheus-SIGAPCP-HELP-O-produto-n%C3%A3o-est%C3%A1-dispon%C3%ADvel-para-uso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:53 min****Ocorrência**Ao tentar incluir um produto na rotina **MATA010 - Cadastro de produtos** é apresentada a mensagem **O produto não está disponível para uso.**

**![Imagem.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11954402552983)**

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**O Sistema identificou uma família cadastrada no **MATA093 - Configurador de Produtos**, com parte ou a totalidade do código informado.  
  
**Solução**Para solucionar essa ocorrência, acesse a rotina **MATA093** e veja se procede a(s) família(s) cadastradas com parte ou a totalidade desse código. Caso proceda, será necessário cadastrar o produto com outro código.  
  
**Exemplo**Ao tentar cadastrar um produto com o código ABC012 é apresentada a mensagem, isso indica que no **MATA093** existe família com o código A, AB, ABC, ABC, ABC0, ABC01 ou ABC012.
