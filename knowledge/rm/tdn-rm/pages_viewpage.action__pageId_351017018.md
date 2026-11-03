---
content_hash: d2c4fb87b30d83a4251fff0826bc94efbbf28f19679edd23a3d4d877e82bb309
fetched_at: '2026-06-29T00:08:55.823133+00:00'
page_id: '351017018'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-2050 DT PRESTAÇÃO DE SERVIÇO EM DESACORDO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351017018
version: 5
---

# **EVENTO DE PRESTAÇÃO DE SERVIÇO EM DESACORDO**

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e projetos.* |
| **Módulo:** | **Totvs Gestão de Estoque, Compras*.e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *CT-e/CT-e OS* | **CONHECIMENTO DE TRANSPORTE ELETRÔNICO**  *CONHECIMENTO DE TRANSPORTE ELETRÔNICO - OUTROS SERVIÇOS* | |
| **Cadastros Iniciais:** | Filial |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | MATFATCMPCRM01-2050 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-2050 |
| **País(es):** | bra |
| **Banco(s) de Dados:** | *SQLServer e Oracle.* |
| **Tabelas Utilizadas:** | TCTEPRESTDESACORDO |
| **Sistema(s) Operacional(is):** | - |

## Descrição

Implementação do processo de Prestação de Serviço em Desacordo para CT-e e CT-e OS.

## **Documentação Adicional**

Quaisquer detalhes adicionais sobre o processo de Prestação de Serviço em Desacordo podem ser encontrados no Manual do CT-e que pode ser adquirido em <http://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=bx74pJ8hXaM=>

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações de uma das seguintes versões:

* *12.1.19.153 ou*
* *12.1.20.101 ou*
* *12.1.21 ou superiores*

## Procedimento para Utilização

Para utilização da operação em desacordo, seguir os passos abaixo:

Observação: O processo descrito abaixo atende tanto a Prestação em Desacordo de CT-es quanto de CT-es OS

Acessar o Cadastro de Filial no caminho **Cadastros → Filial:**

Selecionar a Filial para o qual se deseja enviar a Prestação em Desacordo e acessar o anexo **Prestações em Desacordo (CT-e/CT-e OS)**

Clicar no botão Incluir do Anexo e preencher a **Chave de Acesso** e a **Observação** da Prestação em Desacordo na Tela

Observação: O campo Tipo de Documento é automaticamente preenchido de acordo com a chave de acesso informada.

Após salvar o registro, selecionar o mesmo e, com o TSS aberto, ir em **Processos → Enviar Prestação em Desacordo.**

Esse processo irá enviar o registro para a SEFAZ, e modificará o status do registro para Pendente.

Após isso, selecionar o registro com Status Pendente e, com o TSS aberto, ir em **Processos → Consultar Prestação em Desacordo.**

Após a consulta, a Sefaz retornará se a Prestação em Desacordo foi vinculada com sucesso ao CT-e ou CT-e OS (o que mudará o registro para o Status de **Autorizado**). Ou se houve alguma inconsistência que impediu a Autorização (o que mudará o registro para o Status de **Rejeitado).**
