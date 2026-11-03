---
article_id: 33028490079767
category: SIGAEST - CUSTOS
content_hash: cba08d3fe94b4762e34e201180c504cda3902a930b8a5fb97d6bb4d23371f81a
fetched_at: '2026-06-28T22:39:02.312312+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Posso contabilizar
  movimentos de estorno no estoque?
type: support-article
updated_at: '2025-06-24T20:08:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33028490079767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Posso-contabilizar-movimentos-de-estorno-no-estoque
---

Movimentos internos com o campo **D3\_ESTORNO = 'S'** indicam que foram cancelados ou desfeitos, portanto **não devem ser contabilizados nem considerados no cálculo de custo médio**. Além disso, ao processar a rotina de custo com a opção de excluir estornos, esses registros são removidos localmente, reforçando que **não há validade operacional para contabilização de estornos**.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33028471130775) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
É possível contabilizar um movimento interno que foi estornado, ou seja, com o campo D3\_ESTORNO = 'S'?   
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Movimentos internos que foram estornados, identificados pelo campo **D3\_ESTORNO = 'S',** não são contabilizados e nem considerados nos cálculos de custo.   
  
Isso ocorre porque um movimento estornado representa uma operação desfeita ou cancelada, como por exemplo uma requisição que foi revertida. Dessa forma, não há sentido operacional ou fiscal em efetuar a contabilização de eventos que já foram invalidados.   
  
Além disso, caso a rotina de cálculo de custo médio seja processada com a opção de **\*apagar estornos = sim\***, os lançamentos estornados são excluídos localmente durante o processamento, reforçando que essas movimentações não integram o histórico válido do estoque para fins de custo ou contabilização.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Erro de aplicação na thread de Contabilização*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001884321-MP-SIGAEST-MATA330-Erro-de-aplica%C3%A7%C3%A3o-na-thread-de-Contabiliza%C3%A7%C3%A3o)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
