---
article_id: 16746167374871
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5a132b2d56ba224f62c3afda642c764d226d3d86d00e75d3de16d55699ee536b
fetched_at: '2026-06-28T22:42:44.512035+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MATA638COMPSQ
type: support-article
updated_at: '2023-08-14T21:16:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16746167374871-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MATA638COMPSQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16746158363287) Tempo aproximado para leitura: **00:01:08 min****Ocorrência**Ao tentar vincular um componente com uma operação na rotina **MATA637 - Operação x Componente** é apresentada a mensagem **MATA638COMPSQ - Não existe o componente na sequência informada**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Essa mensagem é apresentada quando na rotina **PCPA200 - Manutenção de estruturas** não há o cadastro deste componente e sequência que se pretende relacionar para o produto em questão  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **PCPA200** e consulte a estrutura do produto e veja se esse componente está relacionado no campo **G1\_COMP - Componente** e qual o conteúdo do campo **G1\_TRT - Sequência** desse registro;  
2. Na rotina **MATA637** preencha no campo **GF\_COMP - Componente** o código do componente e no campo **GF\_TRT - Sequencia** o mesmo código do campo **G1\_TRT** observado no passo 1.
