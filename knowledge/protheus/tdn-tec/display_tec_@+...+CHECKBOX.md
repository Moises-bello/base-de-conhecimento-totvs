---
content_hash: 7958b1f7c433763864509ca3db890e560af2aabd968230dd69fffe4a1270b1b3
fetched_at: '2026-07-02T19:24:25.055384+00:00'
page_id: '496020338'
product: protheus
source: tdn-tec
title: '@ ... CHECKBOX'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+CHECKBOX
version: 3
---

Comando @ ... CHECKBOX

### Sintaxe Mínima

```
@ <nRow>,<nCol> CHECKBOX <lVar>
```

### Sintaxe Completa

```
@ <nRow>, <nCol> CHECKBOX [ <oCheckBox> VAR ] <lVar>   
   [ PROMPT <cCaption>]  
   [ OF | WINDOW | DIALOG <oWnd> ]  
   [ SIZE <nWidth>, <nHeight> ]  
   [ FONT <oFont> ]   
   [ ON CLICK | ON CHANGE <cbClick> ]  
   [ VALID <cbValid> ]  
   [ COLOR | COLORS <nClrText> [,<nClrBack> ] ]  
   [ PIXEL ]   
   [ MESSAGE <cMsg> ]  
   [ WHEN <cbWhen> ]
```

### Include

```
#include "totvs.ch"
```

### Parâmetros

| Cláusula | Tipo | Obrigatória | Descrição |
| --- | --- | --- | --- |
| <nRow> | N | S | Parâmetro obrigatório, indica a linha da tela (em pixels ou coordenadas) onde o componente será exibido. Deve ser usada uma expressão numérica, constante ou variável. |
| <nCol> | N | S | Parâmetro obrigatório, indica a coluna da tela (em pixels ou coordenadas) onde o componente será exibido. Deve ser usada uma expressão numérica, constante ou variável. |
| CHECKBOX |  | S | Cláusula obrigatória, pode ser seguida diretamente da expressão caractere – constante ou variável – que deve ser exibida na tela, ou da cláusula opcional VAR |
| <oCheckBox>VAR | O | N | Quando a cláusula VAR for informada, permite e obriga a especificar um nome de variável AdvPL imediatamente antes da cláusula, no qual o objeto do componente tCHECKBOX() será armazenado, seguido da expressão ou variável lógica cujo conteúdo será mostrado para edição na interface. |
| <lVar> | L | S | Indica o nome da variável cujo conteúdo será editado na interface. deve ser do tipo "L" lógico. |
| OF | WINDOW | DIALOG <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel, folder) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| SIZE <nWidth>,<nHeight> | N | N | Cláusula opcional, quando utilizada deve ser seguida dos parâmetros numéricos <nWidth> e <nHeight>, que respectivamente indicam o comprimento e a altura do componente na interface. |
| FONT <oFont> | O | N | Cláusula opcional, permite informar um objeto AdvPL do tipo TFont(), para que seja possível mostrar o texto no componente usando uma fonte diferente da fonte default do ambiente. |
| ON CHANGE | ON CLICK <cbClick> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código a ser executado quando o estado ou conteúdo do objeto é modificado pela ação sobre o controle visual – ou seja, quando o conteúdo editável da interface for alterado. |
| VALID <cbValid> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código com retorno booleano, a ser executado no momento da perda de foco do componente. A função ou expressão de validação deve retornar .T. (verdadeiro) caso o foco possa sair deste componente. Normalmente usada para validação dos dados de entrada. |
| COLOR | COLORS <nClrText> [ ,<nClrBack] | N | N | Cláusulas opcionais, que quando especificadas, permitem alterar a cor do texto da mensagem a ser exibida pelo componente, e opcionalmente também permite alterar a cor de fundo do texto da exibição. |
| PIXEL |  | N | Cláusula opcional, quando for especificada, indica que o sistema de coordenadas usado nos parâmetros <nRow> e <nCol> são em pixels (ou pontos) a partir da coordenada superior esquerda (0,0) do componente visual pai em uso no qual o objeto será posicionado. |
| MESSAGE <cMsg> | C | N | Indica a mensagem, do tipo dica de contexto (tooltip/hint), que será apresentada ao posicionar o ponteiro do mouse sobre o objeto. |
| WHEN <cbWhen> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código com retorno booleano, a ser executado no momento de troca de foco de componentes da interface. A função ou expressão de validação deve retornar .T. (verdadeiro) caso o componente possa receber foco. |

### Classe usada pelo comando

O comando @ .. CHECKBOX é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TCHECKBOX()** e seu método construtor **NEW().**

### Referências

### Exemplo

text1Exemplo do comando @ ... CHECKBOXtrue

### Resultado
