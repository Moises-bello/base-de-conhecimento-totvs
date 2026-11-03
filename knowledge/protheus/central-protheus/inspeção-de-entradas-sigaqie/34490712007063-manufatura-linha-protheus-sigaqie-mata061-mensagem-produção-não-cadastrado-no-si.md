---
article_id: 34490712007063
category: Inspeção de Entradas (SIGAQIE)
content_hash: b76a2f1f1ae1fb4d648d58c95fc11ffe046d35f031950ce310062dbbf46620c5
fetched_at: '2026-06-28T22:42:27.067007+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - MATA061 - Mensagem Produção não cadastrado
  no SIGAQIE
type: support-article
updated_at: '2025-08-27T18:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34490712007063-Manufatura-Linha-Protheus-SIGAQIE-MATA061-Mensagem-Produ%C3%A7%C3%A3o-n%C3%A3o-cadastrado-no-SIGAQIE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34490684330135) Tempo aproximado para leitura: **00:01:59 min**  
  
**Dúvida**  
Qual a causa da mensagem **Produto não cadastrado no SIGAQIE** exibida na rotina **MATA061 - Atualização Produto x Fornecedor**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Causa**  
A mensagem ocorre quando o parâmetro **MV\_QPESQE6 - Define se a pesquisa via F3 na rotina de Amarração Produto x Fornecedor, será realizada nas Especificações (QE6) ou no cadastro de Produtos (SB1)** está como *T-True*.  
  
**Solução**  
Se o conteúdo do parâmetro for **T**, a rotina **MATA061** irá pesquisar se o produto informado está cadastrado na tabela **QE6 - Especificação do Produto** da rotina **QIEA010 - Especificação do Produto,** caso contrário, com o parâmetro como *F-False*, a pesquisa será somente na tabela **SB1 - Produtos**, sem validar a especificação do produto.
