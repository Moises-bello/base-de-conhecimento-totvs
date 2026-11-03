---
content_hash: 5051b624c43d3c45be60b261c260cdc7d960a86c64589cf764c5d1c6490ec1a5
fetched_at: '2026-06-29T00:09:09.131762+00:00'
page_id: '392500243'
product: rm
source: tdn-rm
title: DSAUGHSCC-1307 DT PROCESSAMENTO DO MAPA, REQUISIÇÃO POR REQUISIÇÃO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=392500243
version: 3
---

##### PROCESSAMENTO DO MAPA DE DISPENSAÇÃO, REQUISIÇÃO POR REQUISIÇÃO

##### Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Mapa de Dispensação | |
| **Parâmetro(s):** | Processa o mapa, requisição por requisição |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZMOVIESTOQUE, SZMOVIESTOQUEITEM, SZAPRAZAMENTO |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria no processamento do mapa de dispensação, visa melhorar a concorrência de processamento de mais de um mapa ao mesmo tempo, por usuários diferentes. Com o parâmetro marcado, o sistema processará cada requisição individualmente. Caso ocorra algum erro ou validação em determinada requisição do mapa, as demais requisições não serão impactadas. Com isso, somente as requisições com erros é que precisarão ser ajustadas e processadas novamente.

Com o parâmetro desmarcado, significa que o processamento das requisições do mapa devem ocorrer sem erros. Caso ocorra algum erro, o processamento é parado, a mensagem é exibida e nenhuma requisição terá afetado o estoque e nem ocorrerá o lançamento na conta do paciente.

### Este parâmetro faz sentido quando **não** se utiliza a dispensação horária por requisição, onde ocorre o processamento total de um mapa.

## Procedimento para Utilização

1. Acesse o menu Opções / Parâmetros / Parâmetros Gerais, seleciona a página Estoques II, no agrupador "Mapa/Painel de Dispensação", marque o parâmetro "Processa o mapa requisição por requisição"
2. Acesse o menu Estoques / Mapa de Dispensação
   1. Selecione o filtro desejado
   2. Selecione os itens para gerar o mapa.
   3. Selecione um paciente e confirme os itens
3. Após confirmar os itens, processe o mapa
4. Para cada etapa será exibida o que o sistema está fazendo.
5. Durante o processamento, caso ocorram erros, o sistema prosseguirá para a próxima requisição e somente exibirá todas as mensagens no final do processo
