---
article_id: 20699249010967
category: SIGAEST - RELATORIOS
content_hash: e438fbaafbd518e6e6a904543a2c27bd7b0d067267a7aec4c172e2670a2861a8
fetched_at: '2026-06-28T22:39:06.215636+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - No cabeçalho do relatório
  aparece informação da filial logada e não da filial selecionada, o que fazer? '
type: support-article
updated_at: '2025-03-12T12:27:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20699249010967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-No-cabe%C3%A7alho-do-relat%C3%B3rio-aparece-informa%C3%A7%C3%A3o-da-filial-logada-e-n%C3%A3o-da-filial-selecionada-o-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20699249002647) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao imprimir qualquer relatório que consiga selecionar a filial ou fazer um filtro nos parametros, o sistema me traz no cabeçalho do relatório informação da filial logada e não da filial que selecionei, o que posso fazer?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Ao imprimir qualquer relatório, mesmo que eu tenha selecionado nos parametros uma filial diferente do que estou logada, o sistema irá trazer no cabeçalho os dados da filial logada conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699249003671)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699301452951)

Isso é padrão do sistema em qualquer relatório, por conta do parametro MV\_EMPCABE que por padrão vem habilitado para mostrar os dados da empresa e filial logada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699305168151)

Sugestão é desabilitar esse parametro que não irá aparecer o grupo da empresa e filial logada no sistema, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20699479293207)

O exemplo acima foi do relatório Kardex (MATR900), porém o conceito segue para qualquer relatório do Protheus.

**Saiba mais:**

*[MP - SIGAEST - MATR260- Data de referência está diferente da "Data Referência" parametrizada. Por qual motivo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022408771-MP-SIGAEST-MATR260-Data-de-refer%C3%AAncia-est%C3%A1-diferente-da-Data-Refer%C3%AAncia-parametrizada-Por-qual-motivo)*

*[Clique aqui e veja mais artigos sobre Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
