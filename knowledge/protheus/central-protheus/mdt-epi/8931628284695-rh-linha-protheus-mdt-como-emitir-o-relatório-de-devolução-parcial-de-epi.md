---
article_id: 8931628284695
category: MDT - EPI
content_hash: 38ef84aeaf309e7b9e21467c148d0e7a8a6a354585c28c0472877d76136a2a84
fetched_at: '2026-06-28T22:44:25.342436+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Como emitir o Relatório de devolução parcial de
  EPI
type: support-article
updated_at: '2024-11-05T11:22:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8931628284695-RH-Linha-Protheus-MDT-Como-emitir-o-Relat%C3%B3rio-de-devolu%C3%A7%C3%A3o-parcial-de-EPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20199545938199) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como emitir o Relatório de devolução parcial de EPI?  
  
**Ambiente**TOTVS RH (Linha Protheus) -Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Sistema irá imprimir o recibo de devolução parcial, apenas se a devolução parcial do EPI for realizada através da rotina **EPI X Funcionário** (*MDTA630*).  
A opção de Devolução Parcial permite ao usuário realizar uma devolução de EPI onde seja particionada, ou seja, caso o funcionário tenha recebido 2 ou mais unidades do mesmo EPI, é possível realizar a devolução em partes. As informações devem ser ajustadas de acordo com as orientações descritas em Campos Devolução Parcial.  
  
Registros provindos da tabela **EPIs Devolvidos (TLW)**que possui relação com a **EPIs Entregues Funcionários****(TNF)**. Todos os campos abaixo são de preenchimento obrigatório.  
  
*Importante!*A Devolução Parcial ou a Devolução Total, só é possível após a impressão do relatório que emite o recibo de entrega, o relatório Recibo de Entrega de EPI (MDTR805).

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Data Dev. (TLW\_DTDEVO) | Permite informar qual a data que o **EPI** foi devolvido. Não é possível informar uma data inferior a data de entrega do **EPI**. |
| Hora Dev. (TLW\_HRDEVO) | Permite informar qual a hora que o **EPI** foi devolvido. Em conjunto com o campo da data, não é possível informar uma data + hora inferior a data de entrega do **EPI**. |
| Quant. Dev. (TLW\_QTDEVO) | Permite informar a quantidade de **EPI** que o usuário vai devolver. A quantidade pode ser total ou parcial da quantidade que foi entregue. |
| Almoxarifado (TLW\_LOCAL) | Permite informar para qual almoxarifado o **EPI** será devolvido. |
| Repor Estoq. (TLW\_TIPODV) | Permite informar se o **EPI** será devolvido fisicamente ao almoxarifado de devolução ou não. Possui as opções **1-Sim**(devolve o **EPI**) ou **2-Não** (não devolve o **EPI).** |

Veja como realizar  devolução de saldo parcial e impressão do recibo de devolução Parcial de EPI.  
  
![gif.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8931832879383)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
