---
article_id: 5396698279703
category: Materiais - Compras (SIGACOM)
content_hash: 48d7547400289c7c18b51b9e2976ac2b9ae52b0ace75b4dbc890845715ed026f
fetched_at: '2026-06-28T22:41:14.465463+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como atualizar o dicionário
  de dados (arquivo SXSBRA.TXT) do Protheus 12
type: support-article
updated_at: '2022-04-12T13:23:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5396698279703-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-atualizar-o-dicion%C3%A1rio-de-dados-arquivo-SXSBRA-TXT-do-Protheus-12
---

**Dúvida**Como atualizar o dicionário de dados  (arquivo SXSBRA.TXT) do Protheus 12  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**

Para atualizar o dicionário de dados do Protheus 12, siga o procedimento abaixo:

- Acesse o Portal do Cliente: [http://suporte.totvs.com](http://suporte.totvs.com/)

- Menu Downloads e Atualizações

- Linha Protheus

- Microsiga Protheus Versão 12.1.XX (onde XX é a versão da Release do P12 que você vai utilizar)

- Todos

- Categoria: Dicionário de dados

- Baixe o DICIONÁRIO DE DADOS COMPLETO - BRASIL se estiver fazendo uma migração de versão anterior do           Protheus para Protheus 12;

- Baixe tanto o DICIONÁRIO DE DADOS COMPLETO - BRASIL quanto o DICIONÁRIO DE DADOS DIFERENCIAL - BRASIL se estiver fazendo uma migração de release do Protheus 12

Obs.: se não estiverem aparecendo as versões, em "Filtros de pacotes" selecione "Todos pacotes disponíveis" e selecione a categoria novamente.  
Após baixar, descompacte o arquivo SXSBRA.TXT na pasta Systemload do Protheus.

Se estiver fazendo migração de versão anterior do Protheus para Protheus 12, o migrador de versão irá utilizar o dicionário completo como base.

Se estiver fazendo migração de release do Protheus 12, após atualizar os arquivos, deve executar o [UPDDISTR](http://tdn.totvs.com/pages/viewpage.action?pageId=181965468).

Aviso:

SOMENTE execute o UPDDISTR se estiver migrando de release do Protheus 12, de uma release antiga para uma release nova. Se estiver fazendo migração de uma versão anterior do Protheus para Protheus 12, NÃO É NECESSÁRIO executar o UPDDISTR.

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
