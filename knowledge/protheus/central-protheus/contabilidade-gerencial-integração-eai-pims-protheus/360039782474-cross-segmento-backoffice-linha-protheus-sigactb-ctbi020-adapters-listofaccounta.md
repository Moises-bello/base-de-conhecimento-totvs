---
article_id: 360039782474
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: 791f9088615457bff0ca2dbf65ee8529d2a30b6a8946fae69026634f0f093921
fetched_at: '2026-06-28T22:40:54.133066+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBI020 -  Adapters ListofAccountantAccount
  e AccountantAccount
type: support-article
updated_at: '2022-06-10T23:13:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039782474-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBI020-Adapters-ListofAccountantAccount-e-AccountantAccount
---

**Dúvida**Qual a diferença entre o *Adapters **ListofAccountantAccount*** e o***AccountantAccount*** para a integração do Plano de Contas no Protheus?  
   
 **Ambiente**Protheus - Contabilidade Gerencial - A partir da versão 12.1.17  
  
**Solução**A diferença entre os *Adapters* ***ListofAccountantAccount*** e o ***AccountantAccount*** é o módulo em que deseja realizar a integração do Plano de Contas no Protheus, onde:

1- ***AccountantAccount*** gera as informações na tabela **CT1**(Plano de Contas) do módulo **SIGACTB**(Contabilidade Gerencial), devendo configurar a mensagem para a rotina **CTBA020** conforme a documentação: [Como configurar a mensagem ACCOUNTANTACCOUNT](https://tdn.totvs.com/pages/releaseview.action?pageId=268816283)

2- ***Listofaccountantaccount*** gera informações na tabela **GUE**(Conta Contábil) do módulo **SIGAGFE**(Gestão de Frete Embarcador), devendo cadastrar o *Adapter* informando a rotina **GFEA090**.​ Para mais detalhamento sobre esta mensagem, pode-se entrar em contato com o suporte do módulo Gestão de Frete Embarcador.

Conforme orientação encaminhada na *issue* DSERCTR1-24718 a Controladoria Protheus utiliza APENAS a mensagem AccountantAccount para integração do Plano de Contas Contábeis com as demais marcas Totvs.

Veja mais sobre Integração:

[MP-SIGACTB-AdaptersDeItengracaoContabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018892132-MP-SIGACTB-QUAIS-S%C3%83O-OS-ADAPTER-s-DE-INTEGRA%C3%87%C3%83O-DA-CONTABILIDADE-)

[CamadaEAI](https://tdn.totvs.com/display/framework/A+camada+do+EAI)
