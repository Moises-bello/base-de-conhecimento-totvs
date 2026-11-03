---
article_id: 360011377811
category: Cálculo
content_hash: 34d55af3029d2d504d2b7b9b2a3441b012d37d938bf10e7c6605552be60fb9f7
fetched_at: '2026-06-28T22:46:29.271302+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular extra de feriado
type: support-article
updated_at: '2025-02-19T01:02:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011377811-RH-RM-PTO-Calcular-extra-de-feriado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17804581921943) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como fazer para considerar feriados no cálculo no espelho do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**Para que o sistema Automação de Ponto considere feriados no cálculo é necessário realizar algumas configurações/validações a partir das regras abaixo:

1. Ter o feriado desejado cadastrado no calendário, para avaliar acesse a documentação abaixo:  
   [Como cadastrar feriados no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011376011)
2. No cadastro de horário vinculado ao funcionário, na aba de Identificação, deve estar marcada a opção Considera Feriados no Cálculo;   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008463731)
3. No Parametrizador do Funcionário | Feriados estar marcada a flag Considera Feriado.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008426292)
