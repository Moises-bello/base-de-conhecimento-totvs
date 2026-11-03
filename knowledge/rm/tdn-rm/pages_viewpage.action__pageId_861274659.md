---
content_hash: e0c4071046b1dd9feb3b2eca21a9cb80d1f06c0e8aab4b77442b28c1cba98250
fetched_at: '2026-06-29T00:11:55.448109+00:00'
page_id: '861274659'
product: rm
source: tdn-rm
title: Kit Pré-montado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=861274659
version: 24
---

Versão 

Disponível para as versões 2410 e superiores.

1. **Visão Geral**
2. **Montar Kit**
3. **Desmontar Kit**
4. **Configurações para Tipo de Movimentos Relacionados ao Kit Pré-Montado**

falsepaineltrueVisão Geral

## **01. VISÃO GERAL**

Para acessar o kit pré-montado deve-se clicar em:

Dessa forma, será mostrado todos os kits montados:

Nas colunas do grid temos:

* Código sequencial;
* Kit - correspondendo ao kit montado;
* Utilizado? - evidenciando se o kit foi ou não utilizado;
* Código de barras
* Validade crítica - corresponde ao item componente do kit que possui a data de validade próxima á sua expiração (de acordo com o parâmetro definido para alerta de validade).

## **01.01. Imprimir etiqueta(s)**

Para imprimir etiquetas de kits montados o usuário poderá selecionar no grid utilizando-se do checkbox e clicando em Processos → Imprimir códigos de barras. 

Montar Kit

## **02. MONTAR KIT**

Para montar um kit basta clicar em: Processos > Montar kit.

Após abrir a tela deve informar qual o kit deseja montar e qual o local de estoque.

Após o preenchimento do kit será listado todos os produtos que o compõem.

É necessário selecionar o local de estoque para habilitar o campo para bipar o produto.

Para adicionar ao kit os itens que não são controlados por lote, basta o usuário selecionar os itens no grid e clicar no botão Adicionar ao Kit.

Para os itens controlados por lote existem duas opções:

* Informar o código de barra no campo de "código do material" e apertar a tecla “enter” no campo para buscar as informações do produto. O campo de lote será preenchido automaticamente de acordo com o código de barras preenchido.

* Selecionar o botão “...” que está ao lado do campo do código do produto. Será aberta a tela de pesquisa do produto.

          O usuário deverá selecionar o produto e clicar em OK. Após fechar a tela deverá clicar em “Adicionar ao kit”.

          Nessa tela de busca só exibiremos os itens que constam no kit.

**Montagem do Kit**

Para montar o kit o usuário deve adicionar todos os produtos.

Após adicionar todos os itens o botão “Montar kit” fica habilitado, vide imagem abaixo.

O usuário deverá definir quantos kits serão montados com aqueles itens.

Permissão de acesso para quantidade de Kits

O campo "Quantidade de kits a serem montados" somente será habilitado, se o perfil do usuário tiver permissão, caso contrário será sempre montado 1 kit.

Após clicar no botão “Montar kit” será exibida uma mensagem de confirmação:

Após montagem será exibida mensagem de confirmação. Nessa mensagem será exibido o nome do kit montado e quantidade criada. Será possível imprimir o código de barras do(s) kit(s) montado(s), conforme imagem abaixo:

Caso feche a tela, o usuário pode verificar todos os kits que foram montados no grid externo.

**Validações**

* O kit é um item de estoque cadastrado anteriormente como "Kit pré-montado". Os itens podem ser alterados apenas nesse momento, no cadastro. Na montagem, os itens não podem ser adicionados ou excluídos do kit.
* Não deve ser possível montar o kit após adicionar mais ou menos itens do que foi determinado pelo padrão. Caso o usuário tente adicionar algum item fora do padrão, deve ser exibida a mensagem "Ação bloqueada. Todos os itens predeterminados no kit padrão já foram adicionados a montagem. O [NOME DO KIT] está completo".
* Caso o lote seja preenchido, deve ser possível adicionar o item ao kit, mesmo sem ter inserido o código de barras.
* Caso um item que não conste no kit tente ser adicionado, deverá aparecer a seguinte mensagem: “Ação bloqueada. Este item não pertence ao [NOME DO KIT] e por isso não pode ser adicionado a montagem”
* Itens vencidos não poderão ser adicionados ao kit. Ao clicar em montar kit, deve aparecer alerta informando ao usuário qual item está vencido e porque não foi possível concluir a montagem do kit. A linha do item vencido deve aparecer em vermelho.
* O botão excluir item deve ser habilitado a partir do primeiro item adicionado ao grid "Itens Adicionados". Ao clicar em "Excluir item" deve ser excluído o item da(s) linha(s) selecionadas.
* O botão "Montar kit" deve ser habilitado quando todos os itens do grid "Itens que compõem o kit" forem selecionados e adicionados, ou seja, a montagem do kit tiver sido concluída.
* Após imprimir etiqueta de kit, a coluna de confirmação de impressão de etiqueta passará a ser sinalizada como "Sim".
* Será possível montar 1 ou N kits com um limite máximo de 999 kits.
Desmontar Kit

## **03. DESMONTAR KIT**

Para desmontar kit basta clicar em: Processos > Desmontar kit. A seguinte tela é apresentada:

Deverá ser adicionado o kit no campo "Código do kit a ser desmontado", utilizando-se do código de barras ou busca manual.

Em seguida, o grid será carregado com os itens componentes daquele kit, conforme exibido na imagem abaixo:

Para concluir a desmontagem o usuário deve clicar no botão Desmontar Kit.

A coluna validade fica em destaque caso o item esteja próximo da expiração da sua validade configurada de acordo com o parâmetro definido de número de dias para alerta de validade.

**Validações**

* O campo de local de estoque é obrigatório:
* O campo de centro de custo é visível quando o sistema é integrado com EMS ou Protheus.
* O código de barras de kit inserido deve ser válido, correspondente a um kit montado que conste em local de estoque.
* Devem constar no grid os itens que constem em kit de estoque, itens esses que foram lançados no ato da montagem.
* Kit só pode ser desmontado em sua totalidade. Portanto, para ser desmontado o kit deve conter todos os itens. Um kit cobrado para algum paciente deverá apenas ser devolvido, e não desmontado.
* O botão trocar lote só ficará habilitado caso selecione um ou mais itens controlado por lote.

## **03.1. TROCAR LOTE**

Para trocar o lote de um item que pertence ao kit o usuário deve selecionar um item controlado por lote e clicar no botão "Alterar lote", conforme imagem abaixo:

Após clicar no botão "Trocar lote" será exibido a seguinte tela:

1 - Lista dos itens selecionados para alterar o lote.

2 - Barra de busca para selecionar os novos lotes dos itens que devem ser alterados.

3 - Grid com os novos itens/lotes alterados.

### **03.1.1 Busca do produto**

Será possível buscar o produto de duas formas diferentes, são elas:

1 - Busca via código de barras: nesse momento o usuário deve inserir/bipar o código de barras do produto no campo grifado abaixo e clicar no "Enter". O item será adicionado automaticamente no grid. Será adicionado a quantidade definida no campo quantidade.

2 - Busca via nome do produto, para isso, o usuário deve clicar no botão marcado abaixo:

Após clicar no botão será aberta a tela de pesquisa onde o usuário poderá buscar o produto por: Nome, Código e até mesmo filtrar pelo grupo de estoque, conforme imagem abaixo:

Na busca serão exibidos apenas os produtos que fazem parte dos itens marcado para alteração na tela de desmontagem. Ao buscar serão exibidos todos os lotes que possuem saldo no local de estoque selecionado para desmontar o kit.

Após selecionar o item e clicar no botão Ok o usuário retornará para tela principal com os dados do item preenchidos, conforme imagem abaixo:

Para confirmar a substituição o usuário deve clicar no botão "Adicionar". Após clicar o item será inserido no grid, conforme imagem abaixo:

**Validações**

* Só será permitido trocar o produto por lotes que possuem saldo no local de estoque da desmontagem.
* A quantidade alterada não poderá ser maior que a quantidade total dos itens selecionados.
* A quantidade alterada pode ser menor que o total da quantidade dos itens selecionados.
* Não será possível adicionar itens que não estão na lista de itens selecionados.

imprimirImprimir Código de Barras

Para imprimir a etiqueta de código de barras do Kit Pré-Montado, será necessário as seguintes configurações:

**1 - Parâmetro Geral do Gestão Hospitalar / Relatórios**

Preencher o nome do relatório no campo "KIT de Mat/Med (Código de Barras)"

**2 - O Relatório de Código de Barras**

É obrigatório o relatório ter parâmetros com os nomes: COLIGADA e NOMECOMP.

**3 - Imprimir Código de barra**

Após executar o processo "Montar kit", é possível imprimir a etiqueta de códigos de barras nos seguintes locais:

**3.1 - Botão "Imprimir"**

Após montagem será exibida mensagem de confirmação. Nessa mensagem será exibido o nome do kit montado e quantidade criada.

Será possível imprimir o código de barras do(s) kit(s) montado(s), clicando no botão "Imprimir", conforme imagem abaixo:

**3.2 - Processo "Imprimir código(s) de barras**

Selecione na grid de visão qual registro deseja imprimir e execute o processo de impressão.

**4 - Sugestão para personalizar a etiqueta de código de barras**

Caso necessite personalizar a etiqueta de código de barras, poderá fazer uma cópia do relatório SAUREL0019 e nesta cópia  alterar os campos conforme sua necessidade.

O relatório “SAUREL00019 Etiqueta de Código de Barras” deve ser utilizado no processo de impressão do menu “Farmácia/Etiqueta de código de barras”.

Para o processo de impressão do menu “Farmácia/Kit Pré-Montado”, o relatório deverá ser personalizado, mudando na sentença SQL do relatório o campo chamado “CHAVE”.

#### **Dica: faça uma cópia do relatório SAULREL00019 e altere o caminho da fonte de dados para a sentença correta :**

|  |  |
| --- | --- |
| **ETIQUETA DE CÓDIGO DE BARRA** | **KIT PRÉ MONTADO** |
| SELECT  SUBSTRING(SZTABW.CHAVE,7,13) CODBARRAS,    CPS1,  CPS2, CPS3, CPN1,CODIGOPRD  FROM    SZTABW(NOLOCK), TPRD(NOLOCK)  WHERE    SZTABW.CODCOLIGADA = :COLIGADA    AND SZTABW.NOMECOMPUTADOR = :NOMECOMP    AND SZTABW.CPN1 = TPRD.IDPRD | SELECT  SZTABW.CHAVE CODBARRAS,    CPS1,  CPS2, CPS3, CPN1,CODIGOPRD  FROM    SZTABW(NOLOCK), TPRD(NOLOCK)  WHERE    SZTABW.CODCOLIGADA = :COLIGADA    AND SZTABW.NOMECOMPUTADOR = :NOMECOMP    AND SZTABW.CPN1 = TPRD.IDPRD |

tipoMovimentoConfigurações para Tipo de Movimentos Relacionados ao Kit Pré-Montado

Os Kits Pré-Montados são um agrupamento de diferentes itens de estoque em um único produto. O kit de cirurgia é sua principal aplicação prática.

Durante a montagem do Kit é feita uma movimentação para retirada dos componentes do estoque e ao mesmo tempo uma movimentação para entrada do kit pré-montado no estoque.

Associamos os tipos de movimentos do BackOffice RM ao Gestão Hospitalar através do menu Parâmetros/Gestão Hospitalar/Integrações/Integração BackOffice/Gestão de Estoque na etapa “Kit Pré-Montado”.

**1 – Movimento (Entrada) – Afeta Estoque**

Utilizado na montagem do kit

#MovKitPreMontadoEntrada

**2 – Movimento (Saída) – Afeta Estoque**

Utilizado na desmontagem do kit e na baixa do kit.

#MovKitPreMontadoSaida

**3 – Movimento (Devolução)**

Utilizado ao realizar uma devolução contendo o kit OU algum item que compõe o kit ao estoque.

O seu comportamento depende do parâmetro de Estoque **“Lança os itens do kit pré-montado na requisição”.**

#MovKitPreMontadoDevolucao

**4 – Movimento (Requisição a paciente)**

Utilizado no processamento de Requisições à Paciente dos Kits.

Quando o mesmo estiver preenchido, o sistema utilizará este tipo de movimento para baixar o kit. Caso contrário, o sistema utilizará o movimento de saída.

Na movimentação de estoque, ao Processar a requisição contendo um kit, o sistema utilizará este código de movimento caso esteja preenchido.

#MovKitPreMontadoRequisicao
