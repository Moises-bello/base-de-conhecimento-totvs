---
content_hash: 4becff8ee41fe373fae6ecb44d7e3335e568cc9517355cc30713a0871684ddb2
fetched_at: '2026-06-29T00:11:26.856289+00:00'
page_id: '721006782'
product: rm
source: tdn-rm
title: Conciliação com Origem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721006782
version: 9
---

A Conciliação Contábil com a Origem, foi criada visando conciliar registros gerados pelo Gestão de Estoque, Compras e Faturamento (Id Movimento) e Financeiro (Id Financeiro).  
Nessa tela também são considerados os lançamentos de origem Contábil (Id Contábil), para conferência.

Para utilizar essa opção utilize o botão presente no rodapé da página:

Visualização da tela

---

## Filtros para acessar a visão

Esses filtros são referentes ao retorno do valor financeiro, não filtram os registros exibidos na visão.

* **Tipo de Lançamento**: Pagar ou Receber (**Obrigatório**)
* Cliente/Fornecedor: É possível selecionar um fornecedor de uma das coligadas selecionadas na visão de conciliação
* Tipo de Documento: É possível selecionar um ou vários tipos de documento por coligada (coligadas selecionadas na visão de conciliação)

Visualização da tela

---

## Dados da Conciliação com Origem

Após selecionar os filtros desejados, a Conciliação com Origem será realizada.

Nessa visão apenas são levados os registros Conciliação Contábil **presentes na tela anterior**, que ainda **não** foram Conciliados e os dados são agrupados por movimento e coligada.

O **valor financeiro**é calculado com base na fórmula que deverá ser informada no cadastro (aba Conciliação) da conta contábil que foi selecionada no filtro.   
A partir disso, é feito uma soma do valor **total** financeiro **agrupados** por Id Movimento (quando existir) e Id Lançamento Financeiro.

O **valor contábil**é calculado com base nos valores de débito e crédito presentes nos lançamentos.   
É feito uma soma do valor **total agrupados** por Id Movimento, Id do Lançamento Financeiro e Id do Lançamento Contábil (caso a origem do lançamento seja essa), **quando existirem**.

A primeira coluna é referente ao ID do Movimento, caso exista, já a segunda é referente ao ID do Lançamento Financeiro (Apenas preenchido caso não exista Movimento) e a terceira é referente ao ID do Lançamento Contábil (caso a origem do lançamento seja essa);

É possível **visualizar** Movimento, Lançamento Financeiro e Lançamento Contábil, para isso basta clicar no link presente nos identificadores;

Visualização da telaInformações importantes

* No cabeçalho, são exibidas informações relacionadas a o quê está sendo conciliado: **Conta/Descrição, Tipo de Lançamento e Período**;
* A tela pode ser movimentada ou minimizada para utilização do RM em paralelo;
* Os registros, por default são agrupados por Coligada. Diferente da tela de , não são mantidas as eventuais alterações.
* É possível realizar filtros na primeira linha da Grid, localizada logo após o Cabeçalho;
* Caso exista diferença entre os valores, a linha ficará destacada de uma cor diferente de branco;
* Para exportar os valores para Excel, basta utilizar o botão logo abaixo do Cabeçalho, todos registros serão exportados para Excel, com o layout em que estão no momento da exportação.
