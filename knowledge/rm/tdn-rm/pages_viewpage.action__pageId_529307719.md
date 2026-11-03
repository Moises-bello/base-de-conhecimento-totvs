---
content_hash: 18f361980ee2b98d6378b6534340238c3a12385a189b84058d19c3e3e2f8556b
fetched_at: '2026-06-29T00:10:35.493661+00:00'
page_id: '529307719'
product: rm
source: tdn-rm
title: FISCAL01-11544 DT Encerramento do Período da Reinf - Regras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=529307719
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Abertura de Período de Apuração Encerramento de Eventos Periódicos |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11544 |

## **02. SITUAÇÃO/REQUISITO**

Ao executar o R-2099 o sistema deverá alertar ao usuário sobre eventos não autorizados, mas não deverá impedir o encerramento e neste caso deve ser gravado no log do histórico uma indicação da escolha do usuário e os detalhes dos eventos não autorizados;

O período de apuração dos tributos não poderá ser reaberto enquanto o período da EFD-REINF permanecer encerrado.

## **03. SOLUÇÃO**

**Funcionalidade: Encerramento de Eventos Periódicos**

**Cenário: Eventos R-20XX não autorizados ou alterados**

Dado que um evento R-5011 é pai de eventos R-20XX

E estes estão com o status: Inconsistente, Não Transmitido, Pendente, Pendente Exclusão ou Rejeitado

Ao executar o processo de Encerramento dos Eventos Periódicos

Então o sistema deve exibir uma tela de diálogo, informando o usuário e solicitando confirmação da execução,

Caso o usuário opte por executar o processo, então o sistema registrará estas observações no histórico do R-5011.

**Funcionalidade: Abertura de Período de Apuração**

**Cenário : Período da EFD-Reinf Encerrado**

Dado que existe um evento R-5011 com o status encerrado (cujo filho R-2099 foi consultado e autorizado),

Ao executar a abertura do período de apuração correspondente

Então o sistema não permitirá reabrir o período: 

Do tributo INSS: Se existir evento R-2010 ou R-2020 filho do R-5011 encerrado, com status diferente de excluído.

Do tributo FUNRURAL: Se existir evento R-2050 filho do R-5011 encerrado, com status diferente de excluído.

Do tributo Contribuição Previdenciária: Se existir evento R-2060 filho do R-5011 encerrado, com status diferente de excluído.
