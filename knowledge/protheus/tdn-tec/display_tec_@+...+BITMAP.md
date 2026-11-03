---
content_hash: 57ed0dbfa8c86444449fdce023c190e34336158343fd269d5992b7bb6c6532dc
fetched_at: '2026-07-02T19:24:24.996058+00:00'
page_id: '494960769'
product: protheus
source: tdn-tec
title: '@ ... BITMAP'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+BITMAP
version: 3
---

Comando @ ... BITMAP

### Sintaxe Mínima

```
@ <nRow>,<nCol> BITMAP RESOURCE <cResName>  
@ <nRow>,<nCol> BITMAP FILE <cFileName>
```

### Sintaxe Completa

```
@ <nRow>, <nCol> BITMAP [ <oBmp> ]  
   [ NAME | RESNAME | RESOURCE <cResName ]   
   [ FILE | FILENAME | DISK <cFileName ]  
   [ NOBORDER ]   
   [ SIZE <nWidth>,<nHeight> ]   
   [ OF | WINDOW | DIALOG <oWnd> ]  
   [ ON CLICK | ON LEFT CLICK <bClick> ]     
   [ ON RIGHT CLICK <bRClick> ]    
   [ SCROLL ]  
   [ ADJUST ]  
   [ CURSOR <oCursor> ]  
   [ PIXEL ]  
   [ WHEN <bWhen>]   
   [ VALID <bValid> ]
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
| BITMAP |  | S | Cláusula obrigatória, identifica o comando |
| <oBmp> | O | N | Podemos especificar um nome de variável AdvPL no qual o objeto do componente tBITMAP() será armazenado. Deve ser utilizado caso seja necessário alterar propriedades do objeto após criado. |
| NAME | RESNAME | RESOURCE <cResName> | C |  | Expressão caractere opcional, pode ser constante ou variável, indica o nome do resource (imagem gravada no repositório de objetos) que deve ser exibido no componente. |
| FILE | FILENAME | DISK <cFileName> | C |  | Expressão caractere, constante ou variável, deve conter o nome do arquivo no disco – a partir do RootPath do ambiente – a ser mostrado pelo componente. Não é necessário especificar esta informação no construtor, a imagem pode ser carregada posteriormente pelo método Load(). O tipo ou formato da imagem suportada está documentado na |
| NOBORDER |  | N | Cláusula opcional, permite especificar que não deve ser desenhada uma borda no componente da imagem. |
| SIZE <nWidth>,<nHeight> | N | N | Permite opcionalmente definir um tamanho da área a ser ocupada pelo componente na interface, especificando o comprimento e a altura como variáveis ou constantes numéricas. |
| OF | WINDOW | DIALOG <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel, folder) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| ON CLICK | ON LEFT CLICK <cbClick> | C | N | Expressão utilizada pelo comando para montar um bloco de código a ser executado caso o usuário realize um clique com o botão esquerdo do mouse sobre a imagem. Não pode ser chamado um CodeBlock, deve ser informada uma função a ser executada de forma literal. |
| ON RIGHT CLICK <cbRClick> | C | N | Expressão similar a especificada na cláusula ON CLICK, porém somente será executada caso a imagem receba um clique com o botão direito do mouse. |
| SCROLL |  | N | Quando informado, indica ao componente que ele está habilitado a habilitar as barras de rolagem lateral e inferior, caso a imagem carregada não caiba no espaço definido para o componente na interface. |
| ADJUST |  | N | Quando informado, permite ajustar a imagem (*stretch*) ao espaço reservado ao componente na interface. Dependendo da relação entre o tamanho real da imagem e do espaço definido para o componente, a imagem pode ficar distorcida. |
| CURSOR <oCursor> | O | N | Cláusula opcional, permite informar um objeto AdvPL do tipo TCursor(), para que seja possível trocar o ponteiro do mouse quando ele estiver sobre a imagem. |
| PIXEL |  | N | Cláusula opcional, quando uma delas for especificada, indica que o sistema de coordenadas usado nos parâmetros <nRow> e <nCol> são em pixels (ou pontos) a partir da coordenada superior esquerda (0,0) do componente visual pai em uso no qual o objeto será posicionado. |
| WHEN <cbWhen> | C | N | Cláusula opcional, permite especificar uma função com retorno booleano, executada a cada troca de foco na interface, para determinar se a imagem atual permite aceitar um evento de clique. |
| VALID <cbValid> | C | N | Cláusula opcional, permite especificar uma função com retorno booleano a ser executada quando o componente – caso habilitado para receber foco – permita a saída do foco do mesmo. |

### Classe usada pelo comando

O comando @ .. BITMAP é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TBITMAP()** e seu método construtor **NEW().**

Algumas propriedades adicionais podem ser definidas através da alteração de propriedades do objeto após a sua criação, como por exemplo transparência. Consulte a documentação da  para maiores detalhes.

### Referências

### Exemplo

text1Exemplo do comando @ ... SAY true
