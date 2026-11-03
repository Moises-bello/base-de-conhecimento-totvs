---
content_hash: 3e89d6a702625c7e1dbc5f6c57bc51cef3fa21c0a0664dc9fabb289755e5e7b4
fetched_at: '2026-06-29T00:08:33.493579+00:00'
page_id: '274323168'
product: rm
source: tdn-rm
title: 730511 FOPCALCULO01-251 - Calcular Recibo de Ferias Automatico
type: documentation
url: https://tdn.totvs.com/display/LRM/730511+FOPCALCULO01-251+-+Calcular+Recibo+de+Ferias+Automatico
version: 116
---

# CALCULAR RECIBO DE FÉRIAS AUTOMÁTICO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Rotina:** | |  | | --- | | **Rotina** | | Calcular Recibo de Férias Automático |  |  | | --- | | **Rotina(s) envolvida(s)** | | Período de Gozo de Férias | |
| **Cadastros Iniciais:** | O parâmetro já vem como default habilitado. Se precisar parar de calcular automaticamente será necessário desmarcar o parâmetro. |
| **Parâmetro(s):** | * Configurações > Parametrizador   + 06.01 - Folha de Pagamento     - 06.01.04 - Férias       * Cálculo         + Calcular Recibo de Férias Automaticamente |
| **Tickets relacionados** | 730511 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FOPCALCULO01-251 |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | SQL SERVER® e Oracle® |
| **Tabelas Utilizadas:** |  |

## Descrição

Esta implementação visa possibilitar a autonomia ao cliente que deseje que não seja calculado automaticamente as férias quando acessar o Recibo e fechar.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado;

## Procedimento para Configuração

Para configurar basta seguir os passos de configuração de parâmetros abaixo:

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **parametrizador**do RM acesse:
   * Configurações > Parametrizador
     + 06.01 - Folha de Pagamento
       - 06.01.04 - Férias

Marque ou desmarque a opção 'Calcular Recibo de Férias Automaticamente' de acordo com sua regra e conclua o processo.

## Procedimento para Utilização

* Acesse o Funcionário.

* Acesse o Anexo 'Movimento > Período Aquisitivo' e selecione o período.

* Acesse a aba 'Período de Gozo' e selecione o período.

* Acesse o 'Visualizar Recibo'.

Ao clicar em 'OK' ou 'Salvar', se o parâmetro estiver habilitado irá fazer o cálculo automaticamente, caso esteja desabilitado o cálculo não será executado.

divs
