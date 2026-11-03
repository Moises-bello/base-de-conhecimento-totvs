---
article_id: 13067161537303
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 489ae073e3852cfffba41dd5e2ecca1f5121021c938a8c733f80a4cf5f27ad77
fetched_at: '2026-06-28T22:42:02.644229+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  campo 03 - Saldo Credor de Período Anterior no registro E210 quando não movimentação
  no período atual?
type: support-article
updated_at: '2023-03-14T12:13:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13067161537303-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-campo-03-Saldo-Credor-de-Per%C3%ADodo-Anterior-no-registro-E210-quando-n%C3%A3o-movimenta%C3%A7%C3%A3o-no-per%C3%ADodo-atual
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 02:00 min** **Dúvida**Como gerar o campo **03 - Saldo Credor de Período Anterior** no registro **E210 - Apuração ICMS Substituição Tributária**  quando não movimentação no período atual?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para que o valor do **Saldo Credor de Período Anterior** seja gerado no campo **03 do E210**, proceda com a seguinte configuração:

1. Configure o parâmetro **MV\_APURANT =** **T**

2. Acesse a **Apuração do ICMS (rotina MATA953)** e deixe a  pergunta **Arq. Período Ante.** na *Wizard* da **Apuração ICMS** em branco.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13067107525015)

Desse forma,  na  apuração,  os valores de períodos anteriores serão validados conforme pastas do sistema referente aos **arquivos .IC0** no que tange ao **ICMS e .ST0** quanto ao **ICMS ST**.

3. Na aba **ST Entradas** da **Apuração**, será apresentado o valor do saldo credor do período anterior, sendo necessário preencher a **UF.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13067128596375)

4. Gere o arquivo txt do **Sped Fiscal** e o **campo 03** do registro **E210,** será apresentado com valor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13067143421079)

Para melhor compreensão, anexo vídeo com exemplo didático do processo realizado.
