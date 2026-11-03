---
content_hash: 9419334e4cbe100f55434cbcef7353fbb6e09c9df83944d181f6e63e745b5b74
fetched_at: '2026-07-02T19:24:25.048178+00:00'
page_id: '496020327'
product: protheus
source: tdn-tec
title: '@ ... GET MULTILINE'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+GET+MULTILINE
version: 2
---

Comando @ ... GET MULTILINE

### Sintaxe Mínima

```
@ <nRow>,<nCol> GET <uVar> MULTILINE
```

### Sintaxe Completa

```
@ <nRow>, <nCol> GET [ <oMultiGet> VAR ] <uVar> MULTILINE  
   [ OF | WINDOW | DIALOG <oWnd> ]  
   [ COLOR | COLORS <nClrText> [,<nClrBack> ] ]  
   [ SIZE <nWidth>, <nHeight> ]  
   [ FONT <oFont> ]  
   [ PIXEL ]  
   [ WHEN <cbWhen> ]  
   [ READONLY ]  
   [ VALID <cbValid> ]  
   [ NO BORDER | NOBORDER ]  
   [ NO VSCROLL ]
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
| GET |  | S | Cláusula obrigatória, pode ser seguida diretamente da expressão caractere – constante ou variável – que deve ser exibida na tela, ou da cláusula opcional VAR |
| <oMultiGet>VAR |  | N | Quando a cláusula VAR for informada, permite e obriga a especificar um nome de variável AdvPL imediatamente antes da cláusula, no qual o objeto do componente tMultiGet() será armazenado, seguido da expressão ou variável caractere cujo conteúdo será mostrado para edição na interface. |
| <uVar> | C | S | Indica o nome da variável cujo conteúdo será editado na interface. Deve ser do tipo "C" Caractere. |
| MULTILINE |  | S | Cláusula obrigatória que indica o uso interno da classe tMultiLine(). Caso esta palavra chave não seja inserida no comando, o pré-compilador pode traduzir a chamada para a criação de um componente da classe tGet(). Esta cláusula também pode ser substituída pelas cláusulas TEXT ou MEMO – apenas por questão de padronização, recomenda-se o uso da cláusula MULTILINE. |
| OF | WINDOW | DIALOG <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel, folder) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| COLOR | COLORS <nClrText> [ ,<nClrBack] | N | N | Cláusulas opcionais, que quando especificadas, permitem alterar a cor do texto da mensagem a ser exibida pelo componente, e opcionalmente também permite alterar a cor de fundo do texto da exibição. \*\* Implementação recente do componente, veja as notas de release para confirmar a partir de qual versão de Application Server e SmartClient esta funcionalidade está disponível. |
| SIZE <nWidth>,<nHeight> | N | N | Cláusula opcional, quando utilizada deve ser seguida dos parâmetros numéricos <nWidth> e <nHeight>, que respectivamente indicam o comprimento e a altura do componente na interface. |
| FONT <oFont> | O | N | Cláusula opcional, permite informar um objeto AdvPL do tipo TFont(), para que seja possível mostrar o texto no componente usando uma fonte diferente da fonte default do ambiente. |
| PIXEL |  | N | Cláusula opcional, quando especificada, indica que o sistema de coordenadas usado nos parâmetros <nRow> e <nCol> são em pixels (ou pontos) a partir da coordenada superior esquerda (0,0) do componente visual pai em uso no qual o objeto será posicionado. |
| WHEN <cbWhen> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código com retorno booleano, a ser executado no momento de troca de foco de componentes da interface. A função ou expressão de validação deve retornar .T. (verdadeiro) caso o componente possa receber foco. |
| READONLY |  | N | Cláusula opcional, quando usada informa ao componente que, mesmo ao ganhar foco, o modo de edição dos dados não deve ser habilitado. O conteúdo pode até ser selecionado e copiado da interface, mas não será editado. |
| VALID <cbValid> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código com retorno booleano, a ser executado no momento da perda de foco do componente. A função ou expressão de validação deve retornar .T. (verdadeiro) caso o foco possa sair deste componente. Normalmente usada para validação dos dados de entrada. |
| NOBORDER | NO BORDER |  | N | Quando informada, esta cláusula define que o componente será criado sem borda na interface. Por padrão ele é criado com borda. |
| NO VSCROLL |  | N | Quando informada, esta cláusula define que o componente não permitirá rolagem vertical – como por exemplo colocar mais linhas de texto do que é possível visualizar na interface. Por padrão a barra de rolagem vertical é habilitada automaticamente ao serem inseridas mais linhas do que a altura do componente na interface é capaz de mostrar. |

### Classe usada pelo comando

O comando @ .. GET MULTILINE é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TMULTIGET()** e seu método construtor **NEW().**

### Referências

### Exemplo

text1Exemplo do comando @ ... GET MULTILINEtrue

### Resultado
