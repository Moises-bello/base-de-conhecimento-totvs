---
content_hash: 8ed5cd8def3cd1aa3a8bc0643fdba28a38bdeead72b6c625948821ef39b3c194
fetched_at: '2026-06-29T00:09:29.152935+00:00'
page_id: '423938824'
product: rm
source: tdn-rm
title: Produto Global
type: documentation
url: https://tdn.totvs.com/display/LRM/Produto+Global
version: 15
---

O sistema TOTVS Gestão de Estoques, Compras e Faturamento possui um cadastro de produtos por coligada.   
Não só atendendo a nova funcionalidade do sistema, Central de Compras, mas também visando facilitar a criação, manutenção e controle do cadastro de produto, foi criado o recurso Produto Global.   
Consiste em compartilhar o mesmo cadastro de produto com mais de uma coligada, sendo assim, não será mais necessário replicar o cadastro de produtos, desde que estejam parametrizadas para esta funcionalidade.   
Em uma única coligada não será possível ter produtos globais e não globais, conceito diferente do Cadastro de Cliente/Fornecedor.  
Podemos ter coligadas parametrizadas para trabalhar com produto global e outras não, sendo assim, o recurso se torna opcional.   
Se uma coligada não possui nenhum produto cadastrado, ou seja, uma coligada nova, podemos iniciar o cadastro de produtos já trabalhando com produto global, basta acessar os parâmetros e configurar para tal função, mas se a coligada já possui produtos cadastrados, existem algumas restrições e consistências a serem realizadas antes da conclusão da parametrização que são detalhadas no processo de Conversão do Cadastro de Produto.

***Atenção!***

Não sendo necessário realizar a conversão para trabalhar com produto global, o usuário deverá atualizar todo o cadastro de produtos já que marcar o parâmetro "Produto Global" não replica os dados específicos do produto como: unidade de medida, preço, fabricante etc., para a coligada em questão. Para atualização o usuário tem três alternativas: Processos>>Atualizar Múltiplos Registros, Cópia de Produtos entre Coligadas ou atualização manual.

A parametrização para utilizar produto global é irreversível, portanto avalie os impactos nos processos utilizados por sua empresa antes de realizar a parametrização.

**Após a parametrização, o que vai alterar no Cadastro de Produto?**

As funcionalidades permanecem a mesmas, validando a coligada corrente.   
Mas se um usuário tem restrições no cadastro do produto, por exemplo, estas restrições devem ser replicadas para as demais coligadas que também trabalham com produto global, visando manter o controle do cadastro.  
Alguns campos do cadastro do produto se alterados, também serão alterados nas demais coligadas que trabalham com produto global, são os campos em comum de um produto, exemplo: IDPRD, CODIGOPRD, NOMEFANTASIA, DESCRICAO e etc.   
Estes campos estão presentes na tabela TPRODUTO, ou seja, todos os campos presentes nesta tabela são campos em comum de um produto.  
Respeitando os processos do sistema TOTVS Gestão de Estoques, Compras e Faturamento e suas integrações, alguns campos ainda serão únicos por coligada, exemplo: CODFAB, FATORREDUCAOICMS, DESCONTOVENDA, CODUNDCONTROLE e etc.   
Estes campos estão presentes na tabela TPRODUTODEF, ou seja, todos os campos presentes nesta tabela, se alterados, vão influenciar apenas a coligada corrente.   
Ao excluir um produto global, este produto será excluído em todas as coligadas parametrizadas para trabalhar com produto global, se tratando do mesmo produto.  
As informações distintas do produto com relação à tabela TPRODUTODEF não são empecilho para a exclusão.

**Obrigatoriedade de campos**

As parametrizações quanto à obrigatoriedade de um campo do produto, feita em uma determinada coligada, não serão replicadas para as demais coligadas que também trabalham com produto global, ou seja, ao incluir um novo produto as consistências serão realizadas de acordo com a coligada corrente.  
  
**Cópia de Produtos entre Coligadas**

Se ao realizar a cópia do produto entre coligadas seja necessário marcar a Opção "\[x\] Substitui registros no destino se eles já existirem", o sistema trata a cópia de um produto global da seguinte maneira:

* Produto Global  → Produto Global: Se tratando do mesmo produto são copiados os dados da tabela TPRODUTODEF da coligada corrente para a coligada de destino.
* Produto Global  → Produto Não Global: Todos os dados serão copiados.
* Produto Não Global   → Produto Não Global: Todos os dados serão copiados.
* Produto Não Global   → Produto Global: Todos os dados serão copiados, porém os dados presentes na tabela TPRODUTODEF não serão replicados para as demais coligadas também parametrizadas para trabalhar com produto global, apenas para a(s) coligada(s) de destino selecionada(s).

*****Atenção!*****

* **Anexos - Clientes/Fornecedores**:  Ao associar um cli/for para um produto global, este cli/for só será apresentado na coligada corrente, mesmo que o cli/for seja global.
* **Anexos - Log do Produto**: Ao realizar uma alteração no cadastro do produto onde o log do produto será atualizado, esta atualização só será exibida na coligada em que a alteração foi realizada.
* **Anexos - Produto Composto**: Ao inserir um produto composto, para um produto global, este produto composto só será exibido na coligada em que foi inserido.
* **Anexos - Substituto/Similar**:  Ao inserir um produto substituto/similar, para um produto global, este produto substituto/similar só será exibido na coligada em que foi inserido.
* **Anexos - Unidade de Medida do Produto**: Ao cadastrar um produto global, as unidades de medida do produto só serão exibidas na coligada em que foi inserido, portanto, caso necessário deverá ser feita a cópia de produto entre coligadas.

**Marca**

Quando se trabalha com o conceito de Produto, ao realizar a conversão de Produto Global, as marcas vinculadas ao anexo de cadastro do produto e marca default do produto são mantidas por Coligada, ou seja, um mesmo produto (global) pode ter marcas diferentes em seu anexo, assim como marcas defaults diferentes em cada Coligada.

Informações Adicionais

* [Como Fazer - Conversão Produto Global](http://tdn.totvs.com/pages/viewpage.action?pageId=42043475)
