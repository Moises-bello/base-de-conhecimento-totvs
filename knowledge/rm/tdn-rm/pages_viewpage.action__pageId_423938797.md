---
content_hash: c23f0f4dfd1a59a5b7050ecaf6b1d93a22e6d19bf5ed51a9734e5e607b9ce61e
fetched_at: '2026-06-29T00:09:29.074302+00:00'
page_id: '423938797'
product: rm
source: tdn-rm
title: Relatório Plano de Contas 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938797
version: 8
---

Pré-Requisitos

Este relatório fará a impressão do Plano de Contas Contábil ou Gerencial em formato de listagem.

**Aba Dados**

O relatório Plano de Contas está disponível em Relatório | Plano de Contas, e tem a finalidade listar as contas cadastradas em uma determinada coligada, ou contas globais. Ao emitir o relatório as informações escolhidas serão gravadas pelo sistema. Assim ao entrar novamente no relatório você visualizará as últimas opções escolhidas.

**Plano de Contas:** Esta parte define qual plano de contas será exibido: Plano de Contas Contábil, contendo as contas contábeis cadastradas, ou Plano de Contas Gerencial, contendo as contas gerenciais cadastradas.

**Grau Contábil/Gerencial:** De acordo com o plano de contas escolhido, será habilitado um menu para escolher o grau de acordo com os níveis das contas exibidas no relatório.

**Ordenação:** É possível parametrizar o relatório Plano de Contas para ser ordenado de acordo com os seguintes campos:

* Código Contábil: A ordenação das contas será pelo código contábil, de forma crescente.
* Código Reduzido: A ordenação das contras será pelo código reduzido, de forma crescente.
* Descrição: A ordenação das contas será pela sua descrição, em ordem alfabética.

**Contas Sintéticas:** Nesta área é possível marcar a opção "Saltar linha ao imprimir", que faz com que a cada conta do tipo sintética, seja saltada uma linha antes de ser impressa a conta seguinte. Caso não esteja marcada essa opção, somente será saltada uma linha a cada nova conta de grau 1.

**Não mostrar contas inativas:** Ao selecionar essa opção, não serão exibidas no relatório as contas contábeis/gerenciais que foram inativadas.

**Distribuição Gerencial:** Quando selecionada essa opção, abaixo das contas que possuem distribuição gerencial, são listadas as contas gerencias que recebem esse repasse, e a porcentagem da distribuição. Esta opção somente será válida quando selecionado o plano de contas contábil, visto que somente contas contábeis podem ter distribuição gerencial.

**Saltar página grupo:** Esta opção somente é válida quando selecionado o tipo de ordenação por Código Contábil. Ao marcar essa opção, a cada novo grupo, ou seja, a cada nova conta de grau 1, é inserida uma quebra de página.

**Ordenação só nas analíticas:**  Ao selecionar essa opção, o relatório somente irá considerar o critério para ordenação nas contas analíticas, de forma que as contas sintéticas permanecem ordenadas de forma crescente. Se escolhida ordenação por Conta Contábil, essa opção não surgirá efeito algum, pois por padrão a ordenação é pelo código da conta, de forma crescente.

**Filtrar Contas:** Uma tela com as opções do filtro será aberta posteriormente no processo de geração do relatório, onde será possível filtrar pelo código das contas ou por um intervalo de códigos.

**Aba Layout**

**Tipo de Arquivo:** É possível gerar o relatório nos formatos CSV, JPEG, HTML, XLS, MHT, RTF, TXT e PDF.

**Utilizar Numeração Sequencial:** Com esta opção marcada, o campo de N.º Página Inicial assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Data de emissão:** Esta opção determina a data desejada para constar no cabeçalho do relatório como sendo a Data de Emissão do mesmo.

**Observação:** Se você quiser que no cabeçalho do relatório não seja impressa a data de emissão, você deverá deixar este campo em branco.

**Quantidade de página por arquivo:** A fim de atender bases de dados com grande volume, poderá ser determinada uma limitação da quantidade de páginas que cada máquina consegue processar e exibir. Ao definir a quantidade de páginas por arquivo, o relatório será quebrado conforme a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório. Ao final do processamento será exibida uma tela com as quebras de páginas que foram geradas na emissão do relatório para conferência.

**Esquerda, Direita, Superior e Inferior:** Permite a configuração das margens Direita, Esquerda, Superior e Inferior do relatório. Podendo aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem Direita, entre 0 e 25 para margem Esquerda e entre 0 e 10 para margem Superior e Inferior.

**Orientação:** O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

**ATENÇÃO ÀS PARAMETRIZAÇÕES!!**

**O relatório somente será impresso de maneira correta quando utilizados os formatos de folha A4 ou Carta (neste caso, a impressora padrão da máquina deve possuir estas configurações).**

**Para os demais formatos o relatório será gerado, mas virá com configurações incorretas.**

Veja Também
