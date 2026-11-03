---
article_id: 4403566376215
category: RH - Soluções para error.log
content_hash: 441e88b6faadc0b7a312359c0dda817a7ce662c4a11bf7b683420ce7319ae142
fetched_at: '2026-06-28T22:44:09.065104+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Erro em várias rotinas do GPE - invalid property
  LORDERSEEKLOAD on {|x|self:LORDERSEEKLOAD := x}(FWSERIALIZE.PRW)
type: support-article
updated_at: '2025-09-11T20:07:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566376215-RH-Linha-Protheus-GPE-Erro-em-v%C3%A1rias-rotinas-do-GPE-invalid-property-LORDERSEEKLOAD-on-x-self-LORDERSEEKLOAD-x-FWSERIALIZE-PRW
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34878406940695) Tempo aproximado para leitura: 00:01:30 min**

**Ocorrência**Ao tentar utilizar Rotinas do módulo de Gestão de Pessoal, gera *error log*: "***invalid property* LORDERSEEKLOAD *on* {|x|self:LORDERSEEKLOAD := x}(FWSERIALIZE.PRW)**" **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre por algum erro no **profile** do usuário e falta de atualização de pacote de **LIB**.  
**Solução**Para correção do erro é necessário:  
**1.** Efetuar a manutenção de profile do usuário com problemas, conforme documentação abaixo:  
[MP - FRAME - Manutenção de Profile de Usuários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025097012-MP-FRAME-Manuten%C3%A7%C3%A3o-de-Profile-de-Usu%C3%A1rios?source=search)  
**2.** Efetuar atualização de pacote de LIB (caso esteja desatualizada):  
<https://suporte.totvs.com/portal/p/10098/download?#000006/368/TFLIB/>

**Saiba Mais:**[RH - Soluções Error Log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log)   
Pacote de expedição contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
