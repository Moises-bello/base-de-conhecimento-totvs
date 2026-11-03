---
article_id: 9855253153175
category: Faturamento - Integrações
content_hash: 3a5d8f2e55f16aed800fbd977bd6fd685fab21b8ccbeace6a0c063be97858b9b
fetched_at: '2026-06-28T22:38:26.631814+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Integração GFE
  com cliente estrangeiro '
type: support-article
updated_at: '2022-10-28T18:32:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9855253153175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-GFE-com-cliente-estrangeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Integração GFE com cliente estrangeiro   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**Realize o cadastro do município, gere a carga **OMSM011** novamente e verifique se na tabela GU7  tem o município cadastrado.  
  
Como no módulo GFE a informação do código de município IBGE é um campo obrigatório na integração, é necessário realizar o cadastro de um município com estado EX e código 99999.  
  
**[Cross Segmentos - TOTVS Backoffice (Linha Protheus)- SIGAFAT- Cadastro de Clientes Estrangeiros Campo A1\_PAIS e Emissão de Nota de Exportação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017801111-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cadastro-de-Clientes-Estrangeiros-Campo-A1-PAIS-e-Emiss%C3%A3o-de-Nota-de-Exporta%C3%A7%C3%A3o-?source=search)**  
  
Caso mesmo com o município cadastrado, o incidente persistir, verificar se o cadastro da tabela (**CC2**) foi integrado para o cadastro de Cidades (**GU7**) do GFE, não sendo integrado, o cadastro precisará ser refeito.  
  
Quando o município for cadastrado com o código IBGE e estiver nas tabelas **CC2** e **GU7** respectivamente, o cadastro de Clientes poderá ser realizado corretamente.
