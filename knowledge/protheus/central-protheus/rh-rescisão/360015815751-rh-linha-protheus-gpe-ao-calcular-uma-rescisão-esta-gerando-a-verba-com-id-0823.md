---
article_id: 360015815751
category: RH - Rescisão
content_hash: 922e62ee3760f32578be73b6e707f776f132ecd1e1a0015aacf67467f1124ee5
fetched_at: '2026-06-28T22:43:48.464834+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular uma rescisão esta gerando a verba com
  ID 0823 - FGTS Recuperar Salário, como ajustar
type: support-article
updated_at: '2026-06-25T12:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015815751-RH-Linha-Protheus-GPE-Ao-calcular-uma-rescis%C3%A3o-esta-gerando-a-verba-com-ID-0823-FGTS-Recuperar-Sal%C3%A1rio-como-ajustar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33712386413463) Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência** **GPEM040** - Ao calcular uma rescisão esta gerando a verba com ID 0823 - FGTS Recuperar Salário, como ajustar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - Versão 12  
  
**Solução**O identificador de cálculo 0823 é gerado quando a base de **FGTS - Fundo de Garantia por Tempo de Serviço**, do salário é negativa e a base de **FGTS** do 13º salário não.  
O sistema gera essa verba apenas para fazer o acerto no **FGTS** recolhido na **GRRF - Guia de Recolhimento Rescisório do FGTS**, onde ele abate da base positiva (por exemplo do 13º salário) a base negativa da folha.  
  
Isso acontece quando o funcionário tem pouco saldo de salário a receber por exemplo e a quantidade de descontos com incidência de **FGTS** é grande.  
  
Apesar de termos criado este tratamento não aconselhamos que seja usado sem antes consultar a Caixa Econômica Federal ou seu jurídico. O tratamento foi desenvolvido a muito anos, com base numa interpretação bem específica da lei, apresentada por um de nossos clientes, mas pouco praticada pelas empresas, principalmente por ser um tratamento pontual da **GRRF**, sem que seja possível fazer a declaração transparente na **SEFIP - Sistema Empresa de Recolhimento do FGTS**, pois a **SEFIP** não prevê envio de base de **FGTS** negativa. Desta forma, terá uma Guia de Recolhimento que não bate com a declaração, pois na declaração, quando a base der negativa, somos forçados, por orientação no manual e layout, levar 0,00.  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE0869 - Ao calcular uma rescisão esta gerando a verba com ID 0823 - FGTS Recuperar Salário, como ajustar?](http://tdn.totvs.com/pages/viewpage.action?pageId=403745490)

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
