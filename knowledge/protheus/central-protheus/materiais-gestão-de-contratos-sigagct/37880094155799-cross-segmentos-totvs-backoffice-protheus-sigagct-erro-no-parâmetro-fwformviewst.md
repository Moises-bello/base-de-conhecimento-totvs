---
article_id: 37880094155799
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3b311ec4723a58cce798dba7fb195e7f0ea174041f48cb78e23e965332075b63
fetched_at: '2026-06-28T22:37:22.745045+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro no parâmetro
  FWFormViewStruct: Campo: CNZ_EC05DB não encontrado na inclusão de Revisão do contrato
  ou erro no parâmetroFWFormGridModel: Invalid Relation IdField: DBL_EC05DB'
type: support-article
updated_at: '2026-05-04T11:56:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37880094155799-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-no-par%C3%A2metro-FWFormViewStruct-Campo-CNZ-EC05DB-n%C3%A3o-encontrado-na-inclus%C3%A3o-de-Revis%C3%A3o-do-contrato-ou-erro-no-par%C3%A2metroFWFormGridModel-Invalid-Relation-IdField-DBL-EC05DB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37880058711063) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Erro no parâmetro FWFormViewStruct: Campo:**CNZ\_EC05DB** não encontrado na inclusão de Revisão do contrato ou erro no parâmetroFWFormGridModel: Invalid Relation IdField: **DBL\_EC05DB** ao acessar Grupo de aprovação

**Ambiente**

Cross Segmentoa - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões]

**Causa**

Erro no parâmetro FWFormViewStruct: Campo:**CNZ\_EC05DB** não encontrado na inclusão de Revisão do contrato

Deve-se verificar, no ambiente em questão, se os campo  **CNZ\_EC05DB**, referentes a entidades contábeis adicionais, existe no dicionário e no banco de dados, ou se não estão devidamente marcados como “usado” no dicionário (tabela CNZ)

Já para o erro erro no parâmetroFWFormGridModel: Invalid Relation IdField: **DBL\_EC05DB**

Deve-se verificar, no ambiente em questão, se os campos  **DBL\_EC05DB**,**DBL\_EC05CR** referentes a entidades contábeis adicionais, existe no dicionário e no banco de dados, ou se não estão devidamente marcados como “usado” no dicionário (tabela DBL)

**Solução**

1. Estes campos são gerados a partir do compatibilizador do módulo de Contabilidade Gerencial (SIGACTB). O suporte e a manutenção desse módulo são de responsabilidade da equipe de suporte do SIGACTB – Contabilidade Gerencial.

Dessa forma, recomendamos que, para obter apoio na criação e configuração adequada do campo, seja realizado o contato com o suporte do módulo SIGACTB, a fim de receber as orientações necessárias para a correta adequação do ambiente.  
   
[MP - SIGACTB: Como Incluir entidade adicional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018873072-MP-SIGACTB-Como-Incluir-entidade-adicional?source=search)

**Saiba Mais:**

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
