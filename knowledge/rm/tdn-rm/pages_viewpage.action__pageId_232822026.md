---
content_hash: be2f262036465b4584337fd4f7cb381bc70400ee8d2feddf8cbcc14d5ad3e606
fetched_at: '2026-06-29T00:06:27.438417+00:00'
page_id: '232822026'
product: rm
source: tdn-rm
title: ER_PCREQ-9555_Aprovação de Cotação via Workflow Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232822026
version: 127
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | PDR\_CP\_MOV010 | **IRM1** | PCREQ-4508 |
| **Requisito1** | PCREQ-9555 | **Subtarefa1** | PDR\_CP\_MOV010-106 |
| **Chamado2** |  | | |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

A integração do Fluig com o TOTVS Gestão de Estoque, Compras e Faturamento para o módulo de Cotação consistirá na geração automática de *workflows de Aprovação**,*no Fluig, de acordo com a parametrização para a aprovação da Cotação e com a prévia aprovação de um usuário para a Geração de Ordem de Compra.

## Definição da Regra de Negócio

* ## **Parâmetros Globais**

  Para a utilização da integração do TOTVS Gestão de Estoque, Compras e Faturamento com o Fluig é necessário configurar em Parâmetros Globais, que está disponível em Ambiente | Parâmetros | Globais, na Pasta Integração Fluig, o Servidor, Usuário, Senha e Id da Empresa no Fluig.

* ## **Parâmetros da Cotação**

*Nos parâmetros de Cotação, que está disponível em Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento, estará disponível na Etapa 13 - Workflow Fluig no Menu **04.06.02 - Workflow Fluig** os campos abaixo através dos quais será parametrizada a Aprovação de Cotação através do Fluig. Vide Protótipo 1.*

* Aprovação: Este campo definirá se a Cotação irá realizar a Aprovação através de Workflow, com as opções Usa e Não Usa.
* Geração Automática de Workflow: Este campo possibilitará realizar a inclusão/alteração de Cotação sem a necessidade de que seja realizada a inclusão do workflow no Fluig, sendo necessário realizar o Processo de Geração de Workflow offline para realizar a inclusão do workflow no Fluig. O parâmetro terá o seu valor padrão como verdadeiro.
* Processo: Este campo irá definir o processo do Fluig que será utilizado para a inclusão do Workflow.
* Estados de Aprovação: Este campo irá definir todos os estados possíveis de aprovação final para o processo selecionado. Não será permitido informar estados repetidos para o mesmo processo.  
    
  Será utilizado para a Geração Automática de Workflows o campo abaixo que está disponível na Etapa 12 - Relatório:
* Relatório Quadro Comparativo Default .Net: O relatório selecionado neste campo será enviado como anexo do processo ao ser gerado o workflow da Cotação.

*Os parâmetros de Cotação por Filial**estará disponível na Etapa 13 - Workflow Fluig no Menu **04.06.02 - Filial X - Workflow Fluig por Filial** serão os mesmos campos supracitados dos quais será parametrizada a Aprovação de Cotação através do Fluig.*

* ## Item Utilizado:

Item Utilizado é um conceito para que seja possível realizar o rastreamento de Workflows com as Cotações que foram geradas Ordem de Compra, e portanto, guardar um histórico. Abaixo é citado em cada processo como é o comportamento deste campo que está nas tabelas de relacionamento e que receberá os valores Verdadeiro(1) e Falso(0).

* ## Inclusão de Cotação

  Na Inclusão da Cotação não será realizada a inclusão de Workflow no Fluig.
* ## Alteração de Cotação

  Na Alteração da Cotação somente será executado o processo de Estorno e Inclusão de Workflow para as Cotações com Status igual a Negociação de Melhor Oferta e Ordem de Compra Parcialmente Gerada e que se faça necessário realizar o Calculo do Quadro Comparativo. Caso, o Item Utilizado do workflow for verdadeiro (1) e o será realizado a inclusão de um novo Workflow, caso contrário será estornado o workflow em aberto e incluído um novo workflow.
* ## Exclusão de Cotação

  Na Exclusão da Cotação é estornado o Workflow, caso o Item Utilizado do workflow for falso (0).
* ## Calcular Quadro Comparativo

  Ao executar o Processo de Calcular Quadro Comparativo será estornado o workflow associado a cotação,  se o Item Utilizado igual a Falso (0), e incluído um novo workflow.
* ## Gerar Ordens de Compra

  Ao executar o Processo de Gerar Ordens de Compra é realizada a consulta no estado do workflow, e de acordo com a parametrização, somente se aprovado será possível gerar o movimento de Ordem de Compra, caso contrário será exibida a mensagem: "Cotação pendente de aprovação no Workflow no Fluig." O campo Item Utilizado terá o seu valor alterado para verdadeiro (1).
* ## Estornar Item não Recebido

  Ao executar o processo de Estorno de Item não Recebido o campo Item Utilizado terá o seu valor alterado para falso (0), somente se for o último Item de Movimento vinculado a Cotação e consequentemente a cotação tiver o seu status alterado para Negociação da Melhor Oferta.
* ## Cancelar Movimento

  Ao executar o processo de Cancelar o Movimento o campo Item Utilizado terá o seu valor alterado para falso (0), somente se for o último Movimento vinculado a Cotação e consequentemente a cotação tiver o seu status alterado para Negociação da Melhor Oferta.

* ## Processo Geração de Workflow

  De acordo com o parâmetro "Geração Automática de Workflow"  será permitido executar as ações da Cotação sem realizar a inclusão do Workflow. Na visão da Cotação terá um processo de Geração Workflow, onde, serão gerados os workflows para as cotações incluídas e que estejam com o Status igual a Negociação de Melhor Oferta e Ordem de Compra Parcialmente Gerada, sendo necessário executar o processo para a Geração de Ordem de Compra quando se utilizar a aprovação por workflow e a parâmetro anterior estiver marcada.

  O processo terá um parâmetro para que seja selecionado um Quadro Comparativo externo ao informado e caso não seja informado o processo irá considerar o campo Relatório Quadro Comparativo Default .Net. que está disponível na Etapa 12 - Relatórios. Vide Protótipo 2.

* ## Workflow de Exemplo

Será disponibilizado um workflow de exemplo para que se possa utilizar a Aprovação de Cotação através do Fluig. Os estados de Aprovação e Reprovação serão Reprovado, Aprovado e Aprova e Gera Ordem de Compra. Na Etapa de Aprovação Automática o Workflow será avançado automaticamente para Etapa Aprovado se o somatório dos valores dos itens da cotação que participam do workflow for inferior a R$ 10.000,00 (Dez mil reais). Vide protótipo 3.

* ## Utilização dos Serviços do Workflow

Será utilizada a classe de DataServer "CmpCotacaoFluigData" do Totvs Gestão de Estoque, Compras e Faturamento para a exibição dos dados do Formulário de aprovação do Workflow do Contrato via o DataSet "wsDatasetCmpNucleus" do Fluig, onde o mesmo, consome o serviço de wsDataServer de nome RMWsDataServer.

Importante: Para consumir o DataSet do Fluig é necessário criar um serviço no TDS para o DataServer do RM. Para maiores informações sobre acesso ao webservice RM acesse:

<http://tdn.totvs.com/pages/releaseview.action?pageId=185748469>

Para maiores informações para realizar cadastro de serviços no Fluig acesse:

<http://tdn.totvs.com/pages/releaseview.action?pageId=73082260#IntegraçãoComAplicativosExternos-AcessandoWebServicesapartirdoFluig>

Para maiores informações para a importação de Workflow acesse:

[Importação e exportação de projeto no Fluig Studio](http://tdn.totvs.com/pages/viewpage.action?pageId=128681226)

***Tabelas Utilizadas***

* *TCCOTACAO – Cotações*
* *TCPARAMETROS – Parâmetros da Cotação*
* *TCCOTACAOWFLUIG - Relacionamento entre Cotação e Workflow Fluig*

### Opcional

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

**Protótipo 03**

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

### Opcional

## Dicionário de Dados

Tabela: TCCOTACAOWFLUIG

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
| **Help de Campo** | Informar o Código da Coligada da Cotação |

|  |  |
| --- | --- |
| **Campo** | CODCOTACAO |
| **Tipo** | VARCHAR |
| **Tamanho** | 15 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Identificador da Cotação |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Código da Cotação |

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
| **Help de Campo** | Informar o Identificador do Workflow do Fluig |

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
| **Help de Campo** | Informar se o Item utilizado no Processo Relacionado |

Tabela: TCPARAMETROS

|  |  |
| --- | --- |
| **Campo** | USAAPROVACAO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar se Usa Aprovação na Cotação |

|  |  |
| --- | --- |
| **Campo** | GERAWORKFLOWAUTOMATICO |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Código da Coligada |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar se Workflow será gerado Automaticamente. |

Tabela: TCPARAMETROSWFLUIG

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
| **Help de Campo** | Informar o Código da Coligada |

|  |  |
| --- | --- |
| **Campo** | IDPARCOMPRAS |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim ( X ) Não (  ) |
| **Descrição** | Identificador de Parâmetros de Compras |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Identificador de Parâmetros de Compras |

|  |  |
| --- | --- |
| **Campo** | PROCESSOFLUIG |
| **Tipo** | STRING |
| **Tamanho** | 100 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Processo de Workflow da Cotação |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Processo de Workflow da Cotação |

|  |  |
| --- | --- |
| **Campo** | ESTADOFLUIG |
| **Tipo** | INTEGER |
| **Tamanho** | 0 |
| **Valor Inicial** | N/A |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Estado de Aprovação da Cotação |
| **Título** | N/A |
| **Picture** | N/A |
| **Help de Campo** | Informar o Estado de Aprovação da Cotação |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
