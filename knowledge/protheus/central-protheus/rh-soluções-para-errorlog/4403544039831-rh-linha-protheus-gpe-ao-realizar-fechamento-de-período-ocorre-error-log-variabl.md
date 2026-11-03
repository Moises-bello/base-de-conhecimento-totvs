---
article_id: 4403544039831
category: RH - Soluções para error.log
content_hash: 8f652a9f3bd1a6e9947771e205c6695d931780c2ab5f11eefabe2593e353e2d9
fetched_at: '2026-06-28T22:44:08.770649+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Ao realizar Fechamento de Período ocorre error
  log - variable does not exist P_DECFALT on GETAFFALTA
type: support-article
updated_at: '2024-04-01T14:09:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403544039831-RH-Linha-Protheus-GPE-Ao-realizar-Fechamento-de-Per%C3%ADodo-ocorre-error-log-variable-does-not-exist-P-DECFALT-on-GETAFFALTA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22405737682071) Tempo aproximado para leitura:**00:02:00** min **Ocorrência**Ao realizar o **Fechamento de Período**, através da rotina **GPEM120**, é apresentado o *error log*: *"**variable does not exist*** **P\_DECFALT** ***on*** **GETAFFALTA(GPEM120.PRX)***"*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Este erro ocorre devido à falta do Mnemônico **P\_DECFALT**carregado no ambiente  
  
**Solução**  
**1.** Para solucionar essa ocorrência, necessário garantir que o Sistema esteja atualizado com o pacote abaixo:  
Expedição Contínua do Gestão de Pessoal: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
 **2.**Acesse o módulo do GPE, na rotina de **Cadastros/Definição de Cálculo/Mnemônicos** para que o Mnemônico **P\_DECFALT**seja criado;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22405737694871)  
  
**3.** Verifique se o erro ainda é apresentado.  
  
**Informações complementares**Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)

**Saiba Mais:**

RH - Linha Protheus - GPE - Como realizar o fechamento mensal de determinado período da folha <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259971?source=search>

RH - Linha Protheus - GPE - Após fechamento do período, Sistema não atualiza status para Fechado no cadastro de períodos: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414532770711?source=search>

RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333?source=search>

RH - Linha Protheus - GPE - Implementação de GRID no Fechamento de Período: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/19124711142679?source=search>

RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o fechamento do período: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/9070502632343?source=search>

RH - Linha Protheus - GPE - Ao realizar Fechamento do Período ocorre error log - variable does not exist P\_DECFALT on GETAFFALTA: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403221266071?source=search>

RH - Linha Protheus - GPE - Implementação do Multi Thread no fechamento da folha: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034908554?source=search>

RH - Linha Protheus - GPE - Por que rotina de fechamento apresenta roteiros com a legenda vermelha: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051753333?source=search>

RH - Linha Protheus - GPE - Erro ao efetuar fechamento da folha: type mismatch on .AND. on GP120FECRES(GPEM120.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063752353?source=search>

RH - Linha Protheus - GPE - Error log no Fechamento do Período - SRDXXX: SetOrder - Index not found. on GPM120THREAD(GPEM120.PRX: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404566399127?source=search>

RH - Linha Protheus - GPE - Error log ao Realizar o Fechamento de Período: Access Violation in function TDIALOG:ACTIVATE on FSRATHREAD(GPEM120.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057807414?source=search>

RH - Linha Protheus - GPE - Error log no fechamento do roteiro array out of bounds ( XX of XX ) on FGRAVATRANS(GPEM120.PRX) : <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021143092?source=search>

RH - Linha Protheus - GPE - Error log no fechamento do período - array out of bounds ( 0 of 0 ) on GP120FECFOL(GPEM120.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406105473303?source=search>

RH - Linha Protheus - GPE - Error log ao efetuar fechamento da folha - type mismatch on .AND. on FCALADT(GPEXCADI.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042764993?source=search>

RH - Linha Protheus - GPE - Error log ao efetuar fechamento: "argument #0 error, expected D->U, function dtos on FPROCTRANS(GPEM120.PRX)": <https://centraldeatendimento.totvs.com/hc/pt-br/articles/5176693642391?source=search>
