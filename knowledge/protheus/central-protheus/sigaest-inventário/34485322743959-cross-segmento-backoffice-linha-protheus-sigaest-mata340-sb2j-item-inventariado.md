---
article_id: 34485322743959
category: SIGAEST - INVENTÁRIO
content_hash: 012522c05b92e25fb6a48460c083edf0a9c55c10e1182f1d9b4aaeed152cc6e8
fetched_at: '2026-06-28T22:38:50.414814+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - SB2J - >
  Item inventariado em data superior
type: support-article
updated_at: '2025-08-28T11:29:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34485322743959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-SB2J-Item-inventariado-em-data-superior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34485310843415) Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**  
No módulo de **Estoque e Custos**, ao tentar processar documentos no inventário ocorre o a validação **SB2J**, que apresenta a seguinte mensagem no relatório de Itens não inventariados:  
**"Item inventariado em data superior"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34507880307351)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - todas as versões  
  
**Causa**  
O erro **SB2J** ao processar o inventário, ocorre porque já foi processado anteriormente uma digitação desse produto com **data posterior** à data que está sendo processado.  
  
**Solução**  
Para que seja possível inventariar o produto nessa data tendo inventário posteriores, é necessário estornar as movimentações desses inventários posteriores na rotina MATA241.

Você pode ver a ultima data de inventário processado para o produto na rotina de Saldo em Estoque(MATA225) no campo Dt.Invent (**B2\_DINVENT**).

Uma vez identificado o movimento com data posterior, estornar o inventário através da rotina **Movimento Múltiplo (MATA241)**. É importante alterar o parâmetro **F12** da rotina para que o estorno seja **Por Item**. Ao confirmar o estorno do inventário na rotina MATA241, será exibida uma mensagem para confirmar se a data do inventário deve ser mantida ou excluída. Neste caso, não é necessário manter a data do inventário, portanto, ela deve ser removida para limpar essa data de inventário superior. Após realizar este procedimento, o inventário pode ser processado novamente com a data que deseja.

**Saiba mais:**  
[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar o estorno (exclusão) de movimento de Inventário?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402384407063)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-)

[*MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data calculada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada?source=search)

[*MP - SIGAEST - MATA271 - Bloqueio de produtos para inventário por data informada*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-MP-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada?source=search)

[*MP - SIGAEST - MATA340 - Inventário rotativo ou cíclico no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058014194)

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033402-SIGAEST-INVENT%C3%81RIO)
