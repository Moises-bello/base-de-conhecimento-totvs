---
content_hash: bad843c8a53abeb876a98d8eb84a90b77545e9906ed063cf69c6a31d876659bc
fetched_at: '2026-06-29T00:09:49.744809+00:00'
page_id: '435105356'
product: rm
source: tdn-rm
title: Despesa de Vendas
type: documentation
url: https://tdn.totvs.com/display/LRM/Despesa+de+Vendas
version: 5
---

**Despesa de Vendas**

---

Conceito sobre ( Despesas ) :  
Despesa é todo o gasto de caráter geral , relacionado com a administração e vendas , como por exemplo: juros, multas, materiais de escritório, segurança privada, etc.  
Um exemplo do cadastro de Despesas do TOTVS Incorporação é a possibilidade de se fazer um cadastro de reembolso, na qual se é feito um gasto e o mesmo é repassado ao dono do imóvel.  
Vejamos um exemplo do cadastro de ( Despesa de Vendas )  
   
**Regra de Reembolso**  
   
**Processo para utilização da Regra de Reembolso:**  
   
  
Tipo de Despesas e Regra de Reembolso  
1º ) Habilitar no perfil de usuário em :  
Serviços Globais | Segurança | Perfis  
Selecionar o Sistema ( Incorporação )  
   
  
   
Habilitar : 01.02.08.03 - Tipo de Despesa  
               01.02.08.03.01 - Tipo de Despesa :Visualizar   
               01.02.08.03.02 - Tipo de Despesa :Incluir  
               01.02.08.03.03 - Tipo de Despesa :Editar  
               01.02.08.03.04 - Tipo de Despesa :Excluir  
   
Habilitar : 01.02.08.04 - Regra de Reembolso   
               01.02.08.04.01 - Tipo de Reembolso :Visualizar  
               01.02.08.04.02 - Tipo de Reembolso :Incluir  
               01.02.08.04.03 - Tipo de Reembolso :Editar  
               01.02.08.04.04 - Tipo de Reembolso :Excluir  
   
  
   
Perfil Habilitado  
Despesas | Tipo de Despesa  
  
   
Cadastrando um Tipo de Despesa  
   
  
   
Despesas | Regra de Reembolso  
   
  
   
Cadastrando Regra de Reembolso  
   
  
   
Utilizando o Reembolso em ( DESPESA DE VENDAS )  
Despesas | Despesa de Venda  
 

Importante!Importante!

Ao selecionar o Tipo de Pagamento para "*Gerar Movimento de Faturamento*" na configuração de uma despesa, o sistema ir exibir o campo de *Data de Entrega*, que será replicado diretamente para o Movimento definido nos Parâmetros de Movimento da Definição da Despesa.

Já ao selecionar o Tipo de Pagamento "*Gerar Lançamento Financeiro*", o campo de data do *Primeiro Vencimento* será apresentada. Isso permite que o lançamento seja gerado com a data de vencimento determinada durante essa parametrização.

   
Neste exemplo, estou criando uma despesa de venda ( Segurança Privada ) que a Imobiliária esta pagando ao Fornecedor : Micro M Computadores LTDA a quantia referente R$ 1.500,00 Reais ao Empreendimento ( Empreendimento Modelos de Cálculo ) Código do Bloco ( 02 ) e Cod Apto ( 000003 ) e sendo repassado este valor para o comprador deste Apartamento.  
   
 Lembrando que para que seja efetivado o Reembolso, o contrato deve estar com STATUS = ( Efetivado )  
   
Gerando a(s) Parcela(s).  
Selecionar - Despesa de Venda | Processos | Gerar Lançamentos de Reembolso  
   
  
    
   
Informando o período para geração da Parcela.  
No exemplo foi feita a parcela com vencimento dia 15/10/2018 e informado o período de Outubro.  
   
  
   
Processo executado e parcela gerada.  
   
**Depois de gerar o Processo, pode se visualizar as Parcelas de Despesas em:**  
Despesa de Venda | Anexos | Parcela de Despesa  
   
  
Na tela abaixo é informado os seguintes campos :  
·          Identificador   
·          Número da Parcela   
·          Vencimento da Parcela   
·          Valor da Parcela  
·          Fornecedor na qual foi feito o Pagamento  
·          Movimento  ( Situação )  
·          Tipo de Movimento ( Nome do Movimento )  
·          Dada de criação  
·          Usuário criação   
·          Data Alteração – Caso seja alterado   
·          Usuário de Alteração   
   
  
Como foi realizado o Reembolso, a parcela é visualizada em:  
Despesa de Venda | Anexos | Parcela de Reembolso  
  
Na tela é informado os seguintes campos:  
   
·          Data Criação  
·          Usuário Criação  
·          Data Alteração  
·          Usuário Alteração  
·          Identificador   
·          Número da Parcela  
·          Vencimento da Parcela  
·          Valor da Parcela   
·         Tipo de Integração Financeira  ( Preenchido automaticamente )  
·         Parcela gerada   
   
  
   
Parcela pode ser visualizada nesta tela, como no cadastro de Venda/Aluguel do comprador do imóvel em seus Lançamentos Financeiros.  
( Veja abaixo como visualizar o lançamento pelo cadastro do Comprador do imóvel )  
   
  
   
Apartamento : 000003  
Localizar o contrato de Venda do Apartamento que gerou a Despesa em :  
Venda | Contrato de Venda  
   
  
   
Localizar o contrato com o Código do Apartamento.  
   
  
   
Editar o Contrato | Compradores.  
Entrar no cadastro do Comprador.  
Lançamento ( Na tela abaixo é informado o lançamento de Reembolso gerado pela Despesa ).  
   
  
   
   
   
Voltar para Manutenção de Empreendimentos
