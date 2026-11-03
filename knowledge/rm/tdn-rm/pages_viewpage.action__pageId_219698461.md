---
content_hash: 1c8bcfe23f52b67be67977621cd2a634df0d98b92432675756f621d634a08678
fetched_at: '2026-06-29T00:06:19.505004+00:00'
page_id: '219698461'
product: rm
source: tdn-rm
title: TTSJSR_DT_Novos_Parâmetros_Intregração_EMS_Datasul
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698461
version: 7
---

# Criação de novos parâmetros para integração EMS Datasul

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Parâmetros EMS | | Cadastro de  Prestadores | |
| **Chamados Relacionados** | TTSJW2 |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | SZPARAMEMS |
| **Sistema(s) Operacional(is):** | Windows |
| **Versões/Release:** | 12.1.8 |

## Descrição

Alterado a tela de integração EMS Datasul criando novos parâmetros para Grupo de Fornecedor (Prestadores, Clinicas, Convênios, Responsável) e foi criado também uma nova aba de Cadastros II possuindo os campos de código de portador, carteira para clientes e fornecedores.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.8.102 deste chamado.

## Procedimento para Utilização

**Exemplo:**

       1.            No TOTVS Gestão Hospitalar (antiga MDI) acessar o menu Opções > Parâmetros > Parâmetro de Integração > Parâmetros EMS.

 O sistema apresenta a tela de Parâmetros EMS ao clicar em Editar.

       2.            Acessar a aba Cadastro, para cada bloco (Prestador/Grupo, Clínicas, Laboratórios, Convênios, Responsável) será listado um novo campo Grupo de Fornecedor.

       3.            Ao Acessar a aba Cadastro II será apresentado um bloco Portador, com os novos campos Código portador cliente, Código portador fornecedor, Código carteira cliente, Código carteira fornecedor.

       4.            Ao cadastrar um novo Prestador essas informações serão necessárias para realizar a integração com o EMS Datasul.

divs
