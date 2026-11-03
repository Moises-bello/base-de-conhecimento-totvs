---
content_hash: 79573061cf8b30dd6d7bef5622812e5a620dc022dd7437711595f16e3eceedb1
fetched_at: '2026-07-02T19:24:25.040087+00:00'
page_id: '496020317'
product: protheus
source: tdn-tec
title: '@ ... MSPANEL'
type: documentation
url: https://tdn.totvs.com/display/tec/@+...+MSPANEL
version: 2
---

Comando @ ... MSPANEL

### Sintaxe Mínima

```
@ <nRow>,<nCol> MSPANEL <oPanel>
```

### Sintaxe Completa

```
@ <nRow>, <nCol> MSPANEL <oPanel>   
   [ PROMPT | VAR <cPrompt> ]   
   [ OF | WINDOW | DIALOG <oWnd> ]  
   [ FONT <oFont> ]  
   [ CENTERED | CENTER ]  
   [ COLOR <nClrText> ]  
   [ SIZE <nWidth,nHeight> ]  
   [ LOWERED ]  
   [ RAISED ]
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
| MSPANEL <oPanel> | O | S | Cláusula obrigatória, indica o uso do componente de agrupamento tPanel(). Deve ser sucedido da variável AdvPL a receber o objeto do componente. |
| PROMPT | VAR <cText> | C | N | Permite especificar uma expressão caractere, constante ou variável, que será usada como título do painel. |
| OF | WINDOW | DIALOG  <oWnd> | O | N | Cláusula opcional, quando informada permite especificar o nome de uma variável AdvPL que contenha o objeto ou componente pai de interface (janela ou diálogo, painel) onde o componente deve ser exibido. Caso seja omitida, o componente será criado na janela ou diálogo ativos no momento. Embora todas as cláusulas sejam suportadas (OF, DIALOG ou WINDOW), por questões de padronização de código, recomendamos o uso da cláusula OF – pois um componente de interface não necessariamente têm seu componente pai definido como uma caixa de diálogo, qualquer outro componente de agrupamento ou *container* pode ser utilizado – como um tPanel, tFolder, etc. |
| FONT <oFont> | O | N | Permite especificar uma fonte diferenciada, que será a fonte padrão dos componentes dentro do painel. |
| CENTERED | CENTER |  | N | Indica que, quando especificado um título do painel através da opção PROMPT ou VAR, este título deve ser exibido centralizado no componente. Por padrão o título é exibido no canto superior esquerdo da área interna do painel. |
| COLOR | COLORS  <nClrText> ,[,<nClrBack>] | N | N | Cláusula opcional, permite alterar a cor do texto da mensagem a ser exibida pelo componente. Deve ser usada uma expressão numérica, constante ou variável. Opcionalmente também especificar a cor de fundo do painel. |
| SIZE <nWidth>,<nHeight> | N | N | Parâmetros opcionais, indicam respectivamente o tamanho horizontal e vertical a ser usado pelo componente. Caso não especificados no construtor, devem ser informados posteriormente para a visualização correta do componente. |
| LOWERED\* |  | N | Indica que o painel será desenhado com uma borda do lado direito e borda inferior |
| RAISED |  | N | Indica que o painel será desenhado com uma borda do lado esquerdo e borda superior |

* O componente MSPANEL (tPanel) é um componente de agrupamento ou "container" de componentes. Logo, podemos utilizá-lo como o componente superior ao usarmos outros componentes de interface, como SAY, GET, BUTTON, etc.
* Este componente pode ser alinhado dinamicamente usando a área do seu componente superior, usando a propriedade **ALIGN** da classe hierarquicamente superior **TCONTROL**.. Para maiores detalhes, consulte a propriedade

### Classe usada pelo comando

O comando @ .. MSPANEL é traduzido em tempo de compilação para utilizar a classe de interface visual do AdvPL **TPANEL()** e seu método construtor **NEW().**

### Referências

### Exemplo

text1Exemplo do comando @ ... MSPANELtrue

### Resultado
