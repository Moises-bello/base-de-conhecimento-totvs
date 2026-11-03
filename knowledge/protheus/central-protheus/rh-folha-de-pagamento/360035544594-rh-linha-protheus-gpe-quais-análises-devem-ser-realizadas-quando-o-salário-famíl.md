---
article_id: 360035544594
category: RH - Folha de Pagamento
content_hash: e26868ed85135b801ee4bb84bfc39b15f736e59ca3ef666ba83148ea25666a03
fetched_at: '2026-06-28T22:44:16.195087+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Quais análises devem ser realizadas quando o Salário
  família não é apresentado no cálculo da folha
type: support-article
updated_at: '2025-08-11T21:41:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035544594-RH-Linha-Protheus-GPE-Quais-an%C3%A1lises-devem-ser-realizadas-quando-o-Sal%C3%A1rio-fam%C3%ADlia-n%C3%A3o-%C3%A9-apresentado-no-c%C3%A1lculo-da-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26331459461527) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Quais análises devem ser realizadas quando o Salário família não é apresentado no cálculo da folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
  
**Solução**Verifique os itens abaixo:  
- Observe se a idade do dependente ultrapassa os 14 anos no mês do cálculo da folha em **Atualizações > Funcionários > Dependentes (GPEA020)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331459466775)  
- Verifique a data Inicio e Final da tabela S003 em **Atualizações > Definições de Cálculos > Manutenção Tabelas (GPEA320)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331459469463)  
- Verifique o valor do **Teto** informado na tabela **S003**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331459471255)  
- Verifique configuração do parâmetro **MV\_SALFD** pelo configurador SIGACFG em **Ambiente > Cadastros > Parâmetros**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331468369047)  
- Verifique nos Tipos de Ausências (quando houver afastamento envolvido), a configuração do campo (Pg. Sal. Fam.) em **Atualizações > Definições de Cálculos > Tipo de Ausências (GPEA430)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331459475351)  
- Verifique se na configuração das verbas quais estão com SIM para Salário Família (Verbas de base deve estar com N) em **Atualizações > Definições de Cálculos > Verbas (GPEA040)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331459478423)  
- Verifique se as verbas de pagamento de salário ( Ids 0031/ 0032/ 0033/ 0041/ 0042) estão com Não no campo Salário Família. Esses identificadores obrigatoriamente já entram na base de cálculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26331468377239)

**Saiba mais:**[RH - Linha Protheus - GPE - O que verificar quando não é calculado salário família para afastado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056342-MP-GPE-O-que-verificar-quando-n%C3%A3o-%C3%A9-calculado-sal%C3%A1rio-fam%C3%ADlia-para-afastado?source=search)

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
