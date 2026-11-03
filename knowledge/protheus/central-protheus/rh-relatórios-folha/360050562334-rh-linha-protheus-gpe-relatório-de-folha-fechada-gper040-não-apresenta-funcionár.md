---
article_id: 360050562334
category: RH - Relatórios Folha
content_hash: 56b74153e5b0bd664e3c297cc0d7618b183d453ca933676f33d947c098089ad1
fetched_at: '2026-06-28T22:43:17.590759+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório de folha fechada (GPER040)  não apresenta
  funcionário quando configurado filtro por centro de custos
type: support-article
updated_at: '2024-08-26T12:14:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050562334-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-folha-fechada-GPER040-n%C3%A3o-apresenta-funcion%C3%A1rio-quando-configurado-filtro-por-centro-de-custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25906724408087) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Relatórios de folha fechada não apresenta funcionário quando configurado filtro por centro de custos  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Funcionário possui transferência posterior à competência do cálculo e o relatório não está selecionado com a opção Centro de Custo do Movimento.   
  
**Solução**Para solucionar essa ocorrência, realize o procedimento abaixo:   
  
1. Acesse **Relatórios > Periódicos > Folha de Pagamento**  e selecionar a opção Centro de Custo do Movimento:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077587634)

Desta forma  o sistema fará a geração do relatório considerando o centro de custo que foi utilizado no cálculo da competência, caso necessite filtrar por um centro de custos nos parâmetros de pergunta da rotina.

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
