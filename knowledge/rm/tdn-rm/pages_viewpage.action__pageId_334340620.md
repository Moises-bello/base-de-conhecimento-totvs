---
content_hash: b5d68e79f9af3db80737b5f05661d475dcf0d32247702bdef9f9f5e252578964
fetched_at: '2026-06-29T00:08:50.819824+00:00'
page_id: '334340620'
product: rm
source: tdn-rm
title: 2112822 RMSAU-2376 DT Guia de Honorário Individual com a tag dadosContratadoExecutante
  igual ao prestador principal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334340620
version: 3
---

# Guia de Honorário Individual com a tag dadosContratadoExecutante igual ao prestador principal

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento de Convênios | SauFaturaAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Condições Contratuais com Convênio | SauCondContratAction | |  |  | |
| **Cadastros Iniciais:** | Condições Contratuais |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Tickets relacionados** | 2112822 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-2376 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Esta implementação tem a finalidade de permitir que no padrão especial "Faturamento para médicos", seja possível definir se na tag <dadosContratadoExecutante> (Guia de honorário individual) serão preenchidos com os dados do médico executante ou do prestado principal.

## Procedimento para Utilização

1. No cadastro do convênio deve estar informado que utiliza o padrão ANS - TISS
2. Acesse as Condições Contratuais do convênio, aba Eletrônico III - TISS
   1. Informe a versão da TISS (a partir da 3.00.00)
   2. Informe no campo Informações Específicas, o valor "Faturamento para Médicos"
   3. Marque o campo "Gerar xml de terceiros em nome do prestador principal nos dados do contratado executante"
3. Registre um atendimento de internação para este convênio, informe a guia de Resumo de internação e faça os lançamentos dos honorários
4. Encerre a conta
5. Acesse a nova MDI, menu Faturamento, opção "Faturamento de convênios"
   1. Filtre pelo convênio configurado
   2. Crie uma nova fatura
6. Acesse o processo "Faturamento de convênios"
   1. Selecione a opção Faturamento
   2. Marque a opção Gerar XML para terceiros
   3. Selecione o tipo de paciente e avance o processo
7. Acesse a pasta onde os xml's foram gerados e confira a tag <dadosContratadoExecutante>
8. XML gerado com o parâmetro desmarcado
