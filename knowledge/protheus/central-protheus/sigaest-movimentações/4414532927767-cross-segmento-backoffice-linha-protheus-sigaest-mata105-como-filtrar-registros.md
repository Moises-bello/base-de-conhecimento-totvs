---
article_id: 4414532927767
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 7cfcf15aea10c744e350056f7833a4329f514141d387a7e4be88d861582394d7
fetched_at: '2026-06-28T22:38:55.686539+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Como filtrar
  registros por legenda?
type: support-article
updated_at: '2026-05-28T13:44:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414532927767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Como-filtrar-registros-por-legenda
---

No TOTVS Protheus, para inibir registros na rotina de Solicitação ao Armazém (MATA105) por filtro de legenda, utilize a expressão CP\_PREREQU = ' ' no filtro de expressão. É possível salvar e aplicar esse filtro para mostrar apenas solicitações não finalizadas, com regras específicas para cada status, como Pré-requisição gerada, Pendente, Em aprovação, Rejeitado e Ordem de Separação Gerada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40795177429527) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como inibir registros na rotina de Solicitação ao Armazém por filtro de legenda?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para efetuar filtros de Legenda na rotina de Solicitação ao Armazém (MATA105), basta efetuar um **Filtro de Expressão CP\_PREREQU = ' '** (com este espaço entre as aspas simples), conforme exemplo abaixo:

1. Na rotina de Solicitação ao Armazém, clique em "Filtrar" na parte superior direita:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414532826519)

2. Clique em Criar Filtro:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414521015319)

2. Selecione a opção "Expressão" e preencha a seguinte expressão abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414532862743)

3. Após preencher a expressão, clique em "Salvar":

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414532883479)

4. Após salvar, o usuário pode clicar em "Outras Ações" -> "Salvar" para fixar esse filtro. Após isso, basta marcar o filtro e clicar em "Aplicar Filtros Selecionados":

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414521095831)

5. Após isso, perceba que ele só filtrará Solicitações ao Armazém que ainda não foram finalizadas:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414532918935)

6. Regra de cada filtro e legenda na rotina Solicitação ao Armazém:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40795177430807)

**Pré-requisição gerada** -> !EMPTY(CP\_PREREQU) .AND. !CP\_STATSA $ 'BR' .AND. EMPTY(CP\_ORDSEP)

**Pendente** -> EMPTY(CP\_PREREQU) .AND. !CP\_STATSA $ 'BR'

**Em aprovação** -> CP\_STATSA == 'B'

**Rejeitado** -> CP\_STATSA == 'R'

**Ordem de Separação Gerada** -> !EMPTY(CP\_ORDSEP)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
