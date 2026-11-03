---
article_id: 19669423785367
category: SIGAEST - INTEGRAÇÕES
content_hash: 2ede07f660b661b2ed4e022205f8f1b9b434efecb272ebe14781242068e7cc5f
fetched_at: '2026-06-28T22:38:46.242344+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração Quírons
  x Protheus - Erro "Erro ao integrar com o estoque: {"ReturnContent":{"Error":"AJUDA:D3_TM"'
type: support-article
updated_at: '2024-10-10T19:53:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19669423785367-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-Qu%C3%ADrons-x-Protheus-Erro-Erro-ao-integrar-com-o-estoque-ReturnContent-Error-AJUDA-D3-TM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19669380128663) Tempo aproximado para leitura: **00**:**02:00 min****Ocorrência**

Quando possuir integração Quírons x Protheus, ao tentar realizar uma entrega de um produto no sistema do Quírons ocorre o erro abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19669389273751)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Esse incidente pode ocorrer por dois motivos:

* Não possuir o parâmetro **MV\_MTI241S** configurado no ambiente do sistema Protheus.
* Possuir o parâmetro no Protheus com o conteúdo vazio, ou com um código de TM diferente de 599

**Solução**

Para solucionar essa ocorrência, deve criar no ambiente Protheus o parâmetro **[MV\_MTI241S](https://tdn.totvs.com/display/public/PROT/PEST052+-+MV_MTI241S+-+Tipo+de+Movimento+EAI)** conforme informado na documentação do mesmo, e informar **um código de TM de saída que você possua em seu ambiente.**

**OBS:** Para cenários de movimentação de entrada onde ocorra o mesmo erro no Quírons deverá validar o mesmo processo, porém, com o parâmetro [**MV\_MTI241E**](https://tdn.totvs.com/display/public/PROT/PEST051+-+MV_MTI241E+-+Tipo+de+Movimento+EAI) **onde o código deve ser 399**.

***Saiba mais:***

[Integração | Protheus x Quírons](https://tdn.totvs.com/pages/viewpage.action?pageId=653566644)
