---
content_hash: 005940af0a7359b78b55e396eff5d013764ec826ec75d892e9d4e3a9fc4c3971
fetched_at: '2026-06-29T00:10:03.945548+00:00'
page_id: '452719177'
product: rm
source: tdn-rm
title: Empréstimos RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719177
version: 2
---

Para controle de empréstimos é possível incluir e/ou alterar informações referentes aos  empréstimos do funcionário, controlando-se valor original, nº de parcelas, periodicidade, saldo devedor.  
    
 **Atenção:**  
 1.     Após o lançamento dos empréstimos, o sistema criará um registro no histórico da parcela lançada no movimento de cada empréstimo com o ano/mês competência, período, tipo do lançamento e valor. Veja em Empréstimos no Cadastro de Funcionários.  
 2.     Para as bases que tem o campo "Utiliza Lançamento Automático de Empréstimo de Férias" marcado nos parâmetros de férias, o sistema automaticamente criará o novo código no cadastro de empréstimo do funcionário, seguindo os seguintes exemplos:

|  |  |
| --- | --- |
| Último código | Código de Empréstimo para o próximo registro |
| 0001 | 0002 |
| 0001-02A | 0001-02A1 |
| 0002A | 0002A1 |
| 0002 - 1A | 0002 - 1A1 |
| 0002 - 1A1 | 0002 - 1A2 |
| EMP/01 | EMP/02 |
| EMP/9 | EMP/90 |
| EMP/99 | EMP/990 |
| EMP/990 | EMP/991 |
| ABC | ABC1 |
| A01 | A02 |
| fgh | fgh1 |
| FERIAS.A1 | FERIAS.A2 |

Os tipos de empréstimos são cadastrados em uma tabela dinâmica que poderá ser alterada de acordo com a necessidade. Esta informação serve para agrupar por quais motivos o funcionário solicitou empréstimo.  
    
 A informação do evento para desconto do empréstimo é fundamental para visualizar o lançamento do desconto na movimentação. No caso de parcelamento do empréstimo, deve ser utilizada, no campo "Fórmula Referência" do cadastro do evento, a função TABEMPRESTIMO que demonstrará a quantidade de parcelas que já foram pagas.  
    
 Para colocar o total de parcelas pagas na coluna "Ref" do evento de desconto de empréstimos, crie a seguinte fórmula:  
 Ø  TABEMPRESTIMO ('NROPARCPAGAS' , 'V' , 'XXXX')   
    
 Onde XXXX é o código do empréstimo.  
    
 A Data Inicio Desconto Empréstimo é o mês de início de desconto do empréstimo do funcionário, isto é, controla o desconto do empréstimo de acordo com a data de desconto. Esta data de início do desconto não pode ser nula e deve ser maior ou igual ao primeiro dia do mês e ano de competência. E o número de parcelas pagas deve ser menor que o número de parcelas que serão divididas para o pagamento do empréstimo pelo funcionário. Também o saldo devedor deve maior que zero.  
    
 O Saldo devedor inicializará com o valor do empréstimo. Entretanto, poderá  ser alterado utilizando o campo "Fórmula de Correção". O saldo devedor deve maior que zero e deverá ser preenchido com valor total do empréstimo, quando for cedido o primeiro empréstimo.  
    
 **Atenção:**  
    
 **Observação:**  
 Não serão lançados nas férias empréstimos com o campo Número Parcelas em branco ou zerado, ou seja, quando o cálculo do desconto do empréstimo for por Fórmula lançamento.   
 A fórmula de lançamento substitui o número de parcelas. Esta fórmula deverá ser utilizada, por exemplo, no caso de ser definido o número de parcelas de acordo com o valor do empréstimo.  
    
 **Exemplo de como fazer uma correção no saldo devedor de um empréstimo:**  
  Primeiro, crie uma sentença SQL em Utilitários | Consultas Sql que retorne o saldo devedor do empréstimo.  
 SELECT SALDODEVEDOR   
 FROM PFEMPRT   
 WHERE PFEMPRT.TIPOEMPRESTIMO = '0003'   
 AND PFEMPRT.CODIGO = '01' AND CHAPA = '0001'  
    
 Segundo, crie uma fórmula que utilize o resultado da sentença SQL acima, para reajustar o saldo devedor do empréstimo.  
  SE EXECSQL ('emprestimo') =1  
  ENTAO ( RESULTSQL ('emprestimo' , ' SALDODEVEDOR')) \* 0.10  
  SENAO 0  
  FIMSE  
    
 O valor retornado pela fórmula é adicionado ao valor do saldo devedor atual antes do valor da parcela ser cobrado.  
    
 Se o saldo devedor for igual a R$100,00, o valor da fórmula será R$ 110,00.  
    
 Através desta fórmula é possível multiplicar o valor do saldo devedor pelo valor do reajuste.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários  
 Informações para o cálculo
