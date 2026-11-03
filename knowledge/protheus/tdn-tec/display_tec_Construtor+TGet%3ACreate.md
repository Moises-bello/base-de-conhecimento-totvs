---
content_hash: 975e566f42a519ed159468c971d46990b47b41ee711035b40ba8df386db15dd9
fetched_at: '2026-07-02T19:24:19.606069+00:00'
page_id: '224119283'
product: protheus
source: tdn-tec
title: Construtor TGet:Create
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TGet%3ACreate
version: 6
---

Construtor TGet:Create

# Construtor TGet:Create

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| bSetGet | codeblock | Indica o bloco de código, no formato {|u| if( Pcount( )>0, := u, ) }, que será executado para atualizar a variável (essa variável deve ser do tipo caracter). Desta forma, se a lista for sequencial, o controle atualizará com o conteúdo do item selecionado, se for indexada, será atualizada com o valor do índice do item selecionado. |  |  |
| nRow | numeric | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nCol | numeric | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| nWidth | numeric | Indica a largura em pixels do objeto. |  |  |
| nHeight | numeric | Indica a altura em pixels do objeto. |  |  |
| cPict | character | Indica a máscara de formatação do conteúdo que será apresentada. Verificar [Tabela de Pictures de Formatação](https://tdn.totvs.com/pages/releaseview.action?pageId=22479526) |  |  |
| bValid | codeblock | Indica o bloco de código de validação, que será executado quando este objeto estiver em foco, e o operador tentar mover o foco para outro componente da interface. Caso o bloco executado retorne .T., será permitida a mudança de foco. Caso o bloco executado retorne .F., não será permitido a remoção do foco do componente. |  |  |
| nClrFore | numeric | Indica a cor do texto do objeto. |  |  |
| nClrBack | numeric | Indica a cor de fundo do objeto. |  |  |
| oFont | object | Indica o objeto, do tipo , que será utilizado para definir as características da fonte aplicada na exibição do conteúdo do controle visual. |  |  |
| uParam12 | logical | Compatibilidade |  |  |
| uParam13 | object | Compatibilidade |  |  |
| lPixel | logical | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| uParam15 | character | Compatibilidade |  |  |
| uParam16 | logical | Compatibilidade |  |  |
| bWhen | codeblock | Indica o bloco de código que será executado quando a mudança de foco da entrada de dados no objeto criado estiver sendo realizada. Se o retorno for verdadeiro (.T.), o objeto continua habilitado; caso contrário, falso (.F.). |  |  |
| uParam18 | logical | Compatibilidade |  |  |
| uParam19 | logical | Compatibilidade |  |  |
| bChange | codeblock | Indica o bloco de código que será executado quando o estado ou conteúdo do objeto é modificado pela ação sobre o controle visual. |  |  |
| lReadOnly | logical | Indica se o objeto pode ser editado. |  |  |
| lPassword | logical | Indica se, verdadeiro (.T.), o objeto apresentará asterisco (\*) para entrada de dados de senha; caso contrário, falso (.F.). |  |  |
| uParam23 | character | Compatibilidade |  |  |
| cReadVar | character | Indica o nome da variável, configurada no parâmetro bSetGet, que será manipulada pelo objeto. Além disso, esse parâmetro será o retorno da função ReadVar(). |  |  |
| uParam25 | character | Compatibilidade |  |  |
| uParam26 | character | Compatibilidade |  |  |
| uParam27 | logical | Compatibilidade |  |  |
| lHasButton | logical | Se definido .T. indica que deve ser aplicado o botão para seleção de Data ou Calculadora. |  |  |
| uParam29 | logical | Compatibilidade |  |  |
| uParam30 | logical | Compatibilidade |  |  |
| cLabelText | character | indica o texto que será apresentado na Label. |  |  |
| nLabelPos | numeric | Indica a posição da label, sendo 1=Topo e 2=Esquerda |  |  |
| oLabelFont | object | Indica o objeto, do tipo , que será utilizado para definir as características da fonte aplicada na exibição da label. |  |  |
| nLabelColor | numeric | Indica a cor do texto da Label. |  |  |
| cPlaceHold | character | Define o texto a ser utilizado como place holder, ou seja, o texto que ficará escrito em cor mais opaca quando nenhuma informação tiver sido digitada no campo. (disponível em builds superiores a 7.00.121227P) |  |  |
| lPicturePriority | logical | Quando .T. define que a quantidade de caracteres permitidos no TGet será baseada no tamanho da máscara (Picture) definida, mesmo que isto exceda a quantidade de caracteres definida na variável bSetGet, até mesmo se ela for vazia (essa variável deve ser do tipo caracter). Além disso este parâmetro ativa o controle dos espaços em branco, não incluindo na variável bSetGet os espaços inseridos automaticamente pela Picture. Ou seja, o TGet retornará somente os espaços em branco efetivamente digitados pelo usuário ou aqueles espaços que já foram inicializados na variável bSetGet. Disponível somente a partir da build 7.00.170117A. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | object | Nova instância da classe TGet |

## Observações

* Em versões superiores à build 7.00.120420A foi implementada a opção para definição de uma label (descrição) do componente visual. Preenchendo os parâmetros cLabelText, nLabelPos, oLabelFont e nLabelColor será disponibilizada, ao topo ou à esquerda, a descrição definida para o componente. Esta característica visa diminuir a quantidade de interações entre o SmartClient e o AppServer na construção de telas, otimizando assim este processo.
* Quando utilizada esta opção não será possível alinhar o componente, sendo a Label um objeto independente ela não será alinhada juntamente com o Controle principal, nesta situação é necessário fazer o posicionamento manualmente.
* A criação automática do label através dos parâmetros desse método não funciona se o componente estiver posicionado em algum layout (como o [TGridLayout](https://tdn.totvs.com/display/tec/TGridLayout)), neste caso é necessário criar o label utilizando o componente [TSay](https://tdn.totvs.com/display/tec/TSay).

## Exemplos

cppEclipsetruefalse
