---
article_id: 360016525251
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 7b0f9b181bf6f4484d7d9912e8956c9dc1e48a4b34dff611c86ddc318b116783
fetched_at: '2026-06-28T22:40:32.400164+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - CTB - Preenchimento do campo CT2_KEY
type: support-article
updated_at: '2022-07-27T14:15:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016525251-Cross-Segmento-Backoffice-Linha-Protheus-CTB-Preenchimento-do-campo-CT2-KEY
---

**Dúvida**Como deve ser preenchido o campo **CT2\_KEY** (responsável pela origem do registro na contabilidade gerencial)?  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80 **Solução**

Este campo será configurado ao utilizar a rotina que se encontra em: Contabilidade Gerencial/ Atualizações/ Cadastros/ Relacionamentos (CTBA090 ) .

A partir dessa rotina é possível informar a ‘chave de busca’ que o respectivo LP fará para gravar as informações.

Atente-se para os campos:

Ordem Busca (CTL\_KEY): Informa a chave de busca no Índice da tabela principal envolvida.  
ALias Arqu (CTL\_ALIAS): Informa a tabela principal envolvida

Exemplo SE5: E5\_FILIAL+E5\_TIPODOC+E5\_PREFIXO+E5\_NUMERO+E5\_PARCELA+E5\_TIPO+DTOS(E5\_DATA)+E5\_CLIFOR+E5\_LOJA+E5\_SEQ

CTL\_ORDER: Informa a ordem da chave de busca conforme o ‘Índice da respectiva tabela’

Exemplo SE5: Ordem: 2
