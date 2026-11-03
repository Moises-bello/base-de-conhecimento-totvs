---
article_id: 22384024706071
category: SIGAEST - PODER DE TERCEIROS
content_hash: 4ee03a55eeb259102bc9851a073956ca2d41cf36fac169513c0df13336cf22fb
fetched_at: '2026-06-28T22:39:03.167241+00:00'
product: protheus
section_id: 1500001538881
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como realizar a Operação
  Triangular no papel de Encomendante sem a nota de cobertura ?
type: support-article
updated_at: '2024-03-28T10:28:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22384024706071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-realizar-a-Opera%C3%A7%C3%A3o-Triangular-no-papel-de-Encomendante-sem-a-nota-de-cobertura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22384046299031) Tempo aproximado para leitura: **00:03:15min****Dúvida**Por questões legais de alguns estados a Nota de Cobertura não é obrigatória, nesses caso, como realizar a operação triangular no papel de Encomendante?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Como sabemos dentro do Protheus para que possamos realizar o controle do Poder de Terceiros, temos que alimentar a tabela SB6 (tabela de controle de poder de terceiros), e dentro do processo de operação triangular o passo que grava as informações nessa tabela seria exatamente no documento de cobertura.

Um outro fato importante é que o poder de terceiros consiste em movimentações via MATA103 - Documento de Entrada e MATA410 - Pedido de Venda com TES que controla poder de terceiro, sabendo disso, não existe rotina interna de poder de terceiros, nem rotina de criação ou ajuste de poder de terceiros, sendo movimentado apenas por notas fiscais.  
   
Para melhor entendimento, já tratamos esse caso com o time de Consultoria Tributária no qual foi documentado o parecer ([Para maiores detalhes clique aqui](https://tdn.totvs.com/x/cYvyE)).  
  
A orientação passada pelo nosso time de consultoria seria realizar uma remessa para poder efetuar esse controle (poder de terceiros, com configurações de TES que não gerem informações fiscais (livro, contábil, financeiro e NF-e) e apenas movimente esse saldo de terceiro.

 

**Importante:** O campo envolvido no poder de terceiro seria apenas o campo F4\_PODER3 = Remessa ou Devolução.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Poder de Terceiros no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538881-SIGAEST-PODER-DE-TERCEIROS)*
