---
article_id: 11338622440983
category: GPE - eSocial - Processo Trabalhista
content_hash: 1d83e2fbd55d22a01bea21a80de9a25780bd2958065b358669b68a09bb6bdabf
fetched_at: '2026-06-28T22:45:00.706536+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Ocorrência 282 Número do processo
  judicial invalido
type: support-article
updated_at: '2024-06-26T14:40:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11338622440983-RH-Linha-Protheus-GPE-eSocial-S-2500-Ocorr%C3%AAncia-282-N%C3%BAmero-do-processo-judicial-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18677178780311) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Código da ocorrência 282: Número do processo judicial invalido. Verifique se as informações do número do processo e tipo do processo estão corretas.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11338325554711)  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre porque o leiaute S-1.2 para o evento S-2500 determina que o número do processo deve ser formado por **20 algarismos se origem = 1**. Se for **origem 2, deve ter 15 algarismos**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11338334173079)  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique no xml do evento S-2500 a origem e quantos algarismos contem no número do processo. Exemplo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11338424558871)  
  
2. Acesse a rotina Processos (APTA100), Atualizações - Processos Trabalhistas - Processos - Processos  
Informe o número do processo deve ser formado por **20 algarismos se origem = 1**. Se for **origem 2, deve ter 15 algarismos**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18677149223191)

3. Verifique a rotina de cadastro de Processo Trabalhista para realizar a alteração  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18677149229207)  
  
3. Gere novamente o evento S-2500 e envie o eSocial  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11338529922583)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
