---
article_id: 36952746417431
category: RH - Cadastros
content_hash: 5a5ec9625310d24b67c94597548d91b482febfef2254d5c50360cd1c6ae700d3
fetched_at: '2026-06-28T22:44:52.748690+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: 'RH - Linha Protheus - PON - Após UPDADE de Release ao efetuar cadastro de
  relógio, gera error log: Opção não disponível no Protheus Função: P0REPVLDCalled
  By'
type: support-article
updated_at: '2025-12-11T19:44:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36952746417431-RH-Linha-Protheus-PON-Ap%C3%B3s-UPDADE-de-Release-ao-efetuar-cadastro-de-rel%C3%B3gio-gera-error-log-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-P0REPVLDCalled-By
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36952746403095) Tempo aproximado para leitura: **01:00:00 min**  
  
**Ocorrência**  
Após *UPDATE de Relase* gera *error log ao efetuar o cadastro de relógio:* **Opção não disponível no Protheus Função: P0REPVLDCalled By {x,lResValid,o o := Self:aEntryCtrls[7],(lResValid := If(o:lModified .or. (o:Cargo <> NIL .and. o:Cargo <> M->P0\_REP),(P0RepVld() ),.T.)),(If(Type('lRefresh') == 'L' .and. lRefresh,Self:EnchRefreshAll(),)),lResValid}**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**  
O erro ocorre pois o fonte PONA030 está com a data do fonte do pacote de Expedição Contínua do Mercado Internacional.  
  
**Solução**  
Para solucionar o problema, será **necessário efetuar atualização do ambiente** com o pacote de expedição contínua abaixo, "aceitando fontes mais antigos"  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  
**Saiba mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
