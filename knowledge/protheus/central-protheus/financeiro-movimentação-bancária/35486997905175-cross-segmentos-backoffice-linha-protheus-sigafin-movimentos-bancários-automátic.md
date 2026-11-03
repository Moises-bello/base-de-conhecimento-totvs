---
article_id: 35486997905175
category: Financeiro - Movimentação Bancária
content_hash: f8d0e5c15f99cb518f1cb714092cfb94f3f9925a89e9b888967e3d4bbd4e3a59
fetched_at: '2026-06-28T22:38:19.369546+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Movimentos Bancários
  Automáticos - FINA100 - MsExecAuto
type: support-article
updated_at: '2025-10-08T17:14:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35486997905175-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Movimentos-Banc%C3%A1rios-Autom%C3%A1ticos-FINA100-MsExecAuto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35487026479639) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Quais os ExecAuto liberados para a movimentação bancária (FINA100)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - todas as versões.  
  
**Solução**  
Este documento apresenta as instruções e detalhes necessários para a execução automática (MsExecAuto) de movimentações bancárias por meio da rotina **FINA100**.

A funcionalidade tem como objetivo automatizar os processos de movimentação bancária — seja de **entrada, saída ou transferência** entre contas — otimizando o fluxo financeiro e reduzindo intervenções manuais.

**PARÂMETROS DA MsExecAuto**  
A chamada da **MsExecAuto** na rotina **FINA100** requer o envio de **três parâmetros**, conforme descrito a seguir:

* **1º Parâmetro:** Deve ser informado o valor **“0” (zero)**, indicando que a execução será automática.
* **2º Parâmetro:** Array contendo as informações necessárias para o preenchimento dos campos exigidos na operação. O conteúdo e a estrutura desse array variam conforme o tipo de movimentação. Para mais detalhes, consulte a seção **“Exemplos de Utilização”**.
* **3º Parâmetro:** Define a **opção de operação** a ser executada automaticamente, de acordo com o tipo de movimentação desejada. As opções disponíveis são:

| Código | Descrição |
| --- | --- |
| 3 | Movimentação Bancária a Pagar (saída) |
| 4 | Movimentação Bancária a Receber (entrada) |
| 5 | Excluir Movimentação Bancária |
| 6 | Cancelar Movimentação Bancária |
| 7 | Transferência entre contas ou caixas |
| 8 | Estorno de Transferência |
| 9 | Classificação |

**EXEMPLOS DE UTILIZAÇÃO:**  
[Movimentos Bancários Automáticos - FINA100 - MsExecAuto](https://tdn.totvs.com/pages/releaseview.action?pageId=516631673)
