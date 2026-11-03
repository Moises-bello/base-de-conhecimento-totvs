---
content_hash: 62d3116db701270c8271e27221d48c21c1b985d882960586e1304dbc8c2842a1
fetched_at: '2026-07-02T19:24:25.028376+00:00'
page_id: '496010033'
product: protheus
source: tdn-tec
title: '@ ... FOLDER'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+FOLDER
version: 2
---

Comando @ ... FOLDER

### Sintaxe Mínima

```
@ <nRow>,<nCol> FOLDER <oFolder>
```

### Sintaxe Completa

```
@ <nRow>, <nCol> FOLDER <oFolder>   
   [ OF | WINDOW | DIALOG <oWnd> ]  
   [ PROMPT | PROMPTS | ITEMS <cPrompt,...> ]   
   [ PIXEL ]  
   [ COLOR <nClrText> ]  
   [ OPTION <nOption> ]  
   [ SIZE <nWidth,nHeight> ]  
   [ MESSAGE <cMsg> ]
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
| FOLDER <oFolder> | C | S | Cláusula obrigatória, indica o uso do componente de agrupamento tFolder(). Deve ser sucedido da variável AdvPL a receber o objeto do componente. |
| OF | WINDOW | DIALOG  <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| PROMPT | PROMPTS | ITEMS <cItem1,...> | AC | N | Permite especificar uma ou mais strings, separadas por vírgula, para serem utilizadas como títulos de cada pasta (folder) criado. Internamente as strings separadas por vírgula serão tratadas como um Array. |
| PIXEL |  | N | Cláusula opcional, quando uma delas for especificada, indica que o sistema de coordenadas usado nos parâmetros <nRow> e <nCol> são em pixels (ou pontos) a partir da coordenada superior esquerda (0,0) do componente visual pai em uso no qual o objeto será posicionado. |
| COLOR  <nClrText> | N | N | Cláusula opcional, permite alterar a cor do texto da mensagem a ser exibida pelo componente. Deve ser usada uma expressão numérica, constante ou variável. |
| OPTION <nOption> | N | N | Indica a pasta selecionada na criação do componente. |
| SIZE <nWidth>,<nHeight> | N | N | Parâmetros opcionais, indicam respectivamente o tamanho horizontal e vertical a ser usado pelo componente. Caso não especificados no construtor, devem ser informados posteriormente para a visualização correta do componente. |
| MESSAGE <cMSg> | C | N | Indica a mensagem, do tipo dica de contexto (tooltip/hint), que será apresentada ao posicionar o ponteiro do mouse sobre o objeto. |

* Quando utilizamos o comando TFOLDER para a criação do componente, e informamos o parâmetro PROMPT (ou PROMPTS ou ITEMS), as abas internas de cada folder já são criadas e nomeadas. As abas podem ser acessadas pela propriedade aDialogs, do tipo ARRAY (vetor), onde cada elemento corresponde ao objeto da aba, para ser possível criar os demais componentes visuais dentro das abas desejadas.
* O componente FOLDER pode ser criado "vazio", e posteriormente adicionamos as abas usando o método .

### Classe usada pelo comando

O comando @ .. FOLDER é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TFOLDER()** e seu método construtor **NEW().**

### Referências

### Exemplo

text1Exemplo do comando @ ... FOLDERtrue

### Resultado

* Ambos os programas terão o mesmo resultado
