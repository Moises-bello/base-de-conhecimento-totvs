---
content_hash: 616b6873b4093eafadade6a55676f92f718e491bab4c8acfe0ed1f7ed00fb687
fetched_at: '2026-06-29T00:10:37.816018+00:00'
page_id: '540895523'
product: rm
source: tdn-rm
title: FISCAL01-12525 DT Reabertura da Sub-apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540895523
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Reabertura de Período de Sub-Apuração |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12525 |

## **02. SITUAÇÃO/REQUISITO**

Implementar nessa issue:  
  
1) O processo de reabertura da Sub- Apuração.   
  
- Este processo deve apenas alterar o status de "Encerrado" para "Aberto".  
  
- O sistema não pode permitir a reabertura caso haja algum período posterior fechado com o mesmo identificador da sub-apuração.  
  
2) Colocar consistência no encerramento do Período de Apuração (principal) para não permitir o encerramento caso haja alguma sub-apuração em aberto.

## **03. SOLUÇÃO**

**Funcionalidade: Reabertura de Sub-Apuração**

Regra I:  
O sistema não pode permitir a reabertura caso haja algum período posterior encerrado com o mesmo identificador da sub-apuração. Entretanto, será possível executar a abertura se os períodos que impedem a execução forem selecionados para mesma execução do processo.

Regra II:  
O sistema exibirá aviso caso hajam períodos selecionados que já se encontram abertos.

Comportamento do Log:  
a)Caso haja somente execuções bem sucedidas, o processo será exibido com o status de Sucesso.  
b)Caso haja somente execuções de alerta ou exista pelo menos uma execução bem sucedida, o processo será exibido com status de Alerta.  
c)Caso haja somente execuções de erro, o processo será exibido com status de Erro.

**Cenário I: Sucesso**

Dado que estão cadastrados em um período: 3 sub-apurações de identificador 1 e 2 cada,  
E todas estão encerradas,  
Ao executar o processo de abertura de período de sub-apuração para as 3 sub-apurações de identificador 1,  
Então o processo deve ser executado com sucesso e os status das sub-apurações de identificador 1 serem alteradas para "aberto".

**Cenário II: Alerta**

Dado que estão cadastrados em um período: 3 sub-apurações de identificador 1 e 2 cada,  
E as sub-apurações de identificador 1 estão encerradas,  
Ao executar o processo de abertura de período de sub-apuração para as 6 sub-apurações juntas.  
Então o processo deve ser executado com alerta e os status das sub-apurações de identificador 2 serem alteradas para "aberto".  
E no log devem ser discriminadas corretamente as execuções.

**Cenário III: Erro**

Dado que estão cadastrados em um período: 3 sub-apurações de identificador 1 e 2 cada,  
E as sub-apurações de identificador 1 estão encerradas,  
Ao executar o processo de abertura para as 2 sub-apurações mais antigas de identificador 1,  
Então o processo deve ser executado com erro e o status das sub-apurações não deve ser alterado.

**Funcionalidade: Encerramento do Período de Apuração**

Regra I:  
O sistema não pode permitir o encerramento do Período de Apuração se houver ao menos uma Sub Apuração aberta.

Comportamento do Log:  
a)Caso haja somente execuções bem sucedidas, o processo será exibido com o status de Sucesso.  
b)Caso haja somente execuções de erro, o processo será exibido com status de Erro.

**Cenário I: Sucesso**

Dado que estão cadastrados em um período: 3 Sub-Apurações de identificador 1 e 2 cada,  
E todas estão encerradas,  
Ao executar o processo de encerramento do Período de Apuração, o mesmo será concluído com sucesso

**Cenário II: Erro**

Dado que estão cadastrados em um período: 3 Sub-Apurações de identificador 1 e 2 cada,  
E as Sub-Apurações de identificador 1 estão abertas,  
Então o processo deve ser executado com erro e o status do Período de Apuração não deve ser alterado.
