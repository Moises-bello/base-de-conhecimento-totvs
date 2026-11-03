---
article_id: 6115290475799
category: Faturamento - Cadastros
content_hash: d9498ac849db0f770407af9abbce163d5291e369951f17138a53a66049c83274
fetched_at: '2026-06-28T22:38:35.313973+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Nota sobre
  alteração de região após a geração da nota '
type: support-article
updated_at: '2022-05-16T13:54:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6115290475799-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Nota-sobre-altera%C3%A7%C3%A3o-de-regi%C3%A3o-ap%C3%B3s-a-gera%C3%A7%C3%A3o-da-nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**O Protheus possui alguma forma de alterar a região do cliente dentro da nota fiscal de saída? Isso causa algum impacto no sistema?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigafat - Todas as versões  
  
**Solução**

Hoje, após a geração da nota, o módulo de faturamento não possui nenhuma rotina de recálculo que possa alterar a informação de região do cliente,  a alteração terá que ser efetuada via cadastro do cliente (**CRMA980, antigo mata030**), ajustando campo **A1\_REGIÂO**.

Caso a informação seja para sair em Danfe e Xml , é necessário avaliar se ambos estão configurados para buscar a informação do cadastro de cliente, para que alteração do cadastro reflita em ambos os documentos. Qualquer dúvida relacionada a Danfe e XML, contate nossa equipe de SPED para melhor orientação.  
 

Em termos de impacto, dentro de faturamento, temos apenas o uso da região para tratar o relatório relatório de **curva ABC (MATR765/MATR765)**, desta forma, não há impacto de processo , já que a alteração é efetuada no cadastro de clientes e o relatório buscará a informação direto desse cadastro.

**Saiba mais:**

[**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como fazer a manutenção do cadastro de região A1\_REGIAO do cadastro de clientes (MATA030)?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044218613-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-fazer-a-manuten%C3%A7%C3%A3o-do-cadastro-de-regi%C3%A3o-A1-REGIAO-do-cadastro-de-clientes-MATA030-)

**[Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Relatório Curva ABC (MATR765 Por Cliente / MATR755 - Por Região)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000735888-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Relat%C3%B3rio-Curva-ABC-MATR765-Por-Cliente-MATR755-Por-Regi%C3%A3o-)**
