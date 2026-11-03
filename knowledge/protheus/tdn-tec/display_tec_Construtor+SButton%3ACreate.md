---
content_hash: d7599f26733590b00b0b315a7bb5e9abc776048a923d5074a7fbda14a6c47bc3
fetched_at: '2026-07-02T19:24:18.730210+00:00'
page_id: '219697942'
product: protheus
source: tdn-tec
title: Construtor SButton:Create
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+SButton%3ACreate
version: 2
---

Construtor SButton:Create

# Construtor SButton:Create

Método construtor da classe.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oWnd | objeto | Indica a janela ou controle visual onde o botão será criado. |  |  |
| nTop | numérico | Indica a coordenada vertical em pixels ou caracteres. |  |  |
| nLeft | numérico | Indica a coordenada horizontal em pixels ou caracteres. |  |  |
| nType | numérico | Indica a imagem do tipo (Exemplo: 1=OK e 2=Cancelar) de botão que será utilizado. Observação: Estas imagens estão carregadas no Smart Client. Para obter o número de cada tipo de botão, consulte a tabela disponível na área "Observações". |  |  |
| bAction | bloco de código | Indica o bloco de código que será executado quando clicar, com o botão esquerdo do mouse, sobre o botão. |  |  |
| lActive | lógico | Indica se habilita(.T.)/desabilita(.F.) o botão. |  |  |
| cMsg | caractere | Indica a mensagem, do tipo dica de contexto (tooltip/hint), ao posicionar o ponteiro do mouse sobre o botão. |  |  |
| bWhen | bloco de código | Indica o bloco de código que será executado quando a mudança de foco da entrada de dados, na janela em que o controle foi criado, estiver sendo efetuada. Observação: O bloco de código retornará verdadeiro (.T.), se o controle permanecer habilitado; caso contrário, retornará falso (.F.). |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe SButton |

## Observações

## Veja a seguir os tipos de botões carregados no Smart Client que podem ser definidos no parâmetro nType:

| Tipo | Nome da Imagem |
| --- | --- |
| 1 | OK |
| 2 | Cancelar |
| 3 | Excluir |
| 4 | Incluir |
| 5 | Parâmetros |
| 6 | Imprimir |
| 7 | Susp. Impr. |
| 8 | Cancelar Impressão |
| 9 | Ordem |
| 10 | Prioridade |
| 11 | Editar |
| 12 | Ouvir |
| 13 | Salvar |
| 14 | Abrir |
| 15 | Visualizar |
| 16 | Cond. Neg. |
| 17 | Filtrar |
| 18 | Financ. |
| 19 | Avançar |
| 20 | Voltar |
| 21 | Avançar |
| 22 | Voltar |
| 23 | Gráfico |

## Exemplos

cppEclipseExemplo 1truefalse
