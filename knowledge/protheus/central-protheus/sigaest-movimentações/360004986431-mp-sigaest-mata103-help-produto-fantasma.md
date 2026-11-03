---
article_id: 360004986431
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 186af886c049a0b315d1abe358079429b7599f7f6aab38c6b670f22aec1fc0ca
fetched_at: '2026-06-28T22:38:54.187048+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: 'MP - SIGAEST - MATA103 - HELP: PRODUTO FANTASMA'
type: support-article
updated_at: '2022-11-09T21:07:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004986431-MP-SIGAEST-MATA103-HELP-PRODUTO-FANTASMA
---

**Dúvida**O que fazer quando o *Protheus* gera a mensagem de help "PRODUTO FANTASMA" na inclusão de Documento de entrada (MATA103)?  
  
**Ambiente**  
Protheus – Estoque – A partir da versão 11.80  
  
**Solução**Qualquer movimentação com produto no qual o campo **B1\_FANTASMA = Sim**, ocorrerá este HELP.

Para este caso proceder com a seguinte forma:

- Tornar o sistema exclusivo e alterar o campo B1\_FANTASMA para "Não";

- Realizar a entrada da nota;

- Ajustar novamente o produto  campo B1\_FANTASMA para "Sim".

O conceito do produto fantasma é somente para estrutura do produto, não podendo ser efetuado nenhuma movimentação no mesmo, seja entrada, saída, ou movimentações internas, inclusive de OP.  
Caso queira fazer qualquer tipo de movimentação, o campo B1\_FANTASMA deve configurá-lo como "Não".

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
