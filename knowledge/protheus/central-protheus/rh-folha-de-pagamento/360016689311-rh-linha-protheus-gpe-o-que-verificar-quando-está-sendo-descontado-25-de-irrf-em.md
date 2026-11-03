---
article_id: 360016689311
category: RH - Folha de Pagamento
content_hash: efc1c060976edc038cc6d9ada18be10af227d82b4d2b6ec335f628d8bc8a387f
fetched_at: '2026-06-28T22:44:11.913890+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  O que verificar quando está sendo descontado 25%
  de IRRF em funcionário que não reside no exterior
type: support-article
updated_at: '2024-09-10T20:04:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016689311-RH-Linha-Protheus-GPE-O-que-verificar-quando-est%C3%A1-sendo-descontado-25-de-IRRF-em-funcion%C3%A1rio-que-n%C3%A3o-reside-no-exterior
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26280433286551) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O que verificar quando na folha de pagamento de um funcionário que não reside no exterior, está gerando desconto de 25% de IRRF na folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa:**  
![kcs_03102018_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012694212)  
  
**Solução**Verificar dentro do cadastro de funcionários (SRA) em **Atualizações > Funcionários > Funcionários (GPEA010)**, na aba **Estrangeiro** o campo Res. Exterior (RA\_RESEXT), e altere o preenchimento para **Não**.   
  
![KCS_03102018.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012696031)  
  
Após alteração do referido campo, é necessário fazer o recálculo da folha que a verba de IRRF automaticamente será calculada conforme a tabela S002 onde se houver base para IRRF haver desconto, no exemplo abaixo não houve desconto pois não havia base para IRRF para cálculo na folha de pagamento.  
  
![kcs_03102018_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360012694232)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
