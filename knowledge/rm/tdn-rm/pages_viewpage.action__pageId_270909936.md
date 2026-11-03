---
content_hash: b178d68ea63a986d54e2349e50723c894d090819022a5bb4b3c5bedd28057da8
fetched_at: '2026-06-29T00:08:25.029723+00:00'
page_id: '270909936'
product: rm
source: tdn-rm
title: TVEZKM MCP-162 DT Enviar CTe sem Informação Veículo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270909936
version: 119
---

# ENVIAR CTe SEM INFORMAÇÃO DO VEÍCULO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Totvs Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CTE006.* | *CT-E - ENVIO DE EVENTO.* | |
| **Tickets relacionados** | TVEZKM |
| **Requisito (informe o requisito relacionado):** | MOV000159 - Conhecimento de Transporte - CTRC e CT-e |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *DFILIAL* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementação do campo Lotação no movimento, para permitir que o sistema envie CT-e sem veículo (Lotação = 0)

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.13.135 deste chamado.

## Procedimento para Utilização

       1.            Campo novo criado no Movimento (Etapa Transporte - Transportadora ) para permitir informar a lotação

       2.            Caso esse campo esteja desmarcado, é necessário informar  o campo "Registro nacional de Transportador de Carga (ANTT) " no anexo de "Dados Fiscais" do cadastro de Filiais.

       3.            Caso no movimento esse parâmetro esteja desmarcado o sistema irá enviar o CT-e sem informar as tags de veículos.

divs
