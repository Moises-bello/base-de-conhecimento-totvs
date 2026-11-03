---
content_hash: 3542cc6a81da5e7703f4df93074dea6b53a1cda4b0d1466d2e62d05242a5719d
fetched_at: '2026-07-02T19:24:24.915730+00:00'
page_id: '490971284'
product: protheus
source: tdn-tec
title: '@ ... SAY'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+SAY
version: 6
---

Comando @ ... SAY

### Sintaxe Mínima

```
@ <nRow>,<nCol> SAY <cText>
```

### Sintaxe Completa

```
@ <nRow>, <nCol> SAY [ <oSay> PROMPT | VAR ] <cText>   
   [ PICTURE <cPict> ]   
   [ OF | WINDOW | DIALOG <oWnd> ]   
   [ FONT <oFont> ]   
   [ PIXEL, PIXELS ]   
   [ COLOR | COLORS <nClrText> [,<nClrBack> ] ]   
   [ SIZE <nWidth>, <nHeight> ]   
   [ HTML ]
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
| SAY |  | S | Cláusula obrigatória, pode ser seguida diretamente da expressão caractere – constante ou variável – que deve ser exibida na tela, ou da cláusula opcional PROMPT ou VAR |
| <oSay> PROMPT | VAR |  | N | Quando a cláusula PROMPT ou VAR for informada, permite e obriga a especificar um nome de variável AdvPL imediatamente antes da cláusula, no qual o objeto do componente tSAY() será armazenado, seguido da expressão ou variável caractere que será mostrada pelo componente. |
| <cText> | C | S | Expressão caractere obrigatória, pode ser constante ou variável, indica o conteúdo a ser mostrado no componente. |
| PICTURE <cPict> | C | N | Cláusula opcional, quando especificada exige que seja informada uma expressão caractere, constante ou variável, que contenha uma máscara de exibição para o conteúdo a ser exibido. Para mais informações sobre como criar uma picture ou máscara de exibição, consulte a documentação sobre pictures de formatação na TDN. |
| OF | WINDOW | DIALOG <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel, folder) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| FONT <oFont> | O | N | Cláusula opcional, permite informar um objeto AdvPL do tipo TFont(), para que seja possível mostrar o texto no componente usando uma fonte diferente da fonte default do ambiente. |
| PIXEL | PIXELS |  |  | Cláusula opcional, quando uma delas for especificada, indica que o sistema de coordenadas usado nos parâmetros <nRow> e <nCol> são em pixels (ou pontos) a partir da coordenada superior esquerda (0,0) do componente visual pai em uso no qual o objeto será posicionado. |
| COLOR | COLORS <nClrText> [ ,<nClrBack] | N | N | Cláusulas opcionais, que quando especificadas, permitem alterar a cor do texto da mensagem a ser exibida pelo componente, e opcionalmente também permite alterar a cor de fundo do texto da exibição. |
| SIZE <nWidth>,<nHeight> | N | N | Cláusula opcional, quando utilizada deve ser seguida dos parâmetros numéricos <nWidth> e <nHeight>, que respectivamente indicam o comprimento e a altura do componente na interface. |
| HTML | L | N | Cláusula opcional, quando usada informa ao componente que o texto a ser exibido deve ser tratado como um conteúdo HTML, que pode conter tags HTML de formatação que devem ser interpretadas, e não mostradas efetivamente como conteúdo do texto |

### Classe usada pelo comando

O comando @ .. SAY é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TSAY() e** seu método construtor **NEW().**

### Referências

### Exemplo

text1Exemplo do comando @ ... SAY true

### Resultado
