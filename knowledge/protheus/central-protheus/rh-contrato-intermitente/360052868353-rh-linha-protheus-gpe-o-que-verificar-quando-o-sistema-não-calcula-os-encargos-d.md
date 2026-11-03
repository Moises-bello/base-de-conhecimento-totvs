---
article_id: 360052868353
category: RH - Contrato Intermitente
content_hash: e1770682ccbec2c9d79cde1ee2e5ef905fa585625ff8c77dac52e17f3acab0d3
fetched_at: '2026-06-28T22:43:40.121301+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando o sistema não calcula os
  encargos de INSS para funcionário intermitente
type: support-article
updated_at: '2025-04-15T17:56:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052868353-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-sistema-n%C3%A3o-calcula-os-encargos-de-INSS-para-funcion%C3%A1rio-intermitente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25966135655447)** Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O que verificar quando o Sistema não calcula as verbas de INSS parte empresa, acidente de trabalho ou terceiros para funcionário em contrato intermitente?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O Sistema busca esses percentuais das **Tabelas S037** e **S038** da rotina **Manutenção de Tabelas**e considera o funcionário em contrato intermitente ,como **Tipo de Contrato** 2 nessas tabelas. Então para que o Sistema calcule o **INSS parte empresa**, **INSS acidente de trabalho** e **INSS terceiros**, é necessário ter o **Tipo de Contrato** 2 relacionado nessas tabelas, conforme abaixo:  
  
**Tabela S037**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083767454)  
  
**Tabela S038** - Para a Tabela S038, se o campo **Tipo de Contrato** estiver vazio, o sistema considera essa mesma linha para o **Tipo de Contrato** 1 e 2:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084935793)  
  
  
**Saiba Mais**

[Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
