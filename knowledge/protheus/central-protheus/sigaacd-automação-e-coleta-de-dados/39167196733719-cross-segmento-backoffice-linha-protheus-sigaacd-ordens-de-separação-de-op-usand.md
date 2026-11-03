---
article_id: 39167196733719
category: SIGAACD - Automação e Coleta de Dados
content_hash: 052548904d3994ba240ca3a8219e6d169111aaed22d63131fffe2fdf56a6a220
fetched_at: '2026-06-28T22:39:12.921697+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Ordens de Separação
  de OP usando produtos com indiretos (ACDA100 - SIGAACD)
type: support-article
updated_at: '2026-03-20T11:54:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39167196733719-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ordens-de-Separa%C3%A7%C3%A3o-de-OP-usando-produtos-com-indiretos-ACDA100-SIGAACD
---

A Ordem de Separação organiza a retirada de materiais para Ordens de Produção, mas produtos de apropriação indireta, usados conforme a necessidade, não têm quantidade fixa prevista. A Ordem de Separação só é gerada se houver saldo no armazém indicado; caso contrário, não será criada. Movimentações desses materiais ocorrem via movimento interno de estoque, não por Ordem de Separação.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39167220569879) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar uma Ordem de Separação por OP, com um produto de apropriação indireta?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

**01. VISÃO GERAL**

A Ordem de Separação de Materiais é um processo utilizado para organizar a retirada de materiais do estoque quando eles precisam ser utilizados em uma Ordem de Produção. Esta etapa da operação ajuda a garantir que os materiais necessários sejam separados no armazém correto antes de serem utilizados no processo produtivo.

No entanto, é importante entender algumas regras desse processo para materiais de apropriação indireta.

|  |
| --- |
| **O que é um produto de apropriação indireta?**    Um produto de apropriação indireta é um tipo de material utilizado na fabricação de outro produto, mas cuja quantidade exata de consumo não pode ser definida previamente. Isso acontece porque esses materiais são usados conforme a necessidade durante o processo de produção. Por exemplo, itens de apoio ao processo produtivo, como lubrificantes, materiais de limpeza ou pequenos insumos, podem variar de consumo de uma produção para outra. Por esse motivo, o sistema não trabalha com uma quantidade fixa prevista para esse tipo de material. |

## **02. EXECUÇÃO**

A Ordem de Separação somente será criada se existir saldo do material no armazém que foi definido no momento do empenho da Ordem de Produção.

Ou seja:

* Se o material tiver saldo disponível no armazém indicado no empenho, o sistema poderá gerar a Ordem de Separação.
* Se não houver saldo nesse armazém, a Ordem de Separação **não será gerada** para essa Ordem de Produção.

Essa verificação é importante para evitar que o sistema gere solicitações de separação de materiais que não estão disponíveis no estoque daquele local.

|  |
| --- |
| Importante    Outro ponto importante é que **materiais de apropriação indireta não são movimentados por meio de Ordem de Separação**.  A movimentação desses materiais dentro do sistema acontece através de um **movimento interno de estoque**, que registra a transferência ou utilização do material entre os armazéns ou locais internos da empresa.  Isso significa que, mesmo que exista um empenho para a Ordem de Produção, a baixa ou movimentação efetiva do material será registrada por esse tipo de movimento interno. |

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Ordens de Separação de OP usando produtos com indiretos (ACDA100 - SIGAACD)](https://tdn.totvs.com/pages/releaseview.action?pageId=1050306495)
