---
content_hash: 054f10633209545122dc881485a06ab01d9bdc428be0ca5a31f7f362735a2590
fetched_at: '2026-06-29T00:11:59.890725+00:00'
page_id: '876227991'
product: rm
source: tdn-rm
title: 'Gerenciamento de Recursos nas Atividades do TOTVS Automação de Testes - Linha
  RM: Consumo e Disponibilização'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=876227991
version: 9
---

No **TOTVS Automação de Testes**, os **Recursos das Atividades** são objetos ou serviços que uma atividade pode **receber** (consumir) ou **fornecer** (disponibilizar) para outras atividades, facilitando a integração e reutilização de dados ou funcionalidades durante a execução dos testes.

## Exemplo de Uso

RecursosRecursos

## Recebe

Este campo se refere aos **recursos que uma atividade consome** durante sua execução. Esses recursos podem incluir:

* **Conexões de banco de dados**: Utilizadas para executar consultas ou transações.
* **WebDrivers**: Instâncias de Selenium WebDriver utilizadas para automação de testes em navegadores.
* **Parâmetros de execução**: Valores de entrada que definem como a atividade deve ser executada (ex.: credenciais, URLs).

## Fornece

Este campo se refere aos **recursos que uma atividade disponibiliza** para outras atividades futuras. Os recursos fornecidos podem ser reutilizados dentro do mesmo fluxo de testes, permitindo maior eficiência e integração entre as atividades.

* **Objetos instanciados**: Como um WebDriver configurado, que pode ser reutilizado por atividades subsequentes.
* **Resultados de processamento**: Informações ou resultados gerados pela atividade, que podem ser utilizados em atividades posteriores.

## Lista de Atividades do TOTVS Automação de Testes que Consomem e Disponibilizam Recursos

true
