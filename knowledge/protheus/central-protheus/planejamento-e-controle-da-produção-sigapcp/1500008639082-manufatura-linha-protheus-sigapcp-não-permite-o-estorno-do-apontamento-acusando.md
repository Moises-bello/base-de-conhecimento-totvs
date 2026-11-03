---
article_id: 1500008639082
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 34482ba12288ae42bf06f638b8f1f0f5f1b2b06102b55ee954937018f7cb593a
fetched_at: '2026-06-28T22:42:44.602304+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não permite o estorno do apontamento
  acusando que o saldo ficará negativo
type: support-article
updated_at: '2026-02-27T21:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008639082-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-permite-o-estorno-do-apontamento-acusando-que-o-saldo-ficar%C3%A1-negativo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38699521475223)*** Tempo aproximado para leitura: **00:02:12 min**  
  
**Ocorrência**  
Ao tentar estornar um apontamento de produção o Sistema não permite informando que o produto ficaria com o saldo negativo no armazém, impedindo a operação, mesmo havendo saldo disponível no momento.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**  
Existem duas causas principais para este comportamento:  
No momento do estorno o Sistema pode validar a posição do estoque no dia em que foi feito o apontamento de produção, e se ao término desse dia o saldo for menor do que a quantidade a ser estornada, essa mensagem é apresentada ao usuário.  
Essa situação ocorre quando o parâmetro **MV\_TPSALDO - Tipo de saldo a ser considerado nos movimentos internos** possui o conteúdo **C**  
  
Diferença entre a quantidade registrada no movimento **SD3 - Movimentações Internas** e o saldo atual na tabela de saldos **SB2 - Saldos físicos e financeiros**. Se a **SD3** possuir mais casas decimais ou um valor arredondado para cima em relação à **SB2**, o sistema entende que você está tentando estornar uma quantidade maior do que a existente.  
  
**Solução**  
Neste caso, verifique primeiramente qual a data deste apontamento, esta informação está no campo **D3\_EMISSAO - Data da emissão** e veja qual a posição do estoque neste dia.  
  
Caso o saldo por data esteja correto, verifique se há resíduo de cálculo nos decimais. Verifique o campo **D3\_QUANT** - **Quantidade** na tabela **SD3** e compare com o campo **B2\_QATU - Saldo Atual** na **SB2**. Se a **SD3** estiver com mais decimais exemplo 216,08333 que a **SB2** 216,083, ajuste o registro da **SD3**para igualar ao valor da **SB2**.  
  
Após o ajuste do movimento para 216,083, realize o estorno novamente.
