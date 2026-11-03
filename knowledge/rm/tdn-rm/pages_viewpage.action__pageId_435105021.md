---
content_hash: 65d0a90458cb07b616784710e433dc8f1401abe294ace773b897c847bc3387b2
fetched_at: '2026-06-29T00:09:47.593000+00:00'
page_id: '435105021'
product: rm
source: tdn-rm
title: Geração Resíduo Moeda Projetada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105021
version: 1
---

**Geração Resíduo Moeda Projetada**    
Para a realização do Cadastro de um contrato de venda, com Resíduo Moeda Projetada parametrizado, o usuário deve seguir os seguintes passos:   
Acessar o ambiente Totvs Incorporação | Menu Cadastros | Cadastros de Vendas e Aluguéis | Incluir um nova venda  
Nesta nova venda, o usuário deverá selecionar a Modalidade referente ao Resíduo Projetado, no qual a mesma já tem o Componente de Resíduo parametrizado de forma correta.  
Dentro do Plano de Negócios, acessar a aba Condições de Vendas e verificar se o componente de Resíduo está informado. Neste exemplo, a venda que está sendo cadastrada está no *Momento Após Entrega*, ou seja, apenas o Componente de *CM Após*, que foi cadastrado com a moeda IGPM que será reajustada irá atuar.   
É importante verificar se o componente de Resíduo está com a flag "Cálculo do Resíduo com Moeda Projetada" marcada. O componente Principal (Exemplo: tipo de parcela Mensal) tem que ser do tipo Modelo Padrão para que ocorra o resíduo, estando também, no mesmo grupo do componente da Resíduo.   
Neste exemplo, é explicado o Processo da Correção Projetada com o Componente de Correção Monetário informado com Periodicidade Mensal.  
Depois de realizar os cadastros, é necessário Gerar o Plano de Financiamento, Efetivar o Contrato e Gerar as Parcelas para o Totvs Gestão Financeira.  
Após o cadastro e efetivação da venda, realize o procedimento que a venta sofrerá até a geração da Parcela de Resíduo. Neste caso, é informado (projetado) um valor (valor não real, ou seja, não imposto pelo governo) para a cotação de uma moeda em um determinado mês que será utilizado na venda.  
   
Acesse:

* Menu Cadastros | Básicos | Cotações | Filtrar a moeda IGPM
* Após filtrar a moeda IGPM, é necessário cadastrar uma nova cotação
* É efetuada a Correção Monetária e baixado a parcela deste mês, nesse caso será realizado o Reajuste no mês de Janeiro
* Ao reajustar o mês de Janeiro, é necessário realizar a baixa do lançamento com o vencimento no mês do Reajuste
* No mês seguinte, o governo já informou a cotação do mês anterior, então é necessário atualizar esta cotação
* Ao efetuar o reajuste de correção do mês atual, o sistema verifica que no mês anterior houve uma atualização, e esta atualização será atribuída ao componente de Resíduo do mês posterior
* Após o Reajuste com a correção correta, o sistema irá calcular o valor que foi alterado na cotação e acumulará o valor do mesmo para a parcela do mês seguinte

Observação: O valor do resíduo, fica na coluna Resíduo na grid do plano de financiamento.  
   
Pelo desuso da funcionalidade, aparecerá no plano de financiamento, ao incluir o componente de resíduo e marcar a opção de cálculo com moeda projetada a seguinte mensagem: "Resíduo Projetado será excluído do sistema na versão 12.1.25".  
A partir da versão 12.1.25 esta parte da funcionalidade de resíduo será descontinuada. Caso haja alguma sugestão, contate a equipe de suporte/desenvolvimento do TIN.
