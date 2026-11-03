---
content_hash: 489a5b35aeaf967846f31bfabecdc884dbc8ce835c99b7cb311f3e9ea0cf1ae9
fetched_at: '2026-06-29T00:09:28.129913+00:00'
page_id: '423938666'
product: rm
source: tdn-rm
title: Copiar Níveis de Centro de Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938666
version: 2
---

Através deste processo será possível fazer a cópia dos sub-grupos de um centro de custo para outro centro de custo, desde que eles estejam no mesmo nível hierárquico. Indique o Centro de Custo de Origem e o Centro de Custo de Destino. No final do processo será apresentado um Log informando quais centros de custos foram copiados e quais apresentaram algum erro. Caso exista um sub-grupo com o mesmo número no centro de custo de destino, o sub-grupo de origem não será copiado, preservando o já existente.

**Exemplo**

Centro de Custo de Origem

2 – Departamentos

2.01 – Diretoria

2.02 – Suporte  

Centro de Custo de Destino

3 – Área Técnica

3.01 – Desenvolvimento  

Após a cópia dos níveis do centro de custo

3 – Área Técnica

3.01 – Desenvolvimento

3.02 – Suporte  

O sub-grupo *Diretoria* não foi copiado porque já existia essa numeração no centro de custo de destino. Observe que no processo de cópia de níveis de centro de custo, apenas as partes do código referentes aos sub-grupos ( .01, .02) são copiadas para o nível principal (3).

**Exemplo**

3 (nível principal) + .02 (sub-grupo) = 3.02 (novo centro de custo)
