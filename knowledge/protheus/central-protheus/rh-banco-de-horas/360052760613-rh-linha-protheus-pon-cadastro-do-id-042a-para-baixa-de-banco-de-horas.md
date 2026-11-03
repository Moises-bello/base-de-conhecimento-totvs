---
article_id: 360052760613
category: RH - Banco De Horas
content_hash: df226ea792b3bb70ae0b1b6641d3387b33b4065f627907d0cef7c62b561812e1
fetched_at: '2026-06-28T22:44:54.188838+00:00'
product: protheus
section_id: 32405029751063
source: central-protheus
title: RH - Linha Protheus - PON - Cadastro do ID 042A para Baixa de Banco de Horas
type: support-article
updated_at: '2025-06-16T19:53:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052760613-RH-Linha-Protheus-PON-Cadastro-do-ID-042A-para-Baixa-de-Banco-de-Horas
---

**Ocorrência**Quando é processado o Fechamento de Banco de Horas, é gerado *log* informando que não existe evento vinculado ao ID de Ponto 042A   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084394853/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Este problema ocorre pois não foi feito o cadastro de evento vinculando o ID de Ponto 042A.  
O Identificador de cálculo **042A** diz respeito a quantidade de meses referente a banco de horas, ele existe para informar na RAIS – Relatório Anual de Informações Sociais, a quantidade de meses referente a banco de horas que foram pagos em folha ou rescisão. Este evento deve ser do tipo **Base Provento**, e deve estar vinculado a um **Código pra Folha** (verba) de **Base Provento**, **tipo Horas** e na pasta banco de horas este evento deve estar com “**N****ão**” para banco de horas.  
  
**Solução**Realizar o cadastro de um novo evento associando o ID de Ponto 042A. Após o cadastro, basta processar o Fechamento de Banco de Horas novamente.  
  
**Saiba Mais:**  
[RH - Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206956208-RH-Ponto-Eletr%C3%B4nico)
