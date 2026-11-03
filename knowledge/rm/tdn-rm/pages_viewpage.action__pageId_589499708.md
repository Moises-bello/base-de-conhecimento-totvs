---
content_hash: 345e1c96797123a6cd548ad045e417bb89bea8a871a00dd8be1b079cce699390
fetched_at: '2026-06-29T00:10:53.878732+00:00'
page_id: '589499708'
product: rm
source: tdn-rm
title: FISCAL01-14604 DT Cópia Parâmetros de Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589499708
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cópia de Parâmetros de Processos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14604 |

## **02. SITUAÇÃO/REQUISITO**

Criar um processo para copiar os parâmetros de processos entre Filiais

Critérios de Aceite:

Criar um processo para copiar os parâmetros de processos entre Filiais  
Criar Documentação sobre o novo cadastro  
Criar teste automatizado para o cenário

## **03. SOLUÇÃO**

Foi implementado o processo de cópia dos parâmetros de processos que está disponível em RM -> Gestão Fiscal -> Cadastros -> Parâmetros de Processos -> Processos -> Cópia de Parâmetros de Processos.

O processo realiza a cópia de um parâmetro de processo e os parâmetros associados para outra filial.

Se existir parâmetro de processo igual na filial de destino, o parâmetro não será copiado e uma mensagem de aviso será emitido através do processo de cópia.

Para visualizar e executar o processo Cópia de Parâmetros de Processos será necessário que o usuário tenha permissão de Inclusão no cadastro de Parâmetros de Processos.
