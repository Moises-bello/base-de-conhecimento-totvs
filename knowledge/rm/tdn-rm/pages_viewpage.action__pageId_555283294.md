---
content_hash: c07d4158cead906d31ee879c48830762b40f8fb9bca050499141caf89fcb9ccd
fetched_at: '2026-06-29T00:10:46.678585+00:00'
page_id: '555283294'
product: rm
source: tdn-rm
title: FISCAL01-12884 DT Processo de Escrituração Fiscal Sem Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555283294
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração\ Estorno Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12884 |

## **02. SITUAÇÃO/REQUISITO**

Evoluir processo da Escrituração Fiscal para que não seja necessário cadastro de Lote de Escrituração.

## **03. SOLUÇÃO**

Implementação do processo Escrituração e Estorno "Sem Lote de Escrituração".

O processo de Escrituração\Estorno de Movimentos foram evoluídos para que não seja necessário cadastro de Lote para execução do processo de Escrituração.

Quando o processo de Escrituração do Lote Fiscal for executado sem selecionar nenhum registro, a tela de processo será exibida com os parâmetros para o filtro de Movimentos.

Esta tela de parâmetros possui as mesmas consistências realizadas pelo cadastro de Lote de Escrituração.

**Observação:** Quando não for informado o campo Período Final, a data considerada será a data de execução do processo.

(**N CAMADAS**) Quando estiver parametrizado N camadas o usuário também tem a opção de agendar a execução do processo

Tela Agendamento do Processo

O fluxo para executar o processo de Estorno da Escrituração é o mesmo da Escrituração.

Tela do processo de Estorno do Movimento

Ao executar o processo ocorre os mesmos processamentos de uma Escrituração\Estorno comum, mas a diferença que os Movimentos ficam associados ao lote "SEM LOTE".
