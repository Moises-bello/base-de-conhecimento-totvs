---
article_id: 360052538013
category: Relatórios e Workflows
content_hash: 32698e6cb90bf232e509c1de1e267568e09c23536fcb9c1a9ce00e4b36116005
fetched_at: '2026-06-28T22:42:31.657143+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Conversão do indicador MTBF para dias
type: support-article
updated_at: '2021-06-17T19:13:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052538013-Manufatura-Linha-Protheus-MNT-Convers%C3%A3o-do-indicador-MTBF-para-dias
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura:**00:01:45 min**  
**Dúvida**Como é realizada a conversão do indicador **MTBF - Mean Time Between Failures** para **dias**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**Buscando disponibilizar uma melhor análise do indicador **MTBF** nos relatórios **MNTR360 - Análise MTBF/MTTR,** é disponibilizado o indicador convertido em **dias**. Para obtenção deste, podem ser considerados dois cenários:

* o primeiro onde é considerado o calendário do bem;
* o segundo onde não é considerado calendário do bem.

Com intuito de exemplificar como é realizado este processo de conversão, abaixo segue o exemplo de ambos cenários:  
  
**1 - Considera Calendário**Quando definido que o indicador deve considerar o calendário do equipamento no processo de conversão para dias, é realizado o cálculo de média do tempo de operação da máquina considerando uma semana:  
Conforme o cenário abaixo:  
Segunda a Sexta: 21:00 Hrs.  
Sábado: 19:40 Hrs.  
Domingo: 01:20 Hrs.  
  
Neste caso obtemos 126:00 de atuação em 7 dias,   
assim chegando a média de 18:00 dia.  
  
**MTBF em Horas** = 20:50 Hrs.  
**Méd. Hrs** = 18:00 Hrs.  
**MTBF em Dias** = **MTBF em Horas / Méd. Hrs**  
**MTBF em Dias** = 1.16 dias  
 **2 - Não Considera Calendário**Para os cenários onde não é considerado o **calendário do equipamento**, não é realizado cálculo para obter a média de tempo disponível por dia do mesmo. Assim sendo considerado que o mesmo está em operação **24 horas por dia**.  
Seguindo o mesmo exemplo:  
  
**MTBF em Horas** = 20:50 Hrs.  
**Méd. Hrs** = 24:00 Hrs.  
**MTBF em Dias** = **MTBF em Horas / Méd. Hrs**  
**MTBF em Dias** = 0.87 dias  
  
**Saiba mais**Verifique também a documentação relacionada ao indicador **MTBF** no artigo [Cálculo do indicador MTBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050761174)
