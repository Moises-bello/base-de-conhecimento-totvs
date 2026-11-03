---
content_hash: e382e0037f653d4201ea47cf12f48b97f56652fdbba3ee93c16f3d110554e56b
fetched_at: '2026-06-29T00:12:15.158055+00:00'
page_id: '971940890'
product: rm
source: tdn-rm
title: FAQ Falhas importação Tabela de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=971940890
version: 10
---

A importação possui um padrão de mensagens para facilitar o entendimento e solução de possíveis problemas.

Quando ocorrerem falhas que iniciam com a palavra '**Linha**', a falha está relacionada a dados inválidos encontrados na linha informada, por exemplo:

* '**Linha 10 - Está em duplicidade'**
* **'Linha 55 - A disciplina COD\_DISCIPLINA: 'Português', não possui vínculo com a matriz aplicada ID\_MATRIZ\_APLICADA: 123 , COD\_CURSO: '4-1', COD\_HABILITACAO: '4-4-1', verifique os dados informados no 'arquivo .csv''**

Os outros tipos de falha geralmente estão relacionados a problemas estruturais do 'arquivo .csv'. Alguns exemplos são:

* **Existem linhas com dados diferentes dos dados da tabela de preço, por favor validar linhas com valores diferentes dos seguintes: COD\_COLIGADA: 1, COD\_NIVEL\_ENSINO: 1, COD\_TABELAPRECO: Código Tabela**
* **É esperado que existam no total 8 colunas, o número de colunas 2 no arquivo não corresponde ao esperado.**

## 1- Dados diferentes dos dados da tabela de preço

Esta falha ocorre quando algum dos dados usados como chave da tabela de preço está incorreto no arquivo 'arquivo .csv'. Ou seja o código da coligada, código do nível de ensino e o código da tabela de preço informada no 'arquivo .csv' devem ser iguais aos dados da tabela de preço onde os dados estão sendo importados.

**Existem linhas com dados diferentes dos dados da tabela de preço, por favor validar linhas com valores diferentes dos seguintes: COD\_COLIGADA: 1, COD\_NIVEL\_ENSINO: 1, COD\_TABELAPRECO: Código Tabela.**

Os dados enviados no arquivo .csv não correspondem aos dados da tabela de preço. Ou seja, existem linhas no arquivo .csv que estão com dados diferentes dos dados da tabela de preço.

Dados do .csv:

COD\_COLIGADA: 1

COD\_NIVEL\_ENSINO: 1

**COD\_TABELAPRECO: Teste 123**

Dados da tabela de preço:

COD\_COLIGADA: 1

COD\_NIVEL\_ENSINO: 1

**COD\_TABELAPRECO: Código Tabela**

O problema está na coluna **COD\_TABELAPRECO.** No está cadastrada como '**Código Tabela**' e no .csv está como '**Teste 123**'

## Solução

#fff

1. Verificar as informações retornadas na mensagem e corrigir todas linhas do 'arquivo .csv' que estão com dados divergentes da tabela de preço.

---

## 2 - Disciplina não possui vínculo com a matriz aplicada

Esta falha ocorre quando existem dados inconsistentes na linha apontada. A inconsistência pode estar no código da disciplina (pode estar inválido) ou o id da matriz aplicada que pode estar inválido ou não possui vinculo com a disciplina.

**Linha 2 - A disciplina código: '0001\_ES', não possui vínculo com a matriz aplicada ID\_MATRIZ\_APLICADA: 500 , COD\_CURSO: '4-1', COD\_HABILITACAO: '4-1-1', verifique os dados informados no 'arquivo .csv'**

## Solução

#fff

1. Verificar se a coluna **ID\_MATRIZ\_APLICADA**informada no 'arquivo .csv' está correta
2. Verificar se a coluna **COD\_DISCIPLINA** informada no 'arquivo .csv' está correta
3. Verificar se a matriz curricular vinculada a matriz aplicada informada na linha possui vinculo com a disciplina informada
4. Após a verificação corrigir os dados informados na linha

---

## 3 - Matriz curricular inativa

Esta falha ocorre quando a matriz curricular vinculada a matriz aplicada cujo ID foi informado na linha esta com 'Status' igual a 'Inativa'

**Linha 2 - Matriz curricular inativa.**

## Solução

#fff

1. Não é possível realizar a importação de dados de uma matriz curricular com 'Status' 'Inativa', para realizar a importação é preciso avaliar a melhor solução.
2. Possíveis soluções:
   1. Avaliar possibilidade de alterar o 'Status' da matriz curricular
   2. Avaliar uso de outra matriz aplicada vinculada a outra matriz curricular

---

## 4 - Falha de codificação de arquivo UTF-8

Este problema ocorre quando o texto do arquivo está codificado com algum tipo diferente de UTF-8. Esta situação pode gerar diversos problemas durante a importação.

Para que os dados do seu arquivo sejam importados corretamente pelo sistema, **é necessário que o arquivo esteja salvo com a codificação UTF-8**.

#### Mas o que isso significa?

Todo arquivo de texto, como um `.csv`, é armazenado no computador com uma **"codificação de caracteres"**. Essa codificação define **como os acentos, símbolos e letras especiais** (como ç, ã, ê, etc.) são gravados e lidos.

A codificação **UTF-8** é a mais utilizada atualmente, pois **suporta corretamente os caracteres da língua portuguesa** e de muitos outros idiomas.

Se o arquivo estiver com **outra codificação diferente**, como ANSI, ISO-8859-1 ou Windows-1252, o sistema **pode não interpretar corretamente os textos**. Isso causa problemas como:

* Troca de letras por símbolos estranhos (ex: "João" virar "JoÃ£o")
* Campos com erro de leitura
* Informações salvas de forma incorreta no sistema

Exemplos de erros devido a codificação diferente de UFT-8.

**Linha 8 - Falha, não foi encontrado o vínculo da disciplina código: '1� Disc' com a matriz aplicada id: 22.**  
**Linha 9 - Falha, não foi encontrado o vínculo da disciplina código: '1� Disc' com a matriz aplicada id: 46.**

No exemplo acima o código da disciplina contém o caractere 'ª' que não foi identificado corretamente durante a importação pois o arquivo não estava em UTF-8

Todos campos de texto no 'arquivo .csv' podem dar este tipo de problema se tiverem caracteres com acentos ou que sejam codificados, os campos são:

* **COD\_TABELAPRECO(**como é um campo chave, se houver erro de caractere inválido, a mensagem exibida está relacionada ao erro**"1- Dados diferentes dos dados da tabela de preço"**citado nesta mesma FAQ)
* **COD\_CURSO**
* **COD\_HABILITACAO**
* **COD\_DISCIPLINA**

## Solução

#fff

1. Ao salvar o arquivo (em Excel, Bloco de Notas, ou outro editor), **escolha sempre a opção "Salvar como" e defina a codificação como UTF-8**.  
   Se tiver dúvidas sobre como fazer isso, nossa equipe de suporte pode te ajudar.

---

## 5 - Coluna vazia ou nula

Esta falha ocorre quando alguma das colunas no 'arquivo .csv' está sem dados, ou com espaço em branco.

Apenas a coluna **VALOR\_CREDITOS**pode estar nula ou vazia, todas outras colunas são de preenchimento obrigatório.

**Linha 2, Coluna: COD\_COLIGADA - Não pode estar vazia ou nula.**

**Linha 3, Coluna: ID\_MATRIZ\_APLICADA - Não pode estar vazia ou nula.**

**Linha 4, Coluna: COD\_NIVEL\_ENSINO - Não pode estar vazia ou nula.**

**Linha 4, Coluna: COD\_CURSO - Não pode estar vazia ou nula.**

## Solução

#fff

1. Avaliar quais dados estão sem preenchimento na linha e informar os dados corretos.

---

## 6 - Linha em duplicidade

Esta falha ocorre quando existem linhas em duplicidade no 'arquivo .csv'.

**Linha 55 - Está em duplicidade**

## Solução

#fff

1. Confirmar quais linhas estão em duplicidade e remove-las.

---

## 7 - Falha de conversão do tipo de dados

Este comportamento ocorre quando os dados da coluna estão em um formato inválido.

Caso alguma coluna do tipo numérico esteja preenchida com o tipo texto, esta falha vai ocorrer.

As colunas que aceitam apenas números são: **COD\_COLIGADA, COD\_NIVEL\_ENSINO, ID\_MATRIZ\_APLICADA**e **VALOR\_CREDITOS**

## Solução

#fff

1. Os dados informados no 'arquivo .csv' devem seguir o seguinte padrão
   1. **COD\_COLIGADA**- código da coligada (numérico)
   2. **COD\_NIVEL\_ENSINO**- código do nível de ensino (numérico)
   3. **COD\_TABELAPRECO**- código da tabela de preço (texto - máximo de 20 caracteres)
   4. **ID\_MATRIZ\_APLICADA**- id da matriz aplicada (numérico)
   5. **COD\_CURSO**- código do curso (texto - máximo de 10 caracteres)
   6. **COD\_HABILITACAO**- código da habilitação (texto - máximo de 10 caracteres)
   7. **COD\_DISCIPLINA**- código da disciplina (texto - máximo de 20 caracteres)
   8. **VALOR\_CREDITOS**- valor dos créditos (número decimal - separador para casa de centavos é '**,**'. Não é preciso usar separador para casa de milhar (**Não usar '.'**)

---

## 8 - Não foi possível encontrar registros para importação

Este comportamento ocorre quando o 'arquivo .csv' não contém nenhum dado ou foi informada apenas 1 linha.

## Solução

#fff

1. Informar pelo menos duas linhas no 'arquivo .csv' com dados válidos

## 9 - É esperado que existam no total 8 colunas,  o número de colunas X no arquivo não corresponde ao esperado

**É esperado que existam no total 8 colunas, o número de colunas 5 no arquivo não corresponde ao esperado.**

Esta falha ocorre quando o arquivo .csv possui um número de colunas diferente de **8**. O sistema espera que sejam informadas 8 colunas no 'arquivo .csv', caso sejam informadas mais ou menos colunas este erro é exibido.

## Solução

#fff

1. Corrigir o 'arquivo .csv' informando as colunas corretamente.

---

## 10 - Utilizando o Excel para modificar os dados no 'arquivo .csv'.

Neste tópico trataremos sobre o uso do Excel como ferramenta para edição do arquivo de importação.

1. É muito importante ter cuidado ao abrir o arquivo .csv no Excel, muitas vezes as colunas do tipo texto podem conter informações que o Excel entenda como tipos incorretos, por exemplo, um texto que o Excel pode entender como data será alterado de forma automática e ficará incorreto. Por este motivo sugerimos que para edição no Excel utilize a função de importação.
2. Para importar o arquivo .csv para o Excel seguir os seguintes passos:
   1. Abra o Excel => Novo => Pasta de trabalho em branco
   2. Na planilha em branco acessar a aba "Dados" => "De Texto"
   4. Selecionar o arquivo que deseja abrir.
   5. Na tela seguinte do assistente de importação deixar como no print abaixo:
      1. Origem do arquivo: 65001: Unicode (UTF-8)
      2. Marcar a opção Meus dados possuem cabeçalhos.
   7. Clique em Avançar.
   8. Na etapa seguinte, **desmarcar** a opção **"Tabulação"** e marcar a opção "Ponto e vírgula". Em "Qualificador de texto: "{nenhum}"
   10. Em seguida clique em Avançar.
   11. Nesta etapa é possível marcar o tipo de dados de cada coluna.
   13. Na tela acima é possível selecionar cada uma das colunas e informar seu tipo de dados. Isso evita que o Excel interprete dados de forma incorreta.
   14. Estão marcados de vermelho o agrupador "Formato dos dados da coluna" e "Visualização dos dados". Podemos ver que na tabela de Visão dos dados existem várias colunas com o texto "Geral" sobre cada uma delas. Dentro de cada coluna tem o nome da coluna proveniente do 'arquivo .csv' e os respectivos dados que serão importados.
   15. É recomendado que as colunas **COD\_TABELAPRECO, COD\_CURSO, COD\_HABILITACAO e COD\_DISCIPLINA,**sejam do tipo texto. Para mudar do tipo Geral para texto, basta clicar sobre a coluna e sem seguida no agrupador "Formato dos dados da coluna" marcar a opção "Texto".
   17. Feito isso, basta concluir que os dados serão importados corretamente e poderão ser editados sem problemas.

##### Após as edições realizadas o processo recomendado para salvar o 'arquivo .csv' é o seguinte:

1. Por padrão o Excel salvar os arquivos com codificação ANSI, se a sua versão do Excel permitir siga os seguintes passos:
   1. Vá em **Arquivo > Exportar**
   2. Selecione **"Alterar o tipo do arquivo"**
   3. Escolha a opção **"CSV UTF-8 (delimitado por vírgulas) (\*.csv)"**
   4. Clique em **Salvar**
2. Caso a versão do Excel utilizada não tenha a opção de CSV UTF-8, siga os seguintes passos:
   1. Vá em **Arquivo > Exportar**
   2. Selecione **"Alterar o tipo do arquivo"**
   3. Escolha a opção **"CSV (delimitado por vírgulas) (\*.csv)"**
   5. Clique em Salvar
   6. Com o arquivo já salvo, abrir o arquivo no bloco de notas, em seguida vá em **Arquivo > Salvar como**
   7. Mudar o tipo de arquivo para **Todos os arquivos (\*.\*)** e mudar a **Codificação para: "UFT-8".**
   8. Mudar o nome do arquivo para .csv ao invés de .txt.
   10. Feito isso será possível importar o arquivo normalmente para o sistema.
