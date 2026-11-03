---
article_id: 13284881280279
category: SIGAEST - LEGAIS
content_hash: cf9416cf2340fa78fe91d4edecb7fc7c41806b08b4eb47b2d6637e735adcb3e6
fetched_at: '2026-06-28T22:38:51.765805+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR947 - Relatório
  da Policia Civil não apresenta valores dos Saldos Inicais (SB9)
type: support-article
updated_at: '2024-01-04T20:11:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13284881280279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR947-Relat%C3%B3rio-da-Policia-Civil-n%C3%A3o-apresenta-valores-dos-Saldos-Inicais-SB9
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:02 min** **Dúvida**Ao gerar o relatório MATR947 - Relatório da Polícia Civil, os saldos dos produtos nas colunas "Saldo Trimestre Anterior" não batem com o saldo dos produtos registrados na tabela SB9. O que fazer?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O relatório MATR947 não considera a tabela de saldos iniciais(SB9), é considerado apenas as entradas(SD1) e saídas (SD2).

Este comportamento ocorre pois o saldo inicial é um processo interno do *Protheus* e não é considerado pelo fisco, portanto o processo que o fisco considera é entrada e saída de nota. Documentação sobre Mapa de Produtos Controlados - Policia Civil (MATR947 - SIGAEST):   <https://tdn.totvs.com/pages/releaseview.action?pageId=561861100>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13285076936215)

***OBS:*** *Sempre que se trata de comportamento de relatórios legais onde o cliente interpreta que o mesmo está se comportando diferente do padrão do Protheus, será necessário abrir um ticket com o Suporte Técnico e encaminhar o embasamento legal para analise do time de consultoria de segmentos.*

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
