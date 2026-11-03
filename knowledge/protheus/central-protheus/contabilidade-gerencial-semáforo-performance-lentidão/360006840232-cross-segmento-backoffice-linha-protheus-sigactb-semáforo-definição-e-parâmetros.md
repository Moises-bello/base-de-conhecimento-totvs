---
article_id: 360006840232
category: Contabilidade Gerencial - Semáforo, Performance, Lentidão
content_hash: a5dbf44c36516511fc0e943e11f3b46ab52f80bd5e8d4d3de90d682f11549b21
fetched_at: '2026-06-28T22:41:02.600677+00:00'
product: protheus
section_id: 1500001537321
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- Semáforo, definição e
  parâmetros.
type: support-article
updated_at: '2021-09-15T17:17:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006840232-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Sem%C3%A1foro-defini%C3%A7%C3%A3o-e-par%C3%A2metros
---

**Dúvida**

Como desabilitar o Semáforo de processamento, documentações complementares sobre semáforo e Controle de transações 

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - SIGACTB  – Contabilidade – A partir da versão 11.8  
  
**Solução**

A rotina processamento de saldos (CTBA190) tem um controle de locação de usuário.  
O parâmetro MV\_ATUSAL= S , atualiza os saldos online porem se algum usuário estiver reprocessando os saldos ou estiver processando alguma contabilização de outro modulo, o sistema bloqueio o usuário ate que o primeiro processo finalize e posteriormente aloca a tabela para o usuário seguinte.  
O reprocessamento de saldos (CTBA190) entra no processo de semáforo pois as tabelas de saldos que precisam de exclusividade.  
  
  
Para que não ocorra mensagem de semáforo é necessário desabilitar todos os parâmetros abaixo.  
MV\_CTBSER : conteúdo 2 (desligado)  
MV\_FN370SE conteúdo 2 (desligado)  
MV\_CTBNFSE : conteúdo 2 (desligado))  
MV\_CTBSERT :  
MV\_ATUSAL: conteúdo N (não)  
MV\_SLD COMP: conteúdo N (não)  
  
\*\* Desta forma o saldo não será mais processado online, o ideal seria criar um schedule para reprocessar durante a noite ou melhor horário para a empresa.  
Ou executar a rotina CTBA190 sempre que precisar emitir o Balancete e processos que envolvam saldos.

* Caso esteja na versão 11

MV\_ATUSAL: conteúdo N (não)

MV\_SLDCOMP: conteúdo N (não)

* Caso esteja na versão 12

Temos um novo processo para atualização de saldos : [CTB0113\_REPROCESSAMENTO\_SALDOS\_POR\_FILA\_P12](https://tdn.totvs.com/display/PROT/CTB0113_REPROCESSAMENTO_SALDOS_POR_FILA_P12)

**Saiba mais**

[MV\_CTBSER - Serialização Processos SigaCTB](http://tdn.totvs.com/pages/viewpage.action?pageId=6068565)

[MP\_SIGACTB - PARÂMETRO MV\_CTBSERD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007047111-MP-SIGACTB-PAR%C3%82METRO-MV-CTBSERD)

[Desabilitar o Semáforo](http://tdn.totvs.com/display/public/PROT/CTB116_DESLIGAR_SEMAFORO_PROCESSAMENTO)

[Controle de Transação - MV\_TTS](http://tdn.totvs.com/pages/releaseview.action?pageId=6814812)
