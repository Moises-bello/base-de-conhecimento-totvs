---
content_hash: 15e54ddc6a035d370aded9e32cb6cf9d0401fc39956390f6eb21a67a53af95a8
fetched_at: '2026-06-29T00:09:08.313091+00:00'
page_id: '387286627'
product: rm
source: tdn-rm
title: DT - Agentes Nocivos - Tabela 23 - Adequação.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=387286627
version: 1
---

# Adequação à Nota de Documentação Evolutiva 01/2018.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Gestão de Pessoas. |
| **Módulo:** | Segurança e Saúde Ocupacional. |
| **Função:** | PPRA | Riscos. |
| **Situação/Requisito:** | Adequação a Nota de Documentação Evolutiva 'NDE 01/2018 - Eventos de Segurança e Saúde no Trabalho - SST' liberada pela receita federal no dia 30/05/2018. |
| **Solução/Implementação:** | Criação de Script para adequação à NDE. |
| ****Documento de Referência:**** |  |

De acordo com a Nota de Documentação Evolutiva 'NDE 01/2018 - Eventos de Segurança e Saúde no Trabalho - SST' liberada pela receita federal no dia 30/05/2018, a tabela 23 - Fatores de Riscos do Meio Ambiente do Trabalho do E-Social foi atualizada pelo governo, fazendo com que os fatores de risco que já tinham sido cadastrados não se adequem mais aos padrões de layout do E-Social.

Para que o sistema considere a nova tabela liberada pela NDE, será necessária a execução do script que está disponível no RM.Atualizador. Para isso, acesse o RM.Atualizador com o usuário do banco de dados.

***Atenção: Antes de realizar qualquer alteração através do RM.Atualizador é necessário realizar o backup do banco de dados.***

Selecione o script ‘eSocial Tabela 23’, esse script possui os ajustes referentes à tabela 23.

Avance

Execute a análise de impactos.

Marque as opções referentes ao backup da base de dados, customizações e o tipo de base de dados.

Acesse os links informados, e caso esteja de acordo, aceite as novidades e procedimentos.

Inicie a atualização da base de dados e conclua o processo.

Após a execução do script será necessário adequar os fatores de risco à nova tabela do eSocial. Essa adequação deverá ser feita manualmente e por isso ao acessar a rotina de riscos pela primeira vez, após a execução do script, uma mensagem será exibida informando sobre a necessidade da alteração.

Caso seja necessário consultar as informações vinculadas aos riscos antes da adequação ao novo layout, estas informações estão disponíveis na tabela VAGENTESNOCIVOSTEMP.
