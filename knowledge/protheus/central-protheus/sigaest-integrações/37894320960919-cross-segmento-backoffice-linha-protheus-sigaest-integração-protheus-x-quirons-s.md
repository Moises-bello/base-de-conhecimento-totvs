---
article_id: 37894320960919
category: SIGAEST - INTEGRAÇÕES
content_hash: 40c12b43ac2d0af335313c9992564881063a79c9d6d4c0caf3607749329d96b5
fetched_at: '2026-06-28T22:38:46.130438+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - INTEGRAÇÃO Protheus
  x Quirons: STOCKLEVEL Não efetua o filtro informado no campo de condição'
type: support-article
updated_at: '2026-01-23T20:04:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37894320960919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-INTEGRA%C3%87%C3%83O-Protheus-x-Quirons-STOCKLEVEL-N%C3%A3o-efetua-o-filtro-informado-no-campo-de-condi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37894320944663) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
Como efetuar o filtro no adapter da MATI225 - STOCKLEVEL no campo de condição?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**  
O Adapter MATI225 - STOCKLEVEL é o adapter responsável por enviar as informações do estoque atual ao QUirons, nos casos em que se faz necessário efetuar um filtro de tipo de produto ou armazém para evitar que produtos que não são utilizados no Quirons sejam enviados.  
  
Para este tipo de necessidade, existem dois cenários possiveis  
  
**Cenário 1:**  
**Filtro Efetuado durante a carga inicial**

Se houver necessidade de filtrar os registros pode se utilizar da seguinte forma:

O campo **Condição (XX4\_EXPFIL)**, Campo que pode receber uma expressão ou ainda uma função advpl, considerando a tabela **SB1** (Descrição Genérica do Produto) e seus respectivos campos. Em ambos os casos, é esperado um resultado lógico deste campo com conteudo verdadeiro para o registro posicionado seja processado.

Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37894290945431)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37894290946327)

**TDN de Apoio:** [**Integração | Protheus x Quírons |**](https://%20https://tdn.totvs.com/x/tKL0Jg%20)

O campo **Expressão SQL (XX4\_EXPSQL)** – Campo que pode receber uma expressão SQL. Esse filtro será executado juntamente com a condição do campo XX4\_EXPFIL, caso esteja preenchido.

Documentação:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37894320948503)

**Cenário 2:**  
**Filtro Efetuado durante a execução da rotina**

Se houver necessidade de filtrar os registros pode se utilizar da seguinte forma:

O campo **Condição (XX4\_EXPFIL)**, Campo que pode receber uma expressão ou ainda uma função advpl, considerando a tabela **SB2** (Saldos Físico e Financeiro) e seus respectivos campos.. Em ambos os casos, é esperado um resultado lógico deste campo com conteudo verdadeiro para o registro posicionado ser processado.  
  
Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37894290949143)

**TDN de Apoio:** [**Integração Adapter Protheus - MATI225 - Consulta Saldo em Estoque (StockLevel) a partir da versão 3.000**](https://tdn.totvs.com/x/DjvAOg)

**IMPORTANTE:** Para realizar envio de produtos que tiveram o estoque alterado com base no último envio é necessário a configuração do SCHEDULE do SCHEDESTMG, conforme documentação abaixo:   
[Envio Ativo para Produtos com Estoque Alterado Desde o Último Envio](https://tdn.totvs.com/x/2WQcEQ)

**Saiba mais:**  
<https://tdn.totvs.com/display/public/framework/A+camada+do+EAI>  
[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
