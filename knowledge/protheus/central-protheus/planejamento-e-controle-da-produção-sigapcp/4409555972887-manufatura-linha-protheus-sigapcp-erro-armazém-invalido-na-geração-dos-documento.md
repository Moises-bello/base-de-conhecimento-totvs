---
article_id: 4409555972887
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 54990d205606045aa1bb6829e14383f763f7d15b6c6804b0c9cab69e76f6f8e9
fetched_at: '2026-06-28T22:42:42.261091+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro armazém invalido na geração dos
  documentos a partir do APS
type: support-article
updated_at: '2021-09-30T17:27:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409555972887-Manufatura-Linha-Protheus-SIGAPCP-Erro-armaz%C3%A9m-invalido-na-gera%C3%A7%C3%A3o-dos-documentos-a-partir-do-APS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min****Ocorrência**Ocorre o erro **REGNOIS - Não existe registro relacionado a chave informada no alias NNR - Locais de Estoque**, quando o **TOTVS APS - Planejamento Avançado da Produção** integra com o Sistema para a geração de **OPs - Ordens de Produção** e **SCs - Solicitações de Compra.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Esse erro ocorre quando a integração com o **APS** não está corretamente configurada no Sistema.  
  
**Solução**Verifique o conteúdo do parâmetro **MV\_APS - Define integração com pacote APS externo para integração**, esse parâmetro deve possuir o conteúdo **TOTVS**.
