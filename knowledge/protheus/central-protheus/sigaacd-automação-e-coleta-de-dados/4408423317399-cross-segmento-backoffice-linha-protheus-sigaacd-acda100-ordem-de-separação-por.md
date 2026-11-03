---
article_id: 4408423317399
category: SIGAACD - Automação e Coleta de Dados
content_hash: 3ac8a3d02a70e3490329786fa278ad9f88ee24d995fe25d49cb3189269289175
fetched_at: '2026-06-28T22:39:11.096892+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD -  ACDA100 - Ordem de
  Separação por Pedido de Venda
type: support-article
updated_at: '2025-12-22T18:18:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408423317399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Ordem-de-Separa%C3%A7%C3%A3o-por-Pedido-de-Venda
---

A Ordem de Separação no TOTVS Protheus gera documentos para separar materiais de pedidos de venda liberados antes do faturamento, sem gerar empenho ou reserva. O processo envolve configurar parâmetros, operadores, cadastros básicos e criar o pedido de venda, seguido da geração da ordem via sistema e execução no Coletor de Dados. Após a separação, gera-se o documento de saída para concluir o fluxo.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35983699394967) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
O que é e como gerar uma Ordem de Separação por Pedido de venda (ordem de separacao por documento de saida via Coletor de Dados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/x/kh44Hg)

A rotina Ordens de separação tem por objetivo gerar documentos para separação de materiais no estoque.

* OS para pedido de venda (mais utilizada):
* Utilizada para separar materiais de pedidos de venda já liberados, antes do faturamento da nota.

**Importante**

Diferentemente do que muitos usuários acreditam ser o correto, a Ordem de Separação **não gera Empenho/Reserva** justamente por se tratar apenas de um processo de checagem dos itens de um Pedido. **O que empenha de fato é a criação do Pedido de Venda**. E, o faturamento do Pedido gera a saída do Estoque.

**Fluxo do Processo**

Ordem de separação por Pedido de Venda:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408414764439)

**Configuração do processo**

Observação:

**Recursos Disponibilizado(s):**

Separação dos itens para posterior geração de Documento de saída via módulo de Faturamento.

**Recursos não disponibilizado(s):**

Embalagem Simultânea;

Embalagem;

Gera Nota Via Coletor;

Imprimir Nota;

Imprimir Etiq. Volume;

Embarque.

**Configurar os parâmetros do sistema**

1. Acessar o modulo Configurador
2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
3. Pesquise pelo parâmetro MV\_CBPE007
4. Edite o parâmetro MV\_CBPE007
5. Gravação das tabelas de Ordens de Separação do ACD com os dados da Nota Fiscal quando a mesma for gerada pelo Protheus

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402257815)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408414812695)

**Configurar de Operador**

* Acessar o modulo Estoque/Custos
* Acessar o Menu > Atualizações > ACD> Operadores
* Clique em "Incluir"
* Informe os campos obrigatórios

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402302103)

**Cadastros básicos para o processo de Ordem de Separação**

**Cadastrar Cliente**

* Acessar o modulo Faturamento
* Acessar o Menu > Atualizações > Cadastros > Clientes
* Clique em "Incluir"
* Informe os campos obrigatórios
* Clique em Salvar

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408414996247)

**Cadastrar condição de pagamento**

* Acessar o modulo Faturamento
* Acessar o Menu > Atualizações > Cadastros > Condições de pagamentos
* Clique em "Incluir"
* Informe os campos obrigatórios
* Clique em Confirmar

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415025815)

**Cadastrar Local de Estoque**

* Acessar o modulo Estoque/Custos
* Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
* Clique em "Incluir"
* Informe os campos obrigatórios
* Clique em "Confirmar"

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415036823)

**Cadastrar TES**

* Acessar o modulo Estoque/Custos
* Acessar o Menu > Atualizações > Cadastros > Movimentações > Fiscais > Tes
* Clique em "Incluir"
* Informe os campos obrigatórios, informando os campos "Tipo do TES" igual a S-Saída, "Atu.Estoque" igual a S-Sim e "Poder Terc." igual a N-Não Controla

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415050263)

**Cadastrar Produto**

* Acessar o modulo Estoque/Custos
* Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
* Clique em "Incluir"
* Informe os campos obrigatórios para o produto acabado
* Clique em "Confirmar"

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415071383)

**Cadastrar saldo.**

* Acessar o modulo Estoque/Custo
* Acessar o Menu > Atualizações > Saldos > Inicial
* Clique em "Incluir"
* Clique em "Salvar"

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415144855)

**Exemplo prático do processo utilizando o Protheus**

**Cadastrar Pedido de venda**

* Acessar o modulo Faturamento
* Acessar o Menu > Atualizações > Pedidos > Pedido de Venda
* Clique Incluir
* Informe os campos obrigatórios para os campo tipo da nota escolhido
* Na grade de produtos deve ser informado a o item que será vendido
* Clique em "Salvar"

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415173911)

**Gerar Ordem de Separação.**

* Acessar Modulo de Faturamento
* Acessar o Menu > Atualizações > ACD > Ordem de Separação
* Clique em Gerar.
* Será apresentado a tela de parâmetros selecione Pedido de Venda informe as opções conforme abaixo:

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415224087)![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415229463)

* Pressione o botão [F12] para configurar conforme abaixo:

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402568343)

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415263127)

* Clique em "Outras ações" > "Gerar"
* Será apresentada a tela que foi configurada. Pressione OK
* Selecione o pedido de venda e clique em "Gerar".

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402600343)

* Próximos passos via Coletor de Dados.

**Acessar ao Meu Coletor de Dados padrão / App "Meu Coletor de Dados"**

* Acessar informando Login do operador.
* Selecionar a Ordem de Separação.

![Ordem_de_separacao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415320471)

* Realizar a separação do item e finalizar ordem de separação.

![Ordem_de_separacao_2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402656535)

**Gerar Documento de saída.**

* Acessar o modulo de Faturamento
* Acessar o Menu > Atualizações> Pedidos > Pedidos de Venda
* Clique sobre o Pedido de Venda clicar em "Outras Ações" e selecione a opção "Prep. Doc. Saída".

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415382423)

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402700439)

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408415396247)

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402717207)

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402734103)

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408402745751)

Com isso, o fluxo desde a criação do Pedido de Venda até a efetivação do Documento de Saída foi concluído, tendo a Ordem de Separação no meio do processo.

### **Curiosidades:**

* No momento que geramos uma ordem de separação vinculada a um pedido de venda, não temos como alterar a quantidade da ordem da ordem de separação quando vincula o pedido de venda.
* O Parametro **MV\_NUMITEN** tambem é usado para o processo em questão, Numero maximo de itens por nota (neste caso por ordem de separacao).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
