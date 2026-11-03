---
content_hash: 761d4e1a73258947aa932db8f427e59ab0247b820ade96da01c635f3e1c45036
fetched_at: '2026-06-29T00:08:49.343512+00:00'
page_id: '329038343'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-1377_DT_INUTILIZACAO_CTE_OS
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-1377_DT_INUTILIZACAO_CTE_OS
version: 2
---

# Inutilização de CT-e OS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Gestão de Estoque, Compras*.e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CT-e OS* | *CONHECIMENTO DE TRANSPORTE ELETRÔNICO - OUTROS SERVIÇOS* | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Tickets relacionados** | *MATFATCMPCRM01-1354* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-1354 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *TCTEINUT* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Implementação do Processo de Inutilização Para CT-e OS

## **Documentação Adicional**

Quaisquer detalhes adicionais sobre CT-e Os podem ser encontrados em [MATFATCMPCRM01-673 DT CT-e OS](http://tdn.totvs.com/display/LRM/MATFATCMPCRM01-673+DT+CT-e+OS)

Quaisquer detalhes adicionais sobre o processo de Inutilização de CT-e OS podem ser encontrados no Manual do CT-e que pode ser adquirido em <http://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bx74pJ8hXaM=>

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.20*

É necessário atualizar o Totvs Sped Services (TSS) para a versão 2.77 ou superior

## Procedimento para Utilização

  Para utilização do processo de inutilização para CT-e OS, seguir os passos abaixo:

**1) ENVIO DA INUTILIZAÇÃO**

Acessar a visão de CT-e OS no caminho **Faturamento → Conhecimento de Transporte - Outros Serviços (CT-e OS).**

Executar o processo **Inutilizar CT-e OS**

O processo abrirá a tela para preenchimento de parâmetros. É necessário preencher todos os itens.

Após a execução do processo o sistema irá criar os registros na Tabela TCTEINUT com status de Pendente.

**2) CONSULTA DA INUTILIZAÇÃO**

Após o envio, é necessário consultar o Status dos registros enviados para a SEFAZ. Para isso, executar o processo **Consultar Inutilização**

O processo abrirá a tela para preenchimento da filial da qual será realizada a consulta.

Após executar o processo, o TSS retornará o status de cada registro Pendente de inutilização.

**3) ANEXO DE CT-E OS INUTILIZADOS**

Para verificar os registros, acessar a cadastro de Filial, e abrir o anexo **CT-e/CT-e OS Inutilizados**

O Anexo abrirá as informações dos registros inutilizados

**4) INUTILIZAÇÃO DE CT-E OS COM STATUS REJEITADO**

É possível realizar a inutilização de registro que esteja com status igual a rejeitado. Basta selecionar o registro e executar o processo **Inutilizar CT-e OS.**

Esse processo, não abrirá a tela de parâmetros e executará o processo para o registro selecionado.

Após a execução do processo e **Consulta da Inutilização** (citada no item 2). será apresentado no anexo da filial o CT-e OS inutilizado. O registro com status Rejeitado que foi selecionado na visão será apagado após a inutilização.
