---
content_hash: 853378958bfd9bdb5632aa8e3d4126ff331f445a848e3208a6c17ce5c207c18b
fetched_at: '2026-06-29T00:08:48.116424+00:00'
page_id: '323620174'
product: rm
source: tdn-rm
title: ER MATFATCMPCRM01-2168 MDF-e - Nota Técnica 2017/003
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=323620174
version: 92
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATFATCMPCRM01 | **IRM/EPIC1** | MATFATCMPCRM01-2168 |
| **Requisito/Story/Issue1** |  | **Subtarefa1** |  |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

De acordo com a Nota Técnica Nota Técnica 2017/003 do MDF-e, foi acrescentado um novo Tipo de Emitente a ser considerado no envio da MDF-e e consistências relacionadas a esse novo tipo.

Abaixo serão descritas as alterações necessárias no sistema para atendimento à Nota Técnica citada.

## 

## Definição da Regra de Negócio

Tela de Edição do Movimento

* Em Transporte | Identificação, o ComboBox **Tipo de Emitente do MDF-e** (TMOVTRANSP.TIPOEMITENTEMDFE) deverá exibir, além das opções já existentes, a opção "3 - Prestador de serviço de transporte que emitirá CT-e Globalizado".

Esse Tipo de Emitente será utilizado pelo transportador que emitirá CT-e globalizado a posteriori para englobar repetidas prestações, nas UF cuja legislação assim o permite ou que goze de regime especial para tal, nas UF onde a legislação dispõe desta forma

Envio do XML

Grupo de Informações "ide"

* A tag "tpEmit" passa a aceitar o valor 3, referente ao Tipo de Emitente "Prestador de serviço de transporte que emitirá CT-e Globalizado". O campo deverá ser preenchido conforme "Tipo de Emitente" preenchido no movimento que originará o MDF-e.

Consistências

1. Alteradas

* Se tipo emitente informado for igual a Prestador de Serviço de Transporte (tpEmit=1) ou Transportador que emitirá CT-e Globalizado (tpEmit=3), modal = rodoviário e CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do Tipo de Transportador (tpTransp) deverá ser diferente de TAC (2).
* Se modal Rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) ou Transportador que emitirá CT-e Globalizado (tpEmit=3): Rejeitar se o grupo de informações do seguro da carga não estiver informado.
* Se modal Rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) ou transportador que emitirá CT-e Globalizado (tpEmit=3) e informado grupo de seguro da carga: Rejeitar se alguma informação do grupo seguro não estiver informada.
* Se modal Rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) ou transportador que emitirá CT-e Globalizado (tpEmit=3), informado grupo de seguro da carga e indicado responsável pelo seguro contratante (tpResp=2): Rejeitar se não estiver informado CNPJ ou CPF do responsável pelo seguro.
* Se modal Rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte (tpEmit=1) ou Transportador que emitirá CT-e Globalizado (tpEmit=3) e não estiverem preenchidos: 1. Responsável pela Geração do CIOT ou 2. Responsável pelo pagamento do Vale-pedágio: Rejeitar se não estiver informado pelo menos um tomador de serviço (grupo infContratante)

2. Incluídas

* Se tipo emitente informado for igual a Transportador que emitirá CT-e Globalizado (tpEmit=3): O grupo de documentos CT-e não pode ser preenchido.
* Rejeitar se tipo emitente informado for igual a Transportador que emitirá CT-e Globalizado (tpEmit=3) e operação interestadual ou com exterior.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* TTMVEXT - Tipos de Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
