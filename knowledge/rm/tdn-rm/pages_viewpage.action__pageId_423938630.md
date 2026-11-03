---
content_hash: 9d7f527391d9b0d1913f704f9d225ba9cf5154e42491ce3a79ae6ac225e89988
fetched_at: '2026-06-29T00:09:28.042422+00:00'
page_id: '423938630'
product: rm
source: tdn-rm
title: Relatório Balanço Patrimonial 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938630
version: 4
---

Pré-Requisitos

O balanço patrimonial é uma demonstração contábil que tem por finalidade apresentar a posição contábil, financeira e econômica de uma entidade em determinada data, representando uma posição estática (posição ou situação do patrimônio em determinada data).

Ele apresenta os ativos (bens e direitos), passivos(exigibilidades e obrigações) e o patrimônio líquido, que é resultante da diferença entre o total de ativos e o total de passivos.

Faz parte de um conjunto de relatórios que compõem as demonstrações contábeis que evidenciam, resumidamente, o patrimônio de uma entidade, quantitativa e qualitativamente. Ele possuirá uma tela de parâmetros dividida em 5 abas (Dados, Filtros, Layout, Assinaturas e Campos) que serão detalhadas a seguir.

**Aba Dados**

**Intervalo de datas** **Data inicial e Data Final:** Deverá ser informada a faixa de datas desejada para a impressão do relatório. Essas datas deverão estar dentro do período contábil vigente. Serão considerados apenas os registros que estiverem entre o período informado.

**Basear na data de cotação:** Essa opção permite a impressão dos valores baseando-se na data da cotação dos lançamentos. Marcando essa opção o sistema buscará os lançamentos que possuírem a data da cotação dentro do período informado no intervalo de datas. Vale ressaltar que essa opção só poderá ser visualizada se, nos "Parâmetros/Lançamentos", a opção "Usa segundo valor" estiver marcada e for informada uma moeda no parâmetro "Símbolo moeda 2º valor".

**Buscar do histórico Contábil:** Essa opção permite a impressão dos registros disponível no histórico contábil. Habilitando essa opção o usuário deverá informar o período em que deseja consultar o histórico contábil.

**Filtro Coligada / Filial / Departamento**

* Todas Coligadas: Opção disponível apenas se o parâmetro 'Acessa Contas Globais' estiver marcado. Marque essa opção para impressão do relatório consolidado. Assim, o relatório será calculado considerando as contas de todas as coligadas do sistema.
* Ativar Filtro: Essa opção permitirá selecionar coligadas, filiais e departamentos cujos dados serão processados e consolidados no relatório. Não marcando o campo "Todas as coligadas", somente a coligada corrente ficará disponível nessa opção.

**Imprimir / filtrar**

* Contas sem movimentação e com saldos: Quando marcada, permitirá que sejam impressas todas as Contas contábeis, que não possuam movimentação no período, mas que possuam saldo.
* Contas com movimentação e com saldos: Quando marcado esta opção, todas as contas contábeis do seu plano de contas que possuírem saldo diferente de zero e movimentação no período informado serão impressas.

**Quebrar página por filial:** Se essa opção for marcada o balanço patrimonial será impresso realizando uma quebra de página a cada nova filial. Vale ressaltar que antes de realizar a quebra serão impressos o texto de reconhecimento, o local e data e as assinaturas, porém para que essas informações sejam exibidas deverão haver uma ou mais assinaturas cadastradas.

**Localização do Símbolo da Moeda:** Essa opção permite ao usuário escolher em qual posição o símbolo da moeda será impresso. Por exemplo, se a moeda do relatório for o EURO e sua posição correta for à direita do valor, basta escolher a opção "Direita do Valor" e os valores serão impressos dessa forma: 99.999,99 EUR Vale ressaltar que as informações da moeda como o símbolo, a descrição da parte fracionário e a descrição da parte inteira serão exibidos de acordo com o cadastro de Moedas e Índices. Se o usuário optar por exibir o saldos de outra moeda serão exibidos os dados da moeda selecionada, caso contrário serão exibidos os dados da moeda padrão.

**Lote:** Opção para filtrar as movimentações feitas nos lotes informados, permitindo a conferência quando a contabilidade ainda não foi integrada ao lote zero. Serão considerados todos os registros que estiverem nos lotes informados pelo usuário, porém vale ressaltar que apenas os lotes das coligadas selecionadas, no filtro de coligada, estarão disponíveis para seleção.

Ao alterar o filtro de coligada os lotes já selecionados serão perdidos, e um aviso será exibido para que o usuário decida se prossegue ou não com a alteração do filtro. Quando a opção de histórico contábil for marcada, o filtro por lote será desabilitado e será considerado o lote 0. Além disso, os lotes selecionados serão perdidos. Um aviso será exibido para que o usuário decida se prossegue ou não com a alteração.

Se o usuário informar um lote diferente de zero, não serão exibidos os saldos anteriores de períodos já liberados de contas sem movimentação após a liberação e antes da data inicial de movimentação informada. Caso nenhum lote seja informado no filtro será considerado o lote 0.

**Aba Filtros**

**Seleção das contas de Ativo, Passivo e Patrimônio Líquido**

Estarão disponíveis para seleção todas as contas existentes no plano de contas, porém para exibir o balanço corretamente será necessário informar as contas que irão representar os grupos do Ativo, Passivo e Patrimônio líquido. Para o relatório serão considerados apenas os registros associados as contas selecionadas. Esse filtro irá trazer, por default, as contas 1 (ativo) e 2 (Passivo). Caso o usuário não informe nenhum item as contas mencionadas anteriormente serão adicionadas, automaticamente, após o usuário sair do componente.

**Histórico Padrão**

Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

**Configurar valores:** Permite definir o tipo de moeda e/ou valor que será utilizado para a impressão do relatório. Também é possível definir a impressão dos valores em milhares.

**Tipo de Valor**

* **Cotação de Outra Moeda:** Marcando essa opção é possível imprimir os relatórios utilizando uma cotação específica de outra moeda. Dessa forma será possível escolher, no ato da impressão, a moeda e o valor da cotação.
* **Primeiro Valor:** Imprime o relatório utilizando o valor da moeda corrente.
* **Segundo Valor:** Imprime o relatório utilizando o segundo valor cadastrado nos lançamentos (esta opção somente estará disponível se o parâmetro de Usa segunda moeda estiver habilitado).

**Dados (cotação de outra moeda):** Deverá ser informada a moeda desejada e o valor da cotação, pois os valores apresentados pelo relatório serão convertidos com base na cotação informada. Para habilitar esses campos é necessário marcar a opção "Cotação de outra moeda".

**Imprimir valores em milhares:** Marcando essa opção os valores apresentados pelo relatório serão impressos em milhares, ou seja, divididos por 1000. No cabeçalho do relatório será impresso o texto "Valores em milhares".

Observação: Vale lembrar que os relatórios expressos em milhares poderão apresentar algumas diferenças em seus valores se tomarmos como base os relatórios convencionais. Isto se dá pelo fato de que ao dividir os valores por 1000 será feito o arredondamento desses valores, que segue as regras de arredondamento da própria máquina.

**Não imprimir os centavos:** Opção disponível somente se a opção "Imprimir valores em milhares" estiver marcada. Marcando essa opção, somente a parte inteira dos valores expressos em milhares serão impressa. Os valores apurados para a emissão do relatório serão divididos por 1000, o resultado dessa divisão será arredondado e somente a parte inteira do resultado será impressa. Os centavos encontrados nesse resultado não serão impressos.

Valor apurado para emissão: R$ 1.583.796,00

Valor dividido por 1000 (mil): R$ 1.583,796

Valor arredondado: R$ 1.583,80

Valor impresso: R$ 1.583

Se essa opção estiver marcada e, se para alguma conta o resultado encontrado nessa divisão for menor ou igual à 0.49, essa conta será impressa no relatório, porém com o valor 0 (zero).

**Conta contábil (Ativa / Inativa):** Esse componente possuirá as opções Todas, Ativas e Inativas. Caso o usuário selecione a opção Ativas o relatório irá exibir apenas contas ativas, porém se o usuário selecionar a opção Inativas o relatório irá exibir apenas contas intivas. Marcando a opção Todas serão exibidas contas ativas e inativas. Vale ressaltar que após selecionar a opção Ativas a opção "Não exibir conta(s) inativa(s) sem movimentação e sem saldo(s)", da aba Dados, será desmarcada e desabilitada.

**Grau Contábil:** Através da caixa de seleção será possível escolher o grau de contas desejado para geração do balanço patrimonial. Exemplo: Grau TOTAL: Todas as contas serão selecionadas (da sintética 1 até a última conta analítica do plano de contas). Grau 1: Somente as contas sintéticas dos grupos serão selecionadas (1 - Ativo, 2 – Passivo, etc), conforme o plano de contas.

**Aba Layout**

**Opções de impressão** **Inserir observação abaixo do título:** Marcando essa opção será possível inserir um texto adicional no cabeçalho do relatório, logo abaixo do título, que poderá ter o tamanho de no máximo de 10 linhas. Caso o texto seja muito extenso o mesmo será truncado.

**Inserir texto adicional no final:** Caso essa opção seja marcada será permitida a digitação de um texto adicional ao final do relatório.

**Alterar título do balanço patrimonial:** Caso essa opção seja marcada poderá ser definido um novo título para o relatório com quantidade máxima de 28 caracteres.

**Exibir dados da filial no cabeçalho:** Marcando essa opção o código da filial e os códigos dos departamentos serão impressos.

**Exibir nome fantasia da filial no cabeçalho:** Marcando essa opção o nome fantasia da filial será impresso.

**Exibir CNPJ da filial no cabeçalho:** Marcando essa opção, quando o relatório for impresso para apenas uma filial, será exibido no cabeçalho do relatório o CNPJ da Filial. Essa opção só ficará visível se houver apenas uma filial selecionada.

**Usar o parâmetro de formato de impressão de saldos para débito/crédito:** Marcando essa opção os valores serão impressos respeitando o parâmetro de formato de impressão de saldos das contas.

**Não exibir sinais nos valores de débito/crédito:** Marcando essa opção os valores serão impressos sem sinal. Ao habilitar essa opção a "Impressão de saldos para débito/crédito" ficará desabilitada.

**Atributos de página:** Os atributos de página permitem ao usuário definir as configurações de página do relatório.

**Tipos de arquivo :** A exportação de arquivos permite ao usuário selecionar diversos tipos de saída do relatório. Dentre as saídas disponíveis podemos citar o CSV, o JPEG, o HTML, o XLS, o MHT, o RTF, o TXT e o PDF.

**Margem:** Essa opção permite que você configure as margens direita, esquerda, superior e inferior do relatório. Será possível aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem direita, entre 0 e 25 para margem esquerda e entre 0 e 10 para as margens superior e inferior.

**Outros** **Utilizar numeração sequencial:** Essa opção só ficará habilitada com quando o parâmetro "Utilizar Numeração Sequencial de Páginas" estiver marcado. Marque essa opção para que o relatório obedeça à numeração sequencial informada nos parâmetros do Totvs Gestão Contábil. Esse recurso auxiliará na emissão de relatórios legais com formatos diferentes em uma única sequência, com a finalidade de encadernação. Com essa opção marcada o campo N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregada a última página impressa dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**N.º página inicial:** Permite informar o número de página inicial para impressão. Com a opção "Utilizar numeração sequencial" marcada esse campo assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

**Data de emissão:** Permite informar a data desejada para constar no cabeçalho do relatório como sendo a data de emissão do mesmo. A data default desse campo será sempre a data atual, por isso a funcionalidade de salvar parâmetro por usuário não deve ser considerada para esse campo. Vale ressaltar que para que a data de emissão não seja impressa basta deixar o campo em branco.

**Descrição da contagem de página:** Determina a descrição que será impressão na emissão do relatório para número de página.

**Quantidade de páginas por arquivo:** O relatório será quebrado, em arquivos, sempre que a quantidade de páginas informadas for atingida. Por exemplo, se forem definidas 5 páginas por arquivo e o relatório possuir apenas uma página será gerado um único arquivo, porém se o relatório possuir 15 páginas o relatório será quebrado em três arquivos de cinco páginas.

**Orientação:** O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

**Aba Assinaturas**

As assinaturas serão opcionais. Caso não sejam informadas elas não sairão no balanço patrimonial.

**Assinatura do balanço patrimonial:** Para incluir as assinaturas o usuário deverá preencher os campos obrigatórios, destacados em negrito, existentes na tela de assinatura do balanço. Vale ressaltar que as assinaturas serão impressas na ordem em que foram incluídas.

**Qualificação do assinante:** O usuário deverá selecionar a qualificação da pessoa que deverá assinar o balanço. Esse campo apresentará as seguintes opções:

* Contador (Responsável pela contabilidade)
* Técnico em contabilidade (Responsável pela contabilidade)
* Titular (Responsável pela empresa)
* Outro
* Sócio-Diretor (Sócio da empresa)

**Descrição da qualificação:** Esse campo só será exibido se a qualificação "Outro" for selecionada. Nele poderá ser informado o nome do cargo como  coordenador, gerente administrativo, etc. Esse campo será alterado de acordo com a necessidade do usuário.

**Nome do signatário:** Nesse campo deverá ser informado o nome da pessoa que irá assinar o balanço patrimonial.

**Complemento:** Esse não é um campo obrigatório, porém nele o usuário poderá adicionar qualquer informação que seja relevante como, por exemplo, o CRC do contador ou o cargo de um sócio-diretor.

**Imprimir assinaturas em uma folha separada:** Ao marcar essa opção as assinaturas serão impressas em uma página separada, mesmo que na página anterior exista espaço para as elas.

**Data da assinatura:** Essa data receberá o mesmo valor da data de emissão, podendo ser alterada a critério do usuário.

**Aba Campos**

Nessa aba estarão disponíveis todos os campos que poderão ser impressos. O balanço patrimonial possuirá os campos Código da conta, Descrição e Saldo atual, que poderão ter seus nomes e tamanhos alterados. Também será possível optar por exibir ou não os campos desejados.

A variação de tamanho de impressão dos campos será alterada conforme a seleção da Orientação Paisagem ou Retrato.

**ATENÇÃO ÀS PARAMETRIZAÇÕES!!**

**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos, o relatório será gerado mas virá com configurações e dimensionamentos de páginas incorretas.**

Veja Também

* [Boletim Técnico Balanço Patrimonial](http://tdn.totvs.com/pages/viewpage.action?pageId=185755317)
