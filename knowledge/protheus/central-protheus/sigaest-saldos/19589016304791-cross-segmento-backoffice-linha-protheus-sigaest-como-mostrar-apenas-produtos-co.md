---
article_id: 19589016304791
category: SIGAEST - SALDOS
content_hash: 7bd104624d5df3b17c6280cd72c4f2a4db4dd53e78ab72727f9cb277252280c3
fetched_at: '2026-06-28T22:39:14.812488+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Mostrar apenas
  produtos com Saldo em Estoque (Sem produtos zerados) no relatório MATR260
type: support-article
updated_at: '2023-12-05T20:50:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19589016304791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Mostrar-apenas-produtos-com-Saldo-em-Estoque-Sem-produtos-zerados-no-relat%C3%B3rio-MATR260
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19588966603159) Tempo aproximado para leitura: **00:02:00 min****Dúvida**

O que fazer quando ao mostrar produtos com saldo em estoque é apresentado zerado no relatório MATR260?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.

**Solução**

Realizar as seguintes validações no produto em questão:

* Verificar no cadastro do produto(MATA010)  na aba Cadastrais se o produto utiliza segunda unidade de medida cadastrada, conforme o Print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19589068461207)

* Caso não utilize segunda unidade de medida, alterar o parâmetro **"QTDE. na 2a.UM. ? = NÃO"** acessando a opção **"Outras Ações/Parâmetros"** conforme o Print do relatório MATR260.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19589005536023)

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*
