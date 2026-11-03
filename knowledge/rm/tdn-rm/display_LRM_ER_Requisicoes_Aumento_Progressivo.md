---
content_hash: a5bf160733165b1deadab925aa28f0ea18369a1624738228a05dee983efd725a
fetched_at: '2026-06-29T00:06:13.853635+00:00'
page_id: '208347507'
product: rm
source: tdn-rm
title: ER_Requisicoes_Aumento_Progressivo
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Requisicoes_Aumento_Progressivo
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.6 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

### Objetivo

Criar nova funcionalidade de alteração de dados funcionais progressivo através das requisições

## 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros de Alteração de Dados Funcionais Progressivo | Criação | RH / Gestão de Pessoas / Configurações / Tipos de Requisição | - |
| Planejar Efetivação de Alteração de Dados Funcionais Progressivo | Criação/Alteração | RH / Gestão de Pessoas / Valorização / Requisições / Alteração de Dados Funcionais / Transferência com alteração de Dados Funcionais | - |
| Efetivar Progressão | Criação | RH / Gestão de Pessoas / Valorização / Requisições / Alteração de Dados Funcionais / Transferência com alteração de Dados Funcionais / Concluir Progressão | - |
| Efetivar Requisição de Alteração de Dados Funcionais / Transferência com alteração de Dados Funcionais | Alteração | RH à Gestão de Pessoas / Valorização à Efetivações / Efetivar Requisição Alteração de Dados Funcionais / Transferência com alteração de Dados Funcionais | - |
| Efetivar Requisição de Alteração de Dados Funcionais / Transferência com alteração de Dados Funcionais | Alteração | RH / Gestão de Pessoas / Valorização à Efetivações / Efetivar Requisição Alteração de Dados Funcionais / Transferência com alteração de Dados Funcionais | - |
| Inserir parecer em lote | Criação | RH / Gestão de Pessoas / Valorização / Requisições / Inserir parecer em lote | - |
| Planejar Efetivação de Alteração de Dados Funcionais Progressivo - Portal | Criação/Alteração | Portal à Meus Dados / Recursos Humanos / Requisições / Requisições / Inclusão de Nova Requisição | - |

**Requisito 1 – Parametrização de tipos de requisição (“Alteração de Dados Funcionais” e “Transferência com Alteração de Dados Funcionais”)**

Somente será permitida a inclusão de parametrização para os tipos de requisições dos tipos: “Alteração de dados funcionais” e “Transferência com alteração de dados funcionais”.

O anexo de “Parametrização” conterá como informações:

* Será exibido um Checkbox “Registro “Padrão” para todas filiais”, quando este Checkbox for marcado, será criado um registro com as regras parametrizadas para todas as filiais existentes na coligada. Caso o Checkbox seja desmarcado, será exibido um lookup multirecord onde serão informadas as filiais que obterão as regras em questão.
* Será exibido um Checkbox “Registro “Padrão” para todos motivos”, quando este Checkbox for marcado, será criado um registro “padrão” com as regras parametrizadas para todos os motivos existentes. Caso o Checkbox seja desmarcado, será exibido um lookup multirecord onde serão informados os motivos que obterão as regras em questão.
* Somente poderá existir 1 regra para uma mesma filial e um mesmo motivo, ou seja, caso a filial belo horizonte esteja parametrizada para o motivo Promoção por exemplo, não poderá ser incluída uma outra parametrização contendo esses dois parâmetros.
* Regra contendo o percentual máximo de aumento sobre o salário.
* Regra utilizando “Fórmula Customizada” e seu respectivo valor percentual máximo esperado.
* Regra contendo o tempo mínimo de casa para receber uma promoção (dias).
* Regra contento um prazo mínimo entre aumentos (dias).
* Será exibido um Checkbox “Permitir progressão?” onde será informado se será permitido o uso de progressão para o tipo de requisição.
* OBS: Cada regra conterá um combobox sobre a ação a ser tomada sobre a regra ao Incluir/Editar uma Requisição (“Alteração dos dados funcionais” / “Transferência com alteração de dados funcionais”) / Progressão. Este combo conterá as seguintes informações:

* “Não validar” define que a regra não será validada na inclusão da requisição.
* “Somente mensagem” define que a regra ao ser validada não apenas exibirá uma mensagem informando que a regra não foi satisfeita.
* “Bloquear” define o bloqueio da alteração/inclusão.

 Para as regras de “Percentual máximo de aumento”, “Tempo mínimo de casa”, “Fórmula customizada” e “Prazo mínimo entre aumentos” será acrescentado um combobox para cada regra com as opções (“Bloquear”, “Exibir Mensagem” e “Não validar”). Esta parametrização irá decidir como a regra será validada ao incluir uma requisição.

 

**Requisito 2 – Alteração nas visões das requisições dos tipos: (“Alteração de dados funcionais” e “Transferência com alteração de dados funcionais”)**

Nas requisições dos tipos: “Alteração de Dados Funcionais” e “Transferência com Alteração de Dados Funcionais”, serão disponibilizados na visão os seguintes campos:

* Filial, tempo de casa, função de origem, tempo na função atual, faixa salarial de origem, salário atual, função proposta, faixa salarial proposta, salário proposto, percentual de reajuste, data da última alteração salarial, motivo mudança salário e previsão.

 Os campos que já existem, continuarão disponíveis.

 Este requisito possibilitará por exemplo configurar a formatação condicional da visão e com isto destacar os registros que não estão dentro da regra desejada.

 

**Requisito 3 – Alterações Winforms / Webforms para registro de Alteração de Dados Funcionais Progressivo**

  As requisições que tratam de alteração de dados funcionais hoje no RM Vitae são:

   - Alteração de dados funcionais;

   - Transferência com alteração de dados funcionais.

 Será criado nas requisições citadas acima a funcionalidade de alteração de dados funcionais progressivo, respeitando os parâmetros configurados em tipos de requisições que também será criado e descrito nesse documento de especificação.

 Existirá duas novas abas (anexo) nos cadastros de requisições competentes chamada de “Alterações de dados funcionais progressivo” e “Transferência com alteração de dados funcionais progressivo”, que será permitido a inclusão de registros, caso esteja parametrizado para utilizar progressão. Se uma requisição conter progressões, as opções de alteração de dados funcionais (salário, níveis, faixas e função), motivo de mudança de função e motivo de mudança salarial serão colocados como somente leitura e tratados na nova aba de progressão. Neste caso os campos de proposta salarial irão refletir a última progressão criada.

 Nessa nova aba (anexo), o usuário poderá inserir previamente os dados de alteração de dados funcionais progressivo. Esses dados serão validados ao salvar a requisição de acordo com os parâmetros definidos em tipos de requisição, caso não houver parametrização para o tipo de requisição, a requisição não passará pelas novas validações.

O sistema não deverá considerar juros compostos (juros sobre juros) quando sugerir os dados de aumento progressivo, ou seja os valores de alteração de dados funcionais progressivo quando se tratar de aumento salarial deve realizar o cálculo de acordo com o salário de origem do funcionário. Será acrescentado na edição da requisição um campo com o total do aumento que será concedido funcionário para a visualização do usuário.

Nos dois tipos de requisições citados serão alterados o comportamento dos controles na tela, bem como sua localização. (Vide protótipo de tela).

Igualmente no ambiente Windows as alterações/criações de telas e funcionalidades descritas acima serão implementadas também no ambiente web (Portal) e somente irão ocorrer nas requisições de “Alteração de Dados Funcionais” e “Transferência com alteração de dados funcionais”.

Na web (Portal) a requisição do tipo “Transferência com alteração de dados funcionais” terá o mesmo comportamento atual, e, nas etapas onde estão disponíveis as alterações salariais atualmente também estará disponível a funcionalidade de alteração de dados funcionais progressivo.

A nova aba de alteração de dados funcionais progressivo funcionará como um anexo da requisição. Ela terá uma visão dos dados e também as funcionalidades comuns do sistema (inclusão, alteração e exclusão de registros).  Os campos disponíveis nesse novo cadastro estão descritos abaixo:

 - Código Identificador (Irá ser sugerido pelo sistema, ou digitado manualmente);

 - Último aumento Concedido (data do último aumento concedido ao funcionário);

- Tempo de Empresa (Tempo que o funcionário tem de trabalho na empresa);

 - Data Mínima de Efetivação do Aumento de Salário (Informado pelo usuário);

 - Data da Efetivação (data da realização da efetivação);

 - Tempo mínimo entre as efetivações;

 - Status (Pendente, Efetivado);

- Dados Atuais do Funcionário:

- Função de Origem;

- Tabela Confidencial;

- Nível Salarial de Origem;

- Faixa Salarial de Origem;

- Salário de Origem;

- Proposta de Alteração:

- Função;

- Tabela Confidencial;

- Nível;

- Faixa;

- Percentual (Percentual a ser aplicado para aumento do salário);

 - Novo Salário (Calculado pelo sistema);

A alteração do salário do funcionário é definida através de parâmetro já existente no sistema, sendo assim ele pode ser definido por nível, faixa ou diretamente.

Um registro de progressão não poderá alterar o salário para um salário menor que o da progressão anterior, bem como a alteração de função não poderá ser igual a de alguma progressão anterior.

As alterações e novas implementações citadas até o momento terão impacto direto nos processos de efetivação de requisições. Os processos “Efetivar Alteração de dados Funcionais” e “Efetivar transferência com alteração de dados funcionais” deverão ser alterados para verificação/validação dos itens referentes a alteração de dados funcionais progressivo (caso houver). Uma requisição dos tipos já citados acima não poderá ser concluída se ainda houver registros de alteração de dados funcionais progressivo em andamento/pendentes na mesma.

Será feita alterações nos processos de Cancelar e Suspender Requisição para informar ao usuário se existem progressões de alteração de dados funcionais efetivadas para requisição selecionada. Além de exibir a informação será necessário que o usuário confirme que deseja cancelar ou suspender uma requisição mesmo sabendo das progressões em andamento. Caso não exista progressões efetivadas, esses alertas não deverão ser exibidos.

**3.1. Exclusão de Alteração de Dados Funcionais Progressivo:**

 Para ambos anexos:

* Rh / Gestão de Pessoas / Valorização / Requisições / Alteração de Dados Funcionais / Anexos / Alteração de Dados Funcionais Progressivo
* Rh / Gestão de Pessoas / Valorização / Requisições / Transferência com Alteração de Dados Funcionais / Anexos / Transferência com Alteração de Dados Funcionais Progressivo

A exclusão de registros será realizada por meio de um processo, considerando:

1. O botão excluir (X) será desabilitado ou ocultado. O usuário não poderá executar esse comando.
2. Será criado um processo, denominado "Exclusão de Alteração de Dados Funcionais Progressivo".
3. Para acessar o processo, o usuário deverá ter acesso de "exclusão" na respectiva Action.
4. Para que o processo seja executado, o usuário deverá selecionar no mínimo um registro.
5. O processo executará a seguintes ações:

 a) Se todos os registros forem selecionados: Todos os registros serão excluídos e os dados da requisição, referentes às alterações de dados, serão atualizados com os dados contidos no registro excluído que tenha a menor data (campo DATAMINEFETIVACAO).

 b) Se apenas um ou mais registros forem selecionados, mas não todos os registros: Os registros selecionados serão excluídos e os dados da requisição, referentes às alterações de dados, serão atualizados com os dados contidos no registro não excluído que tenha a maior data (campo DATAMINEFETIVACAO).

Validações:

- Antes de excluir, todas as validações referentes aos respectivos tipos de requisição deverão ser executadas. Caso a validação indique que o processo deve ser abortado (pelo menos 1 validação é do tipo "Bloquear"), o usuário deverá ser informado sobre as inconsistências e o processo deverá ser cancelado. Atualmente a validação esta validação já está implementada nas respectivas Actions. Esse código deverá ser transferido e adaptado ao processo.

**Requisito 4 – Efetivação das “Progressões” de requisições dos tipos: (“Alteração de dados funcionais” e “Transferência com alteração de dados funcionais”)**

Criar um processo “Concluir Progressão” nos anexos de “Efetivar Alteração de Dados Funcionais” e “Efetivar Transferência com Alteração de Dados Funcionais” que serão responsáveis por executar as efetivações das progressões cadastradas para as requisições de “Alteração de dados funcionais” e, respectivamente, “Transferência de dados funcionais”. Ao ser iniciado, o processo irá abrir uma tela que conterá um Checkbox perguntando ao usuário se ele deseja informar uma data para efetivação, se o checkbox for marcado será habilitado um campo de data perguntando ao usuário qual será a data para efetivação da progressão. Ao ser executado, o processo deverá executar todas regras validadas no processo “Concluir Requisição” na parte de efetivações e ainda validar as seguintes regras abaixo:

* A efetivação das progressões deverá ser realizada na ordem de data mínima de efetivação, caso o usuário tente efetivar uma progressão e exista uma outra progressão pendente com a data mínima de efetivação menor que à da progressão a ser efetivada, será exibido um erro informando que existem outras progressões a serem efetivadas antes.
* Se o processo for finalizado com sucesso, o status da progressão deve ser modificado de “Pendente” para “Efetivado”.
* Se a progressão a ser efetivada for a única restante com o status “Pendente”, o processo deverá alterar seu status para concluído conforme sinalizado acima, e depois concluir a requisição da progressão. OBS: Ao concluir a requisição, o sistema apenas modifica o status da requisição, pois as regras de alteração de salário, faixa e/ou função já foram efetivadas através das progressões.
* Quando a progressão for do tipo “Transferência com alteração de dados funcionais”, o funcionário deve ser sempre transferido na primeira progressão, restando as outras progressões apenas alterações de dados.]
* Ao rodar o processo “Concluir Requisição”, localizado no cadastro de “Efetivações”, caso a requisição possua progressões, o sistema deverá travar a conclusão da requisição e alertar o usuário que a conclusão da requisição somente será realizada quando todas as progressões da requisição forem efetivadas.

* Ao “concluir a progressão” o sistema deverá enviar um email para os envolvidos informando das alterações configurada na progressão tal como era realizado na efetivação da requisição. Caso a progressão a efetivada seja a última pendente, o sistema deverá informar no email que a requisição foi concluída.

**Requisito 5 - Processo para Inserir Parecer em lote para requisições (TODOS OS TIPOS)**

Atualmente para inserirmos um parecer para uma requisição, acessamos o anexo de “Parecer da Requisição” e inserimos um a um os pareceres necessários.

Será criado um processo para criar um Parecer para requisição em lote, ou seja, com esse novo processo poderemos inserir um mesmo parecer para várias requisições de uma só vez.

A regra de negócio para inserir um parecer continua a mesma, porém a aba de “Dados da Requisição” existente no anexo de Parecer não estará disponível no novo processo, portanto não será possível alterar os dados da requisição através do processo.

O processo funcionará de forma objetiva, inserindo um parecer para as requisições selecionadas com a data de emissão (data atual do sistema), o status (Em andamento, Reprovado e Aprovado) escolhido pelo usuário, o funcionário responsável com função e e-mail do mesmo.

Ao final do processo executado com sucesso a requisição terá seu status alterado para o status do último parecer inserido.

Não será permitido rodar o processo para requisições concluídas, reprovadas e/ou canceladas. Somente é permitido inserir parecer para requisição pendente ou em andamento.

## 

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

******Protótipo 03******

********Requisição de Transferência com Alteração de Dados Funcionais – Nova opção para utilizar Alteração de Dados Funcionais Progressivo********

**Requisição de Alteração de Dados Funcionais – Anexo – Visão**

**- Winforms**

**********- Web (Portal)**********

**Requisição de Alteração de Dados Funcionais – Anexo – Edição**

**- Winforms**

****- Web (Portal)****

**Requisição de Transferência com Alteração de Dados Funcionais – Anexo – Visão**

**- Winforms**

****- Web (Portal)****

**Requisição de Transferência com Alteração de Dados Funcionais – Anexo – Edição**

**- Winforms**

****- Web (Portal)****

******Efetivação das “Progressões” de requisições dos tipos: (“Alteração de dados funcionais” e “Transferência com alteração de dados funcionais”):******

**Processo para Efetivar Progressões em lote**

**Processo para Inserir Parecer em lote para requisições**

## Fluxograma

**Regra para validação de parametrização ao salvar Requisito/Progressão**

**Dicionário de Dados**

Tabela de Alteração de Dados Funcionais Progressivo - Solicitação de Criação: VALTDADFUNCPROG

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tipo** | **Detalhe** |
| CODIGO | Int | GAutoInc |
| CODCOLIGADA | DCODCOLIGADA | Foreign Key de GCOLIGADA |
| IDREQ | Int | Foreign Key de VREQPROMOCAO |
| SALARIO | RMDVALOR2 | Novo salário a ser aplicado |
| PERCENTUALAUMENTO | Int | Percentual de aumento a ser aplicado |
| CODFUNCAOALT | String | Foreign Key de PFUNCAO |
| CODTABSALALT | String | Foreign Key de VTABSALARIAIS |
| CODNIVELALT | String | Foreign Key de VNIVELFUNCAO |
| CODFAIXAALT | String | Foreign Key de VFAIXASALARIAL |
| CODMOTMUDFUNCAO | String | Código do motivo de mudança da função |
| CODMOTMUDSAL | String | Código do motivo de mudança de salário |
| DATAMINEFETIVACAO | DateTime | Data mínima para efetivação do aumento do salário. |
| DATAEFETIVACAO | DateTime | Data da efetivação do aumento do salário. |
| STATUS | Char(1) | **“E”** – Efetivado;  **“P”** – Programado; |
| Campos da tabela PFUNC que serão utilizados |  |  |
| CHAPA | DCHAPA | Foreign Key de PFUNC |

Tabela de Transferência com Alteração de Dados Funcionais Progressivo - Solicitação de Criação: VTRANSFALTDADFUNCPROG

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tipo** | **Detalhe** |
| CODIGO | Int | GAutoInc |
| CODCOLIGADA | DCODCOLIGADA | Foreign Key de GCOLIGADA |
| IDREQ | Int | Foreign Key de VREQTRANSFPROMOCAO |
| SALARIO | RMDVALOR2 | Novo salário a ser aplicado |
| PERCENTUALAUMENTO | Int | Percentual de aumento a ser aplicado |
| CODFUNCAOALT | String | Foreign Key de PFUNCAO |
| CODTABSALALT | String | Foreign Key de VTABSALARIAIS |
| CODNIVELALT | String | Foreign Key de VNIVELFUNCAO |
| CODFAIXAALT | String | Foreign Key de VFAIXASALARIAL |
| CODMOTMUDFUNCAO | String | Código do motivo de mudança da função |
| CODMOTMUDSAL | String | Código do motivo de mudança de salário |
| DATAMINEFETIVACAO | DateTime | Data mínima para efetivação do aumento do salário. |
| DATAEFETIVACAO | DateTime | Data da efetivação do aumento do salário. |
| STATUS | Char(1) | **“E”** – Efetivado;  **“P”** – Programado; |
| Campos da tabela PFUNC que serão utilizados |  |  |
| CHAPA | DCHAPA | Foreign Key de PFUNC |

Tabela de Aumento Progressivo de Salário - Solicitação de Criação: VREQPARAMS

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tipo** | **Detalhe** |
| CODIGO | Int | GAUTOINC |
| CODCOLIGADA | DCODCOLIGADA | Foreign Key de GCOLIGADA |
| IDTIPOREQUISICAO | int | Foreign Key de VREQTIPO |
| PERCAUMENTOMAXIMO | Numeric(5,2) |  |
| EXIBEPERCAUMENTOMAX | Char(1) |  |
| RETFORUMACUS |  |  |
| EXIBERETFORMCUST | Char(1) |  |
| DIASTEMPOCASA |  |  |
| EXIBEDIASTEMPOCASA | Char(1) |  |
| DIASULTAUMENTO |  |  |
| EXIBEDIASULTAUMENTO | Char(1) |  |
| TODASFILIAIS | DLOGICO |  |
| TODOSMOTIVOS | DLOGICO |  |
| FORMCALCVALORBASE | Varchar(8) |  |
| PERMITIRPROGRESSAO | DLOGICO |  |

Tabela de Aumento Progressivo de Salário - Motivo: VREQPARAMSMOTIVO

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tipo** | **Detalhe** |
| CODIGO | Int | GAUTOINC |
| CODTIPOPARAMS | Int | Foreign Key de VREQPARAMS |
| CODCOLIGADA | DCODCOLIGADA | Foreign Key de GCOLIGADA |
| CODCLIENTE | Varchar(2) |  |
| DESCRICAO | Varchar(50) |  |

Tabela de Aumento Progressivo de Salário - Motivo: VREQPARAMSFILIAL

|  |  |  |
| --- | --- | --- |
| **Campo** | **Tipo** | **Detalhe** |
| CODIGO | Int | GAUTOINC |
| CODTIPOPARAMS | Int | Foreign Key de VREQPARAMS |
| CODCOLIGADA | DCODCOLIGADA | Foreign Key de GCOLIGADA |
| CODILIAL | Varchar(2) |  |
| NOMEFANTASIA | Varchar(50) |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
