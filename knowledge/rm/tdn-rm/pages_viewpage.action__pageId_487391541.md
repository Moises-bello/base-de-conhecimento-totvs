---
content_hash: 4a4831bf7af1e614822714ed5431da0453f87b6f22409a7324b2eb8fc22eecf8
fetched_at: '2026-06-29T00:10:20.176436+00:00'
page_id: '487391541'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-4505 DT Diagnóstico (análise) de contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=487391541
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Gestão Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Contabilização por competência |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUINTEGRACOES-4505 |

## **02. SITUAÇÃO/REQUISITO**

Em alguns casos, o usuário informa uma competência a ser contabilizada e a mesma não é processada em algumas situações específicas que fazem com que os registros de contratos / competências não sejam elegíveis para processamento conforme veremos mais abaixo.

## **03. SOLUÇÃO**

Implementado o processo de diagnóstico (análise) de contabilizações a fim de informar ao usuário se a competência / contrato está elegível ou não para ser contabilizado.

## **04.  DESCRIÇÃO**

Antes de gerar a contabilização por competência, o usuário poderá rodar o processo de contabilização em modo de diagnóstico o qual, ao final da execução, informará o usuário se o contrato é elegível para ser contabilizado na competência informada.

Caso o contrato seja elegível para ser contabilizado, o sistema gravará um log com status de "Analisado com sucesso" , caso não exista contabilização ou log com status de "Erro" ou "Advertência".

Se o contrato não for elegível para ser contabilizado, o sistema gravará um log com status de "Analisado com advertência" , caso não exista contabilização ou log com status de "Erro" ou "Advertência".

## **05.  EXECUÇÃO DO PROCESSO DE DIAGNÓSTICO (ANÁLISE)**

O diagnóstico será executado a partir do formulário de geração de contabilização por competência ao marcar a opção "Executar contabilização em modo de diagnóstico" no formulário citado.

( **MENU** )

( **FORMULÁRIO DO PROCESSO** )

Ao clicar no botão "Executar", o sistema exibirá uma tela de advertência para o usuário que poderá confirmar ou não a execução do processo.

Importante

Contratos que eram filtrados no processo de contabilização não serão mais filtrados a fim de que os mesmos sejam analisados. Exemplo:

* Contratos cancelados
* Contratos com períodos letivos encerrados para contabilização
* Contratos com situação de matrícula que não gera contabilização por competência
* Contratos com serviços que não geram contabilização por competência
* Contratos sem parcelas

Ao final do processo, o usuário terá um log textual com um resumo do processamento de diagnóstico (análise) e poderá também acessar os logs gerados de forma semelhante à visualização de logs no final do processo de geração de contabilização.

( **LOG TEXTUAL** )

Dica

Conheça mais a funcionalidade de log de contabilizações [<<clicando aqui>>](http://tdn.totvs.com/pages/viewpage.action?pageId=465381685)!

## **06.  SITUAÇÕES DE ADVERTÊNCIA ( CONTRATOS NÃO ELEGÍVEIS PARA CONTABILIZAÇÃO )**

Serão considerados contratos não elegíveis para contabilização, quando a análise detectar as seguintes situações:

1. Contrato cancelado: Contratos cancelados não geram contabilização.
2. Situação de matrícula que não gera contabilização por competência:   
   Campo  desmarcado no cadastro da situação de matrícula no período letivo
3. Período letivo encerrado para contabilização: Períodos letivos encerrados para contabilização não geram contabilização.
4. Contrato do tipo acordo: Contratos gerados por acordo não processam contabilização.
5. Data de competência fora do período de contabilização: Se for informada uma competência fora do período válido para a contabilização, o sistema gravará um log e informará essa situação para o usuário.
6. Contrato sem parcelas: Contratos sem parcelas não serão contabilizados.
7. Contratos com parcelas que não contabilizam por competência: Se o contrato não possuir alguma parcela cujo serviço contabiliza por competência, o mesmo não será contabilizado.

IMPORTANTE

O diagnóstico de contratos somente analisará os contratos que estão no novo modelo de contabilização. Campo NOVOMODELO da tabela SCONTRATOCONT igual a "S"

Contratos contabilizados no modelo antigo, não serão analisados mas serão listados no log na linha: **Qtd contratos não analisados (modelo antigo)...............:0**

O processo de diagnóstico funcionará normalmente com o fracionamento de processos, ou seja, caso o fracionamento de processos esteja habilitado, os contratos poderão ser analisados fracionados.

Conheça mais a funcionalidade de log de contabilizações [<<clicando aqui>>](http://tdn.totvs.com/pages/releaseview.action?pageId=465385372)!
