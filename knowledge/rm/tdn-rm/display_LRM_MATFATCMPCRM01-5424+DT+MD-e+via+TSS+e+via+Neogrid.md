---
content_hash: 6a8df3b674f023ab0f9517df9f886fe21584d2a3981567553a807f6af55d5a5f
fetched_at: '2026-06-29T00:09:12.040988+00:00'
page_id: '415705801'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-5424 DT MD-e via TSS e via Neogrid
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-5424+DT+MD-e+via+TSS+e+via+Neogrid
version: 2
---

# Operações de MD-e serem realizadas tanto por TSS, quanto por Neogrid, respeitando a parametrização da Filial

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MDE.001 | SINCRONISMO DE DOCUMENTOS | |
| **Cadastros Iniciais:** | . |
| **Parâmetro(s):** | . |
| **Ponto de Entrada:** | . |
| **Tickets relacionados** | MATFATCMPCRM01-5424 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-5424 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TMDE |
| **Sistema(s) Operacional(is):** | . |
| **Pacote:** | . |

## Descrição

Implementação do sincronismo de MD-e para somente utilizar o NeoGrid quando estiver parametrizado explicitamente nos parametros da FIlial.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos seguintes pacotes de atualizações:

* 12.1.19.374
* 12.1.20.373
* 12.1.21.118
* 12.1.22

## Procedimento para Utilização

O sistema irá respeitar a parametrização dos dados da Filial para determinar se deve utilizar o MD-e via TSS ou via Neogrid.

Assim teremos os seguintes cenários (todos os parâmetros são do Totvs Gestão de Estoque, Compras e Faturamento):

**CENÁRIO 1**

Na etapa **Integrações → Fiscal → Importação/Envio de Arquivos XML** o parâmetro **Versão TOTVS Colaboração**, marcado com o valor **2.00**

E, nos parâmetros fiscais da Filial, etapa **Importação/Envio de Arquivos XML 1/2** o parâmetro **MD-e** dentro do campo **Tipo Documento Integração TOTVS Colaboração** **DESMARCADO**

Neste cenário, o sistema irá realizar as operações do MD-e (Sincronismo, Manifestação de Eventos, etc) utilizando o TSS.

**CENÁRIO 2**

Na etapa**Integrações → Fiscal → Importação/Envio de Arquivos XML** o parâmetro **Versão TOTVS Colaboração**, marcado com o valor**2.00**

E, nos parâmetros fiscais da Filial, etapa **Importação/Envio de Arquivos XML 1/2**o parâmetro**MD-e** dentro do campo**Tipo Documento Integração TOTVS Colaboração****MARCADO**

Neste cenário, o sistema irá realizar as operações do MD-e (Sincronismo, Manifestação de Eventos, etc) atrave´z da troca de arquivos com o Neogrid através da pasta configurada.
