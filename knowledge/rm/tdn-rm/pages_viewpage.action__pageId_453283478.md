---
content_hash: 08d88dac90c563db8fc5730346918260d4044ddab0f1ad89693a24713791fe83
fetched_at: '2026-06-29T00:10:11.780422+00:00'
page_id: '453283478'
product: rm
source: tdn-rm
title: Gestão - Funções de Fórmulas - Condomínio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453283478
version: 13
---

As funções de fórmulas do módulo condomínio, são utilizadas para realizar cálculos e manipulações de dados quando associadas a alguns campos que possibilitam utilização de fórmulas. Essas funções são essenciais para automatizar operações, realizar análises e gerar resultados com base em dados fornecidos. Aqui estão algumas finalidades comuns das funções de fórmulas.

---

\*TABMEDIDOR

Esta função tem como finalidade obter os valores de campos específicos do medidor e seus anexos, como medições e tarifas associadas. Ela pode ser empregada na fórmula registrada na tarifa do medidor, a qual é executada durante o processo de Calcular Fechamento do condomínio.

Os campos a seguir podem ser utilizados na função para obter o valor:

APLICACAOFRMTARIFA  
COD\_PESS\_EMPR  
CODCOLFRMTARIFA  
CODFRMTARIFA  
CODITEMCOBRANCA  
COMPETENCIA  
CONSTANTE  
CONSUMO  
DATAFINAL  
DATAFINALASSOCIACAO  
DATAINICIAL  
DATAINICIALASSOCIACAO  
DATAMEDICAO  
DESCMEDIDORPAI  
DESCRICAO  
IDCONDMEDIDOR  
IDCONSUMO  
IDFECHAMENTO  
IDMEDIDORSUPERIOR  
IDTARIFA  
MODELOCALCRATEIO  
VALOR

Exemplos de utilização de fórmulas

Os exemplos abaixo fornecem orientações sobre o uso da função `TABMEDIDOR` para extrair informações específicas de campos, como consumo, código do empreendimento e competência. Eles ilustram como obter valores formatados, como 'V' para Valor ou 'D' para Data e Hora.  **Modelo para Consumo:**

***TABMEDIDOR('CONSUMO','V')***Descrição: Primeiro argumento nome do campo. Segundo argumento tipo do campo. Legenda: (V = Valor; I = Inteiro; S = Conjunto de Caracteres; D = Data e Hora).

---

**Modelo para Código do empreendimento:**

***TABMEDIDOR('COD\_PESS\_EMPR', 'V')***   
Descrição: Primeiro argumento nome do campo. Segundo argumento tipo do campo. neste exemplo de fórmula possibilitará retornar o código do empreendimento.  
  
Exemplo de sua utilização:

A condição ***`TABMEDIDOR('COD_PESS_EMPR', 'V') + 100`*** refere-se a uma fórmula que envolve a função `TABMEDIDOR`. Vamos analisar essa expressão:

1. `TABMEDIDOR('COD_PESS_EMPR', 'V')`: Esta parte da expressão utiliza a função `TABMEDIDOR` para retornar o código do empreendimento 'COD\_PESS\_EMPR' com a formatação 'V' (indicando um valor).
2. `+ 100`: Após obter o valor associado do campo 'COD\_PESS\_EMPR', a expressão soma 100 a esse valor.

Portanto, o resultado dessa expressão retornará o código empreendimento (relacionado ao campo 'COD\_PESS\_EMPR') somado com 100. Em resumo, essa fórmula resulta o código do empreendimento acrescido de 100.

---

**Modelo para Competência:  
  
*TABMEDIDOR('COMPETENCIA','D')***   
Descrição: Primeiro argumento nome do campo. Segundo argumento tipo do campo. neste exemplo de fórmula possibilitará retornar a competencia (quando informad mais uma condição.  
  
Exemplo de sua utilização utilizando a condição SE:

***SE***

***TABMEDIDOR('COMPETENCIA','D') = ("01/2022")***

***ENTAO 5***

***SENAO 100***

A condição apresentada está utilizando uma função chamada `TABMEDIDOR` para verificar se o valor associado ao campo 'COMPETENCIA' (competência) é igual a "01/2022". Vamos analisar a expressão passo a passo:

1. `TABMEDIDOR('COMPETENCIA','D')`: Esta parte da expressão utiliza a função `TABMEDIDOR` para obter o valor associado ao campo 'COMPETENCIA' com a formatação 'D' (referindo-se a data). Isso é comparado com a string "01/2022".
2. `= ("01/2022")`: Esta parte compara o valor obtido com a string "01/2022".

A condição completa diz o seguinte:

* Se o valor associado ao campo 'COMPETENCIA' for igual a "01/2022", então o resultado é 5.
* Caso contrário, se o valor associado ao campo 'COMPETENCIA' for diferente de "01/2022", o resultado é 100.

Em resumo, essa condição atribui o valor 5 se a competência for janeiro de 2022 e 100 para qualquer outra competência.

Para mais informações sobre utilização de fórmulas e suas funções acesse:
