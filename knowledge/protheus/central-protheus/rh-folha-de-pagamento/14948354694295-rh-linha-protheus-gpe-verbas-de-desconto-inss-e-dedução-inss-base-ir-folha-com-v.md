---
article_id: 14948354694295
category: RH - Folha de Pagamento
content_hash: 360aba94c10867c9147a6dcff727f47467e409256f608fad8f1e901859058e68
fetched_at: '2026-06-28T22:44:16.431547+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Verbas de Desconto INSS e Dedução INSS Base IR
  Folha com valores diferentes em folha sem cálculo de férias
type: support-article
updated_at: '2024-09-06T20:44:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14948354694295-RH-Linha-Protheus-GPE-Verbas-de-Desconto-INSS-e-Dedu%C3%A7%C3%A3o-INSS-Base-IR-Folha-com-valores-diferentes-em-folha-sem-c%C3%A1lculo-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26196514063895) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Verbas de Desconto INSS (ID 0064) e Dedução INSS Base IR Folha (ID 0167) com valores diferentes em folha sem cálculo de férias.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**  
Percentuais diferentes na tabela S001 da rotina Manutenção tabelas.  
  
**Solução**Para que os valores entre as verbas de Id 0064 e Id 0167 sejam iguais na folha que não existe cálculo de férias, na Tabela S001, os percentuais informados nas colunas %Desc. INSS e %Ded. Base IR devem ser iguais, caso contrário, as verbas serão calculadas com os valores diferentes.

Para ajuste, entre na rotina **Manutenção tabelas** pelo caminho **>Atualizações >Definições Cálculos >Manutenção Tabelas**, entre na tabela **S001** e ajuste os percentuais das colunas, para que fiquem iguais, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14948377848983)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
