---
article_id: 29721004131735
category: SIGAEST - CUSTOS
content_hash: 7f0f4fd8f30145ab6d1694e1261ed25034cbc588640b5d0b9654147a2b9da1cb
fetched_at: '2026-06-28T22:39:00.848285+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo do Complemento
  de Valor pela rotina EICDI154 quando envolve Armazém CQ
type: support-article
updated_at: '2025-03-12T12:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29721004131735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-do-Complemento-de-Valor-pela-rotina-EICDI154-quando-envolve-Armaz%C3%A9m-CQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29720994136983) Tempo aproximado para leitura: **00:05:10 min** **Dúvida**

Como incluir o complemento de Valor originado pela rotina EICDI154 quando a nota origem foi direcionada ao Armazém de Qualidade (MV\_CQ) de forma que o Custo seja apropriado ao Armazém Padrão?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para esses casos específicos, no módulo SIGAEIC na rotina de Complemento de Valor (EICDI154) ao efetuar uma movimentação valorizada, deve-se informar o **Armazém de Destino *diferente* do MV\_CQ**, devido o Armazém de CQ ter o conceito de Armazém segregado e no padrão não tem tratamento para Baixa do Valor da despesa pela rotina EICDI154.

O Armazém de CQ representa o local de inspeção de qualidade da empresa, onde o produto fica segregado ou isolado do restante do estoque durante a analise e seu custo não fará parte do custo do estoque.

As movimentações de entrada valorizadas pelas rotinas MATA241 e EICDI154 ficarão segregadas nesse Armazém. **Para que isso não ocorra**, deve-se informar nas rotinas sempre o **Armazém destino que não seja o MV\_CQ**. Veja o print com exemplo abaixo e também consta anexo um vídeo com exemplo do fluxo.

![inline1479972665.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29721906220311)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque)

[Complemento de Valor para itens do Processo de Importação (SIGAEIC)](https://tdn.totvs.com/x/w7oKDg)
