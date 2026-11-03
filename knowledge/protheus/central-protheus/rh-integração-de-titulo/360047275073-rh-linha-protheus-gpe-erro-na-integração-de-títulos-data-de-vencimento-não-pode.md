---
article_id: 360047275073
category: RH - Integração de Titulo
content_hash: 24874891e31c22ff9d5cdaa4fa06efb1b95ed63638d2e516974e136dbb59df2a
fetched_at: '2026-06-28T22:43:36.315241+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos: Data de vencimento
  não pode ser menor que a data de emissão'
type: support-article
updated_at: '2025-07-15T20:33:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047275073-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-Data-de-vencimento-n%C3%A3o-pode-ser-menor-que-a-data-de-emiss%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33489718934551)** Tempo aproximado para leitura: 00:03:00 min

**Ocorrência**Na integração de títulos é apresentada a mensagem: Erro na integração de títulos - Data de vencimento não pode ser menor que a data de emissão  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE – Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**1)Esse incidente ocorre, pois os campos da tabela SE2 (E2\_VENCTO e E2\_VENCREA) estão fora de ordem;  
2) A data de integração está menor que a data base do sistema.

**Solução:**Para solucionar essa ocorrência, realize os seguintes passos:  
  
Erro apresentado:  
**1) Campos da tabela SE2 (E2\_VENCTO e E2\_VENCREA) estão fora de ordem:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068019753)

Campos fora de ordem , gerando o erro:   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066949274)  
  
Acesse o configurador **Base de dados / Dicionário / Arquivos / Selecionar a tabela SE2 / Campos:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360066949454)**   
  
Altere a ordem dos campos **E2\_VENCTO e E2\_VENCREA** conforme print de tela abaixo:  
**Campo 12 -** E2\_VENCTO  
**Campo 13 -** E2\_VENCREA  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068031773)  
  
Em seguida, acesse a rotina de integração de títulos (Miscelânea -> Títulos -> Integração de títulos - rotina GPEM670) e refaça o processo de integração.

**2) A data de integração está menor que a data base do sistema.**A rotina do Contas a pagar na tabela SE2 faz uma validação no campo E2\_EMISSÃO , que impede a gravação de títulos com data inferior à data do sistema.   
  
**Exemplo:** Data base do sistema : 11/04/2023  
      Data vencimento do título: 06/04/2023  
Ao validar a entrada do título no financeiro, a rotina através do campo E2\_EMISSAO, entende que a data de emissão é maior que a data de vencimento e impede a gravação do título.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13769108359575)  
(figura - acessado na opção incluir).   
  
**Solução:**  
Retornar a data base do sistema de acordo com a data de emissão dos títulos ou integrar os títulos exatamente no dia que forem emitidos.

 Saiba Mais:  
[Página Centralizadora da Integração de títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
