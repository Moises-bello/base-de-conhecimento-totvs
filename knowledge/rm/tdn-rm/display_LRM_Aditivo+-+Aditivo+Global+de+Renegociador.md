---
content_hash: ad8b643c44d86b0dc451689f07231b5a6f20740f5313aa288f3e40dec9777053
fetched_at: '2026-06-29T00:11:42.728592+00:00'
page_id: '795916551'
product: rm
source: tdn-rm
title: Aditivo - Aditivo Global de Renegociador
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivo+-+Aditivo+Global+de+Renegociador
version: 12
---

A partir do Release 12.1.2310 o TCGI permite que sejam incluídas, de forma global, novas parcelas em contratos de financiamento imobiliário que estejam efetivados, de forma simples e eficaz, através da ferramenta **Aditivo Global de Renegociador**.

Esta ferramenta é um aditivo centralizador que irá gerar um ou mais Aditivos de Renegociação de Contrato para as vendas dos Empreendimentos ou Contratos filtrados, que estejam em situação Efetivado, conforme as parametrizações aplicadas nele.

Para acessar o menu de *Aditivo Global de Renegociador* é preciso dar Permissões ao [Perfil](https://tdn.totvs.com/pages/viewpage.action?pageId=146182940) dos Usuários, na opção *[01.01.21.01] Aditivo Global de Renegociador* e seus submenus:

Após a concessão da Permissão acima, esta funcionalidade estará acessível através do menu *Vendas | Contrato | Aditivos de Venda | Aditivo Global de Renegociador:*

Ao acessar esta funcionalidade, o sistema apresenta uma janela com duas etapas para parametrização do aditivo a saber:

Na primeira Etapa, deve-se preencher os dados do aditivo e selecionar as vendas ou empreendimentos a serem processados. Nesta tela temos as seguintes opções:

* **Aplicar:** Define o tipo de registros da visão que podem ser selecionados para serem aditivados. As opções disponíveis são:

* + **Empreendimento:** Ao selecionar esta opção o sistema exibe os dados dos empreendimentos de todas a coligadas, para que as todas vendas em situação efetivadas, associadas a cada um deles sejam aditivadas;

Por uma questão de performance, recomendamos que não sejam processados todos os Empreendimentos no mesmo aditivo.

* + **Contratos de Venda:** Selecionando esta opção o sistema apresenta os contratos de venda, em situação efetivada, de todas as coligadas, que podem ser filtrados conforme a necessidade desejada.
* **Ação:** Selecione a ação que será executada neste aditivo em relação à tratativa das parcelas das vendas a serem aditivadas. São possíveis as seguintes ações:
  + **Incluir Parcelas:** Ao selecionar esta opção, ao termino de execução deste processo, os aditivos de renegociação criados para as vendas irão inserir novas parcelas às Condições de Financiamento das mesmas conforme as demais parametrizações definidas neste aditivo global;
  + **Alterar Parcelas:** Esta opção permite que as parcelas selecionadas na próxima etapa sejam renegociadas, conforme as demais parametrizações aplicadas a este aditivo global;
  + **Desfazer Aditivo Global:** Esta opção permite que os aditivos de renegociação efetivados pelo Aditivo Global filtrado na próxima etapa sejam desfeitos.

Ao realizar esta ação, o sistema irá desfazer os efeitos do Aditivo Global selecionado e irá excluir o mesmo da visão de aditivos globais. Caso haja a necessidade de se manter um histórico, ou gerar algum relatório destes registros, recomendamos que sejam habilitados os Logs de Auditoria, do **[*TOTVS Audit*](https://tdn.totvs.com/display/LRM/TOTVSAudit)**, nas tabelas destas entidades, conforme ações descritas nos documentos da Central de Atendimento da Totvs, abaixo:

* + - [Framework - Framework RM - BD - Habilitar novo Log de Auditoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003811551-Framework-Framework-RM-BD-Habilitar-novo-Log-de-Auditoria-); e
    - [Framework - Framework RM - BD - Detalhamento técnicos Novo Log de Auditoria](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044791453-Framework-Framework-RM-BD-Detalhamento-t%C3%A9cnicos-Novo-Log-de-Auditoria-).

Reforçamos que para que esta ação seja executada com sucesso para todas as vendas aditivadas pelo Aditivo Global selecionado, não podem haver aditivos posteriores aos criados por ele cadastrado na venda;

Importante!

Não é possível de se desfazer o Aditivo Global de Renegociador em cenários que o TCGI está integrado com o Protheus.

* + **Excluir Parcelas:** Ao selecionar esta opção o sistema permite a exclusão de uma ou mais parcelas, conforme os filtros aplicados na opção *Aplicar* e nos campos do agrupador *Selecione os Filtros para Buscar as Parcelas a Serem Renegociadas*, da etapa seguinte a esta e que estão detalhados mais abaixo.

* **Forma de Rateio do Valor por Subunidade:** Este campo somente é exibido com a *Ação* *Incluir Parcelas*. Nesta opção é possível definir como será realizado o rateio do valor aditivado para as subunidades dos contratos de venda em situação *Efetivado*. Estão disponíveis as seguintes opções:
  + **Valor Fixo:** Ao selecionar esta opção, o valor de aditivo parametrizado no campo *Valor Fixo Contrato*, da próxima etapa, será atribuído integralmente a cada contrato de venda filtrado neste Aditivo Global, conforme a *[Modalidade](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades)* parametrizada;
  + **Fração Ideal:** Ao selecionar esta opção, o sistema irá ratear o valor parametrizado no campo Valor Global Aditivo Rateio, com base na [Fração Ideal](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade) de cada Subunidade do Empreendimento ou Contratos, com situação Efetivado, selecionados para serem aditivados. Caso seja selecionado para Aplicar este valor Por Empreendimento, o sistema irá ratear o valor deste campo para todas as Subunidades do Empreendimento que tenham contrato de venda em situação Efetivado, de acordo com a Fração Ideal dessas subunidades.

Sendo assim, para que o Aditivo Global parametrizado desta forma seja executado com sucesso, é preciso que a [Fração Ideal](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade) esteja devidamente preenchida em todas as subunidades do Empreendimento dos contratos de venda que serão aditivos.

Reforçamos que, conforme a Regra de Negócio do cálculo da Fração Ideal, a soma dessas frações de todas as subunidades do Empreendimento, não deve ser maior que 1.

Exemplo: De forma simples, se um empreendimento tem 1.000 subunidades distribuídas em uma determinada quantidade de blocos, a Fração Ideal de cada uma dessas subunidades, é de 0,001, conforme demonstrado pela lógica aplicada:

Número de Subunidades: 1.000

Total Ideal: 1

Fração Ideal: X

Logo: X = 1 / 1.000 = 0,001;

* + **Peso:** Ao selecionar esta opção, o sistema irá ratear o valor parametrizado no campo Valor Global Aditivo Rateio, com base no [Peso](https://tdn.totvs.com/display/LRM/Unidade+-+Anexos+-+Subunidade) de cada Subunidade do Empreendimento ou Contratos, que estejam com situação Efetivado, selecionados para serem aditivados.

Novamente, para que o Aditivo Global parametrizado desta forma seja executado com sucesso, é preciso que o *Peso* esteja devidamente preenchida em todas as subunidades do Empreendimento dos contratos de venda que serão aditivos.

Reforçamos que, conforme a Regra de Negócio de cálculo do Peso, a soma destes, em todas as subunidades do Empreendimento, não deve ser maior que 1.

**Exemplo:** Se um empreendimento tem 1.000 subunidades distribuídas em uma determinada quantidade de blocos, de uma forma simplificada, o Peso de cada uma dessas subunidades, é de 0,001, conforme demonstrado pela lógica aplicada:

Número de Subunidades: 1.000

Peso Total: 1

Peso: X

Logo: X = 1 / 1.000 = 0,001;

* **Código Aditivo Global:** Este é um campo de texto, que é obrigatório e deve conter um texto para identificar cada Aditivo Global. Este identificador deve ser único, não se permitindo dois aditivos globais com o mesmo Código. Este campo tem tamanho de 100 caracteres;
* **Descrição Aditivo:** Este é um campo de texto, que é obrigatório para descrever o aditivo criado e que será usado como descritivo para o aditivo de cada contrato de venda que for criado a partir deste Aditivo Global. Este campo tem o tamanho de 50 caracteres;
* **Data Aditivo:** Informe a data a partir da qual as alterações parametrizadas neste aditivo serão válidas. Esta informação será utilizada como Data de Aditivo dos aditivos criado para cada contrato de venda que for gerado a partir deste processo;
* **Visão de Empreendimento/Contratos de Vendas:** Nesta visão são exibidos os registros de Empreendimentos ou de Contratos de Vendas que devem ser selecionados para serem aditivados. Como estes registros são exibidos de forma global, ou seja, de todas as coligadas, recomendamos que nesta visão se aplique os filtros necessários para selecionar apenas os que serão processados neste aditivo.

Para melhor performance deste processo, recomenda-se que se utilize os filtros nestas entidades, a fim de evitar processar todos os registros ao mesmo tempo.

Preenchidos estas parametrizações, ao avançar para a próxima etapa são apresentadas, de forma dinâmica em relação às Ações selecionadas, as seguintes parametrizações que serão aplicadas nos registros selecionados anteriormente:

* **Selecione as regras e seus valores a serem inseridos no aditivo:** As opções abaixo são utilizadas como parâmetros das [Condições de Financiamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105119) para geração das parcelas dos aditivos de renegociação das vendas selecionadas na visão anterior. As informações deste agrupador são exibidas com as *Ações*: *Inserir Parcelas* e *Alterar Parcelas*.

Devem ser preenchidas as seguintes informações:

* + **Modalidade:** Selecione a [Modalidade](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades) que será a base para a geração das novas parcelas deste aditivo. O sistema exibe as [modalidades](https://tdn.totvs.com/display/LRM/Plano+-+Modalidades) que tenham os *Tipos de Modalidade Todos* e *Aditivos,* parametrizadas para a Coligada dos registros selecionados na visão e também as modalidades que estejam com a opção *Global* marcada.

Caso sejam selecionadas entidades de coligadas diferentes entre si na visão anterior, Empreendimentos ou Contratos de Vendas, o sistema exibirá somente as Modalidades Globais que atendam os *Tipos* acima, para evitar que regras específicas de uma coligada sejam aplicadas a outras.

Atenção!

É importante ter atenção nesta parametrização, uma vez que neste Aditivo Global, não se pode excluir ou incluir os componentes das Condições de Financiamento que estão configurados nestas modalidades. Ou seja, se neste momento o usuário que está parametrizando este aditivo selecionar uma modalidade que tenha o componente de entrada em sua composição, este tipo de parcela será gerando na conclusão deste processo.

Caso o usuário tenha permissão, ele poderá editar estes componentes porém ao realizar esta ação, ele irá editar diretamente a Modalidade, podendo descaracterizar uma as regras utilizadas para se cadastrar as vendas.

Tenho em vista as esclarecimentos acima, recomenda-se que sejam criadas Modalidades que atendam exatamente as condições necessárias para cada tipo de Aditivo e que os usuários que utilizarão este processo estejam cientes dessas condições.

O campo abaixo também tem comportamento dinâmico, sendo exibido e passível de edição, de acordo com a Ação e com a Forma de Rateio do Valor por Subunidade, parametrizadas na etapa anterior. Sendo:

*Ação: Incluir Parcelas + Forma de Rateio do Valor por Subunidade: Valor Fixo*.

* + **Valor Fixo Contrato:** Utilizando as parametrizações acima, este campo é editável e o valor informado será o mesmo valor para cada um dos Aditivos de Renegociação que forem gerados para os contratos de venda que atendam ao filtro aplicado na visão da etapa anterior.

Este valor será distribuído nas parcelas criadas, conforme parametrizado na Modalidade aplicada acima.

*Ação: Incluir Parcelas + Forma de Rateio do Valor por Subunidade: Fração Ideal ou Peso*

* + **Valor Global Aditivo Rateio:** Utilizando as parametrizações acima, este campo é editável e o valor informado será rateado nos Aditivos de Renegociação que forem gerados conforme a Fração Ideal ou o Peso de cada Subunidade, cujos contratos atendam ao filtro aplicado na visão da etapa anterior.

Este valor será distribuído nas parcelas criadas, conforme parametrizado na Modalidade.

Atenção!

Este campo não é editável quando a *Ação* for: *Alterar Parcelas*, *Desfazer Aditivo Global* ou *Excluir Parcelas*.

* + **Data do 1º Vencimento:** Esta informação é utilizada para definir a data do primeiro vencimento das parcelas geradas na conclusão deste processo. Por padrão, ele recebe a mesma Data  Aditivo informada na primeira etapa deste processo;
  + **Data Base Juros/CM:** Esta informação é utilizada para definir a data base para cálculo da Correção Monetária e dos Juros das parcelas geradas na conclusão deste processo, caso a modalidade selecionada tenha estes componentes em sua composição. Por padrão, ele recebe a mesma Data  Aditivo informada na primeira etapa deste processo;

Atenção!

Este campo não é editável quando a *Ação* for: *Excluir Parcelas*.

As opções abaixo também são exibidas e editáveis de forma dinâmica em relação às Ações aplicadas no Aditivo, permitindo a alteração das mesmas, em determinados cenários:

* **Calcular Valor Presente Aditivo:** Marque esta opção para calcular o deságio das parcelas cuja modalidade utilize os juros Price, trazendo as mesma a valor presente em relação à Data do Aditivo. Esta opção somente pode ser manipulada quando a *Ação* for *Alterar Parcelas*. Para a inclusão e exclusão de parcelas, esta opção não pode ser marcada, devido ao fato das parcelas aditivadas ainda não comporem as Condições de Financiamento das vendas;
* **Permitir Negociar Valores Diferentes:** Esta opção deve ser marcada para que o sistema não realize a consistência entre o *valor total negociado* e o *valor total a negociar*. Esta opção já vem marcada e não pode ser alterada para as *Ações* de *Incluir* e *Excluir Parcelas* uma vez que só estão sendo tratadas esses tipo de parcelas no aditivo. Já para a Ação de Alterar Parcelas ela tem edição livre para que o usuário faça a parametrização desejada;
* **Desconsiderar Multa e Juros de Atraso:** Esta opção permite que o sistema desconsidere o valor dos componentes de Multa de Atraso e de Juros de Mora, que são calculados pelo módulo financeiro. Esta opção somente pode ser manipulada quando a *Ação* for *Alterar Parcelas*. Para a inclusão e exclusão de parcelas, esta opção não pode ser marcada, devido ao fato das parcelas aditivadas ainda não comporem as Condições de Financiamento das vendas;
* **Efetivar Aditivo Automaticamente:** Utilize esta opção para determinar se os aditivos dos contratos de venda tratados neste processo serão efetivados automaticamente ou não. Por padrão, esta opção apresenta o default aplicado na opção Efetivar Aditivo Via Renegociador Global, definido na *[Etapa 1 - Parâmetros do Aditivo](https://tdn.totvs.com/pages/viewpage.action?pageId=435105213)*, dos *Parâmetros* do TCGI. Esta opção pode ser alterada a qualquer momento, caso seja necessário realizar algum tipo de conferência nestes aditivos, antes de efetivá-los.

Importante!

Não recomendamos que este parâmetro esteja marcado em cenários em que há a integração entre o TCGI e o Protheus, pelo fato de não ser possível de se desfazer o Aditivo Global de Renegociador, caso alguma parametrização deste não seja aprovada na conferência.

As opções abaixo são exibidas somente com as Ações Alterar Parcelas e Excluir Parcelas:

* **Selecione os filtros para buscar as parcelas a serem renegociadas:** Utilize as opções abaixo para filtrar as parcelas que serão alteradas ou excluídas por este aditivo global. As opções de filtro disponíveis são
  + **Data Vencimento Inicial:** Selecione a data inicial de vencimento a partir da qual as parcelas que serão listadas no filtro. Esta informação não é obrigatória, sendo utilizada para se criar um filtro mais específico e eficaz.
  + **Data Vencimento Final:** Selecione a data final de corte do vencimento das parcelas que serão filtradas. Esta informação também não é obrigatória, sendo utilizada para se criar um filtro mais específico e eficaz.
  + **Tipo Parcela:** Utilize este campo caso deseje filtrar um tipo de parcela específico. Esta informação não é obrigatória
  + **Código Aditivo Global:** Utilize este campo para filtrar as parcelas que foram geradas por um Aditivo Global de Renegociador. Este campo não é obrigatório, porém ele é muito útil caso se deseje tratar rapidamente as parcelas geradas por aditivo específico;

Ao acionar o botão **Filtrar Parcelas** o sistema apresenta uma **visão** com as parcelas filtradas, sendo possível de se aplicar também os filtros do financeiro nesta visão;

O sistema ainda permite ao usuário **Limpar** as condições aplicadas neste filtro.
