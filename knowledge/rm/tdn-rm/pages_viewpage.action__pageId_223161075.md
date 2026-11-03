---
content_hash: 98d6885a16ed923d07939e18dcc2dcbec1287efec6ae131e42d1b8b83802adc4
fetched_at: '2026-06-29T00:06:21.104224+00:00'
page_id: '223161075'
product: rm
source: tdn-rm
title: DT_Fluig_Workflow_Aprovação_de_Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223161075
version: 6
---

# Aprovação de Contrato via Workflow Fluig

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Gestão de Estoque, Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Manutenção de Contrato* | *CtrCntAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de Workflow de Contrato.* | *CtrGeraWorkflowFluigProcAction* | | *Tipos de Contrato* | *CtrTipCntAction* | |
| **Cadastros Iniciais:** | *Tipo de Contrato* |
| **Parâmetro(s):** | *Ambiente | Parâmetros | Globais | Integração Fluig*   *Ambiente | Parâmetros | Gestão de Estoque Compras e Faturamento | Contratos | Workflow Fluig* |
| **Ponto de Entrada:** | **Não se aplica.** |
| **Chamados Relacionados** | **Não se aplica.** |
| **Requisito (ISSUE):** | **PDR\_CP\_MOV008-97** |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL Server e Oracle.* |
| **Tabelas Utilizadas:** | * *TCNT - Contratos* * *TCNCTPAR - Parâmetros do Contrato* * *TITMCNT – Itens de Contrato* * *TITMCNTMEDICAO - Medições de Item de Contrato* * *TITMCNTWFLUIG  - Relacionamento entre Item de Contrato e Workflow Fluig* * *TITMCNTMEDICAOWFLUIG  - Relacionamento entre Medição e Workflow Fluig* * *TTCNWFLUIG - Relacionamento do Tipo e os Parametros de Workflow* * *TTCNWESTADOPERIODICO - Estados de Aprovação do Item Periódico.* * *TTCNWESTADONAOPERIODICO - Estados de Aprovação do Item Não Periódico.* * *TTCNWESTADOMEDICAO - Estados de Aprovação do Item de Medição.* |
| **Sistema(s) Operacional(is):** | *Windows* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | **Não se aplica.** |
| **Versão Expedida:** | *12.1.9* |

## Descrição

A integração do Fluig com o TOTVS Gestão de Estoque, Compras e Faturamento consistirá na geração automática de Workflows de Aprovação, no Fluig, dada a inclusão de um Contrato que esteja parametrizado para o mesmo e que seja necessário a aprovação de um usuário para faturamento.

## Importante

Não será permitido alterar o Cadastro de Tipos de Contrato e o campo "Tipo de Contrato" no cadastro do Contrato caso tenha algum Item de Contrato ou Medição tenha o Item Utilizado como verdadeiro.

Somente Status e Tipo de Contrato quando alterados no Contrato realizam alterações nos Workflows gerados independente do Nível de Aprovação, ou seja, quando o Status for alterado no Contrato para outro que também tenha o campo "Faturar" marcado, não será realizado Estorno e Inclusão. Se for alterado para um Status que também tenha o campo "Cancelar" marcado, deverá ser realizado o estorno e não será realizada a Inclusão.

O campo Status terá o mesmo comportamento para o Item de Contrato, conforme supracitado do Contrato.

Ao realizar alteração no Campo Tipo Faturamento do Item de Contrato, será realizado o estorno, para os Itens e Medições que não tenha sido Utilizado, e inclusão de acordo com os Parâmetros do Tipo de Faturamento anterior à alteração, por exemplo, se um contrato tem 3 Itens de Contrato e é parametrizado o Nível de Aprovação para Contrato os Itens Periódico e Não Periódico e a Medição é por Medição, ao realizar uma alteração do campo da medição para Não Periódico, os Workflows de medição associado a este Item de Contrato serão estornados, bem como, os demais Workflows dos Itens de Contrato Periódico e Não Periódico, devido o Nível de Aprovação ser por Contrato.

## Procedimento para Implantação

Os procedimentos para configuração dos Workflows estão detalhados no link abaixo:

## Procedimento para Configuração

Os procedimentos para configuração no Totvs Gestão de Estoque, Compras e Faturamento:

Uma vez informado o Nível de Aprovação será obrigatório informar o Processo e os Estados de Aprovação. Caso seja selecionado o Nível de Aprovação para Contrato, para dois ou mais Itens de Contrato será gerado apenas um Workflow para aprovação para os mesmos, devendo respeitar a restrição de que o processo e o estado de aprovação para ambos deverá ser o idêntico.

* ## Parâmetros Globais

Para a utilização da integração do TOTVS Gestão de Estoque, Compras e Faturamento com o Fluig é necessário configurar em Parâmetros Globais na Pasta Integração Fluig, o Servidor, Usuário, Senha e Id da Empresa no Fluig.

* ## Parâmetros de Contrato

Nos parâmetros de Contrato estará disponível no Menu 04.05.07 - Workflow Fluig os campos abaixo através dos quais será parametrizada a Aprovação de Faturamento de Contrato através do Fluig.

* Aprovação: Este campo definirá se o Contrato irá realizar a Aprovação através de Workflow, com as opções Usa e Não Usa
* Geração Automática de Workflow: Este campo possibilitará realizar a inclusão de Contratos e/ou Itens de Contrato e Medição sem a necessidade de que seja realizada a inclusão do Workflow no Fluig, sendo necessário realizar o Processo de Geração de Workflow offline para realizar a inclusão do Workflow no Fluig. O parâmetro terá o seu valor padrão como verdadeiro.

Na aba do cadastro de Tipos de Contrato os campos Nível de Aprovação, Processo e Estados de Aprovação ficarão habilitados somente se Aprovação estiver selecionada com Usa e o Usuário tiver permissão de alteração. Os Workflows serão gerados de acordo com o Nível de Aprovação utilizado para cada grupo de Tipo de Faturamento parametrizado. E ao realizar o vínculo do Tipo de Contrato no cadastro do Contrato, o mesmo respeitará as configurações dos campos abaixo para a geração de Workflows.

* Nível de Aprovação: Este campo irá definir o Nível de Aprovação utilizado. As opções disponíveis são: Contrato, Item de Contrato e Medição. Caso, seja selecionado a opção de Contrato, será gerado um único Workflow por Contrato, contendo as informações de todos os Itens de Contrato. Para a opção selecionada de Item de Contrato será incluído um Workflow por Item de Contrato, e caso seja selecionada a opção Medição será gerado um Workflow para cada medição incluída, com as suas respectivas informações.
* Processo: Este campo irá definir o processo do Fluig que será utilizado para a inclusão do Workflow.
* Estados de Aprovação: Este campo irá definir todos os estados possíveis de aprovação final para o processo selecionado. Não será permitido informar estados repetidos para o mesmo processo.

Uma vez informado o Nível de Aprovação será obrigatório informar o Processo e os Estados de Aprovação. Caso seja selecionado o Nível de Aprovação para Contrato, para dois ou mais Itens de Contrato será gerado apenas um Workflow para aprovação para os mesmos, devendo respeitar a restrição de que o processo e o estado de aprovação para ambos deverá ser o idêntico.

## Procedimento para Utilização

 1.  A utilização da aprovação de Contratos através de Workflow Fluig se dará através da Inclusão, Alteração e Exclusão de Contrato, Item de Contrato e Medição, de acordo, com o Tipo de Contrato e suas devidas configurações para Geração de Workflows.

* + ********Item Utilizado:********

    Item Utilizado é um conceito para que seja possível realizar o rastreamento de Workflows com os Contratos e Itens de Contrato / Medição que foram faturados, e portanto, guardar um histórico. Abaixo é citado em cada processo como é o comportamento deste campo que está nas tabelas de relacionamento e que receberá os valores Verdadeiro(1) e Falso(0).
  + **Inclusão:**

    Dada a Inclusão do Contrato para Itens de Medição, caso o nível de aprovação selecionado seja Contrato, será gerado para todos os Itens apenas um Workflow, caso seja selecionada a opção de Item de Contrato será gerado um Workflow para cada Item de Contrato. Se o Nível de aprovação for igual a Medição será gerado um Workflow para cada medição incluída com os seus respectivos dados.

    Para todas as inclusões, se dois ou mais Tipos de Faturamento estiverem utilizando o Nível de Aprovação para Contrato, os Itens de Contrato deverão ser agrupados e gerar apenas um Workflow.

    Dada a Inclusão do Contrato para Itens Periódicos e\ou Não periódicos, caso o nível de aprovação selecionado seja Contrato, será gerado para todos os Itens apenas um Workflow, caso seja selecionada a opção de Item de Contrato será gerado um Workflow para cada Item de Contrato.
  + **Alteração:**

    Para a alteração dos Itens de Contrato Periódicos e Não Periódicos, caso o Nível de aprovação selecionado seja Contrato, somente será incluído o Workflow para os Itens de Contrato que estejam com esta parametrização. Caso, seja selecionado o Nível de aprovação por Item de Contrato, somente os Itens que possuem esta parametrização terão os seus Workflows incluídos. Na alteração do Item de Contrato, se o Item Utilizado do Workflow for verdadeiro (1) e o Nível de aprovação for Contrato ou Item de Contrato será realizado a inclusão de um novo Workflow, caso contrário será estornado o Workflow em aberto e incluído um novo Workflow.

    Para a alteração de Itens de Contrato de Medição, caso o Nível de aprovação selecionado seja Contrato, somente será incluído o Workflow para as Medições dos Itens de Contrato que estejam com esta parametrização. Caso, seja selecionado o Nível de aprovação por Item de Contrato, somente para as Medições dos Itens de Contrato que possuem esta parametrização terão os seus Workflows incluídos. Se o Nível de aprovação for igual a Medição será gerado um Workflow para cada medição na alteração da Medição. Na alteração da Medição, se o Item Utilizado do Workflow for verdadeiro (1) e o Nível de aprovação for Contrato ou Item de Contrato será realizado a inclusão de um novo Workflow, caso contrário será estornado o Workflow em aberto e incluído um novo Workflow.
  + **Exclusão:**  
       
    Na Exclusão de Contrato, Item de Contrato e Medição o Workflow é estornado e incluído Workflows de acordo com a regra de Alteração de Contrato.

2.  Para os Processos de Cancelamento de Contrato, Itens de Contrato, Reajustar e Desfazer Reajuste de Preços serão tratados de acordo com a regra de Alteração de Preço. Entretanto, no Cancelamento não serão incluídos novos Workflows.

3.  No processo de realizar o Cancelamento do Movimento associado ao Item de Contrato ou Medição, será alterado o Item Utilizado do último Workflow aprovado e utilizado. Se houver um novo Workflow não utilizado ao realizar cancelamento do Movimento não poderá alterar o valor do Item Utilizado. Portanto, no cancelamento o Item Utilizado voltará para o valor Falso apenas quando o Item de Contrato tiver o Status "A Faturar'. Exemplo: No caso de Itens de Contrato de Tipo de Faturamento Periódico somente irá alterar o Item Utilizado para falso quando o último movimento gerado for cancelado\excluído.

4.  No Faturamento do Contrato é realizada a consulta no estado do Workflow, e conforme o Nível de aprovação, se aprovado, serão faturados de acordo com a própria regra, os Itens de Contrato Periódicos, Não Periódicos e Medições e o campo Item Utilizado terá o seu valor alterado para verdadeiro (1).

5.  Na visão do Contrato terão botões que possibilitam filtrar os Contratos  aprovados e não aprovados de acordo com o estado do Workflow parametrizado. Quando utilizado o agrupamento por Item de Contrato ou Medição será considerado aprovado quando o Contrato possuir pelo menos um Item ou Medição aprovado.

6.  Na visão do Contrato terá um processo de Geração Workflow Fluig para Contrato, onde, serão gerados os Workflows para os contratos incluídos, sendo necessário executar o processo para faturamento quando se utilizar a aprovação por Workflow e a parâmetro  de Geração Automática de Workflow estiver desmarcada.

7.  Na visão do Contrato será disponibilizado um anexo mestre\detalhe para consulta dos Itens de Contrato e Medição onde haverá as informações do Item de Contrato como Mestre e os detalhes do Workflow com os Identificador e Status do Processo Fluig, e caso seja Item de Medição é fornecido os dados da Medição.

8.  Será disponibilizado um Workflow de exemplo para que se possa utilizar a Aprovação de Contrato através do Fluig. Os estados de Aprovação e Reprovação serão Reprovado e Aprovado. Na Etapa de Aprovação Automática o Workflow será avançado automaticamente para Etapa Aprovado se o somatório dos valores dos itens de contrato que participam do Workflow for inferior a R$ 10.000,00 (Dez mil reais).

divs
