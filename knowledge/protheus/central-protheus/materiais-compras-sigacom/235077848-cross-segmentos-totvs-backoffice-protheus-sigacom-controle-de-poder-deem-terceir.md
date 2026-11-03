---
article_id: 235077848
category: Materiais - Compras (SIGACOM)
content_hash: e2c6bb8effe01bec5f0a4ca647360edb01ad909837fe5c49fadd1485e4a34997
fetched_at: '2026-06-28T22:41:16.196371+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Controle de Poder De/Em
  Terceiros, Entradas, Saídas e Recusas
type: support-article
updated_at: '2023-01-04T10:34:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235077848-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Controle-de-Poder-De-Em-Terceiros-Entradas-Sa%C3%ADdas-e-Recusas
---

**Dúvida**

Controle de Poder De/Em Terceiros, Entradas, Saídas e Recusas.  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17  
  
**Solução**

A decisão de movimentar ou não estoque interfere diretamente nos controles do sistema, tanto no armazenamento de dados, quanto no calculo de custos. Vejamos o que acontece:

* **Poder de/em terceiros** sem movimentação de estoque:

Ao enviar produtos a terceiros (nosso em poder de terceiros), sistema armazena no **SB2**, no campo **B2\_QTER** a quantidade enviada e grava, no **SB6**, registro do movimento com tipo "R" (remessa)

Ao receber produtos de terceiros (de terceiros em nosso poder), o sistema apenas armazena, no **SB6**, registro do movimento com tipo "R" (remessa)

Nesta situação o sistema não movimenta custos, pois não houve movimento de estoque.

Na devolução o sistema gera novo registro no **SB6** com tipo "D" e baixa a quantidade devolvida no **SB2**, **B2\_QTER**

* **Poder de/em terceiros** com movimentação de estoque:

Ao enviar produtos a terceiros (nosso, em poder de terceiros), o sistema armazena no **SB2**, no campo **B2\_QNPT** a quantidade enviada e grava, no **SB6**, registro do movimento com tipo "R" (remessa)

Ao receber produtos de terceiros (de terceiros em nosso poder), sistema armazena no **SB2**, no campo **B2\_QTNP** a quantidade recebida e grava, no **SB6**, registro do movimento com tipo "R" (remessa)

Nesta situação o sistema movimenta custos, portanto, a apuração do custo médio deve ser diária. Deve-se atentar muito para isso, pois somente desta forma o sistema considerará de forma correta as operações de devolução que envolvem terceiros.

Na devolução o sistema gera novo registro no **SB6** com tipo "D" e baixa a quantidade devolvida no **SB2**, **B2\_QNPT** para produtos em poder de terceiros, e **B2\_QTNP** para produtos de terceiros em nosso poder.

Exemplo do **SB6:**

* Operações:
  1. Envio de peças para demonstração a cliente 000001:
     1. **Produto**: 10100 - Microcomputador
     2. **Tipo de Pedido Venda**: N
     3. **TES Poder Terceiros**: R
     4. **TES Atualiza Estoque**: S
     5. Incluir o Produto
     6. Incluir o Cliente
     7. Incluir a **TES** **de** **Saída** (**F4\_PODER3** = Remessa)
     8. Incluir o **Pedido** **de** **Vendas**
     9. Realizar o **Faturamento**
  2. Devolução de peças enviadas para demonstração ao cliente 000001:
     1. **Produto**: 10100 - Microcomputador
     2. **Tipo de NF entrada**: B
     3. **TES Poder Terceiros**: D
     4. **TES Atualiza Estoque**: S
     5. Incluir a **TES** **de** **Entrada** (**F4\_PODER3** = Devolução)
     6. Incluir o **Documento** **de** **Entrada**
  3. Envio de peças para conserto ao fornecedor 000009:
     1. **Produto**: 30304 - Teclado para Microcomputador
     2. **Tipo de Pedido Venda**: B
     3. **TES Poder Terceiros**: R
     4. **TES Atualiza Estoque**: N
     5. Incluir o **Produto**
     6. Incluir o **Fornecedor**
     7. Incluir a **TES** **de** **Entrada** (**F4\_PODER3** = Remessa)
     8. Incluir o **Pedido de Vendas**
     9. Faturar o **Pedido de Vendas**
  4. Devolução de peças enviadas para conserto ao fornecedor 000009:
     1. **Produto**: 30304 - Teclado para Microcomputador
     2. **Tipo de NF entrada**: N
     3. **TES Poder Terceiros**: D
     4. **TES Atualiza Estoque**: N
     5. Incluir a **TES** **de** **Entrada** (**F4\_PODER3** = Devolução)
     6. Incluir o **Documento** **de Entrada**
  5. Recebimento de peças para demonstração do fornecedor 000010:
     1. **Produto**: 20200 - Monitor de Vídeo
     2. **Tipo de NF entrada**: N
     3. **TES Poder Terceiros**: R
     4. **TES Atualiza Estoque**: N
     5. Incluir o **Produto**
     6. Incluir o **Fornecedor**
     7. Incluir a **TES** **de** **Entrada** (**F4\_PODER3** = Remessa)
     8. Incluir o **Documento** **de** **Entrada**
  6. Devolução de peças recebidas para demonstração do fornecedor 000010:

a) Produto: 20200 - Monitor de Vídeo

b) Tipo de Pedido Venda: B

c) TES Poder Terceiros: D

d) TES Atualiza Estoque: N

Incluir a TES de Saída (F4\_PODER3 = Devolução)  
Incluir o Pedido de Vendas  
Faturar o Pedido de Vendas

7) Recebimento de peças para conserto do cliente 000014:

a) Produto: 20201 - C.P.U.

b) Tipo de NF entrada: B

c) TES Poder Terceiros: R

d) TES Atualiza Estoque: N

Incluir o Produto  
Incluir o Cliente  
Incluir a TES de Entrada (F4\_PODER3 = Remessa)  
Incluir o Documento de Entrada

8) Devolução de peças enviadas para conserto ao cliente 000014:

a) Produto: 20201 - C.P.U.

b) Tipo de Pedido Venda: N

c) TES Poder Terceiros: D

d) TES Atualiza Estoque: N

Incluir a TES de Saída (F4\_PODER3 = Devolução)  
Incluir o Pedido de Vendas  
Faturar o Pedido de Vendas

Tabela Controle Poder de/em Terceiros (SB6)

B6\_CLIFOR

B6\_PRODUTO

B6\_DOC

B6\_QUANT

B6\_TES

B6\_TIPO

B6\_CUSTO1

B6\_IDENT

B6\_SALDO

B6\_PODER3

000001

10100

000001

2

520

E

1772,94

000002

0

R

000009

30304

000002

5

530

E

000005

0

R

000010

20200

100000

10

201

D

000006

0

R

000014

20201

200000

3

201

D

000007

0

R

000001

10100

300000

2

200

E

1772,94

000002

D

000009

30304

400000

5

202

E

000005

D

000010

20200

000003

10

540

D

000006

D

000014

20201

000004

3

540

D

000007

D

Conceito Operação Triangular

Empresa B

Empresa A

Empresa C

Operação Triangular consiste em uma transação que envolve mais de 2 empresas para um processo de beneficiamento.

Podemos exemplificar como:

Uma empresa A envia um material à empresa B para beneficiamento e esta envia à empresa C, que deverá efetuar o trabalho e devolver o material diretamente à empresa A.

Desta forma, a Nota Fiscal de Remessa para Beneficiamento será enviada à empresa B, enquanto a Nota Fiscal de Devolução desta mercadoria será enviada pela empresa C.

É possível fazer este controle no Siga através do parâmetro “Operação Triangular (S/N)? “ nas rotinas de Pedido de Venda e Nota Fiscal de Entrada. Os parâmetro são acessados através da tecla [F12] (na versão DOS, pela tecla [F10]).

Nestes casos, a Nota Fiscal Origem pode ser acessada, pressionando a tecla [F4] sobre o campo “Quantidade”, onde serão apresentadas todas as Notas Fiscais do Produto que envolvem Poder de Terceiros.

Desta forma pode-se dar entrada de uma NF do fornecedor C e selecionar a NF de origem do fornecedor B.

EXEMPLO:  
Temos três empresas A, B e C.

Inclui o produto TESTE com saldo inicial.

1) Acessar a empresa A e incluo uma NF de SAIDA (NORMAL) para a empresa B (a empresa B deve ser cadastrada como cliente) para o produto TESTE com qtde = 15 com TES que atualiza estoque e remessa para terceiros.

2) Acessar a empresa B e incluo uma NF de Entrada NORMAL para o fornecedor A (a empresa B deve ser cadastrada como fornecedor) para o produto TESTE com qtde = 15 e TES que atualiza ESTOQUE (não controla poder de terceiros).

3) Na empresa B, lançar a NF de SAIDA – tipo BENEFICIAMENTO do produto TESTE para a fornecedor C, com TES que atualiza estoque e de remessa para terceiro, qtde = 15.

4) Acessar a empresa C e incluo uma NF de Entrada NORMAL do fornecedor B (a empresa B deve ser cadastrada como fornecedor) para o produto TESTE com qtde = 15 e TES que atualiza ESTOQUE com remessa para terceiros.

5) Acessar a empresa C e lançar uma NF de SAIDA – NORMAL para o cliente B do produto TESTE com TES que atualiza estoque e devolução para terceiros, qtde = 15.

6) Acessar a empresa B, e lanço uma NF de ENTRADA - TIPO NORMAL, puxando a NF original da empresa C do produto TESTE com TES que atualiza estoque e de DEVOLUCAO para terceiro, quantidade = 15.

7) Acessar a empresa B, lançar uma NF de SAIDA - NORMAL para a empresa A e atualizando estoque, qtde = 15.

8) Acessar a empresa A, e lanço uma NF de ENTRADA - TIPO BENEFICIAMENTO, puxando a NF original da empresa B do produto TESTE com TES que atualiza estoque e de DEVOLUCAO para terceiro, qtde = 15.

RESUMO

EMPRESA A

EMPRESA B

EMPRESA C

1) NF de Saída - Normal para B como REMESSA para 3o.

2) NF de Entrada – Normal da empresa A.

3) NF de Saída – tipo BENEFIC. para fornecedor C como REMESSA para 3o.

4) NF Entrada – Normal do B como REMESSA de 3o.

5) NF Saída – Normal para A com DEVOLUCAO para 3o.

6) NF de Entrada – tipo NORMAL puxando NF original de C com TES de DEVOLUCAO de 3o.

8) NF de Entrada – tipo BENEFICIAMENTO puxando NF original de B como DEVOLUCAO de 3o.

7) NF de Saída – Normal para a A

***BENEFICIAMENTO PARA PRODUÇÃO***  
Quando há beneficiamento que envolve produção deve-se proceder da seguinte forma:

1. Ter na estrutura um código para beneficiamento;

2. Abre-se uma OP para o produto que será resultado do beneficiamento

3. Emite NF da matéria prima com TES que controla poder de/em terceiros gerando remessa (F4\_PODER3 = "R"). Esta NF será gravada no arquivo de poder de/em terceiros (SB6)

4. Ao receber o material deve-se informar a devolução da matéria-prima com TES que controla poder de/em terceiros (F4\_PODER3 = "D"). Assim o sistema baixa o controle poder de/em terceiros gerado no passo anterior. Informa-se ainda na NF, o produto que é resultado do beneficiamento, neste item deve-se informar o número da OP respectiva ao produto. Desta forma o sistema gerará automaticamente a requisição do material para a OP e atribuirá o custo.

Os seguintes cuidados devem ser tomados e avaliados quando se utiliza controle poder de/em terceiros com movimentação de estoque nestes casos:

1. Se a remessa para beneficiamento é gerada antes da abertura da OP, o TES utilizado não deve movimentar estoque. Caso contrário, se não houver saldo suficiente em estoque após a geração da NF de remessa, o sistema gerará solicitações de compra indevidamente para o produto.

2. A movimentação de estoque é opcional, porém, se utilizada, será considerada no cálculo do MRP

3. Caso seja utilizada a movimentação de estoque na entrada ou saída, deve-se efetuar o mesmo na devolução do material.

***IMPORTANTE :***

**Para casos onde foi efetuada uma nota de saída/retorno controlando o poder de terceiros para um CLIENTE, e o mesmo por algum motivo, rejeitou/recusou essa nota, qual procedimento adotar ?**

Não há pelo sistema padrão uma forma de reabrir o processo de controle de poder de terceiros finalizado, ou baixado parcialmente, com a nota de saída de retorno.

O processo sugerido é:

- Efetuar uma nova entrada (***incluindo assim um novo processo de controle de poder de terceiros***) pela rotina de documento de entrada ( MATA103 ), usando o tipo da nota = B ( para que o sistema habilite o cadastro de cliente ), formulário próprio = Sim. E no item da nota, incluir nos *campos de origem: Número da nota, Série e Item*, com os dados da nota de saída que foi recusada (*essas informações serão puramente informativas, o sistema não efetuará vínculo entre essas notas*). e o TES controlando o poder de terceiros como Remessa.

No momento de se efetuar uma nova saída/retorno, será essa nova entrada que será mencionada, ou seja, esse novo processo de controle de poder de terceiros.

***Obs:***

Veja mais documentações sobre Poder de Terceiros na Página Centralizadora de Compras, na seção de NF de entrada, aba Pode de/Em Terceiros:

<https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000775862/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101880813/mceclip1.png)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
