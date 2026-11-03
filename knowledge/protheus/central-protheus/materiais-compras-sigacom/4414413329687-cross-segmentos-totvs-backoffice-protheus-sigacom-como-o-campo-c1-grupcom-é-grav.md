---
article_id: 4414413329687
category: Materiais - Compras (SIGACOM)
content_hash: 36195ec53b03e47b439fb19097c145ddc53bfaa8b05dd5f66cdfefe506c09eda
fetched_at: '2026-06-28T22:41:15.984133+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como o Campo C1_GRUPCOM
  é Gravado ?
type: support-article
updated_at: '2025-02-21T12:13:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414413329687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-o-Campo-C1-GRUPCOM-%C3%A9-Gravado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:003 min** **Dúvida**

Como o Campo C1\_GRUPCOM é gravado ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Todas as Versões

**Solução**

Para gravar o campo C1\_GRUPCOM verifique os cadastros;

1. Ativar o parâmetro: MV\_RESTCOM para S  
2. No Cadastro de Produtos, definir o Grupo de Compras padrão (B1\_GRUPCOM) para o Produto ou no Cadastro de Solicitantes, definir o Grupo de Materiais, Produtos e qual o Grupo de Compras que está amarrado a este processo.

Desta forma, ao gerar a solicitação de compras (SC1), o campo: C1\_GRUPCOM será gravado conforme a amarração que foi efetuada. Após efetuar a Geração e Atualização da Cotação a solicitação de compras aprovada (SC8) também estará com o campo:

C8\_GRUPCOM gravado inicialmente na tabela SC1 e carregado para a tabela SC8.

Em seguida, ao entrar no Programa de Análise da Cotação e clicar em Analisar, o sistema não deverá permitir a análise da cotação que estiver nesta condição. Porém, se o parâmetro MV\_RESTCOM estiver = "N" a análise irá funcionar normalmente.

Caso seja incluído o Solicitante (Adm Compras - Solicitantes), poderá ser amarrado junto ao solicitante, o Grupo de Compras para o mesmo, caso não seja amarrado o Grupo de Compras no produto, conforme exemplo:

Grupo = \* / Produto= \* / Domínio= I(Inclui) / Grupo de Compras="nro. do Grupo de Compras.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Grupo de Compras](https://tdn.totvs.com/x/f48GEQ)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
