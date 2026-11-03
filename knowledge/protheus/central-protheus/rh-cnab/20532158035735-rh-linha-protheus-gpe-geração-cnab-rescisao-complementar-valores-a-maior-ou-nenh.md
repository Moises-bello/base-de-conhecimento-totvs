---
article_id: 20532158035735
category: RH - CNAB
content_hash: 8d95316d673d3f976d3c7596d6c5047db30bbcbf5dea2a9b443529953789d7b1
fetched_at: '2026-06-28T22:43:39.257661+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Geração CNAB Rescisao Complementar, Valores a Maior
  ou Nenhum Registro Processado
type: support-article
updated_at: '2025-06-16T14:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20532158035735-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-CNAB-Rescisao-Complementar-Valores-a-Maior-ou-Nenhum-Registro-Processado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20532158006295)**Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar arquivo CNAB sistema retorna: Nenhum Registro Processado com os Parâmetros informados!   
ou Sistema traz no CNAB o valor da rescisão original + Complementar.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
   
**Causa**  
É apresentada esta inconsistência quando informado na rescisão complementar os mesmos dados da rescisão Original - Campo: Data de homologação.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o calculo da Rescisão - Miscelânea > Cálculos > Rescisão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20533736326679)  
  
Para que seja gerado um CNAB da Rescisão Complementar, o correto é deixar a data de Homologação (pagamento) diferente da Data da Rescisão Original:  
![](https://totvssuporte.zendesk.com/attachments/token/YANURYSQgY850w8WRfVbKRykx/?name=image.png)  
  
Desta forma, você pode selecionar o mesmo roteiro, alterando apenas a data de pagamento, para que seja gerada apenas da rescisão complementar.  
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
