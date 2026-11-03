---
content_hash: 5fb29b75b4eacb8f9c5177eb4bcb6c7651f4211aac076abcadb6de588c05800c
fetched_at: '2026-06-29T00:08:40.172964+00:00'
page_id: '286212569'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-37 DT Cancelamento de remessa na bolsa retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUINTEGRACOES-37+DT+Cancelamento+de+remessa+na+bolsa+retroativa
version: 104
---

# CANCELAMENTO DE REMESSA PARA BOLETOS EM ABERTO E REMETIDOS ATRAVÉS DO PROCESSO DE BOLSA RETROATIVA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | **RM.** |
| **Segmento:** | *Educacional.* |
| **Módulo:** | **Totvs Educacional.** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Bolsa Retroativa* | **Bolsa Retroativa** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de bolsas** | **Cadastro de bolsas** | | **Cancelamento de remessa** | **Cancelameto de remessa** | | **Regeração de lançamentos financeiros** | **Regeração de lançamentos financeiros** | |
| **Cadastros Iniciais:** | *Alunos Cursos / Habilitações dos Alunos (Ensino Superior) Serviços Bolsas Bolsas por período letivo Contratos Parcelas* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *N/A* |
| **País(es):** | *Todos os países* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Afim de permitir que o processo de bolsa retroativa seja concluído com sucesso para quando a parcela do aluno tiver um boleto em aberto e registro ou remetido, foi criada uma parametrização no processo de bolsa retroativa que faz com que o processo cancele automaticamente a remessa do boleto no sistema financeiro. Assim, o processo de bolsa retroativa concluirá com sucesso para esses casos. Uma vez que boleto tiver a sua remessa cancelada no sistema financeiro será necessário a geração de uma remessa de alteração para que os boletos sejam atualizados no banco.  

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado.

## Atualizações na base de dados

N/A

## Alterações em telas e funcionalidades

1. Criação da aba remessa válido apenas para o modelo antigo de bolsa retroativa. Dentro da aba remessa foi criado uma campo para permitir que o processo de bolsa retroativa cancele a remessa de boletos em aberto automaticamente.

## Vídeo

* *Vídeo hospedado no youtube e inserido no template por meio da macro **Widget Connector**.*

*\*\* Canal do youtube e software de vídeoem definição.*

|  |  |
| --- | --- |
| **Título do Vídeo:** | *Disponibilizado pelo Marketing.* |
| **Introdução:** | *Disponibilizado pelo Marketing.* |
| **Passo a Passo:** | *Capturar diretamente do sistema.* |
| **Finalização:** | *Disponibilizado pelo Marketing.* |

divs
