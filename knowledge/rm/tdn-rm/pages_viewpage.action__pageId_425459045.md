---
content_hash: 3ad229ca66127660f606b2e6f2444dc8aedb5889212334057abbcafc696a3321
fetched_at: '2026-06-29T00:09:33.770290+00:00'
page_id: '425459045'
product: rm
source: tdn-rm
title: Parâmetros do Tipo de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459045
version: 9
---

**Parâmetros do Tipo de Atendimento**

---

Pode ocorrer devido as regras de negócios (área de domínio) da empresa, a necessidade de armazenar informações que não são solicitadas no atendimento. Para esta situação o sistema disponibiliza os parâmetros do atendimento, um campo adicional que pode ser personalizado de acordo com a informação que será armazenada e que podem ser associados a determinados tipos de atendimento. No cadastro diferentes tipos de parâmetros podem ser criados utilizando os formatos disponíveis.  
   
São campos extras que podem ser customizados de acordo com as regras de negócio da empresa. De diferentes tipos de formato, eles atendem a necessidade de gravar informações suplementares aquelas pré-definidas no atendimento. Os formatos podem ser:  
   
**Inteiro** = Valores numéricos inteiros.  
Ex: Quantidade Dias para Solução Atendimento = 10.  
   
**String** = Informações textuais, sendo necessário limitar o tamanho do parâmetro em caracteres.  
Ex.: Complemento da Solicitação = Esta solicitação possui autorização do gestor da área.  
   
**Real** = Valores numéricos fracionados. Números Decimais.  
Ex.: Valor da Requisição = R$ 1000,00.  
   
**Data** = Informação referente ao tempo. Dia/Mês/Ano.  
Ex.: Data Nascimento Cliente = 01/01/1980.  
   
**Texto** = Informações textuais sem limitação pré-definida.  
Ex.: Complemento do Atendimento = Todas as documentações necessárias foram enviadas em formato digital. Favor confirmar resolução e quantidade de arquivos enviados.  
   
**Lógico** = Informações para serem marcadas através de flag´s (Checkbox).  
Ex.: Possui carteira de habilitação?   X Sim      Não  
   
**Link** = Informações que ligam a outros componentes. Ele se subdivide em:

* *E-mail* = Endereço eletrônico para troca de mensagem. Aciona automaticamente o gerenciador de email padrão da máquina. Ex.: [teste@teste.com.br](mailto:teste@teste.com.br)
* *URL* = Aciona o navegador padrão do sistema com o endereço digitado. Ex.: [{+}](http://www.totvs.com/)<http://www.totvs.com+>
* *SkypeLink* = Endereço do usuário de Skype, utilizado para comunicação de voz, vídeo, troca de mensagens entre outros. Aciona o Skype com o endereço informado. Ex.: Usuário = teste.skype

**Tabela =** Informações que são armazenadas através de linhas e colunas nas quais é possível inserir outros tipos de parâmetros, como por exemplo, inteiro, lógico, texto, data etc. A seleção dos registros pode ser dividida em setenças SQL e action´s.

* **Atenção:** Só funciona para winforms.

**Parâmetro baseado em sentença SQL** = Trata-se de um tipo especial de parâmetro, nele o usuário seleciona uma sentença SQL do sistema e ele será apresentado como um lookup, dando a opção do usuário selecionar algum campo resultante dessa sentença para ser o valor do parâmetro. Ao criar a sentença SQL desse parâmetro, é importante ter em mente que nem toda sentença poderá ser usada, ela deve seguir alguma regras importantes de formatação, segue abaixo pontos importantes que devem ser observados:

* O primeiro campo do select deve ser a descrição do campo, de preferência um texto claro indicando ao usuário o que é esse registro.
* O segundo campo deve ser um código único e não nulo, caso ele se repita o sistema não conseguirá encontrar sua descrição em posterior acesso a esse registro.
* Os dois primeiros campos devem ser colunas reais do banco de dados, não é recomendado o uso de campos calculados, mas caso for indispensável, o alias dele deve ser igual ao nome da primeira coluna usada.
* A sentença deve conter a TAG /\*WHERE\*/ ou /\*AND\*/ no local apropriado para que o sistema consiga incluir um filtro no lugar dessa TAG
* Devido ao uso de TAGs, a sentença não deve possuir nenhum trecho comentado (Além da TAG obrigatória).
* É recomendado que a sentença esteja dentro de uma subquery como o modelo abaixo:

                                       SELECT CAMPO1, CAMPO2 FROM (

                                                    SUASENTENCA

                                        ) TABELA /\*WHERE\*/

           Note que nesse caso, a TAG /\*WHERE\*/ já está no lugar apropriado.

* Segue abaixo alguns exemplos de sentenças SQL válidas e inválidas:

**Sentença válida ideal**

          SELECT NOME, CODIGO FROM (  
                                                    SELECT NOME, CODIGO FROM PPESSOA  
                                        ) TABELA /\*WHERE\*/

**Sentença inválida**

          SELECT NOME, MEUCODIGO FROM (  
                          SELECT NOME, (APELIDO + ' - ' + SEXO) AS MEUCODIGO FROM PPESSOA  
                          ) TABELA /\*WHERE\*/

          Motivo dela ser inválida: Essa sentença tem vários problemas

          1 - Será salvo no atendimento o valor do campo MEUCODIGO, esse valor é a concatenação do apelido e do sexo da pessoa, é um valor que pode se repetir causando inconsistência ao se abrir o registro.

          2 - O campo pode ser nulo, fazendo com que o sistema não tenha um valor para salvar.

          3 - O segundo campo é um campo calculado cujo alias não é uma coluna real do banco, também é importante que seja usado como alias o mesmo nome da primeira coluna que compõe o campo calculado, podemos ver isso melhor no exemplo abaixo, repare na coluna que está em negrito.

**Sentença válida porem não ideal**

**A seguinte alteração resolve o problema '3' da lista acima, mas a inconsistência ainda ocorrerá caso o campo se repita ou seja nulo:**

         SELECT NOME, **APELIDO** FROM (  
                          SELECT NOME, (**APELIDO** + ' - ' + SEXO) AS **APELIDO** FROM PPESSOA  
                          ) TABELA /\*WHERE\*/

           Nesse exemplo, usamos um campo calculado composto pelas colunas APELIDO e SEXO, como APELIDO é a primeira coluna, ela deve ser usada como alias.

**Filtrar sentença SQL com dados do atendimento**

          É possível filtrar uma sentença usada em um parâmetro por qualquer campo do atendimento, para isso, basta usar seu nome, como está no banco de dados, na cláusula WHERE precedida do caractere :

          Segue abaixo um exemplo de como ficaria um parâmetro filtrado pela coligada do atendimento

               SELECT MAQUINA, CODATENDENTE FROM HATENDENTE (NOLOCK)   
                           WHERE CODCOLIGADA = :CODCOLIGADA

**Observações:**  
Os parâmetros associados ao tipo de atendimento são apresentados na aba Parâmetros na edição dos atendimentos. Setenças SQL e actions também podem ser vinculadas.

Para sentenças SQL que possuam action , a action será executada na edição do atendimento. Para associar uma Action a sentença sql será necessário que na consulta sql personalizada tenha como colunas a chave primária da action desejada.   
Ex: SELECT ASSUNTOOC, CODATENDIMENTO , CODCOLIGADA, CODLOCAL , CODATENDIMENTO FROM HATENDIMENTOBASE Nesse exemplo,  o parâmetro é montado na forma padrão como  lookup . Ele irá utilizar a primeira coluna ASSUNTOOC para ser a descrição do lookup , a segunda coluna CODATENDIMENTO como o código do lookup e ao associar a Action de atendimento CRMATENDIMENTOEXTACTION a essa sentença a chave primária da action será associada as colunas da sentença no caso a chave primária do atendimento (CODCOLIGADA , CODLOCAL , CODATENDIMENTO).
