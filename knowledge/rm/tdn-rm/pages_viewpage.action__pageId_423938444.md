---
content_hash: d8e4d1ddac732dd9f0e299fb21e3233991bef0a7366b41ed0a69cfe8bcfd9e5d
fetched_at: '2026-06-29T00:09:27.157588+00:00'
page_id: '423938444'
product: rm
source: tdn-rm
title: Relatório Lançamentos Duplicados 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938444
version: 2
---

Pré-Requisitos

Através do relatório Lançamentos Duplicados é possível identificar lançamentos duplicados na base de dados. Com a utilização de filtros disponibilizados no relatório é possível identificar os lançamentos duplicados com facilidade e simplicidade.

Os lançamentos são ordenados pelos campos selecionados para comparação, e pela referência.

Os lançamentos ordenados serão percorridos, e caso todos os campos selecionados para comparação sejam iguais, eles serão impressos no relatório.

**ATENÇÃOS ÀS PARAMETRIZAÇÕES!!**  
**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos, o relatório será gerado mas virá com configurações e dimensionamentos de páginas incorretas.**

O relatório Lançamentos Duplicados pode ser acessado através do menu Relatórios | Lançamentos Duplicados.

**Dados**

Através da guia Dados é possível configurar as seguintes opções para geração do relatório.

**Intervalo de datas inicial e final:** que será obedecido para verificar os lançamentos. Esse parâmetro é obrigatório.

**Buscar do Histórico Contábil:** Esta opção permite a impressão do Relatório baseando o resultado em datas anteriores ao período contábil. Desta forma deve ser informado uma data que seja anterior ao início do período contábil. ( Exemplo: Período Contábil = 01/01/2009 á 31/12/2013. A data a ser informada deve ser inferior a 31/12/2008.)

**Campos para comparação:** Deverão ser marcados os campos que devem ser comparados para que dois ou mais lançamentos sejam considerados duplicados. Esses lançamentos serão exibidos na impressão do relatório.

Estão disponíveis para a comparação os campos de Documento, Data, Código do Histórico Padrão, Valor do Lançamento, Conta Crédito e Conta Débito.

Deve ser marcado, pelo menos, um campo para comparação.

**Imprimir Centro de Custo em Código Reduzido:** Ao marcar esta opção o código do centro de custo deixa de ser impresso, e é substituído pela impressão do código reduzido.  
   
**Filtros**

Podem ser realizados filtros por faixa de números de Documentos ou pelo Histórico Padrão. Os filtros podem ser utilizados individualmente, ou em conjunto.

**Layout**

**Utilizar Numeração Sequencial:** Esta opção só ficará habilitada com o Parâmetro "Utilizar Numeração Sequencial de Páginas" marcado.

Marque esta opção para que seu relatório obedeça à numeração sequencial informada nos parâmetros do Totvs Gestão Contábil.

Com esta opção marcada, o campo de N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Descrição da Contagem de Página:** Determina a descrição que será impressão na emissão do relatório para número de página.

Exemplo:

* Folha 01
* Pag. 01

**Data de emissão:** Digite a data desejada para constar no cabeçalho do relatório como sendo a data de emissão do mesmo. Você poderá digitar simplesmente a data desejada, ou se preferir, poderá selecioná-la através do ícone que se encontra à frente deste campo. Após a seleção, confirme a data escolhida. A data padrão deste campo será sempre a data Atual.

**Quantidade de página por arquivo:** Esta opção foi criada para base de dados com grande volume de dados, por que existe uma limitação da quantidade de página que cada máquina consegue processar e exibir.

Quando informado a quantidade de páginas por arquivo o relatório será quebrado quando a quantidade informada for atingida tornando possível o processamento e a exibição do relatório.

Ao final do processamento será exibo as quebras conforme a imagem abaixo.  

**Margem Esquerda, Direita e Superior:** Esta opção permite que você configure as Margens Direita, Esquerda e Superior do relatório. Você poderá aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem Direita, entre 0 e 25 para margem Esquerda e entre 0 e 10 para margem Superior e inferior.

**N.º Página Inicial:** Digite o número de página inicial para impressão. Com a opção utilizar Numeração Sequencial de páginas marcada, este campo assumirá o valor da sequência automática gerada pelo sistema, de acordo com o definido nos parâmetros, não podendo ser alterado.

**Exportar para arquivos:** A exportação de arquivos permite ao usuário selecionar diversos tipos de saída do relatório. Dentre as saídas disponíveis podemos citar o CSV, o JPEG, o HTML, o XLS, o MHT, o RTF, o TXT e o PDF.

**Orientação:** O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

Veja Também

* [Boletim Técnico Relatório Lançamentos Duplicados](http://tdn.totvs.com/pages/viewpage.action?pageId=185751408)
