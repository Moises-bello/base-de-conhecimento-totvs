---
content_hash: 3d72ba56ac22c97e1499ca566f8171215527bb269022be11b0d59880a7e390de
fetched_at: '2026-06-29T00:08:24.834309+00:00'
page_id: '270906545'
product: rm
source: tdn-rm
title: 330983_DT_Atualização_Capa_Lote_Visão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270906545
version: 113
---

# astro de Lote

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Atualização de datas e valores da capa do lote* | *Atualização de datas e valores da capa do lote* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Cadastro de Lotes* | *Cadastro de Lotes* | |  |  | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | 330983 |
| **Requisito (informe o requisito relacionado):** | N/A |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** |  |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** |  |

## Descrição

Melhoria no cálculo e atualização dos valores capa do lote para que o sistema não realize o cálculo automaticamente ao abrir a visão, pois para alguns clientes estas informações não são utilizadas e os mesmos estavam reclamando de um delay ao abrir a tela.

Foi criado o parâmetro “Não calcular/atualizar capa do lote automaticamente ao abrir a visão de lotes”, ao marcar este parâmetro, o sistema não irá realizar o cálculo automaticamente da capa do lote ao abrir a visão de dados, e para este cenário será disponibilizado na tela uma opção que permite ao usuário acionar um botão que realiza o cálculo dos lotes selecionados.

Para os clientes que necessitam que os valores sejam calculados automaticamente foi realizado também uma melhoria na lógica para que em alguns cenários o cálculo seja aplicado somente para os lotes selecionados.

## Procedimento para Utilização

Modifique os parâmetros do sistema

Acessando a visão de lotes

A visão de lote terá o seguinte comportamento:

**1º Para os lotes em que a opção "Digitar Capa" está marcada:**

O sistema apresentará apenas as informações que são fixadas pelo usuário ao cadastrar o lotes (valor, data inicial e data final), a informações que são calculadas (total de créditos e débitos) serão apresentadas somente se o usuário acionar o botão de calcular.

**2º Para os lotes em que a opção "Digitar Capa" não está marcada:**

Os campos que são calculados (data inicial, data final, total débitos e créditos, valor soma) serão apresentados em branco e seus valores serão mostrados somente se o usuário acionar o botão de calcular.

Calculando valores da capa do lote

Ao acionar o botão destacado abaixo, o sistema realizará o calculo das informações dos lotes selecionados.

divs
