---
content_hash: 858fa396f1cab19e8084ac710450600983994e7022b21316439a82442fa6e9d5
fetched_at: '2026-07-02T19:24:18.811433+00:00'
page_id: '221546347'
product: protheus
source: tdn-tec
title: Construtor TCheckBox:Create
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TCheckBox%3ACreate
version: 2
---

Construtor TCheckBox:Create

# Construtor TCheckBox:Create

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oWnd | object | Indica a janela ou controle visual onde o objeto será criado. |  |  |
| bSetGet | codeblock | Indica o bloco de código que será executado quando o componente for marcado ou desmarcado, normalmente é utilizado para alterar uma variável lógica que representará o estado do componente. |  |  |
| nRow | numeric | Indica a coordenada vertical. |  |  |
| nCol | numeric | Indica a coordenada horizontal. |  |  |
| cCaption | character | Indica o título do objeto. |  |  |
| nWidth | numeric | Indica a largura do objeto. |  |  |
| nHeight | numeric | Indica a altura do objeto. É estipulada uma altura padrão para o objeto de 21pixels, somente sendo possível sua alteração através da aplicação de estilo, utilizando o método SetCss, devidamente documentado no TDN. |  |  |
| uParam8 | numeric | Compatibilidade. |  |  |
| bChange | codeblock | Indica o bloco de código que será executado quando o estado ou conteúdo do objeto é modificado pela ação sobre o controle visual. |  |  |
| oFont | object | Indica o objeto do tipo TFont utilizado para definir as características da fonte aplicada na exibição do conteúdo do controle visual. |  |  |
| bValid | codeblock | Indica o bloco de código de validação que será executado quando o foco sair do componente atual para outro. Caso o bloco retorne verdadeiro (.T.) o foco é trocado para o outro componente, e caso retorne falso (.F.) o foco não é trocado e continua no componente atual. |  |  |
| nClrFore | numeric | Indica a cor do texto da janela. |  |  |
| nClrBack | numeric | Indica a cor de fundo da janela. |  |  |
| uParam14 | logical | Compatibilidade. |  |  |
| lPixel | logical | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| cMsg | character | Indica a mensagem, do tipo dica de contexto (tooltip/hint), que será apresentada ao posicionar o ponteiro do mouse sobre o objeto. |  |  |
| uParam17 | logical | Compatibilidade. |  |  |
| bWhen | codeblock | Indica o bloco de código que será executado quando o componente receber ou perder foco. Observação: Caso o bloco retorne verdadeiro (.T.) o componente ficará habilitado para edição, e caso retorne falso (.F.) o componente ficará desabilitado para edição. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | object | Nova instância da classe TCheckBox |

## Exemplos

cppEclipsetruefalse
