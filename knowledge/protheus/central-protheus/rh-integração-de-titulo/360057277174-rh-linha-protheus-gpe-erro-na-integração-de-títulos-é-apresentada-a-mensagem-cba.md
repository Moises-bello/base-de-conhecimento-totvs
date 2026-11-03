---
article_id: 360057277174
category: RH - Integração de Titulo
content_hash: b2f434b9229c7e13dac9d39609dd343dd69d8bc3da304fb99e8bcc2e0e8ae9c5
fetched_at: '2026-06-28T22:43:36.311056+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos é apresentada a
  mensagem: cBancoAdt := < -- Invalido'
type: support-article
updated_at: '2026-06-10T13:08:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057277174-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-cBancoAdt-Invalido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33799140798743) Tempo aproximado para leitura: **00:01:30 min****

**Ocorrência**Na integração de títulos é apresentada a mensagem: cBancoAdt := < -- Invalido  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**Esse incidente ocorre, pois na rotina **Definição Títulos - GPEM640**, o campo Tipo de Titulo do mesmo foi parametrizado como **PA - Pagamento Antecipado** ao invés de **FOL** e os títulos do módulo **Gestão de Pessoal** não foram tratados para este tipo.   
  
**Solução**Erro apresentado: ![Falha_na_gravacao_cBancoAdt.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360097135814)

Para solucionar essa ocorrência: 

**Acessar:** SIGAGPE ->Miscelânea ->Títulos ->Definição  e Alterar o tipo de Titulo para **FOL** ou outro tipo cadastrado para uso no módulo Gestão de Pessoal:  
  
![defni__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360097135974)  
  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
