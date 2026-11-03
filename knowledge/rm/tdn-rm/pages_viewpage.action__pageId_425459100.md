---
content_hash: 69a7a5d98c200affda07e4f8c56a18dbdcf8d12ce7d78e6172117586f660cea5
fetched_at: '2026-06-29T00:09:33.976778+00:00'
page_id: '425459100'
product: rm
source: tdn-rm
title: Faixa de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459100
version: 8
---

---

Nesta tela, cadastra-se as faixas de cobranças por créditos pré determinado pelos usuários.    
**Campos:**

* Nº Inicial de crédito ao Nº Final de créditos é informado o valor definido para esta faixa ou Valor fixo.
* Você poderá, portanto, informar um valor para os créditos financeiros ou informar um valor fixo para os alunos que estiverem dentro daquela faixa de créditos.

Para que seja utilizada esta funcionalidade, deve-se seguir as parametrizações abaixo:  
Parâmetros Gerais>  
                        15.05 Integração >  
                                                15.05.03 Financeiro >  
                                                                            Fin - Geral 1/3 ( Marcar o parâmetro - Utilizar Faixa de Crédito )  
**Exemplo:**  
   
Aluno A tem matrícula em disciplinas que totalizam 190 créditos financeiros.  
Aluno B tem matrícula em disciplinas que totalizam 280 créditos financeiros.  
   
     Considere o cadastro da faixa de crédito para a matriz aplicada dos dois alunos:  
   
   
Nº inicial - final de créditos:    150 - 200            Valor Fixo: 600,00                                               
                                               201 - 290            Valor por Crédito: 4,00   
Sendo assim, o aluno A irá pagar R$ 600,00 e o aluno B irá pagar R$ 1120,00 (280 \* R$ 4,00).  
   
   
**Informações importantes:**

1. A Faixa de crédito é usada para cobranças de Créditos e não por valores Fixos dos serviços.
2. Quando o usuário informa o valor dos créditos financeiros, essa informação, sobrepõe o cadastro do crédito financeiro (valor) no registro da disciplina da matriz curricular.
3. A Situação de Matrícula da disciplina do aluno tem que estar parametrizada (Status na Disciplina): Conta créditos Financeiros - Cobranças por créditos.
4. No registro da disciplina do período é necessário ter um determinado número de créditos cadastrados para cobrança.

É importante lembrar que o uso de faixa de crédito exige que TODOS valores sejam cobertos pelas faixas cadastradas.

Essas faixas devem incluir o valor inicial 0 até um valor final que pode ser atingido.

**Observação**: O  tem que ser por cobrança de crédito

Veja Também

---
