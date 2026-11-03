---
content_hash: 1463c7b57568000891449aa5627f0b4c882d1ccb0b27dfc18ece05591f3478f3
fetched_at: '2026-06-29T00:09:27.480351+00:00'
page_id: '423938523'
product: rm
source: tdn-rm
title: Razão Cliente Fornecedor/Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938523
version: 10
---

Emite as contabilizações a partir de integrações de aplicativos Nucleus e Fluxus.   
   
**DADOS**

**O Razão Cliente/Fornecedor – Contábil reflete o resumo dos valores lançados, organizados por contas contábeis e em seguida por cliente/fornecedor. Esse relatório tem o objetivo de imprimir somente contas contábeis de clientes/fornecedores, portanto,** **devem ser selecionadas as contas contábeis de clientes/fornecedores na aba Filtro.**

**Deve ser informado um intervalo de Datas** deseja para a impressão do Relatório. Esta data deverá estar dentro do Período Contábil vigente, e somente serão considerados os lançamentos escriturados neste período informado.

**Buscar do histórico contábil:**Esta opção pode ser marcada quando o período selecionado já estiver fechado. Com a mesma habilitada não há necessidade de reabri-lo.

**Basear na data de cotação:**Esta opção permite a impressão dos valores baseado na data da cotação dos lançamentos. Marcando a mesma, o sistema buscará os lançamentos que possuírem a data de cotação dentro do período informado no intervalo de Datas (Esta informação será buscada do campo DATA2 da tabela CPARTIDA).

***Atenção!!***

Esta opção somente será visualizada nesta janela, se nos "Parâmetros | Lançamentos" a opção "Usa segundo valor" estiver marcada e for informada uma moeda no parâmetro "Símbolo moeda 2º valor".

Selecione o tipo de Razão: Neste "checkbox" deve ser definido o tipo de relatório, neste caso, Razão cliente fornecedor /Contábil.

**Lote Contábil:**Poderá ser informado tanto o Lote Zero, quanto demais lotes para a apresentação dos lançamentos desejados.  Observação: Quando marcado a opção de Histórico contábil não estará disponível para ser informado, pois entende-se que todos os registros do histórico contábil são lote zero.

Se informou lote diferente do Lote Zero, não serão exibidos os saldos anteriores de períodos já liberados de contas sem movimentação e antes da data inicial de movimentação informada.

****OPÇÕES****

* **Contas com movimentação e sem rateios:**Quando marcado esta opção, as Contas Contábeis que possuírem movimentação no período mas não possuam rateio gerencial serão impressas.
* **Contas com movimentação e sem saldos:**Quando marcado esta opção, as Contas Contábeis que possuírem movimentação no período e que possuam saldo inicial zerado serão impressas.
* **Contas com movimentação e com saldos:** Quando marcado esta opção, todas as contas Contábeis do seu plano de contas que possuírem saldo diferente de zero e movimentação no período informado serão impressas.
* **Não exibir lançamentos de Estorno/Estornado:**Quando marcada esta opção os lançamentos de estorno/estornado deixarão de ser exibidos pelo relatório.

**Totalizar**

* **Total Geral:** Emite ao final da impressão o total de Débitos, Créditos e Saldo Anterior.
* **Total por Dia:** Emite ao termino dos lançamentos de um dia a totalização de lançamentos do mesmo. Quando habilitado desabilita a opção Total por Mês.
* **Total por Mês:** Emite ao termino dos lançamentos de um mês a totalização de lançamentos do mesmo. Quando habilitado desabilita a opção Total por Dia.
* **Total por Cliente/Fornecedor:** Ao marcar esta opção será apresentada uma totalização por cliente/fornecedor dos valores apurados para cada cliente/fornecedor. Disponível apenas para o relatório razão contábil cliente/fornecedor.

**Selecionar Coligada/Filial/Departamento:**Esta opção permitirá selecionar Coligadas, Filiais e Departamentos cujos dados serão processados e consolidados no relatório. Não marcando o campo "Todas as coligadas", somente a coligada corrente ficará disponível nesta opção.

Observação: Selecionando a opção "Todas Coligadas" o tipo de valor "Cotação de Outra Moeda", existente na aba Filtros, ficará desabilitado, pois o relatório razão não realiza consolidação multimoeda.

**Quebrar página Por Filial:**Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada nova filial. Neste caso, os dados de cada filial serão apresentados separadamente no relatório.

**Quebrar página Por Cliente/Fornecedor:** Ao habilitar esta opção, o relatório será impresso realizando uma quebra a cada novo Cliente/Fornecedor. Neste caso, os dados de cada Cliente/Fornecedor serão apresentados separadamente no relatório. Disponível somente para o relatório razão contábil cliente/fornecedor.  
   
**FILTROS**

**Conta Contábil:** Ao selecionar esta opção será possível configurar uma faixa de Contas Contábeis. Sendo assim, será apresentada uma nova aba de etapa obrigatória de preenchimento, para que seja informada uma, várias, ou até mesmo um intervalo de contas. O relatório será emitido exclusivamente para os lançamentos que possuírem as contas determinadas.

**Cliente/Fornecedor:**Ao selecionar esta opção será possível configurar uma faixa de Cli/For. Sendo assim, será apresentada uma nova aba de etapa obrigatória de preenchimento, para que seja informada uma, várias, ou até mesmo um intervalo de Cli/For. O relatório será emitido exclusivamente para os lançamentos que possuírem os Cli/For determinados.

**Centro de Custo:**Ao selecionar esta opção será possível configurar uma faixa de Centros de Custo. Sendo assim, será apresentada uma nova aba de etapa obrigatória de preenchimento, para que seja informada um, vários, ou até mesmo um intervalo de centros de custo.

**Observação:**Caso seja habilitada a opção de filtrar centros de custo Ativo/Inativo, a seleção da faixa de Centros de Custo irá considerada esta informação. O relatório será emitido exclusivamente para os lançamentos que possuírem os centros de custo determinados.

**Histórico:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

**P****articipante:** Ao selecionar esta opção será possível configurar uma faixa de Participantes. Sendo assim, será apresentada uma nova aba de etapa obrigatória de preenchimento, para que seja informada um, vários, ou até mesmo um intervalo de Participantes. Para o relatório serão considerados apenas os registros que cujos participantes estiverem na seleção de contas definida pelo usuário.

**Tipo de valor / moeda:**Ao selecionar esta opção será apresentada uma nova aba de etapa obrigatória de preenchimento, para que seja informada o tipo de valor desejado. Na aba Informações de valores e moedas que será apresentada, haverá as seguintes opções:

**Tipo de valor:**

* Primeiro Valor: Imprime o relatório utilizando o valor da moeda corrente.
* Segundo Valor: Imprime o relatório utilizando o segundo valor cadastrado nos lançamentos.
* Cotação de Outra Moeda: Essa opção ficará desabilitada para o relatório Razão Cliente/Fornecedor, pois ele não trabalha com multimoeda.
* Dados (cotação de outra moeda): Essa opção ficará desabilitada para o relatório Razão Cliente/Fornecedor, pois ele não trabalha com multimoeda.

**Imprimir valores em milhares:** Marcando esta opção, quando o relatório for impresso, os valores dos lançamentos serão impressos em milhares, ou seja, divididos por 1000, e no cabeçalho do relatório será impresso o texto "Valores em milhares" para que o usuário identifique que, neste relatório, seus valores estarão impressos divididos por 1000. Lembre-se: os relatórios expressos em milhares (dividido por 1000) poderão apresentar algumas diferenças em seus valores se tomarmos como base os relatórios convencionais. Isto se dá pelo fato de que ao dividir os valores por 1000 será feito o arredondamento destes valores, que segue as regras de arredondamento da própria máquina. Então, uma conta que apresente o seu saldo final zerado (total de débitos - total de créditos = 0) poderá apresentar saldo final diferente de zero nos relatórios expressos em milhares devido ao fato do arredondamento dos valores.

**Não Imprimir os Centavos:** Opção disponível somente se a opção "Imprimir valores em milhares" estiver marcada. Marcando esta opção, somente a parte inteira dos valores expressos em milhares será impressa. Os valores apurados para a emissão do relatório serão divididos por 1000 (mil), o resultado desta divisão será arredondado e somente a parte inteira deste resultado, depois que foi arredondado, será impressa. Os centavos encontrados neste resultado não serão impressos. Valor apurado para emissão: R$ 1.583.796,00 Valor dividido por 1000 (mil): R$ 1.583,796 Valor arredondado: R$ 1.583,80 Valor impresso: R$ 1.593 Se esta opção estiver marcada e, se para alguma conta o resultado encontrado nesta divisão for menor ou igual à 0,49, esta conta será impressa no relatório porém com o valor 0 (zero).  
**Centro de Custo(Ativo/Inativo):**Determina se utiliza apenas os centros de custo ativos, inativos ou todos. Serão considerados apenas os lançamentos compatíveis com este filtro.  
**Conta Contábil(Ativa/Inativa):**Determina se utiliza apenas as contas contábeis ativas, inativas ou todas. Serão considerados apenas os lançamentos compatíveis com este filtro.

**LAYOUT**

**Atributo de página para o Livro Razão** Permite definir configurações de impressão de página do relatório. Será aberta a aba Configuração do Livro Razão, com as opções:

**Impressão em formato livro:**Habilitará a alteração dos campos Número do Razão, onde poderá ser informado manualmente o número do Livro a ser impresso, e Número Máximo de Páginas, que determinará quantas páginas o livro terá, sendo que quando a impressão atingir a quantidade informada, será automaticamente criado um novo livro e a numeração atualizada.

**Não reiniciar a contagem de páginas a cada mudança de livro:** Com esta opção marcada, ao iniciar um novo Livro, a sequência de páginas permanecerá conforme a quantidade já emitida anteriormente e não será reiniciada.

**Reservar a última página do livro para o termo de fechamento:** Determina que na contagem saltará a última página da impressão para que possa ser emitido o Termo de fechamento.

**Definir reinicio da numeração da página do Razão:** Habilitará um campo para informar a partir de qual página ele deverá reiniciar a contagem de páginas, sem que este fato influencie na impressão da quantidade de livros.

**Usar os parâmetros de formato de impressão de saldos para Débitos/Créditos:** Marcando esta opção os valores de débito, crédito e movimento serão impressos respeitando o parâmetro de formato de impressão de saldos das contas. Verifique os parâmetros de impressão de Saldo.

**Não exibir sinais nos valores de débito/crédito:** Marcando esta opção os valores das colunas de débitos e créditos serão impressos sem sinal. Observação: Ao habilitar esta opção, a de "Impressão de débitos e créditos respeita o parâmetro de formato de impressão de Saldos fica desabilitada".

**Alterar título:**Permite definir um novo título para o relatório, conforme desejado (máximo de 28 caracteres).

**Inserir texto adicional no final:**Permite a digitação de texto adicional ao final do relatório. Será habilitado o botão que quando clicado será apresentada uma tela onde o usuário possa informar o texto desejado.

**Inserir observação abaixo do título:**Permitirá inserir um texto adicional que sairá impresso no cabeçalho do relatório, abaixo do título, e poderá ter o tamanho de no máximo 10 linhas. Será habilitado um botão que ao clicar será apresentada uma tela onde o usuário possa informar o texto desejado. Caso o texto seja muito extenso o mesmo será truncado.

**Transporte de Saldo:** Ao marcar esta opção, os saldos das contas serão transportados de uma página para outra do relatório quando ultrapassarem a página (disponível apenas para o Razão analítico).

**Mostrar o saldo apenas no último lançamento do dia:**Ao marcar esta opção os valores da coluna de Saldo Acumulado do Razão serão impressos no último lançamento de cada dia.

**Mostrar o saldo apenas no último lançamento do mês:**Ao marcar esta opção os valores da coluna de Saldo Acumulado do Razão serão impressos no último lançamento de cada mês.

**Imprimir em ordem alfabética das descrições das contas:** Ao marcar esta opção, o relatório irá ser exibido com as contas organizadas em ordem alfabética. Caso o relatório seja emitido com quebra, será organizado em ordem alfabética dentro de cada quebra.

**Saltar pág. entre contas contábeis:**Ao marcar esta opção a cada conta contábil será saltada a página.

**Definir Atributos de Página:** Determina a forma para a impressão do relatório.

**Data de emissão:** Esta opção determina a data desejada para constar no cabeçalho do relatório como sendo a Data de Emissão do mesmo.  Observação: Por default essa impressão será sempre a data do dia, mas a mesma poderá ser manualmente alterada para a data desejada.

**Quantidade de página por arquivo:**A fim de atender bases de dados com grande volume, poderá ser determinada uma limitação da quantidade de páginas que cada máquina consegue processar e exibir. Ao definir a quantidade de páginas por arquivo, o relatório será quebrado conforme a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório. Ao final do processamento será exibida uma tela com as quebras de páginas que foram geradas na emissão do relatório para conferência.

**Margem**

**Esquerda, Direita, Superior e Inferior:**Permite a configuração das margens Direita, Esquerda, Superior e Inferior do relatório. Podendo aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem Direita, entre 0 e 25 para margem Esquerda e entre 0 e 10 para margem Superior e Inferior.

**Definir reinicio da renumeração de página:**Digite o número de página inicial para impressão. Com a opção utilizar Numeração Sequencial de páginas marcada, este campo assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

**Atributos de páginas**

**Tipo de Arquivo:**É possível gerar o relatório nos formatos CSV, JPEG, HTML, XLS, MHT, RTF, TXT e PDF. A impressão pode ser apenas visualizada ou Salva em algum **Diretório de Destino** conforme informado. 

**Orientação:** O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

**CAMPOS**

Nesta pasta estão todos os campos existentes e que poderão ser ou não impressos, podendo também modificar os tamanhos de impressão de campo, sempre respeitando o Limite pré-estabelecido do relatório.

A variação de tamanho de impressão dos campos será alterada conforme a seleção da Orientação Paisagem ou Retrato.

Para modificar os campos, basta habilitar os campos que você escolher. Campos: Data, Partida, C.Custo, C.C.Red, Desc. C. Custo, Complemento, Doc., Ref., Filial, Depto, Cod. C. Part., Desc. C. Partida, Lote, Débitos, Créditos e Saldo Atual, Origem da Operação e  Ref. da Origem.

**OBS:** Os campos Origem da Operação e Ref. da Origem estarão disponíveis somente no relatório Razão Contábil Cliente/Fornecedor.

Origem da Operação: será impresso o valor do campo Origem da tabela COPERACAO. Exemplo: FLAN, FLANBAIXA, TMOV, XVENDA, etc.

Ref. da Origem: será impresso a referência do processo que gerou o lançamento contábil. Será feito o rastreamento somente das tabelas FLAN, FLANBAIXA, TMOV e XVENDA para buscar a referência.

Exemplo: se a origem foi FLAN será impresso no campo ref. da origem a referência do lançamento financeiro que gerou a contabilidade.

**Ajustar tamanho automaticamente:** Caso esta opção esteja marcada, o tamanho dos campos, que representam valor financeiro, serão ajustados automaticamente. Após o ajuste, caso o número de caracteres extrapole o limite de caracteres da linha, o tamanho do campo "Complemento" diminuirá para, no mínimo, 15 caracteres. Caso essa condição não seja atendida as colunas não terão seu tamanho alterado.

Importante: Esta opção não está disponível para o Razão contábil sintético.  
   
**ATENÇÃOS ÀS PARAMETRIZAÇÕES!!**  
**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos, o relatório será gerado mas virá com configurações incorretas.**

Veja Também

* [Boletim Técnico Relatório Razão Cliente/Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=185759743)
Mais Informações

* Razão Sintético;
* [Razão Analítico](http://tdn.totvs.com/pages/viewpage.action?pageId=423938450); (oficial para legislação)
* Razão Gerencial / Contábil;
* Razão Contábil / Gerencial;
* Razão Centro de Custo / Contábil;
* [Boletim Técnico Relatório Razão Cliente/Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=185759743)
