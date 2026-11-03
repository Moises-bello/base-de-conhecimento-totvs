---
content_hash: 6fa77b66ce17e19b1bd63954b76f5f9c7368f67490422c48d5440ce14d39b901
fetched_at: '2026-06-29T00:08:48.834205+00:00'
page_id: '327335281'
product: rm
source: tdn-rm
title: DT Desconto por antecipação - Mudança de turma e transferência interna
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327335281
version: 3
---

# DESCONTO POR ANTECIPAÇÃO - MUDANÇA DE TURMA E TRANSFERÊNCIA INTERNA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Gestão Educacional.* |
| **Módulo:** | **TOTVS Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Desconto por Antecipação* | *Desconto por Antecipação* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Mudança de Turma** | *Mudança de Turma* | | **Transferência interna** | ****Transferência interna**** | |
| **Cadastros Iniciais:** | *Cadastro de descontos por antecipação Associação de descontos por antecipação a contratos.* |
| **Parâmetro(s):** | *N/A.* |
| **Ponto de Entrada:** | *N/A.* |
| **Tickets relacionados** | *N/A.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DEDUINTEGRACOES-1132 |
| **País(es):** | *Todos.* |
| **Banco(s) de Dados:** | *N/A.* |
| **Tabelas Utilizadas:** | *FAGRUPADESCONTOPONTUAL e SCONTRATODESCPONTUAL* |
| **Sistema(s) Operacional(is):** | *N/A.* |

## Descrição

Foram criadas as opções de cópias de descontos por antecipação nos processos de "Mudança de turma" e "Transferência interna" a fim de se transferirem os descontos por antecipação cadastrados nos contratos antigos para os contratos novos.

## Mudança de Turma

No módulo Educacional o processo de mudança de turma é acessado através dos processos da matrícula no período letivo: "Matrícula no período letivo" → Processos → "Mudar turma/turno" (Ensino Básico) e "Matrícula no período letivo" → Processos → "Mudar Turma" (Ensino Superior)

A opção de cópia de descontos por antecipação só estará visível se for **ensino básico** e se a base estiver habilitada para trabalhar com desconto por antecipação.

Essa opção só estará habilitada quando o usuário optar por "NÃO" aproveitar o contrato. Caso o usuário opte por aproveitar o contrato, a opção de cópia de descontos por antecipação para um novo contrato, ficará desabilitada.

Ao selecionar a opção "Copiar descontos por antecipação para o novo contrato", o processo copiará os descontos por antecipação cadastrados no contrato com a matriz aplicada de origem para o contrato a ser criado com a nova matriz aplicada de destino escolhida.

Segue abaixo a opção criada no processo de mudança de turma/turno:

Aviso

Se existir mais de um contrato para a mesma matriz aplicada de origem com desconto(s) por antecipação, o sistema não copiará os descontos e mostrará uma mensagem de alerta para o usuário conforme abaixo:

Não foram copiados descontos por antecipação para o contrato gerado para o aluno ES-00307 - ARTHUR BARROS no período letivo 2017/2 porque foram encontrados mais de um contrato com descontos por antecipação para a matriz aplicada de origem.

## Transferência interna

No módulo Educacional o processo de transferência interna é acessado através do menu: "Atividades acadêmicas" → "Transferência interna" → "Transferência interna"

A opção de cópia de descontos por antecipação só estará visível se for **ensino superior** e se a base estiver habilitada para trabalhar com desconto por antecipação.

Essa opção só estará habilitada quando o usuário optar por "NÃO" manter o contrato original e alterar a matriz aplicada para a matriz destino. Caso o usuário opte por manter o contrato original, a opção de cópia de descontos por antecipação para um novo contrato, ficará desabilitada.

Ao selecionar a opção "Copiar descontos por antecipação para o novo contrato", o processo copiará os descontos por antecipação cadastrados no contrato com a matriz aplicada de origem para o contrato a ser criado com a nova matriz aplicada de destino escolhida.

Segue abaixo a opção criada no processo de transferência interna:

Aviso

Se existir mais de um contrato para a mesma matriz aplicada de origem com desconto(s) por antecipação, o sistema não copiará os descontos e mostrará uma mensagem de alerta para o usuário conforme abaixo:

Não foram copiados descontos por antecipação para o contrato gerado para o aluno ES-00307 - ARTHUR BARROS no período letivo 2017/2 porque foram encontrados mais de um contrato com descontos por antecipação para a matriz aplicada de origem.

 Exemplo de Transferência Interna e Mudança de Turma , [Clique Aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=329029368).
