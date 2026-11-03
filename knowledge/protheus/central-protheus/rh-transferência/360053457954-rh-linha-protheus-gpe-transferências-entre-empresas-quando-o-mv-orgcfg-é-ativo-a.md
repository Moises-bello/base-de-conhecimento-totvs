---
article_id: 360053457954
category: RH - Transferência
content_hash: c6ce54a14c726758f5c7cd8746c7a96eb46a0159e0a7bb40d014293a2aa6e013
fetched_at: '2026-06-28T22:43:23.467873+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Transferências entre Empresas quando o MV_ORGCFG
  é ativo apenas na destino
type: support-article
updated_at: '2021-04-28T20:17:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053457954-RH-Linha-Protheus-GPE-Transfer%C3%AAncias-entre-Empresas-quando-o-MV-ORGCFG-%C3%A9-ativo-apenas-na-destino
---

**Dúvida**MP - GPE - Transferências entre Empresas quando o MV\_ORGCFG é ativo apenas na destino  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - A partir da versão 12.1.17  
  
**Solução**O parâmetro MV\_ORGCFG determina ao Protheus a utilização do módulo SIGAORG.  
Quando temos uma transferência de funcionário de uma Empresas e apenas na empresa destino utiliza o MV\_ORGCFG ativado, o Sistema faz a busca pelo Departamento Destino que esteja amarrado ao cadastro de Visões do SIGAORG.  
  
Portanto, mesmo que o cadastro de Departamentos esteja completo, os registros precisam estar atrelados às Visões na tabela RD4 para que o campo Departamento Destino faça a consulta corretamente e permita a inclusão da Transferência, caso contrário, retornará vazio.
