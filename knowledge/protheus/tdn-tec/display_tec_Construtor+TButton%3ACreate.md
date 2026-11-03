---
content_hash: bb5e742c52ea2736fce2653563ad93159775197d1ada5d0463f2de0083096cd5
fetched_at: '2026-07-02T19:24:18.774131+00:00'
page_id: '221544545'
product: protheus
source: tdn-tec
title: Construtor TButton:Create
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TButton%3ACreate
version: 1
---

Construtor TButton:Create

# Construtor TButton:Create

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oWnd | objeto | Indica a janela ou controle visual onde o botão será criado. |  |  |
| nRow | numérico | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nCol | numérico | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| cCaption | caractere | Indica o título do botão. |  |  |
| bAction | bloco de código | Indica o bloco de código que será executado quando clicar, com o botão esquerdo do mouse, sobre o botão. |  |  |
| nWidth | numérico | Indica a largura em pixels do botão. |  |  |
| nHeight | numérico | Indica a altura em pixels do botão. |  |  |
| uParam8 | numérico | Compatibilidade. |  |  |
| oFont | objeto | Indica o objeto do tipo TFont utilizado para definir as características da fonte aplicada na exibição do título do botão. |  |  |
| uParam10 | lógico | Compatibilidade. |  |  |
| lPixel | lógico | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| uParam12 | lógico | Compatibilidade. |  |  |
| cMsg | caractere | Indica a mensagem, do tipo dica de contexto (tooltip/hint), ao posicionar o ponteiro do mouse sobre o botão. |  |  |
| uParam14 | lógico | Compatibilidade. |  |  |
| bWhen | bloco de código | Indica o bloco de código que será executado quando a mudança de foco da entrada de dados, na janela em que o controle foi criado, estiver sendo efetuada. Observação: O bloco de código retornará verdadeiro (.T.), se o controle permanecer habilitado; caso contrário, retornará falso (.F.). |  |  |
| bValid | bloco de código | Indica o bloco de código de validação que será executado quando o conteúdo do objeto for modificado. Retorna verdadeiro (.T.), se o conteúdo é válido; caso contrário, falso (.F.). |  |  |
| uParam17 | lógico | Compatibilidade. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TButton |

## Exemplos

cppEclipseExemplo 1truefalse
