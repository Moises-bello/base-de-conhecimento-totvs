---
content_hash: 551c57d83dfde8973e70a36a6d62939ad5a647a8a972575cdb8cc8479ce89447
fetched_at: '2026-06-29T00:09:28.490418+00:00'
page_id: '423938690'
product: rm
source: tdn-rm
title: Relatório Consistência de Saldos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938690
version: 5
---

O relatório Consistência de Saldos está disponível em Relatório | Consistência de Saldos, e tem a finalidade de demonstrar as possíveis inconsistências de saldos. Apresentando as coisas que possuírem saldo divergente de sua natureza.

Ao emitir o relatório as informações escolhidas serão gravadas pelo sistema. Assim ao entrar novamente no relatório você visualizará as últimas opções escolhidas.

Para a geração dos relatórios é necessário que a impressora padrão configurada na máquina esteja com o formato de Papel A4, Carta, ou com tamanho superior a Carta.

**Dados do relatório**

**Data Inicial e Data Final:** Defina nestes campos a faixa inicial e final de datas limitadoras, para processamento e cálculo dos lançamentos.

**Filtro Automático de Datas:** Ferramenta que simplifica a parametrização das datas, onde é escolhido um ano e um tipo de filtro, que pode ser: Semanal, Mensal, Bimestral, Trimestral, Semestral e Anual, e após selecionar as opções o intervalo de datas é exibido e se confirmado, os valores são inseridos nos campos "Data Inicial" e "Data Final".

**Buscar do histórico contábil:** Ao marcar esta opção, os valores apresentados serão somente os presentes no histórico contábil, ou seja, aqueles que pertencem a um período já encerrado.

**Selecionar Coligada / Filial / Departamento:**  Por padrão, o Relatório Diário é gerado contendo os dados da coligada selecionada e de suas filiais, mas através dessa opção é possível também selecionar todas as coligadas marcando o item "Todas as coligadas", da mesma forma que é possível realizar um filtro mais específico de coligadas, filiais e departamentos através do item "Ativar filtro".

**Campos:** Nesta parte são selecionados os campos que irão aparecer no relatório. As opções são: "Código" (da conta contábil), "Código Reduzido" e "Nome Fantasia (Filial) ". Ao menos uma opção deve ser escolhida entre "Código" e "Código Reduzido" para que o relatório possa ser gerado. A opção "Nome Fantasia (Filial) " só pode ser selecionada caso um filtro por filial esteja marcado.

**Filtro por Conta Contábil:** Uma tela com as opções do filtro será aberta posteriormente no processo de geração do relatório, onde será possível filtrar pelas contas contábeis ou intervalos de contas contábeis.

**Filtro por Centro de Custo:** Uma tela com as opções do filtro será aberta posteriormente no processo de geração do relatório, onde será possível filtrar pelos centros de custos ou intervalos de centro de custo inseridos.

**Exibir dados dos centros de custos no cabeçalho:**Marcando esta opção, o sistema exibirá o código do centro de custo no cabeçalho do relatório. Ela será habilitada quando um ou mais centros de custos forem inseridos na aba Filtro | Centro de custo. Caso contrário, ficará desabilitada. O sistema exibirá apenas os centros de custos que couberem na linha.

**Filtro por Histórico Padrão:** Uma tela com as opções do filtro será aberta posteriormente no processo de geração do relatório, onde será possível filtrar pelos históricos contábeis selecionados. Para este relatório, todos os históricos informados serão DESCONSIDERADOS, não há opção de CONSIDERAR históricos selecionados.

**Definir / Configurar | Tipo de valor / moeda:** Ao selecionar essa opção, em uma tela posterior serão exibidas as parametrizações relacionadas ao tipo de valor e moeda, onde será possível escolher entre a primeira moeda, segunda moeda ou ainda informar uma moeda e valor de cotação. Também nessa parte é possível parametrizar o relatório de forma a mostrar os valores em milhares, com ou sem centavos.

**Parametrizações**

**ATENÇÃO ÀS PARAMETRIZAÇÕES!!**

**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos, o relatório será gerado mas virá com configurações e dimensionamentos de páginas incorretas.**

**Margem Esquerda, Direita, Superior e Inferior:**Permite a configuração das Margens Direita, Esquerda, Superior e Inferior do relatório. Podendo aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 8 para a margem Direita, entre 0 e 15 para margem Esquerda e entre 0 e 10 para margem Superior e Inferior.

**Definir Atributos de Página** Determina a forma para a impressão do relatório.

**Utilizar Numeração Sequencial:** Com esta opção marcada, o campo de N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Descrição da Contagem de Página:** Determina a descrição que será impressão na emissão do relatório para número de página. Exemplo: Folha 01 ou Pág. 01

**Data de emissão:** Esta opção determina a data desejada para constar no cabeçalho do relatório como sendo a Data de Emissão do mesmo. Observação: Se você quiser que no cabeçalho do relatório não seja impressa a data de emissão, você deverá deixar este campo em branco.

**Quantidade de página por arquivo:** A fim de atender bases de dados com grande volume, poderá ser determinada uma limitação da quantidade de páginas que cada máquina consegue processar e exibir. Ao definir a quantidade de páginas por arquivo, o relatório será quebrado conforme a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório. Ao final do processamento será exibida uma tela com as quebras de páginas que foram geradas na emissão do relatório para conferência.

**N.º Página Inicial:** Digite o número de página inicial para impressão. Com a opção utilizar Numeração Sequencial de páginas marcada, este campo assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

Veja Também

* [Boletim Técnico Relatório Consistência de Saldos](http://tdn.totvs.com/pages/releaseview.action?pageId=185751395)
