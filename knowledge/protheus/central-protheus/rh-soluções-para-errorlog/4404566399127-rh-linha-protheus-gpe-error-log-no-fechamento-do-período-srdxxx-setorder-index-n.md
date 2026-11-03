---
article_id: 4404566399127
category: RH - Soluções para error.log
content_hash: efc6f2719256f95e2c6c580437886fff6f2c7ae7d3bb8b061f3294312cae9915
fetched_at: '2026-06-28T22:44:09.113561+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log no Fechamento do Período - SRDXXX: SetOrder
  - Index not found. on GPM120THREAD(GPEM120.PRX'
type: support-article
updated_at: '2024-04-08T19:49:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404566399127-RH-Linha-Protheus-GPE-Error-log-no-Fechamento-do-Per%C3%ADodo-SRDXXX-SetOrder-Index-not-found-on-GPM120THREAD-GPEM120-PRX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22657068201751)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar efetuar o **Fechamento do Período**, através da rotina **GPEM120**, gera *error log*: "**SRDXXX: *SetOrder - Index not found. on* GPM120THREAD(GPEM120.PRX)**"**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre devido à ordenação dos campos e índices da tabela **SRD** estarem incorretos  
  
**Solução**Para que o erro não ocorra mais será necessário efetuar backup da tabela **SRD** e deixá-la no padrão, conforme abaixo:  
Índices:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22657043965207)  
  
Campos:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22657043984663)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22657068244887)  
*\*Após a manutenção da tabela, será necessário recriá-la*Ou ainda, realizar o procedimento de recriação da tabela em formato de Dicionário Padrão, conforme o link abaixo demonstra:  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057637274](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057637274-RH-Linha-Protheus-GPE-Como-criar-dicion%C3%A1rio-padr%C3%A3o-em-meu-ambiente)  
  
**Informações complementares**  
Pacote de Expedição Contínua do Gestão de Pessoal: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
Pacote Acumulado e-Social: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234> 

**Saiba Mais:**

RH - Linha Protheus - GPE - Como realizar o fechamento mensal de determinado período da folha <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027259971?source=search>

RH - Linha Protheus - GPE - Após fechamento do período, Sistema não atualiza status para Fechado no cadastro de períodos: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414532770711?source=search>

RH - Linha Protheus - GPE - Melhoria de performance no fechamento mensal com MV\_CALCTHD ativo: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050884333?source=search>

RH - Linha Protheus - GPE - Implementação de GRID no Fechamento de Período: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/19124711142679?source=search>

RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o fechamento do período: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/9070502632343?source=search>

RH - Linha Protheus - GPE - Ao realizar Fechamento de Período ocorre error log - variable does not exist P\_DECFALT on GETAFFALTA: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403544039831?source=search>

RH - Linha Protheus - GPE - Erro ao efetuar fechamento da folha: type mismatch on .AND. on GP120FECRES(GPEM120.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063752353?source=search>

RH - Linha Protheus - GPE - Error log ao Realizar o Fechamento de Período: Access Violation in function TDIALOG:ACTIVATE on FSRATHREAD(GPEM120.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057807414?source=search>

RH - Linha Protheus - GPE - Error log no fechamento do roteiro array out of bounds ( XX of XX ) on FGRAVATRANS(GPEM120.PRX) : <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021143092?source=search>

RH - Linha Protheus - GPE - Error log no fechamento do período - array out of bounds ( 0 of 0 ) on GP120FECFOL(GPEM120.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406105473303?source=search>

RH - Linha Protheus - GPE - Error log ao efetuar fechamento da folha - type mismatch on .AND. on FCALADT(GPEXCADI.PRX): <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042764993?source=search>

RH - Linha Protheus - GPE - Error log ao efetuar fechamento: "argument #0 error, expected D->U, function dtos on FPROCTRANS(GPEM120.PRX)": <https://centraldeatendimento.totvs.com/hc/pt-br/articles/5176693642391?source=search>
