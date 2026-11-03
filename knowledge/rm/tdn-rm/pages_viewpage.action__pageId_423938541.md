---
content_hash: fccb75d9f0d95c10859f674673ccdc6f1c72589c562ed9391b198d35d68c9405
fetched_at: '2026-06-29T00:09:27.549555+00:00'
page_id: '423938541'
product: rm
source: tdn-rm
title: Relatório Diário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938541
version: 7
---

Pré-Requisitos

O Relatório Diário está disponível em Relatório | Diário, e tem a finalidade demonstrar a movimentação contábil diária da empresa conforme lançamentos existentes em Lote Zero.

**ATENÇÃO ÀS PARAMETRIZAÇÕES!!**

**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos, o relatório será gerado mas virá com configurações e dimensionamentos de páginas incorretas.**

Ao emitir o relatório as informações escolhidas serão gravadas pelo sistema através da opção de Preferências. Assim ao entrar novamente no relatório você visualizará a última opção preenchida/selecionada nos campos.

Para ordenação de impressão de Campos idêntica ao relatório Delphi, as Preferências de impressão existentes devem ser deletadas. Para exclusão clique na imagem de engrenagem das Preferências | Abrir/Excluir, após selecione a preferência, e clique em Excluir.

**Aba Dados**

**Data Inicial e Data Final:** Defina nestes campos a faixa inicial e final de datas limitadoras, para processamento e cálculo dos lançamentos.

**Filtro Automático de Datas:** Ferramenta que simplifica a parametrização das datas, onde é escolhido um ano e um tipo de filtro, que pode ser: Semanal, Mensal, Bimestral, Trimestral, Semestral e Anual, e após selecionar as opções o intervalo de datas é exibido e se confirmado, os valores são inseridos nos campos "Data Inicial" e "Data Final".

**Buscar do histórico contábil:** Ao marcar esta opção, os valores apresentados serão somente os presentes no histórico contábil, ou seja, aqueles que pertencem a um período já encerrado.

**Basear na Data de Cotação:** Esta opção permite a impressão dos valores baseando na data da cotação dos lançamentos. Marcando esta opção, o sistema buscará os lançamentos que possuírem a data da cotação dentro do período informado no intervalo de datas.

**Selecionar Coligada / Filial / Departamento:** Por padrão, o Relatório Diário é gerado contendo os dados da coligada selecionada e de suas filiais, mas através dessa opção é possível também selecionar todas as coligadas marcando o item "Todas as coligadas", da mesma forma que é possível realizar um filtro mais específico de coligadas, filiais e departamentos através do item "Ativar filtro".

**Formato do Diário**

O formato do livro diário pode ser das seguintes formas:

Com código e descrição da conta, o relatório será apresentado por lançamento, onde será informado a operação (débito ou crédito), e poderá ser ordenado das seguintes formas:

* Referência do Lançamento;
* Documento;
* Conta + Referência do Lançamento;
* Conta + Documento;
* Conta + Contrapartida;
* Conta + Contrapartida + Documento;

Com código e descrição das contas a débito e a crédito, o relatório será apresentado mostrando as movimentações das contas de débito e crédito de acordo com os lançamentos, e poderá ser ordenado das seguintes formas:

* Referência do Lançamento
* Documento

Atenção!!

Para bases de dados com grande volume de informações, sugerimos ganho de performance a geração do arquivo em formato PDF direcionando onde o mesmo será salvo (neste caso, não deve ser marcado a opção de visualizar impressão).

**Quebrar página:** Utilizando as opções nessa sessão, é possível parametrizar o relatório para realizar uma quebra de página, das seguintes formas: "Por filial" e "Mensal".

**Totalizar**

Nesta parte estão algumas opções de totalização para o Relatório Diário, é possível escolher todas as opções se desejado. As opções disponíveis para totalização são:

* Imprime totalização diária, onde ao final de cada dia no relatório diário é exibida uma linha contendo a totalização dos valores daquele dia.
* Imprime totalização mensal, onde ao final de cada mês no relatório diário é exibida uma linha contendo a totalização dos valores daquele mês.
* Imprime totalização geral acumulada do início do período contábil, onde ao final o relatório diário é exibida uma linha contendo a totalização dos valores no período selecionado.

**Lote:** Permite filtrar um ou mais Lotes, sendo Zero ou Lote N.

Serão considerados todos os registros que estiverem nos lotes informados pelo usuário.   
Apenas os lotes das coligadas selecionadas no filtro de coligada estarão disponíveis para seleção.   
Quando a opção de histórico contábil for marcada, o filtro por lote será desabilitado e será considerado o lote 0.   
Um aviso será exibido para que o usuário decida se prossegue ou não com a alteração.   
Se informou lote que não o Lote 0, não serão exibidos os saldos anteriores de períodos já liberados de contas sem movimentação após a liberação e antes da data inicial de movimentação informada.  
Caso nenhum lote seja informado no filtro será considerado o lote 0.

**Aba Filtros**

**Filtro por Centro de Custo:** Uma tela com as opções do filtro será aberta posteriormente no processo de geração do relatório, onde será possível filtrar pelos centros de custos ou intervalos de centro de custo inseridos.

**Histórico:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório, há uma opção disponibilizando tal flexibilidade.

**Definir / Configurar | Tipo de valor / moeda:** Ao selecionar essa opção, em uma tela posterior serão exibidas as parametrizações relacionadas à tipo de valor e moeda, onde será possível escolher entre a primeira moeda, segunda moeda ou ainda informar uma moeda e valor de cotação. Também nessa parte é possível parametrizar o relatório de forma a mostrar os valores em milhares, com ou sem centavos.

**Aba Layout**

Nesta aba é possível alterar algumas informações apresentadas no relatório, abaixo estão as opções que podem ser selecionadas.

**Alterar título:** Permite definir um novo título para o relatório, conforme desejado (máximo de 28 caracteres).

**Inserir texto adicional no final:** Se essa opção for selecionada, será aberta uma nova janela, para que o texto adicional seja inserido logo após o final do relatório, incluindo ainda opções de posicionamento de texto e variáveis de data e hora.

**Inserir observação abaixo do título:** Se essa opção for selecionada, será aberta uma nova janela, para que a observação seja inserida logo após o título do relatório, incluindo ainda opções de posicionamento de texto e variáveis de data e hora. Caso o texto seja muito extenso o mesmo será truncado.

**Exibir nome fantasia da filial no cabeçalho:** Essa opção somente será apresentada caso esteja selecionado um filtro por filial. Ao selecionar essa opção, o nome fantasia das filiais selecionadas será apresentado no cabeçalho do relatório; Transporte de débitos e créditos: Ao marcar esta opção, os saldos das contas serão transportados de uma página para outra do relatório.

**Exibir dados dos centros de custos no cabeçalho**

Marcando esta opção, o sistema exibirá o código do centro de custo no cabeçalho do relatório.  
Essa opção será habilitada quando um ou mais centros de custos forem inseridos na aba Filtro| Centro de custo. Caso contrário, ficará desabilitada.  
O sistema exibirá apenas os centros de custos que couberem na linha.

**Atributos de Página:**Determina a forma para a impressão do relatório.

Orientação: O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

Margem Esquerda, Direita, Superior e Inferior: Permite a configuração das Margens Direita, Esquerda, Superior e Inferior do relatório. Podendo aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem Direita, entre 0 e 25 para margem Esquerda e entre 0 e 10 para margem Superior e Inferior.

Utilizar Numeração Sequencial: Com esta opção marcada, o campo de N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

Descrição da Contagem de Página: Determina a descrição que será impressão na emissão do relatório para número de página. Exemplo: Folha 01 ou Pag. 01

Data de emissão: Esta opção determina a data desejada para constar no cabeçalho do relatório como sendo a Data de Emissão do mesmo. Se você quiser que no cabeçalho do relatório não seja impressa a data de emissão, você deverá deixar este campo em branco.

Quantidade de página por arquivo: A fim de atender bases de dados com grande volume, poderá ser determinada uma limitação da quantidade de páginas que cada máquina consegue processar e exibir. Ao definir a quantidade de páginas por arquivo, o relatório será quebrado conforme a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório.

Ao final do processamento será exibida uma tela com as quebras de páginas que foram geradas na emissão do relatório para conferência.

N.º Página Inicial: Digite o número de página inicial para impressão. Com a opção utilizar Numeração Sequencial de páginas marcada, este campo assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

Definir / Configurar | Atributo de página para o Livro Diário: Ao selecionar essa opção, em uma tela posterior serão exibidos os parâmetros para impressão em formato de livro. Ao habilitar a opção "Impressão em formato livro" é possível escolher os seguintes parâmetros:

* Número do Livro Diário, que irá modificar o número do primeiro livro gerado para o escolhido, e os demais seguem em ordem crescente após este;
* Número máximo de páginas, que estabelece um número máximo de páginas em cada livro, passando para um novo livro assim que atingir o limite aqui estabelecido;

A opção "Não reiniciar a contagem de páginas a cada mudança de livro" quando marcada, não reinicia a numeração das páginas a cada mudança de livro, seguindo então uma numeração de páginas de forma crescente; Quando a opção "Reservar a última página do livro para o termo de fechamento" é marcada, entre cada mudanças de livros, o último número de páginas não é exibido, sendo reservado para o termo de fechamento; Ao marcar a opção "Definir reinicio da numeração da página" é exibido ao lado um espaço para ser escolhida o número que será usado a cada reinicio de página, em cada mudança de livro.

**Aba Campos**

Nessa aba é possível configurar quais campos devem ser impressos e o tamanho de cada um. É possível também verificar o tamanho que está sendo utilizado pelos campos e pelas margens em relação ao limite possível. Caso o valor  
ultrapasse o limite não será possível imprimir o relatório.

Regra de impressão para determinados campos: Alguns campos ao serem selecionados para impressão têm comportamentos específicos, a seguir segue sua especificação.

A variação de tamanho de impressão dos campos será alterada conforme a seleção da Orientação Paisagem ou Retrato.

Histórico: Para este campo o limite configurado pelo usuário não determina o corte da informação e sim a quebra de linha quando atingido o limite informado pelo usuário e logo após a quebra será continuado a sua impressão na linha debaixo até que seja impresso toda sua informação.

* Quando o código do histórico padrão contiver variáveis e Houver alguma informação para o complemento será impresso somente a informação do complemento;
* Quando o código do histórico padrão não contiver variáveis e Houver alguma informação para o complemento será impresso a descrição do histórico padrão mais a informação que houver no campo do complemento;
* Quando o código do histórico padrão contiver variáveis e não haver informação para o complemento será impresso a descrição do histórico  juntamente com as variáveis;
* Ver Parâmetro (Quebrar por palavras na impressão do histórico)  que quando habilitado, a impressão de históricos nos relatórios irá respeitar as palavras na quebra de linha, evitando que estas sejam cortadas de uma linha para outra. Com esta opção marcada, haverá mais consumo de espaço na impressão do histórico e consequentemente maior gasto de papel.

Veja Também

* [Boletim Técnico Relatório Diário](http://tdn.totvs.com/pages/releaseview.action?pageId=185751399)
