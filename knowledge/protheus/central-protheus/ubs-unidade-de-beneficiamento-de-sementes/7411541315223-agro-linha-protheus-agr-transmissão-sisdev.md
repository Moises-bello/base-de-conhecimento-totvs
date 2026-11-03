---
article_id: 7411541315223
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: bb0dbee4963f467e26461891aa9fb010c65286751bb74266cfa2ae76114b6ee0
fetched_at: '2026-06-28T22:45:34.780921+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - AGR - Transmissão SISDEV
type: support-article
updated_at: '2025-06-20T15:36:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7411541315223-Agro-Linha-Protheus-AGR-Transmiss%C3%A3o-SISDEV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22233778101271) Tempo aproximado para leitura: **00:00:31 min** **Dúvida**Como realizar uma transmissão ao **SISDEV - INDEA-MT**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - A partir da versão 12.1.17  
  
**Solução**Necessário que o parâmetro **MV\_SISDEV** esteja ativo. Quando é realizado uma **NF de Entrada - MATA103** ou uma **NF de Saída - MATA460** passa por uma função do **Originação de Grãos - AGRO** que valida se este parâmetro **Indica que o usuário utiliza a transmissão -** **MV\_SISDEV** esta ativo e se o produto é semente **SB5 - B5\_SEMENTE**, caso for, gera o registro na tabela **ND3 - Transmissão SISDEV** os quais serão usados para transmissão.  
Na rotina **Integração SISDEV-MT - UBSA010** lista os registros para transmissão e faz a transmissão. A transmissão é realizado via **HTTPPOST** enviando um arquivo para o *webservice* do **sisdev**, o *log* e este arquivo é salvo no **rootPath** configurado no **appserver**, geralmente é a pasta **Protheus\_Data** ou **System**.  
  
Os parâmetros abaixo são usados para configuração dos dados do **SISDEV** para comunicação.  
**MV\_AGRE001 - Informar a URL de entrada de Sementes/Mudas**  
**MV\_AGRS001 - Informar a URL de saida de Sementes/Mudas**  
**MV\_AGRS002 - Informar a URL de saida de Sementes/Mudas-Produtor**  
**MV\_AGRH002 -  Informar o Encode Base64 do user:password da**
