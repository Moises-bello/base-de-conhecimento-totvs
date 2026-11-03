---
article_id: 26438476614935
category: Escrita Fiscal - Configurador de Tributos
content_hash: bd1ddeb79bf5408244f6076abc40312cb2f4df06e80ff1c405556efad9a3bc85
fetched_at: '2026-06-28T22:39:17.386705+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Como configurar
  as regras dos impostos quando um imposto influencia o cálculo de outro?
type: support-article
updated_at: '2025-11-03T17:40:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26438476614935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-configurar-as-regras-dos-impostos-quando-um-imposto-influencia-o-c%C3%A1lculo-de-outro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26438476595735) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como configurar as regras dos impostos quando um imposto influencia o cálculo de outro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Ao configurar o FISA170, é crucial garantir que todas as regras de cálculo dos impostos estejam devidamente configurada e que cada imposto seja tratado de forma independente dentro do Configurador de Tributos.   
  
Isso evita conflitos entre o FISA170 e configurações do legado, que podem levar a resultados inesperados e incorretos na gravação dos valores.

Para cada imposto que influencia o cálculo de outros impostos, elabore uma regra específica dentro do FISA170. Certifique-se de que, após a configuração das novas regras, as configurações legadas sejam desconsideradas, uma vez que o FISA170 tem prioridade sobre o legado.
