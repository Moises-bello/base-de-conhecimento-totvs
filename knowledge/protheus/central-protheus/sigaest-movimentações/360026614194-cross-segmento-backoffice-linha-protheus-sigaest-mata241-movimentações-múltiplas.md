---
article_id: 360026614194
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 69c51913c5c46b8a1ed6f7358d8976891641b6ba13db3a28a81e2bc890e98649
fetched_at: '2026-06-28T22:38:56.968068+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Movimentações
  Múltiplas (Conceito e Informações)
type: support-article
updated_at: '2025-12-09T12:22:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026614194-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Movimenta%C3%A7%C3%B5es-M%C3%BAltiplas-Conceito-e-Informa%C3%A7%C3%B5es
---

A rotina MATA241 (Movimentação Múltipla) no TOTVS Protheus permite lançar vários itens em um único documento, facilitando entradas ou saídas de produtos no estoque conforme o tipo de movimento (Requisição, Devolução ou Produção). Configurações adicionais permitem visualizar e aglutinar lançamentos contábeis e considerar saldo de terceiros. O sistema não limita o número de itens por movimentação, e o saldo dos produtos pode ser consultado diretamente na rotina.

**Dúvida**  
O que é e como realizar uma Movimentação Múltipla pela rotina MATA241?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A rotina de Movimentação Interna Modelo 2 ou Movimentação Múltipla , possui como diferencial a possibilidade de lançar vários itens no mesmo documento, diferentemente da forma de movimentação interna simples (MATA240 - descontinuada). Essa rotina permite ao usuário gerar movimentos de entrada ou saída de produtos no armazém, a depender do Tipo do Movimento inserido no cabeçalho da rotina por meio do campo **TM**

Definição dos Tipos de Movimentos:

Os tipos são cadastrados e configurados a partir da rotina MATA230 - Cadastro de Tipos de Movimentações, podendo ter 3 opções:

- Requisição: esta deve, por regra de Sistema, ter seu código entre 501 e 999 (sendo que o código 999 é reservado para uso interno do Protheus para movimentações de saídas automáticas). Requisição nada mais é do que quando há uma requisição de um material do almoxarifado, ou seja, **uma saída de saldo do armazém**.

- Devolução: esta deve, por regra de Sistema, ter seu código entre 001 e 499 (sendo que o código 499 é reservado para uso interno do Protheus para movimentações de entradas automáticas). A devolução, por sua vez, consiste quando há a necessidade de devolver um material ao almoxarifado, **ou seja, uma entrada de saldo no armazém**.

- Produção: podendo ser qualquer código entre 001 e 499, caracterizado para uso de movimentos de Produção (que engloba conceitos de MRP - Manufatura). Este tipo de movimento é exclusivo para finalidades produtivas de materiais. Normalmente seu tipo de movimento é ligado ao parâmetro [**MV\_TMPAD**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024821953-Manufatura-Linha-Protheus-SIGAPCP-Como-o-Sistema-identifica-a-TM-no-apontamento-atrav%C3%A9s-do-MATA680-ou-MATA681)

**Processo:**

1. Acesse o caminho Atualizações -> Movimentações -> Internas -> Movimentação Múltipla (MATA241)

2. Assim que a rotina for apresentada, podemos verificar que a mesma possui um comando [F12] onde serão apresentados 3 parâmetros de configuração da rotina.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29361365434007)

- **Mostra lançamentos contábeis** ? Essa opção permite que na Digitação de Movimentos Internos seja apresentado os lançamentos e que permita a  Digitação dos Lançamentos Contábeis.

- **Aglutina Lançamentos contábeis ?**Essa opção é bem mais clara indo direto ao encontro da opção acima, essa pergunta se o sistema deve Aglutinar os Lançamentos Contábeis.

- **Considera saldo de Terceiro?**Essa pergunta informa se o Saldo De/Em Poder de Terceiros devera ser considerado nas Movimentações Internas.

3. Após realizar as configurações acima selecione o botão de "Incluir". Assim, a tela de configuração da rotina ser apresentada, digite as informações necessárias e confirme a movimentação.

Exemplo: Requisição (saída de saldo do armazém) de quantidade 10 do produto MP-0026

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29361365436567)

4.  Após finalizar o preenchimento das informações do cabeçalho e da primeira linha, caso seja necessário realizar uma nova movimentação, basta pressionar o botão da seta para baixa no teclado físico e o sistema irá adicionar uma segunda linha. A rotina não possui um limite especifico de linhas a serem inclusas, porém deve ser avaliado se os produtos a serem movimentados no processo podem ocupar a mesma movimentação, isso de acordo com sua regra de negócios.

**Observação**: Poderá observar que assim que a tela de configuração de campos da rotina for apresentada, a tela permite o comando [F4] no campo "Quantidade" (após selecionar o produto) para verificar o saldo que o produto possui no estoque sem ter que sair da rotina para checar o saldo.

Exemplo do produto MP-0026:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29361365438615)

### **Além da rotina Movimentação Múltipla quais outras rotinas que posso utilizar para fazer devolução ou requisição de saldo em quantidade no produto ?**

Pode utilizar a rotina Inventário de produto para fazer a baixa ou a devolução de saldo de um produto.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA340 - Processo padrão para Inventariar produtos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
