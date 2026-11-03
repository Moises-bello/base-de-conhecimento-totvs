---
article_id: 360011962151
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 707d2f5a49e848b57e78c1bdfa5cea6bfc5bb9edd459643562f5d0d89bb796b5
fetched_at: '2026-06-28T22:38:53.927053+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como efetuar Baixa
  do C.Q. (MATA175)?
type: support-article
updated_at: '2021-10-29T17:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011962151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-efetuar-Baixa-do-C-Q-MATA175
---

**Dúvida**Qual o passo a passo para efetuar Baixa do C.Q. (MATA175)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

A rotina Baixa de C.Q tem o objetivo de controlar o fluxo dos produtos direcionados ao Controle de Qualidade. Além disso, transfere os produtos do Armazém do Controle de Qualidade, previamente cadastrado e definido no parâmetro **MV\_CQ**, para o armazém digitado.

**OBS:** Caso queira saber como deixar o sistema configurado para efetuar este controle [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011947711)

Para transferir ao Controle de Qualidade, as notas fiscais devem pertencer a mesma filial. Deve haver um diretório de gravação para a avaliação do C.Q., definido no parâmetro MV\_DIRCQ.

**Para efetuar a baixa do Controle de Qualidade:**

***1.*** Selecione as opções **Atualizações -> Movimentos. Internos -> Baixas do CQ (MATA175**). O sistema apresentaRÁ a tela com as movimentações do Controle de Qualidade.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008560872/mceclip0.png)

***2.*** Posicione o cursor sobre a movimentação a ser analisada e clique na opção "**Liberar/Rejeitar**", preenchendo os campos conforme descrição a seguir:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008560992/mceclip1.png)

Esta tela apresenta uma linha com os dados originais da movimentação, que não pode ser alterada. Para liberar ou rejeitar é necessário criar uma nova linha onde será definida que quantidade será liberada ou rejeitada.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008595531/mceclip2.png)

**Número -**A cada entrada de materiais destinada ao CQ, o sistema gera um número para sua identificação conforme o parâmetro "MV\_DOCTRAN". Este campo apresenta o número da movimentação do Controle de Qualidade. É preenchido automaticamente pelo sistema e não pode ser alterado.

**Armazém -**Este campo mostra o armazém do CQ, definido no parâmetro “MV\_CQ”

**Cod. Produto -**Este campo mostra o código do produto.

**Unid. Medida -**Este campo mostra a Unidade de Medida do Produto.

**Lote -**Este campo apresenta o lote do produto. Utilizado para produtos que trabalham com rastreabilidade.

**Sub-lote -**Este campo apresenta o sub-lote do produto. Utilizado para produtos que trabalham com rastreabilidade.

**Sequencia -**Sequência do item da movimentação.

**Tipo -**Neste campo deve ser definido o tipo de movimentação a ser feita. Para a linha original o sistema assume 0 para o tipo. Digite **"1"** para Liberar ou **"2"** para Rejeitar

O sistema pode ainda atribuir outros valores ao campo "Tipo", porém o usuário pode apenas trabalhar com os tipos 1 (Liberação) e 2 (Rejeição).

**Descrição -**Este campo apresenta a descrição do tipo de movimentação, ou seja, Liberado ou Rejeitado.

**Quantidade -**Informe a quantidade do Item que deseja Liberar/Rejeitar.

**Saldo -**Este campo mostra o saldo restante no CQ após efetuada a movimentação.

**Observação -**Digite suas observações.

**Qtd. 2a UM -**Quantidade na segunda unidade de medida, calculada pelo sistema.

**Saldo da 2a UM -**Saldo restante na segunda unidade de medida.

**Sequencial -**Subdivisão do número da movimentação do CQ. Campo preenchido pelo sistema.

**Armazém Des. -**Este campo mostra o armazém de destino do produto após a liberação ou a rejeição. Em caso de Rejeição o campo será preenchido com o valor do parâmetro "MV\_CQ", e em caso de Liberação o campo será preenchido com o número do armazém padrão definido no campo "B1\_LOCPAD" do Cadastro de Produtos. Se for necessário, é possível alterar estes armazéns.

**Data Transf. -**O sistema assume a data base.

**Sub-Lote -**Este campo mostra o novo sub-lote definido pelo sistema, caso o produto esteja incluído no controle de rastreabilidade.

**Estorno -**Este campo é marcado com "S" caso a movimentação tenha sido estornada.

**Mot. Rejeição -**Selecione o código do motivo de rejeição. O sistema permite que sejam criados novos motivos para rejeição. O que deve ser feito no Módulo Configurador, incluindo um item na Tabela (43) de Motivo de Perda/Rejeição.

**Descr. Rejeição -**Este campo mostra a descrição do Motivo da Rejeição.

**Como estornar uma liberação/rejeição de C.Q?**

Basta selecionar o movimento da rejeição de CQ. Após isso, na linha da rejeição/liberação, marque um X na coluna "Estorno"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411777477271/mceclip0.png)

Com isso, a legenda volta a ficar verde:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411777716759/mceclip1.png)

Também é possível visualizar o detalhamento da avaliação do C.Q, mostrando o estorno da rejeição:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411780974231/mceclip2.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações de Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
