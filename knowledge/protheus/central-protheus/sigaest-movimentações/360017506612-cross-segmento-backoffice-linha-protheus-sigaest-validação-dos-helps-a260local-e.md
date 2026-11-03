---
article_id: 360017506612
category: SIGAEST - MOVIMENTAÇÕES
content_hash: d1f926b332e38a711a512aadcffe9415f86b9ec0d1f788ee66ba51cb2603ec03
fetched_at: '2026-06-28T22:38:58.454204+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação dos Helps
  A260LOCAL e A241LOCAL  em Movimentos Internos
type: support-article
updated_at: '2026-06-16T21:33:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017506612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-dos-Helps-A260LOCAL-e-A241LOCAL-em-Movimentos-Internos
---

O sistema apresenta os Helps A260LOCAL e A241LOCAL ao cadastrar um novo item e realizar movimentação interna quando o produto não possui relacionamento com o armazém informado. Para resolver, crie esse vínculo na rotina MATA220 ou configure o parâmetro MV\_VLDALMO = N para criar o armazém na movimentação. Problemas com execauto da rotina MATA261 podem exigir ajustes no código para considerar espaços.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30249042868631)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Ao cadastrar um novo item e realizar uma movimentação interna, o sistema apresenta os Helps **A260LOCAL e A241LOCAL**. Como resolver?

![a260local.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30249058381591)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Pode-se ainda configurar o parâmetro **MV\_VLDALMO = N** para que o armazém seja criado no momento da movimentação, não validando a existência do mesmo na tabela SB2 (Saldos Físico e Financeiro).

O help assistente A260LOCAL será exibido, caso o produto em questão não possua relacionamento com o armazém informado na movimentação.  
  
Deve-se criar o relacionamento entre Produto X Armazém através da rotina Saldos em estoque **MATA220** no caminho (Atualizações - Saldos - Inicial ), informando produto e armazém.

### 

### **O HELP em questão esta ocorre com o uso do Execauto da rotina MATA261?**

Caso esse HELP ocorra com o execauto da rotina MATA261 : [Cross Segmento - Backoffice Linha Protheus - ADVPL - Exemplo execauto MATA261](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022885712-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Exemplo-execauto-MATA261)

Mas não ocorra no "padrão", que seria o uso da rotina em si, verificamos internamente em conjunto com um de nossos clientes, que esse ponto pode ser fator de uso indevido das condições do proprio execauto, como por exemplo o uso de sentenças no codigo do produto, a serem ou não deconsiderados "espaços" para achar o registro de origem ou destino.

**Relacionado:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP BLOQLOC5 em movimento de Transferência entre armazéns - Causa e Correção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020275791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-BLOQLOC5-em-movimento-de-Transfer%C3%AAncia-entre-armaz%C3%A9ns-Causa-e-Corre%C3%A7%C3%A3o)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Movimentações do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
