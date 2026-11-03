---
content_hash: 83c6d90c32feb16db8cdfcf9a40c128f36c3e402655369268189eea75ca99f95
fetched_at: '2026-06-29T00:10:56.806371+00:00'
page_id: '593047841'
product: rm
source: tdn-rm
title: CRIAÇÃO FÓRMULA VISUAL - Copiar Dados Contador/Representante entre Filiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593047841
version: 34
---

## **Objetivo**

Este documento visa demonstrar como implementar uma fórmula visual no RM Gestão Fiscal para copiar/alterar dados cadastrais do Contador  das Filiais (o mesmo procedimento serve para os dados do Representante. Também podendo ser utilizado para outras necessidades).

## **Necessidade**

Quando um Representante ou um Contador precisam ter seus dados incluídos/alterados em uma ou mais Filiais, o procedimento é realizado Filial por Filial, tornando-se um processo lento e passível de erros.

## **Solução**

Foi criada uma Fórmula Visual buscando facilitar o processo citado, de forma que a manipulação dos dados possa ser realizada em massa e minimizando os erros. A Fórmula Visual irá copiar os dados de uma Filial selecionada para outras filiais/coligadas selecionadas pelo usuário durante o processo.

## **Passo-a-passo de como criar a Fórmula Visual**

Observação: Caso a fórmula visual não seja criada exatamente igual ao passo-a-passo (seguindo inclusive a mesma sequencia) o nome das atividades podem alterar e consequentemente será necessário ajustar os vários parâmetros da fórmula visual para os novos nomes.

falseFormulas1º Passo

Para se criar uma Fórmula Visual basta acessar o módulo de **Serviços Globais** - aba **Gestão | Ferramentas de Análise | Fórmula Visual | Fórmula Visual**

Imagem

Uma aba se abrirá. Clique em Incluir.

Imagem

Escolha um nome e a categoria da Fórmula, marque-a como Ativo, e se quiser coloque uma descrição e clique em OK.

Imagem2º Passo

Dê um duplo clique na Fórmula criada para abrir sua edição.

Imagem

A seguinte aba irá se abrir, e é aqui que iremos iniciar o desenho de nossa fórmula.

Imagem3º Passo

A Fórmula Visual tem por objetivo copiar os dados de uma Filial selecionada para as demais filiais informadas no processo. Para isto, será necessário adicionar uma validação para que o processo somente execute caso tenha apenas uma filial selecionada.

Adicionando a validação para que não permita executar o processo caso possua mais de uma filial selecionada.

Selecione uma nova atividade de "Se/Senão".

Imagem

Arraste para o Fluxo da Fórmula Visual.

Imagem

Clique com o botão direito do mouse em um dos lados da atividade "Se/Senão" e selecione a opção Excluir.

Imagem

Selecione no lado que ficou da atividade, nas propriedades em Condition seleciona a opção "Condição de Regra Declarativa".

Imagem

Expanda a Condition e no campo ConditionName clica nos três pontinhos (...).

Imagem

Adicione uma nova Condition com a informação abaixo. Após isto, salve o registro e selecione a condition.

Informação da Condição: this.Tables[0].DataTable.Rows.Count > 1

Imagem

Selecione uma nova atividade de Exceção e arraste para dentro da condição adicionada anteriormente.

Imagem

Selecione a atividade de Exceção adicionada no Fluxo, na aba Propriedades adicione a mensagem que será exibida para o usuário.

Obs: A mensagem pode ser customizada conforme a necessidade da empresa.

Imagem4º Passo

Adicionando a consulta SQL que irá selecionar os dados de da Filial de Origem a serem copiados para a(s) filial(is) de destino.

Selecione uma nova atividade de Consulta SQL e arraste para o Fluxo da Fórmula Visual (Abaixo da atividade Se/Senão adicionada anteriormente).

Imagem

Clique com o botão direito do mouse em cima da atividade de Consulta SQL e selecione a opção "Selecionar Consulta SQL".

Imagem

Clique no ícone para incluir uma nova consulta e adicione uma consulta SQL que retorne os campos que deseja copiar. Exemplo:

SELECT \* FROM DFILIAL (NOLOCK)  
WHERE CODCOLIGADA = :CODCOLIGADA  
AND CODFILIAL = :CODFILIAL

Importante: O SQL deve possuir a coligada e filial como parâmetro no WHERE conforme exemplo acima para conseguir pegar os dados da Filial selecionada.

Imagem

Selecione a consulta SQL criada anteriormente.

Imagem

Selecione a Atividade de Consulta SQL adicionada e preencha os parâmetros nas Propriedades.

**CODCOLIGADA:** Activity=RMSWorkflow, Path=Tables[0].Item["CODCOLIGADA"].AsShort

**CODFILIAL:** Activity=RMSWorkflow, Path=Tables[0].Item["CODFILIAL"].AsShort

Imagem5º Passo

No processo o usuário precisará selecionar a(s) filial(is) de destino para onde os dados serão copiados. Neste passo será criado os parâmetros do processo para o usuário preencher.

Clicar em Fluxo de Trabalho Sequencial e acessar a aba de Propriedades (Essas são as propriedades da Fórmula Visual).

Imagem

Na parte de Parâmetros em Definição dos Parâmetros clicar nos três pontinhos (...).

Imagem

Clicar no ícone para adicionar uma nova tabela de parâmetros e colocar o nome da tabela = PARAMETROS e clicar em Ok.

Imagem

Selecionar a tabela de parâmetros criada na lateral esquerda e preencher os campos conforme abaixo:

CODCOLIGADA - Código da Coligada - Opcional desmarcado - Visível marcado - Tipo System.Int16

CODFILIALINICIAL - Código da Filial de Destino Inicial - Opcional desmarcado - Visível marcado - Tipo System.Int16

CODFILIALFINAL - Código da Filial de Destino Final - Opcional desmarcado - Visível marcado - Tipo System.Int16

Imagem6º Passo

Adicionando a consulta SQL para retornar os dados da(s) filial(is) de destino que foram selecionadas nos parâmetros.

Selecione uma nova atividade de Consulta SQL e arraste para o Fluxo da Fórmula Visual (Abaixo da outra atividade de Consulta SQL adicionada anteriormente).

Imagem

Clique com o botão direito do mouse em cima da atividade de Consulta SQL adicionada no passo anterior e selecione a opção "Selecionar Consulta SQL".

Imagem

Clique no ícone para incluir uma nova consulta e adicione uma consulta SQL que retorne os dados da(s) filial(is) de destino. Exemplo:

SELECT CODCOLIGADA, CODFILIAL FROM DFILIAL (NOLOCK)  
WHERE CODCOLIGADA = :CODCOLIGADA  
AND CODFILIAL >= :CODFILIALINICIAL  
AND CODFILIAL <= :CODFILIALFINAL

Importante: O SQL deve possuir a coligada, filial inicial e filial final como parâmetro no WHERE conforme exemplo acima para conseguir pegar os dados preenchidos nos parâmetros do processo.

Imagem

Selecione a consulta SQL criada anteriormente.

Imagem

Selecione a Atividade de Consulta SQL adicionada e preencha os parâmetros nas Propriedades.

**CODCOLIGADA:** Activity=RMSWorkflow, Path=ParameterTables["PARAMETROS"].Item["CODCOLIGADA"].AsShort

**CODFILIALFINAL:** Activity=RMSWorkflow, Path=ParameterTables["PARAMETROS"].Item["CODFILIALFINAL"].AsShort

**CODFILIALINICIAL:** Activity=RMSWorkflow, Path=ParameterTables["PARAMETROS"].Item["CODFILIALINICIAL"].AsShort

Imagem7º Passo

Será necessário validar se os filtros informados pelo usuário no processo encontrou pelo menos uma filial de destino.

Selecione uma nova atividade de Se/Senão e arraste para o Fluxo da Fórmula Visual (Abaixo da segunda atividade de Consulta SQL adicionada no passo anterior).

Imagem

Clique com o botão direito do mouse em um dos lados da atividade "Se/Senão" adicionada anteriormente e selecione a opção Excluir.

Imagem

Selecione no lado que ficou da atividade, nas propriedades em Condition seleciona a opção "Condição de Regra Declarativa".

Imagem

Expanda a Condition e no campo ConditionName clica nos três pontinhos (...).

Imagem

Adicione uma nova Condition com a informação abaixo. Após isto, salve o registro e selecione a condition que acabou de ser criada.

this.rmsConsSQLActivity2.Tables[0].DataTable.Rows.Count == 0

Imagem

Selecione uma nova atividade de Exceção e arraste para dentro da condição adicionada anteriormente.

Imagem

Selecione a atividade de Exceção adicionada anteriormente, na aba Propriedades adicione a mensagem que será exibida para o usuário.

Obs: A mensagem pode ser customizada conforme a necessidade da empresa.

Imagem8º Passo

Como pode encontrar várias filiais de destino, será necessário percorre-las para executar a copia em cada filial.

Selecione uma nova atividade de ForEach e arraste para o Fluxo da Fórmula Visual (Abaixo da segunda atividade de Se/Senão adicionada no passo anterior).

Imagem

Selecione a atividade de ForEach adicionada, acesse a aba Propriedades e clique no ícone **Ligações**.

Imagem

No campo **Lista de Items**, apague a informação (nenhum) e preencha o campo com o valor abaixo:

Activity=rmsConsSQLActivity2, Path=Tables[0].Rows

Imagem

Selecione uma nova atividade de Sequência e arraste para dentro do ForEach adicionada anteriormente.

Imagem9º Passo

Abrindo o DataSet da(s) Filial(is) de Destino para poder copiar as informações.

Selecione uma nova atividade de Ler Registro e arraste para dentro da atividade de Sequencia adicionada no passo anterior.

Imagem

Selecione a atividade de Ler Registro adicionada, na aba Propriedades preencha o Nome do DataServer = FisFilialFiscalData e aperte Tab no teclado.

Imagem

Preencha os campos abaixo com as seguintes informações:

**Código da Coligada:** Activity=rmsForEachActivity1, Path=Fields["CODCOLIGADA"].AsShort

**Código da Filial:** Activity=rmsForEachActivity1, Path=Fields["CODFILIAL"].AsShort

Imagem10º Passo

Copiando as informações para a(s) filial(is) de destino.

**IMPORTANTE:** No exemplo informamos apenas o Nome e o Bairro do Contador. Pode adicionar mais campos conforme a necessidade da empresa. O mesmo processo é utilizado para as informações do Contador e Representante. Então, caso queira preencher outros campos, basta adicionar uma Expressão para cada campo desejado e informar o nome do campo na base de dados. Abaixo exemplo dos dois campos.

Selecione uma nova atividade de Expressão e arraste para dentro da atividade de Sequencia, abaixo da atividade de Ler Registro.

Imagem

Selecione a atividade de Expressão adicionada, na aba Propriedades preencha os campos abaixo:

**Expressões:** Valor Original (Ex: rmsConsSQLActivity1.NOMECONTADOR)

**Valor Calculado:** Campo de Destino (Ex: Activity=rmsReadRecordActivity1, Path=Fields["NOMECONTADOR"].AsString)

**Obs:** Para os demais campos desejados, basta mudar o nome do campo nos parâmetros acima. Este exemplo é do campo NOMECONTADOR.

Imagem

Exemplo de uma nova Expressão adicionada para o Bairro do Contador.

**Expressões:** rmsConsSQLActivity1.BAIRROCONTADOR

**Valor Calculado:** Activity=rmsReadRecordActivity1, Path=Fields["BAIRROCONTADOR"].AsString

Imagem

Observação: Pode-se adicionar quantas expressões forem necessárias. Uma para cada campo que deseja copiar, com as suas origens e destinos preenchidos corretamente conforme demonstrado acima.

11º Passo

Fechando o DataSet da(s) Filial(is) de Destino após copiar as informações.

Selecione uma nova atividade de Salvar Registro e arraste para dentro da atividade de Sequencia adicionada no passo anterior (Abaixo das Expressões).

Imagem

Selecione a atividade de Salvar Registro adicionada, na aba Propriedades preencha o campo **Atividade Ler Registro** com a atividade adicionada no Passo 9.

Imagem12º Passo

Salvando a Fórmula Visual.

Clique no ícone Salvar para que a fórmula visual criada seja salva.

Imagem

## **Passo-a-passo para associar a Fórmula Visual como um Processo no cadastro de Filiais**

A fórmula visual será associada na tela de cadastro de Filiais como um "Processo" onde os usuários poderão executa-la quando necessário.

falseConfigurando1º Passo

Após criado/importado a Fórmula Visual devemos acessar **Gestão Fiscal | Cadastros | Globais | Filiais | Processos | Fórmula Visual | Gerenciar**

Imagem2º Passo

A seguinte janela de Gerenciamento de Fórmula Visual se abrirá.

Basta selecionar a aba **Processos de Fórmula Visual** e clicar no ícone de **Processos - Adicionar Fórmula Visual** (destacado em vermelho)

Imagem3º Passo

A janela de **Fórmula Visual** se abrirá.

Imagem

Basta selecionar a fórmula desejada, clicar em **OK.** O registro ficará da seguinte forma:

Imagem

## **Executando o processo disponível no cadastro de Filiais**

Exemplo de utilização do processo disponibilizado para os usuários de Cópia das Informações para as Filiais. O processo será exibido para os usuários no cadastro de Filiais e poderá ser executado quando necessário.

falseConfigurando1º Passo

Após todos os passos, chegou o momento em que iremos utilizar a Fórmula Visual, para isto basta acessar **Gestão Fiscal | Cadastros | Globais | Filiais**

No exemplo, iremos copiar os dados da Filial nº 1.

Para verificar como está a informação do Nome e Bairro do Contador da Filial 1, selecionar a Filial e clicar em **Anexos | Dados Fiscais** e selecionar a aba **Contador**

Imagem2º Passo

Neste passo, vamos alterar alguns dados do Contador.

No exemplo, iremos alterar os campos:

**Nome**

**de:** Décio Antonio da Silva

**para:** João da Silva

**Bairro**

**de:** Funcionarios

**para:** São Bento

Realizar as alterações e salvá-las.

Imagem3º Passo

Após realizadas as alterações do Contador na Filial 1 (mudanças do campo: nome e bairro) e salvá-las, vamos aplicar as alterações para outras Filiais.

Para isto, vamos selecionar a Filial 1, clicar em **Processos | Fórmula Visual | Alterar Dados Contador Por Filial** (Fórmula Visual Cadastrada)

Imagem4º Passo

Uma janela se abrirá e nela iremos preencher os seguintes dados:

**Código da Coligada** - O Código da Coligada da(s) filial(is) de Destino, para onde você deseja copiar os campos. (No exemplo irei utilizar a 1)

**Filial início** - Corresponde ao Código da Filial Inicial de Destino, para onde você deseja copiar os campos . (No exemplo irei utilizar a 2)

**Filial Final** - Corresponde ao Código da Filial Final Destino, para onde você deseja copiar os campos . (No exemplo irei utilizar a 4)

Neste exemplo, será copiado as informações para as filiais 2, 3 e 4 da Coligada 1.

Imagem

Após preenchidos os dados, basta clicar em executar.

A Filial Inicial não pode ser maior do que a Filial Final. Ex.:

**Filial Início:** 4

**Filial Final:** 2

5º Passo

Após executado o processo, vamos abrir as Filiais 2, 3 e 4 e verificar se as alterações foram aplicadas.

12Filial 2 - AntesFilial 2 - DepoisFilial 3 - AntesFilial 3 - DepoisFilial 4 - AntesFilial 4 - Depois

Em resumo, estamos copiando a informação dos campos Nome e Bairro dos dados do Contador da Filial 1 para as Filiais 2, 3 e 4.

**Observação:**

As fórmulas Visuais podem ser importadas e exportadas entre as bases (Por exemplo criar em homologação e depois importa-la para o ambiente de Produção).

Para isto, basta seguir procedimento de Importação disponível no link abaixo:

[Importar/Exportar Fórmula Visual](https://tdn.totvs.com/x/34vFAw)

Dados Contador e RepresentanteDadosContador

 Os dados de Contador e Representante podem ser encontrados no módulo **Gestão Fiscal | Cadastros | Globais | Filiais | Anexos | Dados Fiscais**:

Imagem
