---
content_hash: 59a223f7110ba68dabc2aac0ce339adb0067a9674a29a9432a0d6619a7acc8c2
fetched_at: '2026-06-29T00:09:09.989938+00:00'
page_id: '394220902'
product: rm
source: tdn-rm
title: DT Cópia do Mapeamento do Plano de Contas Consolidado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394220902
version: 3
---

# Cópia do Mapeamento do Plano de Contas Consolidado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Contábil |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Processo | Cópia do Mapeamento do Plano de Contas Consolidado |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Planos de contas paralelos | Tipos de Planos de Contas Paralelos | | Contas Paralelas | Contas Paralelas | |
| **Cadastros Iniciais:** | Plano de Contas Paralelo  Contas Paralelas |
| **Parâmetro(s):** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [http://jiraproducao.totvs.com.br/browse/](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7687)[CONTROLADORIA01-1881](http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1881 "Automatismo para criar relacionamento entre contas") |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | CCONTA2, CCTACTA2 |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.22 |

## Descrição

O processo tem como objetivo copiar, para as coligadas de destino, a associação das contas contábeis do plano de contas paralelo informado pelo usuário. Serão copiados os mapeamentos de todas as contas contábeis que possuírem o mesmo código na coligada de destino. As contas que possuírem códigos diferentes serão listadas em um log. Se a coligada de destino possuir mapeamento a cópia não será realizada e uma mensagem informativa será adicionada no log. Vale ressaltar que o processo só será exibido pela controladora (coligada de origem), ou seja, as controladas não devem visualiza-lo.

A tela possui os seguintes campos:

1 - Coligada de Origem: Exibe a controladora e suas controladas ativas.

2 - Plano de Contas (Capa): Esta opção lista todos os planos de contas paralelos, existentes na coligada corrente (controladora), que tenham como finalidade "Consolidação de Saldos".

3 - Coligadas de Destino: Este opção exibe a controladora e suas controladas ativas, com exceção da coligada de origem.

Todos os campos acima são obrigatórios.

## Procedimento para Utilização

1 - Acesse um plano de contas paralelo cuja finalidade seja "Consolidação de Saldos".

2 - Selecione o processo "Cópia de Mapeamento do Plano de Contas Consolidado".

3 - Selecione o plano de contas consolidado desejado e informe as coligadas de destino.

4 - Execute o processo.
