---
content_hash: c34328c7cf2f7cc28cec5c147dc409ca3998b3ca5f3e504df84d6743f9e86d68
fetched_at: '2026-07-02T19:24:19.748389+00:00'
page_id: '244421865'
product: protheus
source: tdn-tec
title: TWebEngine:New
type: documentation
url: https://tdn.totvs.com/display/tec/TWebEngine%3ANew
version: 10
---

Construtor TWebEngine:New

# Construtor TWebEngine:New

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oWnd | objeto | Indica a janela ou controle visual onde o objeto será criado. |  |  |
| nRow | numérico | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nCol | numérico | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| nWidth | numérico | Indica a largura em pixels do objeto. |  |  |
| nHeight | numérico | Indica a altura em pixels do objeto. |  |  |
| cUrl | caractere | Indica a URL a ser executada, em schemas como: http:// https:// ou file:// |  |  |
| nPort | numérico | Porta do WebSocket para comunicação entre o Navegador e o SmartClient |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TWebEngine |

Importante - SmartClient HTML

Por motivos de segurança, o browser não permite navegação para um arquivo local dentro de um iframe, portanto não é possível utilizar file:// no parâmetro cUrl quando utilizamos o SmartClient HTML.

#### Exemplo

cppEclipsetruefalse
