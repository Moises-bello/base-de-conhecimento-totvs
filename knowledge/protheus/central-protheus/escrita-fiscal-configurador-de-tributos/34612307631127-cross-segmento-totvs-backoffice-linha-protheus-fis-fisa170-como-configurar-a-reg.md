---
article_id: 34612307631127
category: Escrita Fiscal - Configurador de Tributos
content_hash: e90b89a2e20c8724b3edca612aa36ce90bde4e7ee47998b74ff483b547734904
fetched_at: '2026-06-28T22:39:17.383967+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  a Regra de NCM para todos os estados?
type: support-article
updated_at: '2025-11-18T22:25:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34612307631127-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-a-Regra-de-NCM-para-todos-os-estados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34612338692375) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como configurar a Regra de NCM para todos os estados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para que o sistema realize corretamente o cálculo de determinado imposto em todos os estados, é necessário configurar a alíquota diretamente na Regra de NCM.

Exemplo utilizando o imposto **ICMS**:

1. Acesse a rotina de **Configuração da Regra de NCM**.
2. Selecione o tributo **ICMS**.
3. Vá até a aba **Alíquota por Tributo**.
4. Nos campos **UF Origem** e **UF Destino**, preencha com o valor `**` (dois asteriscos).

O preenchimento com `**` indica ao sistema que a alíquota configurada será aplicada abrangendo todas as combinações possíveis de estados.

Assim, não é necessário cadastrar manualmente cada UF envolvida, tornando o processo de parametrização mais ágil e prático.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34612761939607)
