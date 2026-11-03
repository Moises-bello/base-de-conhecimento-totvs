---
content_hash: 483118cb733f410c87f7bef4ae7323d27bea109ca6994da8d9aa178695dbff6c
fetched_at: '2026-06-29T00:09:27.540048+00:00'
page_id: '423938538'
product: rm
source: tdn-rm
title: Aba Layout - Balancete
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Layout+-+Balancete
version: 18
---

**ATENÇÃOS ÀS PARAMETRIZAÇÕES!**

**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos, o relatório será gerado mas virá com configurações incorretas.**

**Descrições das contas com tabulação:** Válido para todos os tipos de balancete. Marcando esta opção, a descrição das contas será impressa respeitando uma tabulação por nível de conta.

Observação: Será descontado da descrição o espaço de tabulação.

Ordem alfabética nas contas analíticas / centro de custo: Quando gerado o Balancete que utilizam contas gerenciais ou centro de custa a ordenação alfabética também servirão para contas gerenciais e centros de custo.

**Usar o parâmetro de formato de impressão de saldos para Débito/Crédito:** Válido para todos os tipos de balancete. Marcando esta opção os valores de débito, crédito e movimento serão impressos respeitando o parâmetro de formato de impressão de saldos das contas. Observação: Ao habilitar esta opção, a opção de "não exibir sinais nos valores de débito/ crédito" fica desabilitada.

**Não exibir sinais nos valores de débito/crédito:** Válido para todos os tipos de balancete, ao marcar esta opção os valores das colunas de débitos e créditos serão impressos sem sinal. Observação: Ao habilitar esta opção, a de "Impressão de débitos e créditos respeita o parâmetro de formato de impressão de Saldos" fica desabilitada.

**Alterar título do balancete:** Válido para todos os tipos de balancete. Caso esta opção seja habilitada, poderá ser definido um novo título para o relatório, conforme desejado. Com quantidade máxima de 28 caracteres.

**Inserir texto adicional no final:** Válido para todos os tipos de balancete. Caso habilite esta opção, será permitida a digitação de texto adicional ao final do relatório.

**Inserir observação abaixo do título**: Válido para todos os tipos de balancete. Marcando esta opção, você poderá inserir um texto adicional que sairá impresso no cabeçalho do relatório logo abaixo do título e que poderá ter o tamanho de no Máximo 10 linhas. Caso o texto seja muito extenso o mesmo será truncado.

**Exibir dados dos centros de custos no cabeçalho:**

Marcando esta opção, o sistema exibirá o código do centro de custo no cabeçalho do relatório.

Essa opção será habilitada quando um ou mais centros de custos forem inseridos na aba Filtro| Centro de custo. Caso contrário, ficará desabilitada.

O sistema exibirá apenas os centros de custos que couberem na linha.

**Exibir nome fantasia da filial no cabeçalho:** Marcando esta opção, quando o relatório for impresso será apresentado o nome-fantasia das filiais, caso tenham sido cadastrados. Observação: Este campo somente estará ativos se for selecionada apenas uma filial.

**Exibir CNPJ da Filial no cabeçalho:** Marcando esta opção, quando o relatório for impresso para apenas uma filial, será exibido no cabeçalho do relatório o CNPJ da coligada corrente e da Filial. Quando você não marcar esta opção, ou o relatório for impresso para mais de uma filial, será exibido apenas o CNPJ da coligada corrente.

**Utilizar Numeração Sequencial:** Esta opção só ficará habilitada com o Parâmetro "Utilizar Numeração Sequencial de Páginas" marcado. Marque esta opção para que seu relatório obedeça à numeração sequencial informada nos parâmetros do TOTVS Gestão Contábil.

Este recurso auxiliará na emissão de relatórios legais com formatos diferentes em uma única sequência com finalidade de encadernação. Por exemplo, emite-se o Razão da 1ª a 20ª página, logo em seguida emite-se um balancete da página 21ª a 40ª e assim sucessivamente. Desta forma a sequência de página será continua feita automaticamente.

Com esta opção marcada, o campo de **N.º Página Inicial** assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Data de Emissão:** Digite a data desejada para constar no cabeçalho do relatório como sendo a data de emissão do mesmo. Você poderá digitar simplesmente a data desejada, ou se preferir, poderá selecioná-la através do ícone que se encontra à frente deste campo. Após a seleção, confirme a data escolhida. A data default deste campo será sempre a data Atual. Dessa forma, a funcionalidade de salvar parâmetro por usuário para relatório para este campo não deve ser considerada. Observação: Se você quiser que no cabeçalho do relatório não seja impressa a data de emissão, você deverá deixar este campo em branco.

**Quantidade de página por arquivo:** Esta opção foi criada para base de dados com grande volume de dados, por que existe uma limitação da quantidade de página que cada máquina consegue processar e exibir. Quando informado a quantidade de páginas por arquivo o relatório será quebrado quando a quantidade informada for atingida tornando possível o processamento e a exibição do relatório.

**Margem Esquerda, Direita, Superior e Inferior:** Esta opção permite que você configure as Margens Direita, Esquerda e Superior do relatório. Você poderá aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem Direita, entre 0 e 25 para margem Esquerda e entre 0 e 10 para margem Superior e inferior.

**Orientação:**O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

**Exportar para Arquivo:** Nesta opção estarão disponíveis vários formatos como Word (RTF), PDF, Arquivo texto (TXT), Excel, dentre outros, do qual o usuário poderá utilizar para a exportação do resultado do relatório para seu armazenamento.

**Observação:** Para facilitar a utilização das fórmulas, ao exportar o relatório para arquivos em formato Excel (Microsoft Excel .XLSX), o sistema irá exportar de forma fixa os valores devedores positivos e os valores credores negativos.

Atenção

Quando estiver gerando o Balancete Contábil ou o Balancete Gerencial, se optar pela exportação em Excel ou CSV algumas parametrizações que refletem na exibição do relatório ou na totalização das informações serão ignoradas, independente de como tiverem sido parametrizadas na tela

                             

Como o intuito da exportação em planilha é possibilitar o trabalho nos dados de forma "crua", ao optar por esse tipo de exportação alguns parâmetros serão desconsiderados. Portanto, não será realizada totalização no relatório e nem a quebra. Os parâmetros abaixo serão desconsiderados internamente durante a geração do arquivo:

Também é importante destacar que a quantidade de caracteres dos campos será desconsidera, pois em Excel e CSV as informações devem ser exibidas sem cortes. Por exemplo, se os campos Débitos e Créditos possuírem tamanho 1, ao gerar o arquivo o conteúdo não ficará restrito a um caractere, ele será exibido sem corte.
