---
content_hash: b09334789a8860aba89b40d2851f2bbde16db863e9ca1507c3a6db8cb3b508b3
fetched_at: '2026-06-29T00:09:27.165349+00:00'
page_id: '423938447'
product: rm
source: tdn-rm
title: Relatório Listagem de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938447
version: 2
---

A partir do relatório listagem de lançamentos é possível verificar lançamentos e rateios distribuídos entre suas contas, conforme parametrização.

**Dados:**

**Data inicial/Data final:** Nestes campos, o usuário deverá informar o período desejado para a impressão do Relatório.

Estas datas deverão constar dentro do período contábil vigente. Exceto quando a opção "Buscar do histórico contábil" estiver marcada.

**Buscar do histórico contábil:** Com essa opção marcada o relatório irá buscar os lançamentos disponíveis no histórico contábil. Portanto, nesses casos deverá ser informada uma data inicial e final compreendida em exercícios já fechados. Assim, os lançamentos serão buscados na tabela de histórico.

**Tipo de listagem**

Listagem de lançamentos

O sistema exibirá os lançamentos de acordo com os parâmetros informados.

Listagem de lançamentos e rateio

O sistema exibirá os lançamentos e, logo abaixo, os rateios distribuídos entre suas contas.

Mesmo que o rateio esteja inconsistente ele será impresso, com um destaque "Rateio inconsistente", informando que há divergência entre o valor rateado e o valor total do lançamento.

Observação:

Selecionando o tipo de listagem de lançamentos e rateios, o sistema irá habilitar a aba "campos rateio".

**Referência inicial e final**

O usuário poderá emitir o relatório filtrando por faixa de referência.

**Documento inicial e final**

O usuário poderá emitir o relatório filtrando por uma faixa de documento.

**Selecionar Coligada/Filial**

Ativando este filtro é possível selecionar as filiais e departamentos cujos dados serão processados e consolidados no relatório.

**Imprimir valores em milhares**

Com essa opção marcada os valores dos lançamentos serão impressos em milhares (divididos por 1000) e no cabeçalho do relatório é apresentada a informação "Valores em milhares".

**Ordenar emissão por**

O usuário poderá definir se os dados apresentados no relatório serão ordenados por data, id. Lançamento ou Id. Partida.

**Imprimir valores em milhares**

Quando essa opção for marcada, o relatório irá apresentar o texto "valores em milhares" no cabeçalho e os valores dos lançamentos serão impressões em milhares (divididos por 1000).

**Exibir dados da filial no cabeçalho**

Essa opção só será apresentada quando for ativado o filtro por filial. Com essa opção marcada, os dados da filial serão apresentados no cabeçalho do relatório.

**Lote**

O sistema permite que sejam informados lotes contábeis dos lançamentos que serão apresentados no relatório.

Observações:

Se nenhum lote for informado serão exibidos apenas lançamentos do lote zero.

Se a opção de histórico contábil for marcada o filtro por lote é desabilitado.

**Lote de origem**

A listagem também poderá ser exibida filtrando por lote de origem. Caso não seja selecionado nenhum lote de origem o sistema irá considerar nenhuma informação nesse filtro.  
   
**Filtros:**

**Conta Contábil**

É possível emitir o relatório filtrando lançamentos de uma ou mais contas. Não se trata de uma informação obrigatória.

**Histórico Padrão**

Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

**Atributos de Página:**

**Orientação**

O formato das páginas do relatórios poderão ser definidas por paisagem ou retrato.

**Tipo de Arquivo**

O tipo de arquivo do relatório, permite ao usuário selecionar diversos tipos de saída. Dentre as saídas, estão disponíveis o CSV, o JPEG, o HTML, o XLS, o MHT, o RTF, o TXT e o PDF.

**Margem em milímetros**

Esta opção permite configurar as margens direita, esquerda, superior e inferior do relatório. Elas poderão aumentar ou diminuir utilizando espaçamentos entre 0 e 10 para as margens direita, superior e inferior e entre 0 e 25 para a margem esquerda.

**N.º página inicial**

Número de página inicial para impressão. Com a opção "Utilizar numeração sequencial de páginas" marcada, esse campo irá assumir o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

**Utilizar numeração sequencial**

Essa opção só ficará habilitada com o parâmetro "Utilizar numeração sequencial de páginas" marcado. Ele deverá ser marcado para que o relatório obedeça à numeração sequencial informada nos parâmetros do Totvs Gestão Contábil. Com essa opção marcada, o campo "N.º página inicial "irá assumir o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

Automaticamente será carregado a última página impressa para dentro do campo "Nº página inicial".

**Descrição da contagem de página**

Determina a descrição que será impressão na emissão do relatório para número de página. Exemplo: Folha 01, Pág. 01.

**Data de emissão**

Essa data constará no cabeçalho do relatório como sendo a data de emissão do mesmo.

**Quantidade de páginas por arquivo**

Essa opção é necessária para base de dados com grande volume de informações, visto que, existe uma limitação da quantidade de páginas que cada máquina consegue processar e exibir.

Quando informada a quantidade de páginas por arquivo o relatório será quebrado assim que a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório.  
   
**Campos**

Nessa guia será possível configurar quais campos deverão ser impressos e o tamanho de cada um deles. Os seguintes campos estão disponíveis:

* Referência
* Documento
* Data
* Débito
* Crédito
* Partida
* Filial
* Centro de Custo
* Reduzido C. Custo
* Lote Origem
* Lote Atual
* Departamento
* Valor
* Histórico
* Complemento
* Conta Gerencial
* Reduzido Gerencial
* Descrição Gerencial
* Lançamento Gerencial

Campos Rateio

Essa aba será apresentada somente quando a opção "Listagem de lançamentos e rateio" disponível na aba dados, for selecionada.

* Conta Gerencial
* Reduzido Gerencial
* Descrição Gerencial
* Valor Gerencial
