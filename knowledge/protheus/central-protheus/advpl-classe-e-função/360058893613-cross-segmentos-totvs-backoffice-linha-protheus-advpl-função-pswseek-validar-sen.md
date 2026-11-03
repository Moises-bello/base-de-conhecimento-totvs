---
article_id: 360058893613
category: ADVPL - Classe e Função
content_hash: 329ffb1c97bab1546dafe7d9ded9e0ae9cf1c472f3f6d31d69f5db8541157cdd
fetched_at: '2026-06-28T22:40:19.447676+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função Pswseek:  Validar
  Senha'
type: support-article
updated_at: '2022-08-18T02:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058893613-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Pswseek-Validar-Senha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**  
A função Psweek() não está validando quando é na ordem senha, como fazer para validar por senha?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A função **Pswseek()** somente tinha este comportamento na **versão 10** do sistema. A partir da versão **versão 11** ela parou de avaliar a senha do usuário, pois tratar-se de falha de **segurança**.  
Não existe hoje no Protheus nenhuma api que informe se a senha do usuário está correta.
