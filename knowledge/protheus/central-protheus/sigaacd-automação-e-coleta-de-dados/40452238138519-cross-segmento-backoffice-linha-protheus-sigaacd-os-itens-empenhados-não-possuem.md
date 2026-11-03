---
article_id: 40452238138519
category: SIGAACD - Automação e Coleta de Dados
content_hash: ab4c04af9c045449d0c2477eed39d8972c6c8a4bcf0632cbfea16df6d7f1c6ce
fetched_at: '2026-06-28T22:39:13.636501+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Os itens empenhados
  não possuem saldo em estoque suficiente para a produção de uma unidade do produto
  da OP
type: support-article
updated_at: '2026-05-13T22:25:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40452238138519-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Os-itens-empenhados-n%C3%A3o-possuem-saldo-em-estoque-suficiente-para-a-produ%C3%A7%C3%A3o-de-uma-unidade-do-produto-da-OP
---

Ao gerar uma Ordem de Separação por OP e aparecer a mensagem "Os itens empenhados não possuem saldo em estoque suficiente para a produção de uma unidade do produto da OP", deve-se configurar o parâmetro MV\_CBRQEST, que define se a estrutura do produto é considerada no saldo para a geração da ordem (.T. para considerar, .F. para não considerar).

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40452238132375) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao gerar uma Ordem de Separação por OP, apresenta a mensagem " Os itens empenhados não possuem saldo em estoque suficiente para a produção de uma unidade do produto da OP" como corrigir?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para correção do Help apresentado "Os itens empenhados não possuem saldo em estoque suficiente para a produção de uma unidade do produto da OP", é necessário configurar o parâmetro da imagem abaixo:

|  |  |
| --- | --- |
| MV\_CBRQEST | Considera a estrutura do produto x saldo na geração da ordem de separação.   * .T. - Considera * .F. - Não |

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Parâmetros (SX6) - Automação e Coleta de Dados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
