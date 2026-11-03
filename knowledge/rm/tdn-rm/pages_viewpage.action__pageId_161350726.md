---
content_hash: 1fb2c948339eff7159db1e45062e68301fde6f0386662b6ea7ca990034fa355f
fetched_at: '2026-06-29T00:05:57.015697+00:00'
page_id: '161350726'
product: rm
source: tdn-rm
title: FÓRMULA VISUAL - Atividade Expressão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=161350726
version: 8
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplos de utilização**
3. **Como cadastrar a Atividade de Expressão para executar em uma API**

## **01****.** **VISÃO GERAL**

O objetivo deste documento é mostrar como deve ser utilizada a atividade "Expressão" de uma Fórmula Visual.  

## **02. EXEMPLOS DE UTILIZAÇÃO**

### A. EXEMPLO 1

      Para nosso primeiro exemplo, utilizaremos as atividades "**Consulta SQL**", "**Expressão**" e "**Gerar Exceção**".

falseConfigurando o Aplicativo Confiável no ADFS1º Passo:

Primeiramente, é necessário arrastar a atividade "Consulta SQL" para o "fluxo de trabalho" sequencial em sua fórmula visual:

2º Passo:

Clique com o Botão direito do mouse na atividade e selecione uma consulta SQL:

3º Passo:

Utilizamos a seguinte Consulta SQL em nossa pesquisa:

* **Select** VALORORIGINAL **from** TFLAN **where** NUMERODOCUMENTO='00000433'

4º Passo:

Note que essa Consulta SQL está nos retornando um valor numérico com 4 casas decimais.  
Vamos utilizar a Atividade Expressão para converter esse valor para o formato 162,02.   
  
Adicione a Atividade Expressão:

5º Passo:

Após atividade ter sido adicionada ao fluxo de trabalho é necessário configurar as propriedades da atividade.  

Clique em  para montar a sua expressão.

| **Propriedades**   * **Nome:** Nome da Atividade * **Descrição:** Descrição da Atividade * **Habilitado:** Opção de habilitar ou desabilitar a atividade * **Expressões:** Expressões a serem calculadas, (separadas por * **Usar Valor Nulo:** Define se o valor deverá ser calculado caso o valor da expressão seja Nulo. * **Valor Calculado**: Valor Calculado da Expressão. |
| --- |

6º Passo:

Neste exemplo, iremos adicionar uma Expressão que utiliza a função "Format", que têm por objetivo formatar determinado valor.

7º Passo:

Na criação de sua expressão, observe que ao colocar o ponteiro do mouse encima da função, é exibida sua sintaxe. Como parâmetro para a expressão, podemos utilizar dados de outras atividades da Fórmula Visual (Como no exemplo, o valor de nossa Consulta SQL).

8º Passo:

A sintaxe da função "Format" é: Format("valor", "string máscara")

Em nosso exemplo, teremos como "valor" o resultado da nossa Consulta SQL e usaremos "'##,##0.00'" como string máscara.

Format( rmsConsSQLActivity1.VALORORIGINAL, "###,##0.00" )   
**Obs:** Na Expressão, usamos "," (Virgula) para separador de milhares e "." (Ponto) para separador decimal.

9º Passo:

Adicione a atividade Gerar exceção

10º Passo:

Nas propriedades da atividade Gerar Exceção, busque o valor da Expressão como Mensagem para verificar se realmente o valor da base foi convertido para a Máscara definida pela atividade Expressão.

11º Passo:

Salve, execute sua Fórmula Visual e verifique os dados.

      

### **B. EXEMPLO 2**

      Neste exemplo, utilizaremos a expressão dentro de um "**Para Cada Iteração**", utilizando o campo *Concatenar valor no campo calculado*:

exemplo21º Passo

Arraste as atividades "**Ler Visão**", "**Para Cada Iteração**", "**Expressão**" (duas) e "**Gravar Log do Processo**", conforme a ordem abaixo:

2º Passo

Na atividade *rmsReadViewActivity1*, insira no campo **Nome do Dataserver** o valor *GlbColigadaDataBR*, e no **Filtro**, o valor *1=1*.

Na atividade *rmsExpressionActivity1*, insira no campo **Expressões** o valor:

Na atividade **rmsForEachActivity1*, insira no campo **Lista de Items**, o valor:*

E, na última atividade (*rmsWriteLogAcitivity1*), insira, no campo **Informação**, o valor:

3º Passo

Agora, atentaremos à atividade principal, a *rmsExpressionActivity2*, na qual obteremos o valor a ser retornado:

No campo **Valor Calculado**, apontamos para o campo *Value* da atividade *rmsExpressionActivity1*:

Já no campo **Expressões** colocaremos a expressão a ser calculada, e concatenada na *rmsExpressionActivity1*, o seguinte valor:

Deixamos o campo **Concatenar valor no campo calculado** como *True*.

Resultado

Ao **Salvar e Executar**, obteremos o seguinte resultado:

Observe que o campo **Concatenar**fez com que a expressão 2 concatenasse seus valores durante o laço de repetição causado pela atividade *Para Cada Iteração*.  
Caso esse campo fosse marcado como *False*, obteríamos apenas a última expressão gerada:

## **03****.** **COMO CADASTRAR A ATIVIDADE DE EXPRESSÃO PAR EXECUTAR EM UMA API**

      Para o exemplo vamos utilizar o contexto de usuário (UserControllerServer) juntamente com as atividades de **"Expressão"** e **"Gerar Exceção",** para trazer os campos UserName e FormatedName depois de recuperar um (GET) na API de usuário

      Leia mais sobre [Fórmula Visual em API](https://tdn.totvs.com/x/9YynI)

* A Fórmula Visual deve estar cadastrada com a opção Executa em API (POCO)habilitada, conforme exibido na imagem abaixo.

* Para o exemplo utilizado, é necessário adicionar o gatilho o "UserControllerServer" no gatilho "Depois de recuperar (get)", para que a nossa formula retorne corretamente o resultado da expressão.

      Na Atividade de expressão,  foi selecionado o campo "**Expressão**" e parametrizado para ser visualizado os campos UserName e FormatedName como mostra a imagem abaixo:

      No campo **"Valor Calculado",** foi selecionado a atividade de **"Gerar Exceção",**para visualizar a mensagem da expressão como mostra a imagem abaixo:

      Após salvar a fórmula, é necessário acessar a API de Usuários para realizar um "GET" e visualizar o resultado da expressão, como mostra a imagem abaixo:
