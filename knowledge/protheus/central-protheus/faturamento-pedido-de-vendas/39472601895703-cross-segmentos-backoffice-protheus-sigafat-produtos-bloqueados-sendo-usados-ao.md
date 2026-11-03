---
article_id: 39472601895703
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 4a3945014ee586777fb682b99fe26ca2a51688acacba02b2d088822a28aefa68
fetched_at: '2026-06-28T22:38:42.570996+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Produtos bloqueados sendo
  usados ao retornar
type: support-article
updated_at: '2026-04-02T20:25:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39472601895703-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Produtos-bloqueados-sendo-usados-ao-retornar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39472601868951) Tempo aproximado para leitura: 00:**01:30min**  
  
**Dúvida**  
Por que o sistema permite criar um pedido do tipo devolução para um item bloqueado durante o processo de Retorno do Documento de Entrada?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
Esse comportamento é nativo do sistema e ocorre devido à ordem das validações realizadas pela rotina de Retornar.

Ao utilizar o processo de retorno a partir de um Documento de Entrada, o sistema amarra a nota de origem antes de realizar a busca e a validação do status atual do produto. Como o item foi inserido no Documento de Entrada original sem impeditivos (ou seja, o bloqueio do produto foi aplicado posteriormente à entrada), o sistema compreende que a operação de retorno é válida para aquele documento específico.

Em contrapartida, durante a inclusão manual de um pedido, o bloqueio impede o uso do produto. Isso acontece porque não é possível vincular o documento de origem (campo C6\_NFORI) antes da inserção e validação das regras do produto na interface.

Desta forma, a função de retornar atua corretamente ao permitir a transação para produtos cuja entrada original ocorreu sem bloqueios prévios.
