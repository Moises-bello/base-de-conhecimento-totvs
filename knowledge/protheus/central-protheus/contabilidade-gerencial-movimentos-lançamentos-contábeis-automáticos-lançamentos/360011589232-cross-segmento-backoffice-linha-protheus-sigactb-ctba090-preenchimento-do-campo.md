---
article_id: 360011589232
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 572abec16b6ff085ccbd13474a9551f3b23c0b15c2e2844072aaf06f6674d41e
fetched_at: '2026-06-28T22:40:32.293464+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA090 Preenchimento
  do Campo CT2_KEY
type: support-article
updated_at: '2024-12-11T11:36:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011589232-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA090-Preenchimento-do-Campo-CT2-KEY
---

**Dúvida**

Como deve ser preenchido o campo **CT2\_KEY** (responsável pela origem do registro na contabilidade gerencial?

**Ambiente**  
Protheus  – Contabilidade – A partir da versão 11.80  
  
**Solução**

Este campo deve ser configurado por meio da rotina ([**CTBA090 – Relacionamentos**](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba090_relacionamentos.htm)) em: Contabilidade Gerencial/ Atualizações/ Cadastros/ Relacionamentos.

A partir dessa rotina é possível informar a ‘chave de busca’ que o respectivo LP fará para gravar as informações.

Atente-se para os campos:

CTL\_KEY: Informa a chave de busca no Índice da tabela principal envolvida.

Exemplo:

**Tabela SE5:**

E5\_FILIAL+E5\_TIPODOC+E5\_PREFIXO+E5\_NUMERO+E5\_PARCELA+E5\_TIPO+DTOS(E5\_DATA)+E5\_CLIFOR+E5\_LOJA+E5\_SEQ

**CTL\_ORDER**: Informa a ordem da chave de busca conforme o ‘Índice da respectiva tabela’

Ordem: 2

* <http://tdn.totvs.com/display/PROT/CTB0084_+Preenchimento+do+Campo_CT2_KEY>
* [CTB - Rastreamento Lanctos Contabeis](http://tdn.totvs.com/pages/releaseview.action?pageId=44401466&preview=%2F44401466%2F44695795%2FCTB_NOVO_RASTREAMENTO_CONTABIL_TFRGPW.pdf)

**Observação** : Para saber qual é a chave e a respectiva ordem de uma determinada tabela, basta acessar a rotina: **Base de Dados** (via configurador), opção: Índices.

Saiba mais:

[Cadastro Relacionamentos](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba090.htm)

[Configurações especiais](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba090_configuracoes_especiais.htm)
