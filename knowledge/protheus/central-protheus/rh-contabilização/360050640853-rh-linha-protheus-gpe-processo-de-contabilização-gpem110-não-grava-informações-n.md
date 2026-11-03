---
article_id: 360050640853
category: RH - Contabilização
content_hash: 35418d0de3fe347a0dbcd2e5e214d020021b30b5eda8b461797b08bd3e7931f8
fetched_at: '2026-06-28T22:43:46.152576+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Processo de contabilização (GPEM110) não grava
  informações na tabela CT2
type: support-article
updated_at: '2021-06-07T13:25:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050640853-RH-Linha-Protheus-GPE-Processo-de-contabiliza%C3%A7%C3%A3o-GPEM110-n%C3%A3o-grava-informa%C3%A7%C3%B5es-na-tabela-CT2
---

**Ocorrência**Processo de contabilização (GPEM110) grava informações na tabela CTK , porém não grava informações na tabela CT2  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**   
**O parâmetro**MV\_PRELAN está configurado como N, p**ara nunca gerar pré-lançamento.** Se o documento não bater o fato contábil não será contabilizado, caso contrário serão tratados como lançamentos contábeis efetivos.

**Solução:**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse Configurador->Base de Dados->Dicionário->Base Dados->Parâmetros  
  
2. Selecione o parâmetro MV\_PRELAN:  
  
3. Altere o parâmetro para D:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075805974/mceclip0.png)   
  
4. Refaça  o processo de contabilização e verifique se os lançamentos contábeis foram gravados na tabela CT2.

**ATENÇÃO:** Esse parâmetro pertence **ao módulo Ativo e Contábil**, sendo necessário verificar se a alteração de configuração do parâmetro impactará em outro rotina ou procedimento do Departamento.
