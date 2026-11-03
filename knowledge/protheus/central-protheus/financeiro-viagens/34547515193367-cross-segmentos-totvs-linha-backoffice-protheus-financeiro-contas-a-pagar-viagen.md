---
article_id: 34547515193367
category: Financeiro - Viagens
content_hash: 549b4f3d89d51601e700a73e44525761a84edfe894c920715cd2f37d9471268c
fetched_at: '2026-06-28T22:38:21.520904+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - TOTVS Linha Backoffice Protheus - Financeiro - Contas a Pagar
  - Viagens - Falha na gravação automatica - AJUDA:ERROR_PCO.
type: support-article
updated_at: '2025-09-01T20:59:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34547515193367-Cross-Segmentos-TOTVS-Linha-Backoffice-Protheus-Financeiro-Contas-a-Pagar-Viagens-Falha-na-grava%C3%A7%C3%A3o-automatica-AJUDA-ERROR-PCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34547515128727) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao efetuar a geração de titulos relacionados a adiantamentos ou prestação de contas com integração ao PCO, ocorre a mensagem de bloqueio - **AJUDA:ERROR\_PCO**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34547515131287)  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse cenário ocorre, pois quando usamos rotinas que são acionadas através de ExecAutos, exemplo do **FINA050 - Contas a Pagar**, não possuem intervenção de usuário, ou seja, o usuário não poderá ajustar a contigencia ou ver os detalhes em tempo de processamento diferente da rotina **FINA050 manualmente.**  
  
**Imagem de exemplo, no processo manual da FINA050 com bloqueio de saldos**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34547515133591)

Portando, ao processar contas a pagar de origem do Viagens com integrações de outros modulos, a configuração deve estar de acordo para a inclusão automatica, sem intervenção do usuário, ou seja, o PCO precisa estar devidamente configurado sem bloqueio de saldos afim de executar o processo automaticamente;  
  
**Solução**  
Acesse o PCO e ajuste a informação apresenta no HELP do Viagens, como exemplo, tivemos um problema de saldo previsto x realizado, então neste caso, antes de gerar o contas a pagar, deve ajustar o saldo previsto no PCO - Modulo 57  
  
**Saiba mais**  
[**Viagens - Financeiro - P12**](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)  
[**Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Como realizar a integração entre os módulos do Protheus com o PCO.**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19496129058455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Como-realizar-a-integra%C3%A7%C3%A3o-entre-os-m%C3%B3dulos-do-Protheus-com-o-PCO)
