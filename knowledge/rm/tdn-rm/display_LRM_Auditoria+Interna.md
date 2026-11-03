---
content_hash: da65ed2c9ddb4c2b6dd615cd822b7ac3beba20516605be386b992217f3969eb2
fetched_at: '2026-06-29T00:11:06.398883+00:00'
page_id: '634263886'
product: rm
source: tdn-rm
title: Auditoria Interna
type: documentation
url: https://tdn.totvs.com/display/LRM/Auditoria+Interna
version: 33
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Auditoria Interna**
3. **Itens da Auditoria Interna**
4. **Realizar Auditoria Otimizada**
5. **Realizar Auditoria Completa**
6. **Retornar para Auditoria**
7. **Parâmetros**

SumárioVisão Geral

## **01. Visão Geral**

A rotina de Auditoria Interna consiste em uma análise detalhada das contas liberadas pelo faturamento, garantindo que o setor de auditoria possa revisar todos os serviços prestados, como exames, medicamentos, procedimentos médicos e outros itens cobrados, antes que a conta seja enviada para a operadora. Essa etapa é fundamental para evitar erros, disputas com convênios e glosas.

Esse processo é geralmente realizado por uma equipe dedicada da operadora ou por um time independente do setor de faturamento do prestador, trazendo uma perspectiva imparcial aos processos. Essa abordagem ajuda a distribuir o trabalho de forma mais eficiente, evitando o conflitos de responsabilidades entre o time de Faturamento e Auditoria.

Auditoria Interna

## **02. Tela de Auditoria Interna**

O módulo de Auditoria Interna pode ser acessado em **Faturamento** > **Particular e Convênios** > **Auditoria Interna**.

Ao acessar a tela, serão exibidos os seguintes campos para realizar o filtro:

* + **Convênio** (obrigatório): Define o convênio para a pesquisa.

    - **Apenas convênios ativos**: Este campo, marcado por padrão, retorna apenas convênios ativos para serem informados na pesquisa.
  + **Período** (obrigatório): Define o início e o fim do período. Por padrão, é definido entre o primeiro e o último dia do mês atual.
  + **Unidade de Faturamento** (opcional)
  + **Status da Auditoria** (opcional): Com as opções **Todos**, **Pendente**, **Iniciada** e **Concluída**.
  + **Status da Parcial** (opcional): Com as opções **Todos**, **Elaboração**, **Liberada** e **Faturada**.
  + **Tipo de Paciente** (opcional): Com as opções **Todos**, **Internos** e **Externos**.

Após preencher os filtros, basta clicar em "Filtrar" para carregar os registros. Os dados exibidos incluem atendimento, parcial, paciente e o status da auditoria.

Itens da Auditoria Interna

## **03. Itens da Auditoria Interna**

Após efetuar a pesquisa, é possível abrir um formulário para o registro selecionado e clicando em "Editar".

Neste formulário serão exibidas todas as informações contidas na visão anterior como somente leitura, um campo editável para informar alguma observação da auditoria (habilitado apenas após efetuar a auditoria) e uma lista dos itens da conta.

Realizar Auditoria Otimizada

## **04. Realizar Auditoria Otimizada**

Para realizar a auditoria, é necessário selecionar uma conta (apenas uma por vez), então clicar no botão "Realizar Auditoria Otimizada" ou "Realizar Auditoria Completa".

Na tela de processamento da auditoria otimizada, há um cabeçalho que exibe informações da conta, como o nome do paciente, o atendimento e o total da conta. Esse total é recalculado automaticamente sempre que há alterações nas seleções de registros ou nos valores dos campos de quantidade e valor unitário.

Logo abaixo, são listados todos os itens do anexo da visão principal. Um painel adicional, com campos editáveis, permite a manipulação detalhada do registro que está atualmente selecionado.

Para auditar um item, é necessário modificar a quantidade e/ou o valor unitário, além de preencher o Tipo de Auditoria Pré-Glosa e o Motivo de Auditoria Pré-Glosa. O preenchimento do campo de observações é opcional.

Para agilizar o preenchimento dos campos de quantidade e valor, existe a funcionalidade de replicação. Por exemplo, se o valor de um item foi alterado de 10,00 para 15,00 e ele foi lançado 10 vezes na conta, é possível clicar em "Replicar Valores" para aplicar essa alteração automaticamente a todos os lançamentos do item.

Também há uma opção de reverter a auditoria. Essa funcionalidade restaura os campos "Qtd. Alterada" e "Valor Un. Alterado" para os valores originais, ou seja, "Qtd. Original" e "Valor Un. Original", registrados na conta do paciente.

 Além disso, os valores alterados são destacados com um fundo amarelo claro, facilitando sua identificação.

Na lateral esquerda, existe uma aba de conclusão, com o preenchimento opcional da campo observação.

Após selecionar o(s) item(s) e alterar seu valor unitário e/ou quantidade, basta clicar em "Executar" que a auditoria é aplicada aos registros alterados e aos campos preenchidos, gerando um log detalhado dos itens processados ou de eventuais avisos de negócio.

Dica

Mesmo que existam itens selecionados na grid por meio da coluna de marcação (check), todos os registros serão enviados para serem processados. A coluna de marcação é utilizada exclusivamente para as funcionalidades de replicação de valores e reversão da auditoria dos itens em tela.

Realizar Auditoria Completa

## **05. Realizar Auditoria Completa**

Para realizar a auditoria, é necessário selecionar uma conta (apenas uma por vez), então clicar no botão "Realizar Auditoria Otimizada" ou "Realizar Auditoria Completa".

A realização da auditoria completa é efetuada pela tela da elaboração de contas, tornando-se mais fácil incluir itens faltantes e realizar a impressão da conta médica.

Como a auditoria é efetuada em determinada parcial, a elaboração de contas exibe apenas esta parcial, bloqueando a edição da mesma ou da inclusão de novas parciais.

A auditoria dos itens pode ser efetuada acessando as abas dos grupos de gastos (honorário, diária, etc...), selecionando um dos itens lançados, abri-lo e ir ate aba Auditoria.

Com isso será exibida a tela de auditoria, informando valores e quantidades originais, e permitindo informar a quantidade e/ou valor unitário auditado.  
Deve-se informar também o tipo e motivo de pré-glosa, e pode-se informar uma observação.

Após o preenchimento de todas as informações, basta clicar em "Salvar" que a auditoria do item será realizada.

Para inclusão de um item na auditoria, basta clica no icone de inserir do grupo d gasto e preencher o item desejado, podendo alterar seu valor unitário.

Após preenchimento ir na aba Auditoria para preencher os campos obrigatórios da auditoria,

Dica

Caso seja adicionado um novo item na conta durante a auditoria, o processo será executado automaticamente após salvar.

Todos os itens auditados são identificados com um check na coluna 'Auditoria'.

Quando houver uma diferença entre a quantidade original e uma quantidade menor, essa diferença será transferida para itens grátis.

Ao fechar fechar rotina de **Elaboração de contas,** será exibida **mensagem de confirmação** .Com opções "Sim - Concluir auditoria" e "Não - Manter auditoria em andamento".

Será alterado o **status da auditoria** para "Concluída" quando o usuário confirmar a conclusão da auditoria e um  formulário de conclusão será chamado onde poderá ser informado observações da auditoria.

Retornar para Auditoria

## **06. Retornar para Auditoria**

Para retornar uma parcial para auditoria, o status da auditoria deve estar como '**Concluída**' e o status da parcial como '**Liberada**'. Somente nessas condições será possível retornar a parcial para correção.

A parcial não pode ser alterada se seu status estiver como '**Faturada**', pois já integra uma remessa destinada ao convênio. No entanto, caso a remessa ainda não tenha sido enviada, será possível realizar a auditoria. Nesse caso, é necessário retornar a conta para correção utilizando a rotina de Faturamento para Convênio, selecionar a opção 'Retornar para Auditoria', realizar as alterações necessárias e concluir a auditoria novamente.

O processo de retornar para auditoria, pode ser realizar de duas formas

* + Reabrir auditoria e manter os itens auditados - os itens permanecem auditados e o status da auditora muda para Iniciada
  + Cancelar auditoria e excluir os itens auditados - os itens voltam para o seu valor original e o status da auditoria volta para pendente.

Parâmetros

## **07. Parâmetros**

Atenção!

Ao habilitar a auditoria de contas em elaboração, esteja ciente de que isso pode impactar o fluxo de trabalho e a consistência dos dados, já que as contas ainda não estão finalizadas. Recomenda-se utilizar essa opção apenas em situações específicas e com acompanhamento rigoroso da equipe responsável.

Por padrão, e **o recomendado**, é que a auditoria interna seja realizada apenas em **parciais com status "liberadas para faturamento"**. No entanto, é possível configurar o parâmetro **"Faturamento → Permite auditar contas em elaboração"** para que o sistema também exiba contas em elaboração, permitindo a realização do processo de auditoria.
