---
content_hash: c99c4dc6f4de984c82f02667a2b1418c61e8b599c461c82b7db995b25d05288a
fetched_at: '2026-07-02T19:24:18.821423+00:00'
page_id: '221546350'
product: protheus
source: tdn-tec
title: Construtor TCheckBox:New
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TCheckBox%3ANew
version: 2
---

Construtor TCheckBox:New

# Construtor TCheckBox:New

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nRow | numeric | Indica a coordenada vertical. |  |  |
| nCol | numeric | Indica a coordenada horizontal. |  |  |
| cCaption | character | Indica o título do objeto. |  |  |
| bSetGet | codeblock | Indica o bloco de código que será executado quando o componente for marcado ou desmarcado, normalmente é utilizado para alterar uma variável lógica que representará o estado do componente. |  |  |
| oDlg | object | Indica a janela ou controle visual onde o objeto será criado. |  |  |
| nWidth | numeric | Indica a largura do objeto. |  |  |
| nHeight | numeric | Indica a altura do objeto. É estipulada uma altura padrão para o objeto de 21 pixels, somente sendo possível sua alteração através da aplicação de estilo, utilizando o método SetCss, devidamente documentado no TDN. |  |  |
| uParam8 | numeric | Compatibilidade. |  |  |
| bLClicked | codeblock | Indica o bloco de código que será executado quando clicar, com o botão esquerdo do mouse, sobre o objeto. |  |  |
| oFont | object | Indica o objeto do tipo TFont utilizado para definir as características da fonte aplicada na exibição do conteúdo do controle visual. |  |  |
| bValid | codeblock | Indica o bloco de código de validação que será executado quando o foco sair do componente atual para outro. Caso o bloco retorne verdadeiro (.T.) o foco é trocado para o outro componente, e caso retorne falso (.F.) o foco não é trocado e continua no componente atual. |  |  |
| nClrText | numeric | Indica a cor do texto da janela. |  |  |
| nClrPane | numeric | Indica a cor de fundo da janela. |  |  |
| uParam14 | logical | Compatibilidade. |  |  |
| lPixel | logical | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| cMsg | character | Indica a mensagem, do tipo dica de contexto (tooltip/hint), que será apresentada ao posicionar o ponteiro do mouse sobre o objeto. |  |  |
| uParam17 | logical | Compatibilidade. |  |  |
| bWhen | codeblock | Indica o bloco de código que será executado quando o componente receber ou perder foco. Caso o bloco retorne verdadeiro (.T.) o componente ficará habilitado para edição, e caso retorne falso (.F.) o componente ficará desabilitado para edição. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | object | Nova instância da classe TCheckBox |

## Exemplos

cppEclipsetruefalse
