---
article_id: 360051123153
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e05b93c410b771a4ef3361eb3ef53974aa39305de2f00bdc6bc54d83154c7e78
fetched_at: '2026-06-28T22:42:03.771664+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Campo 2  - CST_ICMS do Registro H020 - Informação Complementar do
  Inventário
type: support-article
updated_at: '2021-04-28T14:25:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051123153-MP-FIS-Campo-2-CST-ICMS-do-Registro-H020-Informa%C3%A7%C3%A3o-Complementar-do-Invent%C3%A1rio
---

**Dúvida**Campo 2 - CST\_ICMS do Registro H020 - Informação Complementar do Inventário  
  
Foi solicitado melhoria no cadastro de informações para o campo 2 (CST\_ICMS - Situação Tributária do ICMS Tabela 4.3.1) do registro H020 , para que na gravação do mesmo, possa buscar do cadastro do TES  campo Sit Trib ICM (F4\_SITTRIB) que está amarrada ao produto (B1\_TS) quando não houver informação no campo do produto B1\_ CLASFIS, pois dificilmente as duas informações estarão em  branco e popular os dois cadastros é redundante.  
  
 **Ambiente**  
Protheus – Livros Fiscais  – A partir da versão 11.80  
  
**Solução**  
Referente a solicitação de melhoria, obtivemos o retorno abaixo da nossa equipe de desenvolvimento:

Informamos que não será possível buscar as informação do cadastro do TES, pelos motivos apresentados abaixo:   
  
1- O registro H020 - Informação Complementar do Inventário, pede apenas uma informação por produto.  
  
 Ao fazer a consulta no cadastro de TES teríamos N ocorrências.  
  
2- O leiaute solicita que seja apresentada as informações mais relevantes do produto o que não estará necessariamente no movimentos.  
  
3- Ao gerar o registro devemos buscar as informações do produto sem avaliar individualmente as operações, função do cadastro de TES.
