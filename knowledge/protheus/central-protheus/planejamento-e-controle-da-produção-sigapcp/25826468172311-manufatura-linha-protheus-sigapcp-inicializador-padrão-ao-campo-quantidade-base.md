---
article_id: 25826468172311
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b026953d6232068420ef5b0459719b5e0bd5b5b0846bb83345569b8eec651510
fetched_at: '2026-06-28T22:42:43.419866+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Inicializador padrão ao campo quantidade
  base
type: support-article
updated_at: '2024-08-22T19:02:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25826468172311-Manufatura-Linha-Protheus-SIGAPCP-Inicializador-padr%C3%A3o-ao-campo-quantidade-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25826508069783) Tempo aproximado para leitura: **00:00:55 min** **Dúvida**Como definir um inicializador padrão para a variável **nQtdBase** que é apresentada no **PCPA200**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O campo relacionado à variável **nQtdBase** é o **B1\_QB**, da tabela **SB1**, sendo assim a sugestão é definir um inicializador padrão para o campo **B1\_QB**.  
Desse modo, ao cadastrar um novo produto o campo **B1\_QB** é preenchido e ao incluir a estrutura para esse item essa informação é apresentada na variável **nQtdBase** da rotina **PCPA200**, e utilizada no cálculo da necessidade dos componentes ao gerar os empenhos.  
  
**Glossário  
nQtdBase** - Quantidade Base  
**PCPA200** - Estrutura dos produtos  
**SB1** - Descrição genérica do produto   
**B1\_QB** - Quantidade base da estrutura
