---
content_hash: ffaad209f44c6bfdb4e8ec9f8db5d27ff4fb83f44d9825438c935518dbff3af7
fetched_at: '2026-06-29T00:10:52.149175+00:00'
page_id: '570360348'
product: rm
source: tdn-rm
title: Pacotes de Procedimentos e Pacotes de Diária Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570360348
version: 32
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Cadastrar um Pacote**
3. **Itens Extra Pacote**
4. **Faixa de Codificação**
5. **Lançando o Pacote**
6. **Estorno de Pacotes**
7. **Diárias**
8. **Mudança de Leito**
9. **Débito de Diárias**
10. **Reprocessamento Pacote**
11. **Responsável pela Diferença da Diária**
12. **Tratar Pacote Como Procedimento para Atendimento Interno**
13. **Tratar Pacote Como Procedimento para Atendimento Externo**

itensVisão Geral

## **01. VISÃO GERAL**

Pacotes são negociações que ocorrem entre o Hospital e Operadora de Saúde com determinados procedimentos que geram um volume considerável onde a Operadora de Saúde negocia um valor abaixo, caso a conta aberta fosse cobrada.

Cadastrar um Pacote

## **02. CADASTRAR UM PACOTE**

Para configurar um item como pacote, acessar: **Cadastros >** **Faturamento > Tabelas de Procedimentos  e serviços**

Após seguir o caminho para chegar até a tela de tabelas de Pacotes e Diárias Globais, preencha as seguintes informações: 

1. Código Tabela
2. Valor do Pacote
3. Qtde. Diárias (Apenas quando o tipo de pacote é Procedimento, para Diárias a quantidade é sempre 1)
4. Código Pacote
5. Código Próprio
6. Descrição Pacote
7. Tipo Pacote

Itens Extra Pacote

## **03. ITENS EXTRA PACOTE**

Após cadastrar um novo pacote é opcional realizar o vinculo do **pacote** com os **itens extra pacotes** que o sistema deverá alterar o item de débito na parcial, automaticamente como Incluído no Pacote, caso o mesmo esteja na conta já lançado.

Itens Extar Pacote

Itens Extra Pacotes são aqueles itens que quando utilizados, podem ser cobrados junto ao Pacote. Exemplo. No **PACOTE PARTO NORMAL** é prevista a cobrança do **ANTIBIOTICO**, caso o mesmo seja incluída na Parcial para que seja cobrado. Na impressão da conta ou no XML da fatura, serão exibidos dois itens de outras despesas, no caso o pacote e o medicamento citados no exemplo acima.

Acessar na nova MDI a aba Cadastro > Faturamento > Condições Contratuais com Convênios > Pacotes do Contrato

Para proceder com o vinculo, primeiro informe o **Pacote, o mesmo deve pertencer a uma Tabela de DTS.**

**Observação: Para conseguir informar o campo "Código Pacote", o mesmo deve estar cadastrado para a tabela utilizada pela condição contratual, se existir tabela diferenciada ela deve ser criada em duplicidade passando o** **código** **da tabela****diferenciada.**

Em seguida inclua os **Itens Extra Pacote** conforme negociado com a operadora, qualquer um dos itens dos grupos de gastos podem ser vinculados.

Informe a quantidade que aquele item pode ser marcado como incluído ao pacote, ou seja, se o convênio permite a cobrança na quantidade máxima de 2, somente os 2 primeiros itens encontrados na Parcial serão marcados como incluídos no Pacote.

Para este cadastro é possível informar uma faixa de Itens, ou seja, todos os Itens dentro da Faixa Inicial e Final farão parte dos itens Extra Pacotes.

É possível informar uma unidade de atendimento para uso dos itens extra pacote, caso seja informada uma unidade de atendimento especifica, estes itens apenas serão incluídos no pacote, caso o atendimento seja na unidade especificada neste cadastro.

O Campo tipo de faixa, serve apenas para indicar se a faixa será um MatMed ou um Procedimento, a depender da opção selecionada, o sistema fará a buscar ao clicar nos botões Faixa Inicial/Final por Matmed ou Procedimento.

Importante!

Se a quantidade no item na Parcial for superior a quantidade informada no cadastro do Item Extra Pacote, **o sistema não irá marcar o item como incluído no Pacote**. Exemplo: Temos o item de débito XPTO com a quantidade 3 no cadastro de Item Extra Pacote e na Parcial o mesmo item possui 1 lançamento com a quantidade 5, nesse caso o sistema não irá marcar o item como incluído no Pacote.

Faixa de Codificação

## **04. FAIXA DE CODIFICAÇÃO**

Para que o item cadastrado seja considerado como pacote, o mesmo deve estar na **faixa de codificação de Serviços**.

Caso seja necessário incluir uma nova faixa, seguir os seguintes passos:

1) Acesse **Cadastros** > **Faturamento** > **Condições Contratuais com Convênios**.

2) Selecione o convênio (Exemplo Unimed).

3) Clique em cima do **Padrão de Faturamento e Codificação**.

4) Em Padrões de Faturamento e Codificação, acesse aba **Códigos 3**.

5) Inclua o código do item na faixa de **Serviços**.

Lançando o Pacote

## **05. LANÇANDO PACOTE**

Atenção!

Existem duas maneiras de **lançamento de pacotes de procedimento**, a tradicional através do lançamento do pacote através da aba de Taxas e Serviços e uma segunda através de um processo.

**Lançamento do Pacote através do botão Incluir**

Siga os passos abaixo para lançar o pacote numa parcial:

1) Acesse a Elaboração de Contas do paciente.

2) Na aba de **Taxas e Serviços**, lance o pacote que foi configurado.

3) O item será lançado na **parcial e a coluna Pacote será gravada com o valor Sim.**

4) É possível incluir lançamentos da conta em aberto para que façam parte do Pacote, para isso clique com o botão direito é utilize a opção "Inclui Item na cobrança do Pacote".

**Lançamento do Pacote através do Processo**

Atenção!

O Pacote de Diária Global só pode ser incluído na Parcial através desse processo.

Siga os passos abaixo para lançar um pacote de diária global ou pacotes de procedimentos numa parcial:

1) Acesse a Elaboração de Contas do paciente, em **Faturamento > Elaboração de Contas.**

2) Na aba de **Taxas e Serviços**, selecione em **Processos >** **Lançamento Pacote**.

3) Na tela de processo que será aberta, já carregará os campos Data Pacote, Local Uso e Centro Custo, assim, precisando apenas informar o pacote pro procedimento e/ou Incluir lançamentos de Pacote de Diária Global.

* A Data Pacote, é utilizada apenas como data inicial do pacote por procedimento, pois os pacotes de diárias são lançados automaticamente em todos os dias sem um pacote.

**Observação**: Para conseguir informar o Pacote por Procedimento, o mesmo deve estar cadastrado para a tabela utilizada pela condição contratual utilizada neste atendimento, e cadastrado no anexo "Pacotes do Contrato" das condições contratuais (conferir tópico 4).

Então basta clicar em "Executar" para que o processo seja executado.

4) Ao terminar o processo.

* Se informado um **Pacote por Procedimento**, será incluído um registro na aba **Taxas e Serviços**.
* Se marcado **Incluir lançamentos de Pacote de Diária Global**, será incluído um registro na aba **Taxas e Serviços** para cada dia sem um pacote, depois de inserido o pacote por procedimento, caso informado.  
  Observação: O pacote lançado na conta deve estar configurado no cadastro de Diárias anexo das Condições Contratuais.

  Atenção!

  O pacote lançado na conta deve estar configurado no cadastro de Diárias da condição Contratual. Mais informações no tópico "**07. DIÁRIAS**".
* Se para cada pacote lançado na conta, há **Itens Extra Pacote**, e estes itens existirem lançados (não importa se em Honorários, Taxas e Serviços, MatMed...), o mesmo será incluído no pacote.

5) É possível incluir lançamentos da conta em aberto para que façam parte do Pacote, para isso selecione o registro marcando a caixa de seleção > Processos > Inclui Item na cobrança do Pacote.

6) Pode-se identificar se o item está no pacote, pela coluna **Incluído Pacote** com o valor **Sim.**

Estorno de Pacotes

## **06. ESTORNO DE PACOTES**

Em todas as abas dos grupos de gastos da conta, é possível estornar um item, em **Processos > Estornar Lançamento.**

Ao executar este processo, se o item estornado for um pacote, todos os itens que foram incluídos no pacote por causa do lançamento deste pacote, serão removidos do pacote automaticamente.

O mesmo ocorre ao reverter o estorno, onde todos os itens removidos do pacote durante o estorno, serão novamente incluídos no pacote.  
O processo fica localizado em **Processos > Reverter estorno indevido.**

Diárias

## **07.****DIÁRIAS**

Como mencionado acima, durante o processo de lançamento de pacotes, pode-se marcar a opção "Incluir lançamento de Pacote Diária Global?".  
Com isso, se o campo for marcado, lançará na conta os pacotes de diária global e/ou isolamento.

Os pacote utilizados são configurados no cadastro de Diárias anexado nas Condições Contratuais, podendo configurar um **Pacote Diária Global** e/ou um **Pacote Diária Isolamento**.

Atenção!

Para conseguir informar os pacotes, os mesmos devem estar cadastrados para a tabela de DTS desta condição contratual.

O cadastro do Diárias fica localizado em **Cadastros** > **Faturamento** > **Condições Contratuais** > anexo **Diárias**.

Com o cadastro do Diárias devidamente efetuado, ao executar o processo de lançamento de pacotes com o campo "Incluir lançamento de Pacote Diária Global?" marcado, lançará na conta um dos pacotes informados,  
onde, se o leito ocupado pelo paciente estiver configurado como "Isolamento", utilizará o **Pacote Diária Isolamento**, senão utilizará o **Pacote Diária Global.**

Esta informação pode ser verificada no cadastro do leito localizado em **Cadastros** > **Registro e Controle** > **Leitos**, campo "**Bloqueado para Internação**".

Mudança de Leito

## **08. MUDANÇA DE LEITO**

Durante a internação de um paciente, pode ocorrer do mesmo ser trocado de leito, e este processo é efetuado no módulo localizado em **Atendimento > Internação > Outros > Mudança de Leito**.

Nesta tela, se localiza o paciente e atendimento, onde já é identificado o leito atual, e no campo "Novo Leito" é selecionado para qual leito o paciente foi.  
Atenção para o campo "Data Transf", pois pode-se informar a data da transferência retroativa.

Esta explicação está sendo feita, pois como os pacotes de diária são configurados no leito, se mudaram o leito, pode ser que os pacotes agora sejam outros.

Ao executar o processo de lançamento de pacotes, lançará para cada dia sem um pacote, um pacote de diária global ou isolamento, de acordo com o leito do paciente naquele dia.

**Exemplo**: Vamos simular que um paciente ficou internado do dia 1 ao 5, onde começou no leito A e no dia 3 foi transferido para o leito B.  
No cadastro do leito A está configurado o pacote X e no leito B o pacote Y.  
Será lançado na conta 5 pacotes de diária (um para cada dia), onde nos dias 1 e 2 será o pacote X, nos dias 4 e 5 o pacote Y e no dia 3 será lançado um destes dois pacotes, sendo que o que definirá qual, é a hora da transferência comparada com o valor informado em **Cadastros > Condições Contratuais > aba Parâmetros I, campo "Horário limite para cálculo de nova diária".**   
Se a mudança do leito for efetuada antes da hora configurada, será utilizado o pacote do novo leito, senão do leito antigo.

Débito de Diárias

## **09. DÉBITO DE DIÁRIAS**

Na conta do paciente, a partir do momento que se lança uma diária, todos os dias devem ter uma diária lançada.  
Esta regra também é utilizada para pacotes de diária global ou isolamento.

**Utilitários > Débito de Diárias**,

Este processo localiza todas as contas em aberto que possuem pacotes de diária, e se o dia atual não tiver um pacote lançado, lançará o pacote configurado no cadastro do leito deste dia

Reprocessamento Pacote

## **10. REPROCESSAMENTO PACOTE**

**Elaboração de contas > aba Taxas e Serviços > processos > Reprocessamento Pacote**.

Foi criado um processo para reprocessar os pacotes, onde este tem como objetivo lançar na conta pacotes de diária para os dias sem pacote (caso exista ao menos um pacote de diária lançado), e revisar os itens incluídos no pacote.

Exemplos:

1) Supondo que hoje seja dia 5, e uma conta foi aberta no dia 1, e no dia 3 foi executado o processo de lançamento de pacotes, onde este lançou os pacotes de diária do dia 1 ao 3 normalmente.  
Ninguém executou o processo de Débito de Diárias nos dias 4 e 5, assim não completando estes dias com pacotes.  
Este reprocessar efetuará o lançamento dos pacotes de diárias nestes dias faltantes.

2) Supondo que foi lançado um ou mais pacotes na conta, e que itens foram incluídos no pacote durante o processo.  
No pacote em questão, existia um medicamento X com quantidade 3, e na conta existe este medicamento lançado duas vezes, com quantidades 2 e 5.  
Como resultado do processo, somente o medicamento com quantidade 2 será incluído no pacote, pois o saldo disponível é 3.  
Depois disso, editaram este cadastro, alterando a quantidade de 3 para 6, e reprocessaram.  
Isso fará com que o saldo 6, seja suficiente para incluir no pacote o medicamento de quantidade 5, assim este será incluído no pacote e o de quantidade 2 não.

Responsável pela Diferença da Diária

## **11. RESPONSÁVEL PELA DIFERENÇA DA DIÁRIA**

Como mencionado anteriormente, os pacotes de diária global ou isolamento são configurados na diária da condição contratual.  
A diária utilizada na conta do paciente é buscada através do leito informado no registro do atendimento, ou na mudança de leito.

Porém pode ocorrer algum cenário onde o leito/diária utilizados no atendimento não condizem com o plano do paciente, como exemplo, um paciente com plano de **enfermaria**, mas o hospital no momento está lotado, sem leitos de enfermaria disponíveis, e por este motivo utiliza um leito de **apartamento**, e quando isso acontece, o sistema pede para informar uma diária para que seja calculada a diferença do valor cobrado, que normalmente seria a diária correta a ser utilizada caso tivessem leitos disponíveis, e isso faz com que seja obrigatório informar o responsável pela diferença.

Com isso, é lançada na conta do paciente uma diária com o valor da diária de diferença solicitada, e...

* Se o responsável pela diferença for o **Paciente**, lançará a diferença em **Gastos Particulares**.
* Se o responsável pela diferença for o **Hospital**, lançará a diferença em **Itens Grátis**.
* Se o responsável pela diferença for o **Convênio**, lançará a diferença normalmente na conta em **Diárias**, pois tudo lançado na conta é para ser cobrado do convênio

Até aqui é um comportamento já antigo do sistema, porém agora este comportamento também é utilizado para os pacotes.

Exemplo, se o paciente possui um plano de enfermaria e utilizou um leito de apartamento com o hospital como responsável pela diferença, lançará a diária normalmente e a diferença em itens grátis.  
Com isso, buscará na diária utilizada (no caso a de apartamento) o pacote no cadasstro de diárias da condição contratual, e lançará este pacote com o valor do pacote vinculado a diária da diferença (de enfermaria).  
Supondo que o pacote de apartamento custe 3.000,00 e o de enfermaria custe 2.000,00, lançará um pacote de 2.000,00 (valor do pacote "correto", que neste caso é o de enfermaria), e a diferença (3.000,00 - 2.000,00 = 1.000,00) em itens grátis para cada dia utilizando este leito.

Tratar Pacote Como Procedimento

## **12. Tratar Pacote Como Procedimento para Atendimento Interno ou Externo**

Por padrão o pacote é enviado no XML na lista de Outras Despesas. Se habilitado, o mesmo será enviado na lista de Procedimentos.

* Quando marcado, os pacotes vinculados a um procedimento executado serão enviados no XML TISS como Procedimentos Executados, permitindo o envio da equipe médica com base no procedimento vinculado. Caso não seja vinculado nenhum procedimento ao pacote na aba de Taxas e serviços, a tag de equipe não será enviada
* Quando desmarcado, os pacotes continuarão sendo tratados como Outras Despesas no XML, sem envio de equipe médica associada ao pacote.

Parametrização necessária. Se marcado e informado o procedimento vinculado, no xml deve sair a tag de equipe.

Selecionar o procedimento associado ao pacote.

No arquivo XML, ficará conforme imagem abaixo:

Caso parâmetro não esteja marcado, continuará enviando como outras despesas.
