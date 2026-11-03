---
article_id: 360013703051
category: Faturamento - Cadastros
content_hash: 55e21e4d7b73e81046bf313edcf9389cf2f3760258387a68eb0182a4a78b310f
fetched_at: '2026-06-28T22:38:35.505256+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 1 of 0 ) on MA030TRANS(MATN030.PRX)
type: support-article
updated_at: '2021-11-17T20:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013703051-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-1-of-0-on-MA030TRANS-MATN030-PRX
---

**Ocorrência**

Ao incluir um cliente, gera o erro: **array out of bounds ( 1 of 0 ) on MA030TRANS(MATN030.PRX) 08/09/2017 14:44:36 line : 578**  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Causa**

O erro indica a falta do campo **AO4\_CHVREG,** o sistema está buscando a referência do campo e não está encontrando. Isso pode ocorrer por alguns motivos:

1. O campo não existe no dicionário SX3;
2. Não está marcado como Usado;
3. Não está marcado para uso do módulo em questão;
4. O campo encontra-se na posição incorreta.

**Solução**

Para solucionar o problema é necessário atualizar o Dicionário de Dados e executar o UPDDISTR para correção do arquivo SX3: [**Atualizador de Dicionário de Dados UPDDISTR**](https://tdn.totvs.com/x/nJLYCg)
