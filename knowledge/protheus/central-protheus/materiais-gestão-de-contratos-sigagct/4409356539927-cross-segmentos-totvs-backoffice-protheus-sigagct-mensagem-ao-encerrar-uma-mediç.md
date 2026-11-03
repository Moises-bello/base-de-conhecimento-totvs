---
article_id: 4409356539927
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 505d43a94d197517764668179bc5a7a60a0ba01a4413aeb91e6eb84d9ad3722b
fetched_at: '2026-06-28T22:37:23.893689+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Mensagem ao Encerrar
  uma Medição: Este pedido foi vinculado a um contrato e por isto não pode ter este
  campo alterado'
type: support-article
updated_at: '2021-09-24T20:17:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409356539927-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Mensagem-ao-Encerrar-uma-Medi%C3%A7%C3%A3o-Este-pedido-foi-vinculado-a-um-contrato-e-por-isto-n%C3%A3o-pode-ter-este-campo-alterado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 01:20

**Dúvida**

Ocorrência da Mensagem ao encerrar uma Medição:

Este pedido foi vinculado a um contrato e por isto não pode ter este campo alterado, apontando as tabelas SC5 e SC6 e a linha do produto como inválido

Exemplo: Produto - C6\_PRODUTO := 00000002 < -- Invalido

Este pedido foi vinculado a um contrato e por isto não pode ter este campo alterado.  
Tabela SC5 08/09/2021 09:59:13  
Tipo Pedido - C5\_TIPO := N  
Cliente - C5\_CLIENTE := 000158  
Loja Entrega - C5\_LOJAENT := 01  
Loja - C5\_LOJACLI := 01  
DT Emissao - C5\_EMISSAO := 08/09/2021  
Cond. Pagto - C5\_CONDPAG := 002  
Moeda - C5\_MOEDA := 1  
Num.Contrato - C5\_MDCONTR := 000000000000002  
Num.Medicao - C5\_MDNUMED := 000003  
Num.Planilha - C5\_MDPLANI := 000001  
Natureza - C5\_NATUREZ := 100105  
Taxa Moeda - C5\_TXMOEDA := 1  
Indenizacao - C5\_DESCONT := 0  
Despesa - C5\_DESPESA := 0  
Numero - C5\_NUM := 001224  
--------------------------------------------------------------------------------  
Tabela SC6 08/09/2021 09:59:13  
Erro no Item 1  
--------------------------------------------------------------------------------  
Num. Pedido - C6\_NUM := 001224  
Item - C6\_ITEM := 01  
Produto - C6\_PRODUTO := 00000002 < -- Invalido  
Descricao - C6\_DESCRI := GESTAO DE COMERCIALIZACAO DE E  
Quantidade - C6\_QTDVEN := 1  
Prc Lista - C6\_PRUNIT := 1000  
Prc Unitario - C6\_PRCVEN := 1000  
Vlr.Total - C6\_VALOR := 1000  
Entrega - C6\_ENTREG := 30/06/2021  
Unidade - C6\_UM := UN  
Cliente - C6\_CLI := 000158  
Loja - C6\_LOJA := 01  
Tipo Saida - C6\_TES := 611  
Armazem - C6\_LOCAL := 01  
Item Medicao - C6\_ITEMED := 001  
Vlr Desconto - C6\_VALDESC := 0  
C.Custo - C6\_CC :=  
C Contabil - C6\_CONTA := 310101005  
Item Conta - C6\_ITEMCTA :=  
Classe Valor - C6\_CLVL :=  
- CONTRA := 000000000000002  
Codigo - REV :=  
- NUMMED := 000003  
- NUMPLA := 000001  
- ITEMPL := 001  
- IDPED := 1  
- PARENV :=  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

Uma das possibilidades no qual  ocorre o erro, trata-se do campo C6\_ITEMED na aba uso, não estar informado com usado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409363639191/mceclip0.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409356731799/mceclip2.png)

**Para a correção: Marque o campo como usado.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409356687639/mceclip1.png)

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
