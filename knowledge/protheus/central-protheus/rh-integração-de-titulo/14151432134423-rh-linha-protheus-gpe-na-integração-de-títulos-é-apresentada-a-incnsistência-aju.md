---
article_id: 14151432134423
category: RH - Integração de Titulo
content_hash: d80e51fa8bab8396c02bdc6ca39e5e462a3743586503653d948a1c8c35fd5462
fetched_at: '2026-06-28T22:43:36.376511+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na integração de títulos é apresentada a incnsistência:
  AJUDA : REGBLOQ Este Registro está boqueado para uso'
type: support-article
updated_at: '2025-07-15T20:36:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14151432134423-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-incnsist%C3%AAncia-AJUDA-REGBLOQ-Este-Registro-est%C3%A1-boqueado-para-uso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao realizar a integração de títulos, é apresentada a incnsistência: "AJUDA : REGBLOQ Este Registro está boqueado para uso".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14149285394071)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Este incidente ocorre quando o cadastro do Fornecedor do Título está bloqueado.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o Módulo 04 - Estoque/Custos / Atualizações / Cadastros / Fornecedores (MATA020), localize o fornecedor e clique em Alterar;  
  
2. Altere o conteúdo do campo "Bloqueado" (A2\_MSBLQL) para Não e clique em Confirmar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14150989154071)  
  
3. Acesse o Módulo 07 - Gestão de Pessoal / Miscelanea / Títulos / Manutenção (GPEM660), localize o Título que apresentou a inconsistência e clique em Alterar;  
  
4. Altere o conteúdo do campo "Integ. Financ" (RC1\_INTEGR) de 2 - Inconsistente para 0 - Não Liberado e clique em Confirmar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14151147638551)

4. Acesse Miscelanea / Títulos / Integração Financeiro (GPEM670), e preencha as perguntas para integração do titulo e o título será integrado corretamente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14151247454615)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14151275939095)

**Saiba Mais:**[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
