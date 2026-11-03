---
article_id: 8668630314519
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 08e26a16c2cdf4823a525d7fad980b7e236e5547bdbc9e06bfbbd2f543d7bf1a
fetched_at: '2026-06-28T22:38:32.855868+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Retorno com
  Tipo Pedido B- Utiliza Fornecedor sem configurar controle de Poder de Terceiro.
type: support-article
updated_at: '2022-09-06T10:58:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8668630314519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Retorno-com-Tipo-Pedido-B-Utiliza-Fornecedor-sem-configurar-controle-de-Poder-de-Terceiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como incluir pedido de Retorno com o Tipo de Pedido B- Utiliza Fornecedor sem configurar controle de Poder de Terceiro.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**Acesse a rotina Pedido de Venda MATA410 e clique em Incluir, e siga passos abaixo:  
  
1º Campo Tipo Pedido informe B-Utiliza Fornecedor;  
  
2º Campo Fornecedor informe o mesmo que está no Documento de Entrada;  
  
3º Campo Produto, Quantidade e Preço Unitário, conforme está no Documento de Entrada;  
  
4- Campo TES informe o código da TES do Retorno;  
Obs:  Não utilize TES que a CFOP é de finalidade de Devolução, isto por que o tipo de pedido não é devolução, e a Sefaz vai criticar que tipo pedido e a CFOP estão com finalidades diferentes.

5- Preencher manualmente os campos NF Origem, Serie e Item, conforme esta no Documento de Entrada:  
Exemplo de como localizar estas informações:  
  
![pp01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8668231126807/pp01.png)

**OBS: Este processo de retorno é para quando a Nota de Entrada está lançado na rotina Documento de Entrada (MATA103) sem o controle de Poder de Terceiro(F4\_PODER3=R), e que na Nota de Saída de retorno gere informação da chave da nota origem na Tag refNFe.**
