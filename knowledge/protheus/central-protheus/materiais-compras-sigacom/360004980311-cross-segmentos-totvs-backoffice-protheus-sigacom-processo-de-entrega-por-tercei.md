---
article_id: 360004980311
category: Materiais - Compras (SIGACOM)
content_hash: e57a652c28713725243179e3991d8daa7a8f3eac3527394efd7f559d8b431a6b
fetched_at: '2026-06-28T22:41:10.308792+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Processo de Entrega
  Por Terceiros
type: support-article
updated_at: '2023-07-27T18:59:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980311-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Processo-de-Entrega-Por-Terceiros
---

**Dúvida**Como realizar o processo de Entrega por Terceiro ?

**Localização**

Brasil

**Ambiente**Protheus – Compras – A partir da versão 11.80

**Solução**

Por exemplo : Foi comprado do fornecedor **Lojas Alpha** mas a entrega é realizada por outro fornecedor, como incluir a nota de entrada sendo que o pedido foi incluído com a Lojas Alpha **?**

A Entrega por Terceiros permite estabelecer uma relação flexível entre fornecedores para viabilizar a entrega de mercadorias aos clientes, desta forma, é possível selecionar pedidos de compras de fornecedores diferentes daquele informado no cabeçalho do **Documento de Entrada**, com base no cadastro de **Entrega Por Terceiros.**

Dentre os procedimentos que contemplam o Pré-Documento, o Documento de Entrada e o TOTVS Colaboração, atualmente é possível listar os pedidos de compras do fornecedor informado no cabeçalho do documento, ou, seja, o sistema carrega na consulta de pedidos com base no cabeçalho.

Entretanto, quando o parâmetro **MV\_FORPCNF = T** está habilitado também é possível apresentar os pedidos de compras de fornecedores diferentes informados com base no cadastro de Entrega por Terceiros.

Abaixo mais detalhes sobre o processo citado acima.

No Pré-Documento de Entrada e no Documento de Entrada, ao relacionar o novo fornecedor ao pedido de compras, será subtraída a quantidade recebida do saldo do pedido e, caso não atenda 100% do total, o pedido pode ser atendido por este ou outros fornecedores. O tratamento financeiro e fiscal está relacionado ao fornecedor informado no cabeçalho do Documento de Entrada.

Ao realizar o estorno do Documento de Entrada, a quantidade será atualizada e o pedido de compras será reaberto para ser atendido por este ou outros fornecedores.

Acesse a rotina Atualizações > Administração de Compras > Entrega por Terceiros(COMA001).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070733393/mceclip0.png)

Como executar esse cadastro ?

Ao acessar a Entrega por Terceiros clique em Incluir e preencha os campos: 

1. Informe o código ou utilize a consulta padrão para selecionar o Fornecedor que consta no Pedido de Compras. Exemplo: 000002.  
**Loja:** informe o número da loja que corresponde ao Fornecedor escolhido. Este campo é preenchido automaticamente quando o Fornecedor for selecionado via consulta padrão no campo Código. Exemplo: 01.  
**Nome**: campo preenchido automaticamente de acordo com o conteúdo informado no Código. Exemplo: Mercado MB.  
**Item**: preenchido automaticamente para identificação dos Fornecedores. Exemplo: 001  
**Fornecedo**r: informe o código ou utilize a consulta padrão para selecionar o Fornecedor que entregará o Pedido de Compras. Exemplo: 000003.  
**Loja**: informe o número da loja que corresponde ao Fornecedor escolhido. Este campo é preenchido automaticamente quando o Fornecedor for selecionado via consulta padrão no campo Fornecedor. Exemplo: 01  
**Nome Fornec**.: preenchido automaticamente e apresenta o nome do Fornecedor escolhido. Exemplo: Fornecedor Extra Hipermercado. *A seta para baixo para adicionar uma linha que possibilita o preenchimento de todos os Fornecedores que poderão atender a entrega de produtos em nome do fornecedor informado no Pedido de Compras.*

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069622734/mceclip1.png)

2. Clique em Salvar para concluir o procedimento de inclusão.

3. Na janela principal da rotina Entrega por Terceiros também estão disponíveis as opções:  
**Alterar**: permite incluir e/ou excluir os Fornecedores que estão vinculados ao Fornecedor que do Pedido de Compras.  
**Visualizar**: exibe os Fornecedores que estão vinculados ao Fornecedor que entregará o Pedido de Compras.

4. Tabelas Utilizadas: CPW - Grupo de Fornecedor e CPX - Itens do Grupo de Fornecedor.

5. No processo do documento de entrada, após o processo descrito acima, ter sido realizado, será possível a troca de fornecedores, quando o pedido for apresentado pela opção em outras ações ou pelo atalho F5.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069624234/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070741373/mceclip3.png)

Abaixo segue segue exemplo na prática :

* O fornecedor Borracharia ABC é de quem será comprado o produto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088053774/mceclip0.png)

Porém qualquer um dos fornecedores amarrados a ele, poderá efetuar a entrega, logo será o fornecedor que emitirá a nota, sendo esse código preenchido no cabeçalho da pré nota / documento de entrada, conforme exemplo abaixo :

* Onde o fornecedor do pedido de compras é o Borracharia ABC (código 000006), porém a entrega e a nota são efetuados pelo fornecedor Extra (código 000007)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089183093/mceclip1.png)

Logo, o sistema apresentará na consulta de Pedidos (F5), os dois fornecedores.

**Importante:**

Para que o pedido seja apresentado ao criar a Pré-Nota (MATA140) ou Documento de Entrada (MATA103) verificar se o F12 ao entrar na rotina está conforme o print:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409677480855/mceclip0.png)

***Obs.:***

***O Processo de "Entrega por Terceiros" do Compras, apenas possibilita que a entrega do PC ocorra por um fornecedor previamente cadastrado na rotina COMA001 que possui vínculo com o fornecedor original (Do Pedido de Compras). Atualmente não existe nenhum indicativo no Pedido de Compras que determine que a entrega foi realizada por um terceiro (Fornecedor Diferente), ocorrendo, dessa forma, apenas a baixa do saldo no Pedido de Compras.***

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
