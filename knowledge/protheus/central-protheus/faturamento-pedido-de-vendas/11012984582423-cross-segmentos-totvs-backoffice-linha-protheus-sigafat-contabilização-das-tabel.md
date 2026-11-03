---
article_id: 11012984582423
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0a72fccef7ef849136c0e16eebfcb7cceddec07eee402a0f72894ee0cd7e91a6
fetched_at: '2026-06-28T22:38:42.641037+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Contabilização
  das tabelas fiscais via faturamento
type: support-article
updated_at: '2024-01-22T14:33:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11012984582423-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Contabiliza%C3%A7%C3%A3o-das-tabelas-fiscais-via-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20536778519575) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como contabilizar as tabelas fiscais via Faturamento (SFT e SF3)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Os LPs 610 e 620 são destinados a contabilização de itens do Documento de Saída (SD2) e do cabeçalho do Documento de Saída (SF2), logo os ponteiros de tabelas estarão nestes registros, assim, o ponteiramento de qualquer outra tabela deve ser feito através de uma sintaxe.

Os Lançamento Padronizados podem ser ajustados de acordo com a regra necessária para a contabilização, podendo inclusive ser utilizadas funções em seus campos macro executáveis, logo podem ser consultados registros de outras tabelas através de funções como a **Posicione()**, que retorna o dado desejado, ou através de uma "**Função de usuário**" que em seu retorno devolva a informação a ser processada.

Para exemplos de utilização dos LPs do Documento de Saída para contabilização dos impostos, verifique a documentação:

* [Contabilização dos Impostos no Documento de Saída](https://tdn.totvs.com/x/kxnyM)
