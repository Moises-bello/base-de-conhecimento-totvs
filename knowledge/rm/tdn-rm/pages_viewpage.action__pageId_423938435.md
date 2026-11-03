---
content_hash: eb011cb4640818ae314b4a9ca422b897f9d752f2287579c55e10a4f4b9705ec6
fetched_at: '2026-06-29T00:09:26.817669+00:00'
page_id: '423938435'
product: rm
source: tdn-rm
title: Relatório Retrospectiva Contábil 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938435
version: 9
---

[Pré-Requisitos](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938497)

O Relatório de Retrospectiva possibilita consultar e imprimir, de forma retrospectiva, informações de lançamentos contábeis, independente do período em que as partidas tenham sido registradas, totalizando-os mensalmente e organizando-os em níveis de agrupamento que poderão representar Contas Contábeis, Contas Gerenciais  ou Centros de Custo, de acordo com os parâmetros que forem determinados, obedecendo um formato de exibição baseado em uma série de outras configurações que o usuário indicar.

**Estrutura do Relatório**

Agrupamento

Os parâmetros de agrupamento permitem que o usuário defina o Tipo de informação em cada um dos níveis. Dessa forma, as combinações resultam nos modelos de relatórios existentes na versão anterior, bem como outros que as possíveis combinações permitirem construir. Para a parametrização de um relatório Contábil | Gerencial, por exemplo, basta que no campo Tipo de informação do nível um seja escolhida a opção Conta Contábil e no campo de mesmo nome referente ao nível dois seja escolhida a opção Conta Gerencial. As combinações possíveis são:

* Contábil
* Gerencial
* Centro de Custo
* Contábil / Gerencial
* Contábil / Centro de Custo
* Gerencial / Centro de Custo
* Gerencial / Contábil
* Centro de Custo / Contábil
* Centro de Custo / Gerencial

Grau

Define o limite de níveis de grupos de totalização serão exibidos.

Exibir contas sintéticas

Se não estiver marcado, apenas as contas, ou centros de custo, analíticas, aquelas de níveis mais baixos, quais são indicados no lançamento contábil, aparecerão, omitindo os grupos de totalização.

Exibir contas sem movimento

Se estiver marcado, exibirá qualquer conta, ou centro de custo, independente que algum lançamento lhe tenha sido atribuído no período determinado pelo usuário.

Exibir somente código reduzido

Se estiver marcado, apenas exibirá os códigos reduzidos das contas.

Definir intervalo

Se estiver marcado, ao continuar o processo, é exibida uma etapa onde o usuário pode limitar a faixa de contas, ou centros de custo, que devem ser exibidas no relatório.

Totalização

Determina qual tipo de valor deve ser exibido para cada conta, ou centro de custo, referente aos meses do período determinado. São quatro opções:

* Crédito: Soma dos créditos do período determinado.
* Débito: Soma dos débitos do período determinado.
* Saldo: O saldo do mês, acumulando o saldo do mês anterior.
* Movimento: A subtração entre a soma dos créditos e a dos débitos do período determinado.

Campos

* Permite o usuário indicar a exibição ou ocultação de determinados campos não obrigatórios no relatório, sendo eles:
* Código Reduzido: O código reduzido da conta, ou centro de custo.
* Descrição: Descrição da conta, ou centro de custo.
* Total do período: Uma última coluna, que soma os valores das demais colunas mensais.

Filial

* Quebra por Filial: Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada nova filial. Neste caso, os dados de cada filial serão apresentados separadamente no relatório.
* Exibir Nome Fantasia e Exibir CNPJ: Apresenta dos dados de CNPJ/Nome Fantasia das Filiais quando existir quebra de Páginas.
* Quebrar por Grupo: se marcada, fará com que a cada código de conta, ou centro de custo, de nível mais elevado (1, 2, 3...) uma nova página seja criada.

**Dados do Relatório**

Data inicial e Data Final

Informe a faixa de datas desejada para a impressão do Retrospectiva. As datas selecionadas deverão compreender um período máximo de doze meses, e estar dentro do Período Contábil vigente ou não, basta que para uma data anterior ao período, seja marcada a opção "Buscar do Histórico contábil".

O campo data será carregado automaticamente com a última data informada no Relatório, salvo nas preferências.

Ao lado do campo data, que pode ser utilizado a opção "filtro automático de datas" que possibilita retornar os períodos fixos (Semanal, Mensal, Bimestral, Trimestral, Semestral) e aplica-lo como período do Balancete.

Buscar do Histórico Contábil

Esta opção permite a impressão do Relatório Retrospectiva baseando o resultado em datas anteriores ao período contábil. Desta forma deve ser informado uma data que seja anterior ao inicio do período contábil.

Basear na Data de Cotação

Esta opção permite a impressão dos valores baseando na data da cotação dos lançamentos. Marcando esta opção, o sistema buscará os lançamentos que possuírem a data da cotação dentro do período informado no intervalo de datas. Observação: Esta opção somente será visualizada nesta janela, se nos "Parâmetros/Lançamentos" a opção "Usa segundo valor" estiver marcada e for informada uma moeda no parâmetro "Símbolo moeda 2º valor".

Selecionar Coligada / Filial / Departamento

Esta opção permitirá selecionar Coligadas, Filiais cujos dados serão processados e consolidados no relatório. Os Departamentos somente estarão visíveis caso a base esteja parametrizada para usar departamento.

* Todas as Coligadas

Opção disponível apenas se o parâmetro 'Acessa Contas Globais' estiver marcado. Marque esta opção para impressão do relatório consolidado. Assim, seu relatório será calculado, levando em conta as contas de todas as coligadas de seu sistema. Não marcando o campo "Todas as coligadas", somente a coligada corrente ficará disponível na opção abaixo.

Obs.: Para a impressão do relatório consolidado para todas as Coligadas, todas as máscara existentes terão de ser iguais para todas as coligadas existentes no sistema.

* Ativar filtro

Neste campo é possível selecionar as coligadas/ filiais/departamentos deverão ser emitidos no relatório. Para fazer a seleção é necessário clicar no ícone do lookup (...) a frente da descrição Ativar filtro. Será aberta uma janela onde estará visível todas as Coligadas (se o campo Todas Coligadas estiver habilitado), Filiais e Departamentos (Caso o parâmetro usa departamentos esteja habilitado). A visualização é feita de acordo com a hierarquia de cada campo. Cada coligada visualizada, terá logo abaixo suas respectivas filiais que por sua vez terão seus respectivos departamentos.

Histórico Padrão

Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

Tipo de Valor / Moeda

Permite escolher o valor e/ou moeda que será utilizado para a impressão de seu relatório.

* Primeiro Valor: Imprime o relatório utilizando o valor da moeda corrente.
* Segundo Valor: Imprime o relatório utilizando o segundo valor cadastrado nos lançamentos.
* Cotação de Outra Moeda: Marcando esta opção, você poderá imprimir os relatórios utilizando uma cotação específica de uma outra moeda, além da moeda principal e da segunda moeda. Desta forma você poderá escolher no ato da impressão em qual moeda seu relatório será impresso, e qual o valor da cotação.

Observação: Você deverá informar qual a moeda desejada e qual o valor da cotação, pois o sistema utilizará uma cotação única nesta opção e todos os valores apresentados no relatório serão convertidos com base no valor informado neste campo.

Título do relatório

Neste campo poderá ser definido um novo título para o relatório, conforme desejado. Com quantidade máxima de 70 caracteres.

Utilizar Numeração Sequencial

Esta opção só ficará habilitada com o Parâmetro do sistema "Utilizar Numeração Sequencial de Páginas" marcado. Marque esta opção para que seu relatório obedeça à numeração sequencial informada nos parâmetros do TOTVS Gestão Contábil.

Este recurso auxiliará na emissão de relatórios legais com formatos diferentes em uma única sequência com finalidade de encadernação. Por exemplo, emite-se o razão da 1ª a 20ª página, logo em seguida emite-se um balancete da página 21ª a 40ª e assim sucessivamente. Desta forma a sequência de página será continua feita automaticamente.

Com esta opção marcada o campo de N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial.

Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

Descrição da Contagem de Página

Determina a descrição que será impressão na emissão do relatório para número de página. Exemplo: Folha 01 ou Pag. 01

Data de Emissão

Digite a data desejada para constar no cabeçalho do relatório como sendo a data de emissão do mesmo. Você poderá digitar simplesmente a data desejada, ou se preferir, poderá selecioná-la através do ícone que se encontra à frente deste campo. Após a seleção, confirme a data escolhida. A data default deste campo será sempre a data Atual. Dessa forma, a funcionalidade de salvar parâmetro por usuário para relatório para este campo não deve ser considerada.

Observação: Se você quiser que no cabeçalho do relatório não seja impressa a data de emissão, você deverá deixar este campo em branco.

Quantidade de página por arquivo

Esta opção foi criada para base de dados com grande volume de dados, por que existe uma limitação da quantidade de página que cada máquina consegue processar e exibir. Quando informado a quantidade de páginas por arquivo o relatório será quebrado quando a quantidade informada for atingida tornando possível o processamento e a exibição do relatório.

Margem Esquerda, Direita, Superior e Inferior

Esta opção permite que você configure as Margens Direita, Esquerda e Superior do relatório. Você poderá aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 8 para a margem Direita, entre 0 e 15 para margem Esquerda e entre 0 e 10 para margem Superior e inferior.

Orientação

Usuário escolhe gerar o relatório em orientação retrato ou paisagem. É recomendado que quando o usuário use uma quantidade maior de meses seja utilizada a orientação paisagem.

Exportar para Arquivo

Nesta opção estarão disponível vários formatos como Word (RTF), PDF, Arquivo texto (TXT), Excel, dentre outros, do qual o usuário poderá utilizar para a exportação do resultado do relatório para seu armazenamento. Após realizar todos os procedimentos e clicando em Avançar / Executar, o relatório será gerado, sendo possível salvar o relatório clicando no ícone SALVAR, ou apenas visualizar o mesmo.  
  
Nota: Para exportação de arquivo do tipo texto (TXT) o tamanho das colunas correspondente aos valores mensais comportam mais caracteres, com isso, para valores superiores a 15 caracteres utilize essa exportação.

Veja Também

* [Boletim Técnico Relatório Retrospectiva](http://tdn.totvs.com/pages/viewpage.action?pageId=185751406)
