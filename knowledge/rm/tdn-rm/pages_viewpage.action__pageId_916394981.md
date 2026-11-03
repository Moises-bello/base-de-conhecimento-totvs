---
content_hash: 21ae5ca7a1c75c334bb7671bc405325fe0669c238e42d3d8191a0e54b792f73b
fetched_at: '2026-06-29T00:12:06.855407+00:00'
page_id: '916394981'
product: rm
source: tdn-rm
title: DT -Compensação Banco de horas - Mensagem ao excluir eventos no Sindicato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=916394981
version: 9
---

## **01. DADOS GERAIS**

| **Produto:** | **RM** |
| --- | --- |
| **Linha de Produto:** | **Linha RM** |
| **Segmento:** | **RH** |
| **Módulo:** | **TOTVS Automação de Ponto** |
| **Função:** | **Compensação Banco de Horas** |
| **País:** | **Brasil** |
| **Requisito/Story/Issue:** | **[DRHJORNRM-7409](https://jiraproducao.totvs.com.br/browse/DRHJORNRM-7409)** |

## **02. VERSÕES**

* A partir dos patches:

  + 12.1.2502.104 e superiores.

## **03. SITUAÇÃO/REQUISITO**

Ao  excluir um evento do sindicato que tem horas no banco de horas e  realizar o processo de compensação e lançamento para zerar o banco de horas as informações o codigo do evento esta sendo apagado na tabela ABANCORFUNDETALHE 

## **04. SOLUÇÃO**

O sistema não permitirá realizar a exclusão do evento no sindicato caso esse evento esteja vinculado no cálculo do banco e na compensação caso não exista algum evento a compensação não será concluída e será demonstrada mensagem para o usuário.

## **05. EXEMPLO**

11Sindicato- Excluíndo evento considerado no cálculo Banco de horas

Na tabela ABANCOHORFUNDETALHE o evento 0024 se encontra calculado para a chapa 00001

Ao realizar a exclusão do evento será demonstrada a mensagem para o usuário.

2Compensação Banco de Horas- Mensagem para usuário caso evento do Banco não exista no sindicato

Funcionário vinculado em um novo sindicato que não possui alguns eventos vinculados.

Ao realizar a compensação será demonstrada a mensagem:

Será necessário ajustar os eventos no sindicato para realizar a compensação.

A compensação é realizada

## **06. ASSUNTOS RELACIONADOS**
