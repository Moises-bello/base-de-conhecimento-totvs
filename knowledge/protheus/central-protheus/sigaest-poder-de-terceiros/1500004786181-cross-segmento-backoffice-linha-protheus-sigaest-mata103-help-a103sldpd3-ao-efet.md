---
article_id: 1500004786181
category: SIGAEST - PODER DE TERCEIROS
content_hash: 16556f2eb71ae99e1c200d7b97ccf8d72c8cdad7ed87234f8587eb61132e72ba
fetched_at: '2026-06-28T22:39:03.200338+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA103 - HELP A103SLDPD3
  ao efetuar retorno (devolução) de Remessa em Poder de Terceiros
type: support-article
updated_at: '2023-08-08T17:09:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004786181-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA103-HELP-A103SLDPD3-ao-efetuar-retorno-devolu%C3%A7%C3%A3o-de-Remessa-em-Poder-de-Terceiros
---

**Dúvida**Na rotina **Documento de Entrada (MATA103)** ao efetuar o retorno da Remessa em Poder de Terceiros, quando ao salvar o documento é apresentaado o ***HELP "****A103SLDPD3** - O saldo em quantidade do Poder de Terceiros será finalizado com esta devolução, contudo ainda existe um saldo financeiro de R$ ....*" impossibilitando a finalização da Baixa do Poder de Terceiros. Como resolver?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16615228647703)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Primeiramente revisar os parâmetros **MV\_LIBESB6 = .T.** e **MV\_BLOQSB6 = .F.** (Caso o MV\_BLOQSB6 não existir no ambiente, não é necessário criar).

 - Exemplo de Testes:

Em um cenário de exemplo onde temos:

Produto: PA72

Qtde: 1

Saldo Financeiro: R$ 1000,00

Fazemos uma remessa do PA72, Qtde 1 e Custo Unit e Total de R$ 1000,00 a um terceiro (via MATA410) utilizando TES de saída com **F4\_PODER3 = R e F4\_ESTOQUE = S.**

Ao efetuar o retorno (devolução) dessa remessa, acessamos à MATA103 - Documento de Entrada, selecionamos o cabeçalho com Cliente/Fornecedor com base na Remessa, Produto e TES com **F4\_PODER3 = D e F4\_ESTOQUE = S**. Só que no retorno, por algum motivo o Custo Unit. e Total será de 950,00. Neste caso, ao salvar a nota é apresentado o HELP abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006432942)

Neste caso, para a rotina permitir que a baixa seja concluída mesmo com B6\_PRUNIT diferente da Remessa, é importante deixar o parâmetro **MV\_LIBESB6 = .T. e MV\_BLOQSB6 = .F.** (ou se não existir no ambiente, não é necessário criar).

Com isso, o Protheus permite concluir com a baixa do Poder de Terceiros com  o novo custo (e na SB6 -> B6\_PRUNIT com o mesmo valor da Remessa para não dar diferença no poder de terceiros).

**Saiba mais:**

*[MP - SIGACOM – Qual a função do parâmetro MV\_LIBESB6 no Retorno do Poder de Terceiros ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023635071-MP-SIGACOM-Qual-a-fun%C3%A7%C3%A3o-do-par%C3%A2metro-MV-LIBESB6-no-Retorno-do-Poder-de-Terceiros-?source=search)*

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012199513-SIGAEST-PODER-DE-TERCEIROS)*
