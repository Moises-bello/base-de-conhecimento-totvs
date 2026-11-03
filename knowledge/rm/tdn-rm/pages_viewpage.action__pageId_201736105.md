---
content_hash: 1cbbfe847c518cf00fa36e4f91b10f267b49d1aa1ccc98905cae91465a87abe9
fetched_at: '2026-06-29T00:06:07.341406+00:00'
page_id: '201736105'
product: rm
source: tdn-rm
title: ER_PCREQ-6393_Fluig_Workflow_Aprovação_de_Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201736105
version: 35
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | PDR\_CP\_MOV006 | **IRM1** | PCREQ-4508 |
| **Requisito1** | PCREQ-6393 | **Subtarefa1** | PDR\_CP\_MOV006-908 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 A integração do Fluig com o TOTVS Gestão de Estoque, Compras e Faturamento consistirá na geração automática de *workflows de Aprovação**,* no Fluig, dada a inclusão de um Contrato que esteja parametrizado para o mesmo e que seja necessário a aprovação de um usuário para faturamento.

## Definição da Regra de Negócio

* ## Parâmetros Globais

Para a utilização da integração do TOTVS Gestão de Estoque, Compras e Faturamento com o Fluig é necessário configurar em Parâmetros Globais na Pasta Integração Fluig, o Servidor, Usuário, Senha e Id da Empresa no Fluig.

* ## Parâmetros de Contrato

Nos parâmetros de Contrato estará disponível no Menu **04.05.07 - Workflow Fluig** os campos abaixo através dos quais será parametrizada a Aprovação de Faturamento de Contrato através do Fluig.

* Aprovação: Este campo definirá se o Contrato irá realizar a Aprovação através de Workflow, com as opções Usa e Não Usa.
* Geração Automática de Workflow: Este campo possibilitará realizar a inclusão de Contratos e/ou Itens de Contrato e Medição sem a necessidade de que seja realizada a inclusão do workflow no Fluig, sendo necessário realizar o Processo de Geração de Workflow offline para realizar a inclusão do workflow no Fluig. O parâmetro terá o seu valor padrão como verdadeiro.  
    
  Na aba do cadastro de Tipos de Contrato os campos Nível de Aprovação, Processo e Estados de Aprovação ficarão habilitados somente se Aprovação estiver selecionada com Usa e o Usuário tiver permissão de alteração. Os workflows serão gerados de acordo com o Nível de Aprovação utilizado para cada grupo de Tipo de Faturamento parametrizado. E ao realizar o vínculo do Tipo de Contrato no cadastro do Contrato, o mesmo respeitará as configurações dos campos abaixo para a geração de workflows.
* Nível de Aprovação: Este campo irá definir o Nível de Aprovação utilizado. As opções disponíveis são: Contrato, Item de Contrato e Medição. Caso, seja selecionado a opção de Contrato, será gerado um único Workflow por Contrato, contendo as informações de todos os Itens de Contrato. Para a opção selecionada de Item de Contrato será incluído um workflow por Item de Contrato, e caso seja selecionada a opção Medição será gerado um Workflow para cada medição incluída, com as suas respectivas informações.
* Processo: Este campo irá definir o processo do Fluig que será utilizado para a inclusão do Workflow.
* Estados de Aprovação: Este campo irá definir todos os estados possíveis de aprovação final para o processo selecionado. Não será permitido informar estados repetidos para o mesmo processo.  
    
  Uma vez informado o Nível de Aprovação será obrigatório informar o Processo e os Estados de Aprovação. Caso seja selecionado o Nível de Aprovação para Contrato, para dois ou mais Itens de Contrato será gerado apenas um workflow para aprovação para os mesmos, devendo respeitar a restrição de que o processo e o estado de aprovação para ambos deverá ser o idêntico.
* ## Item Utilizado:

  Item Utilizado é um conceito para que seja possível realizar o rastreamento de Workflows com os Contratos e Itens de Contrato / Medição que foram faturados, e portanto, guardar um histórico. Abaixo é citado em cada processo como é o comportamento deste campo que está nas tabelas de relacionamento e que receberá os valores Verdadeiro(1) e Falso(0).
* ## Inclusão:

  De acordo com a parametrização realizada no cadastro do Tipo de Contrato vinculado ao Contrato, o processo de geração de Workflow no Fluig, se dará conforme abaixo para cada Tipo de Faturamento do Item de Contrato:

* ## Itens Periódicos e Não Periódicos

Na Inclusão do Contrato, caso o nível de aprovação selecionado seja Contrato, será gerado para todos os Itens Periódicos e\ou Não periódicos apenas um Workflow, caso seja selecionada a opção de Item de Contrato será gerado um workflow para cada Item de Contrato.

Será gerado o workflow somente para os Itens  que possuírem Status com a opção de Faturar marcada, para que o usuário possa realizar a aprovação no Fluig. Caso o workflow não tenha sido aprovado o usuário não poderá faturar o Item de Contrato. 

* ## Medição

Na Inclusão do Contrato, caso o nível de aprovação selecionado seja Contrato, será gerado para todos os Itens de Medição apenas um Workflow, caso seja selecionada a opção de Item de Contrato será gerado um workflow para cada Item de Contrato. Se o Nível de aprovação for igual a Medição será gerado um workflow para cada medição incluída com os seus respectivos dados.

 Será gerado o workflow somente para as medições que possuem Status igual a "A Faturar", para que o usuário possa realizar a aprovação do Fluig. Caso o workflow não tenha sido aprovado o usuário não poderá faturar a Medição.

Para todas as inclusões, se dois ou mais Tipos de Faturamento estiverem utilizando o Nível de Aprovação para Contrato, os Itens de Contrato deverão ser agrupados e gerar apenas um workflow.

* Alteração:

De acordo com a parametrização realizada no cadastro do Tipo de Contrato vinculado ao Contrato, o processo de geração de Workflow no Fluig, se dará conforme abaixo para cada Tipo de Faturamento do Item de Contrato:

* ## Itens Periódicos e Não Periódicos

Na alteração do Item de Contrato, caso o Nível de aprovação selecionado seja Contrato, somente será incluído o Workflow para os Itens de Contrato que estejam com esta parametrização. Caso, seja selecionado o Nível de aprovação por Item de Contrato, somente os Itens que possuem esta parametrização terão os seus workflows incluídos. Na alteração do Item de Contrato, se o Item Utilizado do workflow for verdadeiro (1) e o Nível de aprovação for Contrato ou Item de Contrato será realizado a inclusão de um novo Workflow, caso contrário será estornado o workflow em aberto e incluído um novo workflow.

* ## Medição

Na alteração de Item de Contrato, caso o Nível de aprovação selecionado seja Contrato, somente será incluído o Workflow para as Medições dos Itens de Contrato que estejam com esta parametrização. Caso, seja selecionado o Nível de aprovação por Item de Contrato, somente para as Medições dos Itens de Contrato que possuem esta parametrização terão os seus workflows incluídos.  Se o Nível de aprovação for igual a Medição será gerado um workflow para cada medição na alteração da Medição.  Na alteração da Medição, se o Item Utilizado do workflow for verdadeiro (1) e o Nível de aprovação for Contrato ou Item de Contrato será realizado a inclusão de um novo Workflow, caso contrário será estornado o workflow em aberto e incluído um novo workflow.

**Importante**Importante

Não será permitido alterar o Cadastro de Tipos de Contrato e o campo "Tipo de Contrato" no cadastro do Contrato  caso tenha algum Item de Contrato ou Medição tenha o Item Utilizado como verdadeiro.

Somente Status e Tipo de Contrato quando alterados no Contrato realizam alterações nos Workflows gerados independente do Nível de Aprovação, ou seja, quando o Status for alterado no Contrato para outro que também tenha o campo "Faturar" marcado, não será realizado Estorno e Inclusão. Se for alterado para um Status que também tenha o campo "Cancelar" marcado, deverá ser realizado o estorno e não será realizada a Inclusão.

O campo Status terá o mesmo comportamento para o Item de Contrato, conforme supracitado do Contrato.

Ao realizar alteração no Campo Tipo Faturamento do Item de Contrato, será realizado o estorno, para os Itens e Medições que não tenha sido Utilizado, e inclusão de acordo com os Parâmetros do Tipo de Faturamento anterior à alteração, por exemplo, se um contrato tem 3 Itens de Contrato e é parametrizado o Nível de Aprovação para Contrato os Itens Periódico e Não Periódico e a Medição é por Medição, ao realizar uma alteração do campo da medição para Não Periódico, os workflow de medição associado a este Item de Contrato serão estornados, bem como, os demais workflows dos Itens de Contrato Periódico e Não Periódico, devido o Nível de Aprovação ser por Contrato.

* ## Exclusão

Na Exclusão de Contrato, Item de Contrato e Medição o Workflow  é estornado e incluído de acordo com a regra de Alteração de Contrato.

* ## Cancelamento de Contrato

No Cancelamento de Contrato o Workflow  é estornado, quando Item Utilizado igual a Falso (0), de acordo com a regra de Alteração de Contrato, porém não é incluído um novo workflow.

* ## Cancelamento de Item de Contrato

No Cancelamento de Item de Contrato o Workflow  é estornado, quando Item Utilizado igual a Falso (0), de acordo com a regra de Alteração de Contrato, porém não é incluído um novo workflow.

* ## Descancelamento de Contrato / Item de Contrato

No Descancelamento de Contrato/Item de Contrato o Workflow  é incluído de acordo com a regra de Alteração de Contrato.

* ## Cancelamento do Movimento

Ao realizar o Cancelamento do Movimento associado ao Item de Contrato ou Medição, será alterado o Item Utilizado do último workflow aprovado e utilizado. Se houver um novo workflow não utilizado ao realizar cancelamento do Movimento não poderá alterar o valor do Item Utilizado. Portanto, no cancelamento o Item Utilizado voltará para o valor Falso apenas quando o Item de Contrato tiver o Status "A Faturar'. Exemplo: No caso de Itens de Contrato de Tipo de Faturamento Periódico somente irá alterar o Item Utilizado para falso quando o último movimento gerado for cancelado\excluído.

* ## Desfazer Reajuste e Reajuste de Valores de Contrato

No Desfazer Reajuste de Contrato e no Reajuste de Valores de Contrato o Workflow é incluído de acordo com a regra de Alteração de Contrato.

Para a opção Reajusta ao Faturar não será realizada nenhuma ação para os Workflows.

* ## Faturamento

Será realizado o Faturamento pela Visão do Contrato de acordo com a regra abaixo:

No Faturamento do Contrato é realizada a consulta no estado do workflow, e conforme o Nível de aprovação, se aprovado, serão faturados de acordo com a própria regra, os Itens de Contrato Periódicos, Não Periódicos e Medições.

## - Contrato

No Faturamento do Contrato é realizada a consulta ao estado do workflow, e conforme o Nível de aprovação o Nível de aprovação para Contrato, se aprovado, serão faturados de acordo com a própria regra, os Itens de Contrato Periódicos, Não Periódico e Medição, e o campo Item Utilizado sempre ao faturar terá seu valor alterado para verdadeiro, caso o ultimo workflow gerado ainda não tenha sido utilizado.

## - Item de Contrato

 No Faturamento do Item de Contrato é realizada a consulta ao estado do workflow, e conforme o Nível de aprovação o Nível de aprovação para Item de Contrato, se aprovado, serão faturados de acordo com a própria regra, os Itens de Contrato Periódicos, Não Periódico e Medição, e o campo Item Utilizado sempre ao faturar terá seu valor alterado para verdadeiro, caso o ultimo workflow gerado ainda não tenha sido utilizado.

## - Medição

No anexo da Medição o Faturamento é realizada a consulta ao estado do workflow, e conforme o Nível de aprovação o  Nível de aprovação para Medição, se aprovado, serão faturadas de acordo com a própria regra e o campo Item Utilizado sempre ao faturar terá seu valor alterado para verdadeiro, caso o ultimo workflow gerado ainda não tenha sido utilizado.

## - Faturamento por Lote

No Faturamento por Lote  é realizada a consulta ao estado do workflow para cada Contrato a ser faturado, se aprovado,  serão faturados de acordo com a própria regra. Para todos os itens não faturados devido a não aprovação do workflow será incluído no Log a mensagem "Item pendente de aprovação de workflow no Fluig.". O campo Item Utilizado terá o seu valor preenchido de acordo com a regra de Faturamento supracitada.

* ## Tabelas de Relacionamento Contrato x Fluig

Para que se mantenha um relacionamento entre os Workflows e o Contrato terá a tabela TITMCNTWFLUIG que contem os valores do Identificador do Contrato, Item de Contrato, Item Utilizado e do Processo no Fluig, que será utilizada para todos os agrupamentos de Contrato e Item de Contrato dos parâmetros do Contrato. Quando for utilizado o agrupamento de Medição terá a tabela TITMCNTMEDICAOWFLUIG que contem os valores do Identificador do Contrato, Item de Contrato, Item de Medição, Item Utilizado e do Processo no Fluig e está tabela terá um vinculo com a Medição de Contrato.

* ## Visão de Contrato

Na visão do Contrato terão botões que possibilitam filtrar os Contratos  aprovados e não aprovados de acordo com o estado do workflow parametrizado. Quando utilizado o agrupamento por Item de Contrato ou Medição será considerado aprovado quando o Contrato possuir pelo menos um Item ou Medição aprovado.

* ## Processo de Geração Workflow Off-line

De acordo com o parâmetro "Geração Automática de Workflow"  será permitido incluir o Contrato sem realizar a inclusão do Workflow. Na visão do Contrato terá um processo de Geração Workflow Off-line, onde, serão gerados os workflows para os contratos incluídos,

sendo necessário executar o processo para faturamento quando se utilizar a aprovação por workflow e a parâmetro anterior estiver marcada.

* ## Anexo do Contrato

Na visão do Contrato será disponibilizado um anexo mestre\detalhe para consulta dos Itens de Contrato e Medição onde haverá as informações do Item de Contrato como Mestre e os detalhes do Workflow com os Identificador e Status do Processo Fluig, e caso seja Item de Medição é fornecido os dados da Medição.

* ## Formulário do Contrato

 

No formulário do Contrato serão disponibilizados campos que auxiliem na análise para aprovação do Workflow. Os campos são:

Contrato: Código, Nome, Data e Natureza do Contrato, Data Início e Fim, Valor Total, Observação e Tipo do Contrato.

Item de Contrato: Sequencial do Item de Contrato, Produto, Quantidade, Preço Faturamento, Valor Total, Condição de Pagamento, Quantidade de Faturamento, Tipo de Faturamento e Status do Faturamento.

Item de Contrato -> Condições Gerais: Condição de Pagamento a Prazo, Movimento Gerado, Filial Emitente, Destinatário, Cliente, Data Inicio e Fim, Dia e Carência do Faturamento.

 Item de Contrato -> Aditivos: Sequencial do Aditivo, Data Prorrogação, Valor, Efeito, Classificação, Percentual e Tipo.

Item de Contrato -> Medição: Sequencial da Medição, Data, Quantidade, Valor, Valor Total.

Item de Contrato -> Rateio Centro de Custo: Centro de Custo, Percentual, Histórico.

Item de Contrato -> Rateio Departamento: Departamento, Percentual, Histórico.

* ## Workflow de Exemplo

Será disponibilizado um workflow de exemplo para que se possa utilizar a Aprovação de Contrato através do Fluig. Os estados de Aprovação e Reprovação serão Reprovado e Aprovado. Na Etapa de Aprovação Automática o Workflow será avançado automaticamente para Etapa Aprovado se o somatório dos valores dos itens de contrato que participam do workflow for inferior a R$ 10.000,00 (Dez mil reais). Vide protótipo 3.

* ## Utilização dos Serviços do Workflow

  Será utilizada a classe de DataServer "CtrCntFluigData" do Totvs Gestão de Estoque, Compras e Faturamento para a exibição dos dados do Formulário de aprovação do Workflow do Contrato via o DataSet "wsDatasetCntNucleus" do Fluig, onde o mesmo, consome o serviço de wsDataServer de nome RMWsDataServer.

  Importante: Para consumir o DataSet do Fluig é necessário criar um serviço no TDS para o DataServer do RM. Para maiores informações sobre acesso ao webservice RM acesse:

  <http://tdn.totvs.com/pages/releaseview.action?pageId=185748469>

  Para maiores informações para realizar cadastro de serviços no Fluig acesse:

  <http://tdn.totvs.com/pages/releaseview.action?pageId=73082260#IntegraçãoComAplicativosExternos-AcessandoWebServicesapartirdoFluig>

  Para maiores informações para a importação de Workflow acesse:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Globais | [Alteração] | [BackOffice -> Gestão de Estoque, Compras e Faturamento -> Ambiente -> Parâmetros -> Globais -> Integração Fluig] | - |
| Parâmetros Gestão de Estoque, Compras e Faturamento | [Alteração] | [BackOffice -> Gestão de Estoque, Compras e Faturamento -> Ambiente -> Parâmetros -> Gestão de Estoque, Compras e Faturamento -> Contratos -> Workflow Fluig] | - |
| Contrato | [Envolvida] | [BackOffice -> Gestão de Estoque, Compras e Faturamento -> Contratos -> Manutenção de Contratos] | - |

***Tabelas Utilizadas***

* *TCNT - Contratos*
* *TCNCTPAR - Parâmetros do Contrato*
* *TITMCNT – Itens de Contrato*
* *TITMCNTMEDICAO - Medições de Item de Contrato*
* *TITMCNTWFLUIG  - Relacionamento entre Item de Contrato e Workflow Fluig*
* *TITMCNTMEDICAOWFLUIG  - Relacionamento entre Medição e Workflow Fluig*
* *TTCNWFLUIG - Relacionamento do Tipo e os Parametros de Workflow*
* *TTCNWESTADOPERIODICO - Estados de Aprovação do Item Periódico.*
* *TTCNWESTADONAOPERIODICO - Estados de Aprovação do Item Não Periódico.*
* *TTCNWESTADOMEDICAO - Estados de Aprovação do Item de Medição.*

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

******Protótipo 03******

******Protótipo 04******

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

## Dicionário de Dados

Tabela: TITMCNTWFLUIG

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Coligada do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | IDCNT |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Identificador do Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Identificador do Contrato |

|  |  |
| --- | --- |
| **Campo** | NSEQITMCNT |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Sequencial do Item de Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Sequencial do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | IDFLUIG |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Identificador do Workflow do Fluig |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Identificador do Workflow do Fluig |

|  |  |
| --- | --- |
| **Campo** | ITEMUTILIZADO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( ) Não ( X ) |
| **Descrição** | Item utilizado no Processo Relacionado |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar se o Item utilizado no Processo Relacionado |

Tabela: TITMCNTMEDICAOWFLUIG

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Coligada do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | IDCNT |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Identificador do Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Identificador do Contrato |

|  |  |
| --- | --- |
| **Campo** | NSEQITMCNT |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Sequencial do Item de Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Sequencial do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | NSEQMEDICAO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Sequencial do Item de Medição |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Sequencial do Item de Medição |

|  |  |
| --- | --- |
| **Campo** | IDFLUIG |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Identificador do Workflow do Fluig |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Identificador do Workflow do Fluig |

|  |  |
| --- | --- |
| **Campo** | ITEMUTILIZADO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( ) Não ( X ) |
| **Descrição** | Item utilizado no Processo Relacionado |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar se o Item utilizado no Processo Relacionado |

Tabela: TTCNWFLUIG

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Coligada do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | CODTCN |
| **Tipo** | STRING |
| **Tamanho** | 5 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código do Tipo do Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código  do Tipo do Contrato |

|  |  |
| --- | --- |
| **Campo** | NIVELAPROVACAOPERIODICO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nível de Aprovação de Item Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Periódico |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIGPERIODICO |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow de Item Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Periódico |

|  |  |
| --- | --- |
| **Campo** | NIVELAPROVACAONAOPERIODICO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nível de Aprovação de Item Não Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Não Periódico |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIGNAOPERIODICO |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow de Item Não Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Não Periódico |

|  |  |
| --- | --- |
| **Campo** | NIVELAPROVACAOMEDICAO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nível de Aprovação de Item de Medição |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item de Medição |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIGMEDICAO |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow de Item de Medição |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item de Medição |

Tabela: TTCNWESTADOPERIODICO

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Coligada do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | CODTCN |
| **Tipo** | STRING |
| **Tamanho** | 5 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código do Tipo do Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código  do Tipo do Contrato |

|  |  |
| --- | --- |
| **Campo** | NIVELAPROVACAOPERIODICO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nível de Aprovação de Item Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Periódico |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIGPERIODICO |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow de Item Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Periódico |

|  |  |
| --- | --- |
| **Campo** | ESTADOFLUIG |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Estado de Aprovação do Item Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Estado de Aprovação do Item Periódico |

Tabela: TTCNWESTADONAOPERIODICO

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Coligada do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | CODTCN |
| **Tipo** | STRING |
| **Tamanho** | 5 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código do Tipo do Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código do Tipo do Contrato |

|  |  |
| --- | --- |
| **Campo** | NIVELAPROVACAONAOPERIODICO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nível de Aprovação de Item Não Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Não Periódico |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIGNAOPERIODICO |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow de Item Não Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item Não Periódico |

|  |  |
| --- | --- |
| **Campo** | ESTADOFLUIG |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Estado de Aprovação do Item Não Periódico |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Estado de Aprovação do Item Não Periódico |

Tabela: TTCNWESTADOMEDICAO

|  |  |
| --- | --- |
| **Campo** | CODCOLIGADA |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Coligada do Item de Contrato |

|  |  |
| --- | --- |
| **Campo** | CODTCN |
| **Tipo** | STRING |
| **Tamanho** | 5 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Código do Tipo do Contrato |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código do Tipo do Contrato |

|  |  |
| --- | --- |
| **Campo** | NIVELAPROVACAOMEDICAO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Nível de Aprovação de Item de Medição |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item  de Medição |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIGMEDICAO |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow de Item  de Medição |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Nível de Aprovação de Item de Medição |

|  |  |
| --- | --- |
| **Campo** | ESTADOFLUIG |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Estado de Aprovação do Item de Medição |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Estado de Aprovação do Item de Medição |

### (Opcional)

## Grupo de Perguntas

 

*<Informações utilizadas na linha Protheus>.*

 

**Nome: FINSRF2**

|  |  |
| --- | --- |
| **X1\_ORDEM** | 01 |
| **X1\_PERGUNT** | Emissão De |
| **X1\_TIPO** | D |
| **X1\_TAMANHO** | 8 |
| **X1\_GSC** | G |
| **X1\_VAR01** | MV\_PAR01 |
| **X1\_DEF01** | Comum |
| **X1\_CNT01** | '01/01/08' |
| **X1\_HELP** | Data inicial do intervalo de emissões das guias de DARF a serem consideradas na seleção dos dados para o relatório |

### (Opcional)

## Consulta Padrão

*<Informações utilizadas na linha Protheus>*

**Consulta: AMB**

|  |  |
| --- | --- |
| **Descrição** | Configurações de Planejamento |
| **Tipo** | Consulta Padrão |
| **Tabela** | “AMB” |
| **Índice** | “Código” |
| **Campo** | “Código”; ”Descrição” |
| **Retorno** | AMB->AMB\_CODIGO |

### (Opcional)

## Estrutura de Menu

*<Informações utilizadas na linha Datasul>.*

**Procedimentos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Procedimento** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Módulo** |  |  |  |
| **Programa base** |  |  |  |
| **Nome Menu** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Registro padrão** | Sim | Sim | Sim |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Release de Liberação** |  |  |  |

**Programas**

|  |  |  |  |
| --- | --- | --- | --- |
| **Programa** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Nome Externo** |  |  |  |
| **Nome Menu/Programa** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Nome Verbalizado**[1]**** | (Max 254 posições) | (Max 254 posições) | (Max 254 posições) |
| **Procedimento** |  |  |  |
| **Template** | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) |
| **Tipo**[2]**** | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Categoria**[3]**** |  |  |  |
| **Executa via RPC** | Sim/Não | Sim/Não | Sim/Não |
| **Registro padrão** | Sim | Sim | Sim |
| **Outro Produto** | Não | Não | Não |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Query on-line** | Sim/Não | Sim/Não | Sim/Não |
| **Log Exec.** | Sim/Não | Sim/Não | Sim/Não |
| **Rotina (EMS)** |  |  |  |
| **Sub-Rotina (EMS)** |  |  |  |
| **Localização dentro da Sub Rotina (EMS)** |  |  |  |
| **Compact**[4]**** | Sim/Não | Sim/Não | Sim/Não |
| **Home**[5]**** | Sim/Não | Sim/Não | Sim/Não |
| **Posição do Portlet**[6]**** | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right |
| **Informar os papeis com os quais o programa deve ser vinculado** |  |  |  |

**Cadastro de Papéis**

*<O cadastro de papéis é obrigatório para os projetos de desenvolvimento FLEX a partir do Datasul 10>.*

*<Lembrete: o nome dos papeis em inglês descrito neste ponto do documento, devem ser homologados pela equipe de tradução>.*

|  |  |
| --- | --- |
| **Código Papel** | **(máx 3 posições)** |
| **Descrição em Português\*** |  |
| **Descrição em Inglês\*** |  |

---

[1] Nome Verbalizado é obrigatório para desenvolvimentos no Datasul 10 em diante.

[2] Tipo é obrigatório para desenvolvimento no Datasul 10 em diante

[3] Categorias são obrigatórias para os programas FLEX.

[4] Obrigatório quando o projeto for FLEX

[5] Obrigatório quando o projeto for FLEX

[6] Obrigatório quando o projeto for FLEX

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
