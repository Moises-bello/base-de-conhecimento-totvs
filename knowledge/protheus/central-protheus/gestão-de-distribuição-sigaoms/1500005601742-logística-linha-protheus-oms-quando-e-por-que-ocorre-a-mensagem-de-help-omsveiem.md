---
article_id: 1500005601742
category: Gestão de Distribuição (SIGAOMS)
content_hash: 856d4ba21b24895159762234e55671cf104351a9133090b414931d88fcad5ea5
fetched_at: '2026-06-28T22:45:50.113312+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Quando e por que ocorre a mensagem de help
  OMSVEIEMP
type: support-article
updated_at: '2021-08-12T10:17:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005601742-Log%C3%ADstica-Linha-Protheus-OMS-Quando-e-por-que-ocorre-a-mensagem-de-help-OMSVEIEMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura**: 00:00:54 min**  
**Ocorrência**Quando e por que ocorre a mensagem de **help OMSVEIEMP**, ao **associar o veículo** na rotina de **Montagem de Carga - OMSA200**?  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Causa**O **help OMSVEIEMP** ocorre quando o parâmetro **MV\_ALOCVEI está habilitado**.  
Este parâmetro indica se no **carregamento** o **veículo** será **alocado e reservado até o seu retorno**.  
Com este parâmetro é possível deixar um **veículo reservado**, impossibilitando o seu uso em outra carga, caso este seja solicitado. Ao tentar **associar o veículo** na rotina de **Montagem de Carga - OMSA200**, será apresentado o help abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007621921/mceclip0.png)

**Solução**Para que o **help OMSVEIEMP** não seja apresentado, realize os seguintes passos:  
1. Desabilite o parâmetro **MV\_ALOCVEI**;  
2. Estorne o processo da montagem de cargas que foi realizado anteriormente;  
3. Efetue as montagens de carga novamente.
