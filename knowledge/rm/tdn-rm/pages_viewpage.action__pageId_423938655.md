---
content_hash: 8501c05b53274f238c5b744268e1a3b5c906aecc2f2ca15774f5dbc108ff7cc1
fetched_at: '2026-06-29T00:09:28.086493+00:00'
page_id: '423938655'
product: rm
source: tdn-rm
title: Relatório Acompanhamento Orçamentário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938655
version: 3
---

O Relatório acompanhamento orçamentário permite a visualização dos valores orçados e movimentados, das contas com distribuição gerencial, com totalização pelas contas contábeis selecionadas.   
   
**Aba 'Dados'**

**Data Inicial/Data Final:** Deve ser informado um intervalo de datas desejada para a impressão do Relatório. Estas datas deverão estar dentro do período contábil vigente.

**Acumulado a partir de:** Data a partir da qual os valores orçados e movimentação serão acumulados. Sistema exibirá no relatório a colunas "Orçado Acumulado" e "Movimento Acumulado" com esses dados.  
Ela poderá ser diferente da data informada nos campos data inicial e final, mas deve estar obrigatoriamente inserida no período informado

**Lote Contábil:** Permite filtrar um ou mais Lotes, sendo Zero ou Lote N.

Serão considerados todos os registros que estiverem nos lotes informados pelo usuário.

Apenas os lotes das coligadas selecionadas no filtro de coligada estarão disponíveis para seleção.

**Selecionar Filial/Coligada/Departamento:** Esta opção permitirá selecionar Coligadas, Filiais cujos dados serão processados e consolidados no relatório. Os Departamentos somente estarão visíveis caso a base esteja parametrizada para usar departamento.

Observação:

Quando o orçamento/lançamento não possuir departamento, deverá ser marcada a opção "Incluir departamentos Nulos no Filtro"

**Quebrar página:**

Quebra por Filial: Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada nova filial. Neste caso, os dados de cada filial serão apresentados separadamente no relatório.  
Quebra por grupo contábil:  Ao marcar esta opção será realizada uma quebra de página a cada novo grupo contábil orçado.

**Layout:**

Incluir contas sem movimentação

Marcando essa opção, o sistema irá apresentar no relatório as contas gerenciais que não tiveram movimentação no período, mas que possuam saldo anterior. Também serão apresentadas as contas contábeis associadas as contas gerenciais existentes no rateio do plano de contas.

Exibir dados dos centros de custos no cabeçalho:

Marcando esta opção, o sistema exibirá o código do centro de custo no cabeçalho do relatório.

Essa opção será habilitada quando um ou mais centros de custos forem inseridos na aba Filtro| Centro de custo. Caso contrário, ficará desabilitada.

O sistema exibirá apenas os centros de custos que couberem na linha

Exibir dados da filial no cabeçalho

Marcando essa opção, o sistema irá imprimir os dados da filial no cabeçalho do relatório.

Exibir nome fantasia da filial no cabeçalho

Marcando essa opção, será exibido o nome fantasia da filial no cabeçalho do relatório, essa opção só estará visível caso não seja utilizado o filtro 'Toda as coligadas'.

Exibir CNPJ da filial no cabeçalho

Marcando essa opção, será apresentado no relatório o CNPJ da filial no cabeçalho.

Inserir observação abaixo do título

Permite inserir um texto adicional que sairá impresso no cabeçalho do relatório logo abaixo do título.

Inserir texto adicional no final

Permite a digitação de texto adicional ao final do relatório.

Alterar título

Marcando essa opção o usuário poderá definir um novo título para o relatório.

**Atributos de página:** Os atributos de página permitem ao usuário definir as configurações de página do relatório.

**Tipos de arquivo:** A exportação de arquivos permite ao usuário selecionar diversos tipos de saída do relatório. Dentre as saídas disponíveis podemos citar o CSV, o JPEG, o HTML, o XLS, o MHT, o RTF, o TXT e o PDF.

**Margem:** Essa opção permite que você configure as margens direita, esquerda, superior e inferior do relatório. Será possível aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem direita, entre 0 e 25 para margem esquerda e entre 0 e 10 para as margens superior e inferior.

**Aba 'Filtros'**

**Conta Contábil:** Permite emitir o relatório filtrando por uma ou mais contas contábeis e/ou faixa de contas utilizadas no orçamento e na movimentação. Essa informação é obrigatória para emissão.

**Conta Gerencial:** Permite emitir o relatório filtrando por uma ou mais contas gerenciais e/ou faixa de contas utilizadas no orçamento e na movimentação.

**Centro de Custo:** Permite emitir o relatório filtrando por uma ou mais centro de custos e/ou faixa de centro e custo utilizados no orçamento e na movimentação.

**Histórico:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

**Campos**

Nesta aba estão todos os campos existentes e que poderão ser ou não considerados no relatório, basta que seja selecionado o campo desejado, o mesmo esteja como ícone "Imprimir" habilitado, pois caso contrário o mesmo não será impresso. Nesta aba é possível também alterar o tamanhão dos campos desde que o total de caracteres não seja ultrapassado.

A variação de tamanho de impressão dos campos será alterada conforme a seleção da orientação paisagem ou retrato.
