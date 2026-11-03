---
article_id: 8371752460055
category: ADVPL - Classe e Função
content_hash: 212f054cebd8556985f2ec2b5783e7f5a617dd13eb92e7d4cb304c3e71b1b04b
fetched_at: '2026-06-28T22:40:18.254006+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -função FWGetRunSchedule
  compilada em TLpp não funciona.
type: support-article
updated_at: '2022-08-23T18:06:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8371752460055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-fun%C3%A7%C3%A3o-FWGetRunSchedule-compilada-em-TLpp-n%C3%A3o-funciona
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**A função **FWGetRunSchedule** compilada em **TLpp** sempre retornar **.F.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Exemplo**

A função **FWGetRunSchedule** retornará sempre **.F.** (Falso) no **TLpp**, pois o **TLpp** não realiza a chamada das funções estáticas

Exemplo a função estática **SchedDef**, o sistema executa a rotina como um processo específico, como se fosse um *job*, caso seja montado um fonte .**prw** mas nome do fonte diferente do nome da função, o cenário seria o do **TLpp,** pois necessita ter o mesmo nome do .**prw**  para que seja passada a instrução para função que executa internamento funções estáticas em outros fontes.

**Solução**

Atualmente o **TLpp** não realiza a chamada das funções estáticas.

Por tanto para uso em Schedule recomenda-se utilizar funções **AdvPL**(.**prw**).  
  
**Saiba Mais**

[**TL++**](https://tdn.totvs.com/pages/viewpage.action?pageId=334340072)

**[SchedDef e FWGetRunSchedule](https://tdn.totvs.com/pages/releaseview.action?pageId=271167961)**
