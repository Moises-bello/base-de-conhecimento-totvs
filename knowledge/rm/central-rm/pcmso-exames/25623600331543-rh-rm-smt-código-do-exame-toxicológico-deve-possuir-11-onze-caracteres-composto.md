---
article_id: 25623600331543
category: PCMSO / Exames
content_hash: cd94af45c834b2e705705aa65e60f4da5f85f201c3655265acb32e3a1b1d25ac
fetched_at: '2026-06-28T22:47:42.094442+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT - Código do exame toxicológico deve possuir 11 (onze) caracteres,
  composto por duas letras (dois primeiros caracteres) e nove algarismos (últimos
  nove caracteres).
type: support-article
updated_at: '2025-09-19T19:23:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25623600331543-RH-RM-SMT-C%C3%B3digo-do-exame-toxicol%C3%B3gico-deve-possuir-11-onze-caracteres-composto-por-duas-letras-dois-primeiros-caracteres-e-nove-algarismos-%C3%BAltimos-nove-caracteres
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25623555720855) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao incluir o exame toxicológico e informar o código do exame, a seguinte mensagem de erro é exibida:  
  
*'Código do exame toxicológico deve possuir 11 (onze) caracteres, composto por duas letras (dois primeiros caracteres) e nove algarismos (últimos nove caracteres)'*  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - **TOTVS Segurança e Saúde Ocupacional** - A partir das versões **12.1.2310.233, 12.1.2402.181, 12.1.2406.114** e superiores.  
  
**Causa**O erro ocorre quando o código do exame informado não segue o padrão definido pelo Leiaute, no qual deve conter **duas letras (dois primeiros caracteres) e nove algarismos (últimos nove caracteres)**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623555723543)  
  
**Solução**Para que o erro não ocorra, é necessário informar o código do exame conforme solicitado no Leiaute do eSocial.  
  
Segue um exemplo de como o código do exame toxicológico deve estar no sistema para geração do evento S-2221 para melhor entendimento:  
  
***AA123456789***Lançamento do exame toxicológico através do Prontuário Médico: ***![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623600298775)***Lançamento do exame toxicológico quando utiliza-se o parâmetro **'Controlar o registro de Exames Toxicológicos no TOTVS Folha de Pagamento (Labore)':** ***![](https://centraldeatendimento.totvs.com/hc/article_attachments/25623555727511)*****Importante**

Somente os exames com datas superiores a 01/08/2024 possuem este padrão de código solicitado pelo eSocial. Além disso, apenas os exames iguais ou posteriores à esta data serão aceitos neste evento.**Saiba mais**

- [RH - RM - SMT - Gerar o evento S-2221 - Exame Toxicológico do Motorista Profissional Empregado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30323268699927)- [RH - RM - SMT - Evento S-2221 - Exame Toxicológico do Motorista Profissional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24912970647703)
