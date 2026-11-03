---
content_hash: 2dd3ef48cbf1fecc43f0ed9fcca269ea0761f46cfec9afd51082da5b4ea56357
fetched_at: '2026-06-29T00:08:40.224641+00:00'
page_id: '286220473'
product: rm
source: tdn-rm
title: DT CNAB STATUS PENDENTE REMESSA
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+CNAB+STATUS+PENDENTE+REMESSA
version: 107
---

# Novo valor para status de remessa para boletos 'Pendente Remessa'.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | FIN000087 | *Integração Bancária* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | FIN000268 | Boleto | |
| **Cadastros Iniciais:** | *Inclusão de Boleto* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5FINANCEIRO01-1715 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *FBOLETO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Inclusão de um novo valor para o campo 'Status de Remessa' - (FBOLETO.CNABSTATUS)

Este status será responsável por identificar Boletos que já passaram por remessa e que tiveram sua remessa cancelada e/ou sofreu alguma alteração no sistema e que criará a necessidade do reenvio da remessa.

#### Status de Remessa para os boletos

0 - Não Remetido;

1 - Remetido;

2 - Registrado;

3 - Recusado;

4 - Baixado;

5 - Registrado Online;

6 - Cancelado;

7 - **Pendente Remessa.**

## Procedimento para Implantação

Á funcionalidade estará disponível a partir da versão 12.1.17.120 ou superior e 12.1.18.1

|  |  |
| --- | --- |
| **Nome da Variável:** | *CNABSTATUS* |
| **Tipo:** | *INTEIRO* |
| **Descrição:** | *Status da remessa* |
| **Valor Padrão:** | *0 - Não Remetido* |

## Procedimento para Configuração

* Não existe configuração no sistema para habilitar a funcionalidade, após atualização do sistema para as versões mencionadas o sistema já disponibilizará o novo valor para o campo.

## Procedimento para Utilização

Para os boletos com status da remessa igual a "Remetido" e que haja necessidade de cancelar a remessa junto ao banco, será necessário o reenvio da remessa de cancelamento. Para que atenda a está regra, foi criado o novo status "Pendente Remessa" que tem como objetivo identificar os boletos que tiveram a remessa cancelada dentro do sistema e que ainda necessitam do reenvio da remessa para que sejam atualizados junto ao sistema bancário.

Para boletos que possuam o Status da remessa igual a "Remetido" ao realizar o processo de "Cancelamento Remessa de Boleto" o status do boleto será alterado para "Pendente Remessa" conforme imagem abaixo:

Obs.:

* Para que o status do boleto seja atualizado para "Cancelado", será necessário realizar o retorno de cobrança com o código de retorno "Cancelado";
* Para lançamentos vinculados ao boleto e que possua o status remessa igual a "Remetido", e que necessite realizar baixa manual (parcial ou total) dos lançamentos o Status da remessa do boleto será alterado para "Pendente remessa", pois é necessário reenviar as informações junto ao sistema bancário.

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
