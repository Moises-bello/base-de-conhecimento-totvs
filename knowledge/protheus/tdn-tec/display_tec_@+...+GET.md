---
content_hash: 4c8488407cbd1710f405fd3423b3b6a16c606a84a434f0d8e6487005b3c3965b
fetched_at: '2026-07-02T19:24:25.018398+00:00'
page_id: '494976243'
product: protheus
source: tdn-tec
title: '@ ... GET'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+GET
version: 3
---

Comando @ ... GET

### Sintaxe Mínima

```
@ <nRow>,<nCol> GET <uVar>
```

### Sintaxe Completa

```
@ <nRow>, <nCol> GET [ <oGet> VAR ] <uVar>   
   [ OF | WINDOW | DIALOG <oWnd> ]  
   [ PICTURE <cPict> ]   
   [ VALID <cbValid> ]  
   [ COLOR,COLORS <nClrText> [,<nClrBack> ] ]  
   [ SIZE <nWidth>, <nHeight> ]  
   [ FONT <oFont> ]   
   [ PIXEL | PIXELS ]   
   [ WHEN <cbWhen> ]  
   [ ON CHANGE <cbChange> ]  
   [ READONLY ]  
   [ PASSWORD ]
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
| <oGet>VAR |  | N | Quando a cláusula VAR for informada, permite e obriga a especificar um nome de variável AdvPL imediatamente antes da cláusula, no qual o objeto do componente tGET() será armazenado, seguido da expressão ou variável caractere cujo conteúdo será mostrado para edição na interface. |
| <uVar> | C | S | Indica o nome da variável cujo conteúdo será editado na interface. Pode ser do tipo "C" Caractere, "N" Numérico ou "D" Data. |
| OF | WINDOW | DIALOG <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel, folder) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| PICTURE <cPict> | C | N | Cláusula opcional, quando especificada exige que seja informada uma expressão caractere, constante ou variável, que contenha uma máscara de formatação de entrada de dados para o conteúdo a ser editado. Para mais informações sobre como criar uma picture ou máscara de exibição, consulte a documentação sobre pictures de formatação e edição na TDN. |
| VALID <cbValid> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código com retorno booleano, a ser executado no momento da perda de foco do componente. A função ou expressão de validação deve retornar .T. (verdadeiro) caso o foco possa sair deste componente. Normalmente usada para validação dos dados de entrada. |
| COLOR | COLORS <nClrText> [ ,<nClrBack] | N | N | Cláusulas opcionais, que quando especificadas, permitem alterar a cor do texto da mensagem a ser exibida pelo componente, e opcionalmente também permite alterar a cor de fundo do texto da exibição. |
| SIZE <nWidth>,<nHeight> | N | N | Cláusula opcional, quando utilizada deve ser seguida dos parâmetros numéricos <nWidth> e <nHeight>, que respectivamente indicam o comprimento e a altura do componente na interface. |
| FONT <oFont> | O | N | Cláusula opcional, permite informar um objeto AdvPL do tipo TFont(), para que seja possível mostrar o texto no componente usando uma fonte diferente da fonte default do ambiente. |
| PIXEL | PIXELS |  | N | Cláusula opcional, quando uma delas for especificada, indica que o sistema de coordenadas usado nos parâmetros <nRow> e <nCol> são em pixels (ou pontos) a partir da coordenada superior esquerda (0,0) do componente visual pai em uso no qual o objeto será posicionado. Embora ambas sejam suportadas (PIXEL ou PIXELS), esta é uma particularidade deste componente. Por questões de padronização de código, recomenda-se que seja usada quando desejável apenas a clausula PIXEL |
| WHEN <cbWhen> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código com retorno booleano, a ser executado no momento de troca de foco de componentes da interface. A função ou expressão de validação deve retornar .T. (verdadeiro) caso o componente possa receber foco. |
| ON CHANGE <cbChange> | C | N | Expressão caractere, que será utilizada para gerar um bloco de código a ser executado quando o estado ou conteúdo do objeto é modificado pela ação sobre o controle visual – ou seja, quando o conteúdo editável da interface for alterado. |
| READONLY |  | N | Cláusula opcional, quando usada informa ao componente que, mesmo ao ganhar foco, o modo de edição dos dados não deve ser habilitado. O conteúdo pode até ser selecionado e copiado da interface, mas não será editado. |
| PASSWORD |  | N | Cláusula opcional, quando usada informa ao componente que cada caractere será representado na interface por um "\*" (asterisco). Normalmente este modo é usado na interface para campos de preenchimento de senhas, ocultando o conteúdo original em edição. |

### Classe usada pelo comando

O comando @ .. GET é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TGET()** e seu método construtor **NEW().**

### Referências

### Exemplo

text1Exemplo do comando @ ... GETtrue

### Resultado
