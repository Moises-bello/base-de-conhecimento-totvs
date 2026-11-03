---
content_hash: 2697eb3cab7f29079a7533f2bc3dd26e0d5a3f32010684887343866c56325567
fetched_at: '2026-07-02T19:24:18.960600+00:00'
page_id: '223157707'
product: protheus
source: tdn-tec
title: Construtor TDialog:New
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TDialog%3ANew
version: 4
---

Construtor TDialog:New

# Construtor TDialog:New

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| nTop | numérico | Indica a coordenada vertical superior em pixels ou caracteres. |  |  |
| nLeft | numérico | Indica a coordenada horizontal esquerda em pixels ou caracteres. |  |  |
| nBottom | numérico | Indica a coordenada vertical inferior em pixels ou caracteres. |  |  |
| nRight | numérico | Indica a coordenada horizontal direita em pixels ou caracteres. |  |  |
| cCaption | caractere | Indica o título da janela. |  |  |
| uParam6 | qualquer | Compatibilidade. |  |  |
| uParam7 | qualquer | Compatibilidade. |  |  |
| uParam8 | qualquer | Compatibilidade. |  |  |
| uParam9 | qualquer | Compatibilidade. |  |  |
| nClrText | numérico | Indica a cor do texto. |  |  |
| nClrBack | numérico | Indica a cor de fundo. |  |  |
| uParam12 | qualquer | Compatibilidade. |  |  |
| oWnd | objeto | Indica a janela mãe (principal) da janela que será criada. O padrão é a janela principal do programa. |  |  |
| lPixel | lógico | Indica se considera as coordenadas passadas em pixels (.T.) ou caracteres (.F.). |  |  |
| uParam15 | qualquer | Compatibilidade. |  |  |
| uParam16 | qualquer | Compatibilidade. |  |  |
| uParam17 | qualquer | Compatibilidade. |  |  |
| nWidth | numérico | Indica a largura da janela em pixels. |  |  |
| nHeight | numérico | Indica a altura da janela em pixels. |  |  |
| lTransparent | lógico | Se .T. permitira que a Dialog receba um fundo transparente. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TDialog |

trueObservações

* Para utilização da propriedade lTransparent é necessário definir a Dialog sem bordas, utilizando a função nOR, conforme exemplo abaixo:

  cppEclipsetruefalse
* A propeidade lTransparente só funciona para rotinas executadas como programa inicial, fora da interface do ERP.
* As propriedades "nTop", "nLeft", "nBottom", "nRight", "nWidth", "nHeight" são limitadas a utilização de janelas fora de uma [TWorkSpace](https://tdn.totvs.com/display/tec/TWorkSpace). Dentro de uma tWorkSpace a posição e tamanho devem ser informadas no "ON INIT" pelo método [SetCoors](https://tdn.totvs.com/display/tec/TSrvObject%3ASetCoors):

## Exemplos

cppEclipsetruefalse
