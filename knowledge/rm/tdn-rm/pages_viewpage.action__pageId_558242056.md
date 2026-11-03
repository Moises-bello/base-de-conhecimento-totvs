---
content_hash: 6384479b45f79fbe54ee0e251d3fb221892cac2ed6e05208a0e396682e001c9a
fetched_at: '2026-06-29T00:10:47.517068+00:00'
page_id: '558242056'
product: rm
source: tdn-rm
title: MP 936 - BEM - Importação de Dados da Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=558242056
version: 11
---

O Módulo TOTVS Folha de Pagamento possui o recurso de Importação de dados do RM Labore, que possibilita atualizar os registros dos funcionários com as informações do BEM.

O processo pode ser acessado em Configurações | Importações | Importações de Dados da Folha de Pagamento:

falseImportante

Os campos do BEMestão disponíveis no processo de importação a partir dos patchs:

* 12.1.26.262
* 12.1.27.247
* 12.1.28.156

É necessário importar novamente o layout FOPLAY0039 09.004.006 Exportação de Funcionarios.TotvsGen disponível na pasta Gerenciador de Saídas no diretório de instalação da versão.

Importação de Dados Cadastrais do Funcionário

Para importação de dados cadastrais, o processo permite sobrescrever os dados. Assim, orientamos a exportar os dados mais atualizados do funcionário, editar os campos que deseja alterar do funcionário conforme a disposição do mesmo arquivo e importar o mesmo utilizando o processo acima. A documentação com os campos do Layout pode ser consultado em .  A exportação pode ser feita utilizando o relatório FOPLAY0039 09.004.006 Exportação de Funcionarios.TotvsGen disponível pelo produto. Abaixo iremos exemplificar o processo:

falseObservação

Os dados do funcionário serão sobrescrito. É importante fazer a exportação conforme orientado acima usando os dados mais atualizados do funcionário e ficar atento para alterar somente os campos desejados evitando assim inconsistência nos dados cadastrados do funcionário.

Exportando o Funcionário usando o processo de Gerador de Saídas, foi criado o arquivo abaixo em .txt:

Os campos são separados por ponto e vírgula no arquivo e os referentes ao Cadastro do BEM são a partir da posição 367:

***Suspensão de Contrato***

No exemplo abaixo preenchemos os dados para uma adesão por suspensão de contrato:

Também é possível fazer a alteração da Situação do funcionário. Neste caso é necessário editar as posições 55 referente ao código de situação, 348 referente a data da mudança e 349 referente ao motivo da mudança:

Após terminar a edição, salvar o arquivo. Em seguida importar o mesmo usando o o processo de importação de dados da Folha de Pagamento:

 

A aba BEM no cadastro de Funcionário será preenchida com as informações do Arquivo:

A Situação do Funcionário será alterada para C:

Os Históricos de Situação, Afastamento e do BEM serão inseridos conforme as alterações:

 

O evento S-2230 do funcionário foi incluído na fila de eventos do eSocial:

*Alterando uma Suspensão de Contrato (prorrogação, cancelamento, antecipação)*

Para fazer a alteração, basta exportar os funcionário elegíveis e colocar as informações no arquivo. No exemplo abaixo iremos prorrogar a suspensão por mais 30 dias. É necessário informar a data de mudança.

Importando o arquivo após a alteração, a aba do BEM foi atualizada com informação:

No histórico do BEM foi inserido o registro referente a alteração:

falseObservação

A importação só irá aceitar que apenas um dos campos **Data do** **Cancelamento, Data da Antecipação ou Dias de Prorrogação** seja informado, ou nenhum, emitindo a mensagem de erro caso seja informado para um mesmo arquivo mais de um deles ou todos: '*Para atualização do B.E.M. apenas um dos campos deve ser informado: Ou a Data do Cancelamento, Ou a Data de Antecipação, Ou os Dias de prorrogação, Ou nenhum deles*.'

*Informando data fim do afastamento*

O processo de Importação de dados da Folha de Pagamento também tem a opção de importação de histórico de afastamento, onde o mesmo pode ser utilizado para informar a data de retorno do afastamento. O produto possui o layout FOPLAY0019 09.003.002 Exportação de Históricos de Afastamento.TotvsGen que pode ser usado para exportar os dados dos funcionários elegíveis. A documentação do Layout pode ser consultada em . Abaixo iremos exemplificar o processo:

Exportando o histórico de afastamento do funcionário usando o processo de Gerador de Saídas, foi criado o arquivo abaixo em .txt:

Os campos são separados por ponto e virgula e a posição da data fim do afastamento é a 3, conforme a documentação do link acima:

A data de retorno foi preenchida:

Fazendo a importação do arquivo histórico de afastamento do funcionário alterado utilizado a opção abaixo:

 

A data fim do afastamento foi preenchida conforme a data informada no arquivo:

***Redução de Salário/Jornada***

No exemplo abaixo preenchemos os dados para uma adesão por Redução de Jornada/Salário:

Após terminar a edição, salvar o arquivo. Em seguida importar o mesmo usando o o processo de importação de dados da Folha de Pagamento:

A Aba bem foi alterada com os dados informados e o Histórico do BEM incluído:

O Evento S-2206 foi criado na fila de eventos do eSocial:

*Alterando uma Redução de Salário/Jornada (prorrogação, cancelamento, antecipação)*

Para fazer a alteração, basta exportar os funcionário elegíveis e colocar as informações no arquivo. No exemplo abaixo iremos antecipar a redução para o dia 02/05/2020. É necessário informar a data de mudança.

Importando o arquivo após a alteração, a aba BEM do cadastro de funcionário foi alterado. O Histórico com o registro foi incluído:

 

O evento S-2206 foi criado com a alteração para ser enviado para o eSocial:
