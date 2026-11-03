---
content_hash: 5bc7b639de5f1bf600981658ac50a41aee84892afab87231d9c6643cf6a728e3
fetched_at: '2026-06-29T00:10:08.550837+00:00'
page_id: '452719535'
product: rm
source: tdn-rm
title: Fórmulas / Funções - A
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719535
version: 4
---

**Função A** = Retorna valor de um acumulador

**Sintaxe** = A ('CÓD. DO ACUMULADOR')

**Tipo de Retorno** = Valor

**Exemplo:**  
Código da fórmula: AC01 = Retorna valor do acumulador de código 01 (Comissão).   
Texto da fórmula: **A('01')**

**Observações:**

* O código do acumulador deve ser informado entre aspas.
* Quando utilizado no cálculo do recibo de férias, será considerando os eventos lançados no recibo de férias que estejam configurados com o código do acumulador. Neste caso não é considerado os eventos lançados na Ficha Financeira, mesmo se os mesmos estiverem com o mesmo código do acumulador da fórmula. Para considerar os eventos da Ficha Financeira no cálculo do recibo, orientamos a usar a função de fórmula **ACUMFF.**
* No Teste da Fórmula, sempre será verificado a Ficha Financeira.
* Os acumuladores são incluídos ou editados no cadastro de tabelas dinâmicas. No cadastro de eventos, você define se valores deste serão guardados em determinado acumulador.

**Atenção:**  
As variáveis de fórmula que são relativas à movimentação do funcionário, como a **A**, não devem ser utilizados para fórmula de seleção. Porque no momento da seleção, o sistema ainda não executou a movimentação do funcionário. Desta forma, estas funções/variáveis irão retornar sempre "zero".

* **Função ABS** = Valor Absoluto
* **Sintaxe** = ABS (VALOR)
* **Tipo de Retorno** = Valor
* **Função ACUMFF** = Acumulador de ficha financeira
* **Sintaxe** = ACUMFF(MÊS, ANO, 'CÓD. DO ACUMULADOR')
* **Tipo de Retorno** = Valor

**Observação:**  
Este acumulador deverá ser criado em TABELAS DINÂMICAS - INT34

* **Função ADIANT** = Retorna percentual de adiantamento
* **Sintaxe** = ADIANT
* **Tipo de Retorno** = Valor

**Exemplo:**  
ADIANT  
Supondo que o funcionário Antônio tem um percentual de adiantamento de 40%, o retorno da fórmula, para esse funcionário, seria 40.

* **Função ADMDEM** = Retorna admitido ou demitido no mês
* **Sintaxe** = ADMDEM
* **Tipo de Retorno** = Valor

**Exemplo:**  
ADMDEM  
Supondo que o funcionário Itamar foi admitido ou demitido no mês de competência, o retorno será **1**. Se houvesse sido admitido ou demitido em outros meses, retornará **0**.

* **Função ALTEROUCADASTRO** = Retorna 1 se houver alteração no cadastro do funcionário e 0 se não houver alteração.
* **Sintaxe** = ALTEROUCADASTRO('string')
* **Tipo de Retorno** = Valor

**Observação:** Na sintaxe, o campo string deverá ser informado com qual campo do cadastro será validado.  
**Exemplo:**  
ALTEROUCADASTRO ('FUNCAO')  
ALTEROUCADASTRO ('SECAO')  
Esta função está contemplando se houve alteração no cadastro dos campos: FUNCAO e SECAO.  
**Dica:**  
Esta função poderá ser utilizada no campo **Fórmula para Criticar o Cadastro de Funcionários** no parametrizador em Folha de Pagamento | Funcionário | Restrições Cadastrais.

* **Função ANO** = Retorna ano de competência.
* **Sintaxe** = ANO
* **Tipo de Retorno** = Valor
* **Função ANOCX** = Retorna ano-caixa.
* **Sintaxe** = ANOCX
* **Tipo de Retorno** = Valor
* **Função ANODT** = Retorna ano de uma data.
* **Sintaxe** = ANODT ('DATA')
* **Tipo de Retorno** = Valor

**Exemplo:**  
ANODT('23/01/1997')  
Retorna: **1997**  
ANODT (DNASCIM)  
Supondo que a data de nascimento de um funcionário seja 10/09/1961, retorna **1961**.  
**Dica:** No parâmetro DATA da sintaxe pode ser uma função que retorna data no lugar da data específica.

* **Função ARRED** = Arredonda um valor sem casas decimais.
* **Sintaxe** = ARRED (VALOR)
* **Tipo de Retorno** = Valor
* **Função ARREDONDA =** Arredonda um valor com casas decimais.
* **Sintaxe** = ARREDONDA (VALOR, VALOR)
* **Tipo de Retorno** = Valor

**Exemplo:**   
Quando há várias casas decimais e o arredondamento será apenas para duas casas decimais:   
ARREDONDA(777.7784,2) = 777,78

* **Função ARREDVALOR** = Arredonda um valor com casas decimais.
* **Sintaxe** = ARRED (VALOR, VALOR)
* **Tipo de Retorno** = Valor
* **Função ASCII** = Retorna o código ASCII de um caractere.
* **Sintaxe** = ASCII ('STRING')
* **Tipo de Retorno** = Valor
* **Função ATRIBUI** = Atribui valor a uma memória.
* **Sintaxe** = ATRIBUI(NÚMERO DA MEMÓRIA, INDEFINIDO**)**
* **Tipo de Retorno** = De acordo com o que for atribuído à memória

**Exemplo:**  
ATRIBUI (1, RC)  
Memória de nº 1 guardará valor do salário nominal.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Cadastro de Fórmulas](http://tdn.totvs.com.br/pages/viewpage.action?pageId=403746924)  
Fórmulas Específicas do Módulo Folha de Pagamento
