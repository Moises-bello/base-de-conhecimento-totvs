---
article_id: 360056822674
category: RH - Integração de Titulo
content_hash: 6726f870648ecdae52fc0b053d1727eda3574cc1e29d422eab11b4af99a91852
fetched_at: '2026-06-28T22:43:36.387254+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Na integração de títulos é apresentada a mensagem:
  E2_PREFIXO:= GPE<-- Inválido'
type: support-article
updated_at: '2025-07-15T18:08:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056822674-RH-Linha-Protheus-GPE-Na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-E2-PREFIXO-GPE-Inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16175113510807)**Tempo aproximado para leitura: 00:02:00 min**Ocorrência**Na integração de títulos é apresentada a mensagem: E2\_PREFIXO:= GPE<-- Inválido **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096455074)  
  
Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todos os Releases  
  
**Causa**Esse incidente ocorre quando o Cadastro do Fornecedor atrelado à Definição do Título está Bloqueado.

**Solução**  
1. Passo: Acesse o Módulo Ativo Fixo (SIGAATF) / Atualizações / Cadastros / Fornecedores (MATA020), Selecione o fornecedor atrelado na Definição do Título e clique em Alterar;

2. Passo: Verifique se o campo "Bloqueado" (A2\_MSBLQL) está preenchido com Sim, como no exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16174589148183)

3. Passo. Altere o conteúdo do campo "bloqueado" para "**2 - Não**" e clique em Confirmar.

4. Passo. Acesse o módulo Gestão de Pessoal (SIGAGPE) / Miscelanea / Títulos / Manutenção (GPEM660)/ Localize o Título que gerou a inconsistência e clique em Alterar;

5. Passo. Altere o campo "integ. Financ." (RC1\_INTEGR) para "**0 - Não Liberado**" e clique em Salvar;

6.Passo. Acesse Miscelanea / Títulos / Manutenção (/ Integração Financeiro (GPEM670) e Prossiga com a integração do Título.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como integrar títulos do Gestão de Pessoal com o Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037639133)   
[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
