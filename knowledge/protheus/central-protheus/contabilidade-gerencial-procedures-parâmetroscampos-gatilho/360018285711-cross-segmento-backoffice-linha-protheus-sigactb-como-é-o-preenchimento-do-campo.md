---
article_id: 360018285711
category: Contabilidade Gerencial - Procedures, Parâmetros,Campos, Gatilho
content_hash: d3e80336ea614c5b9d4ab85c489c530aabe2fc96070822cb82d84879ef5255f6
fetched_at: '2026-06-28T22:41:01.433418+00:00'
product: protheus
section_id: 1500001537361
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB: Como é o preenchimento
  do campo CT2_KEY?'
type: support-article
updated_at: '2022-07-19T13:45:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018285711-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-%C3%A9-o-preenchimento-do-campo-CT2-KEY
---

**Dúvida**Como é o preenchimento do campo CT2\_KEY?

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 11.80 **Solução**

|  |  |
| --- | --- |
| Este campo deve ser configurado por meio da rotina ([**CTBA090 – Relacionamentos**](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba090_relacionamentos.htm)) em: **Contabilidade Gerencial/ Atualizações/ Cadastros/ Relacionamentos.**  A partir dessa rotina é possível informar a ‘**chave de busca**’ que o respectivo **LP** fará para gravar as informações.  Atente-se para os campos:  **CTL\_KEY**: Informa a chave de busca no Índice da tabela principal envolvida.  **Exemplo SE5:**E5\_FILIAL+E5\_TIPODOC+E5\_PREFIXO+E5\_NUMERO+E5\_PARCELA+E5\_TIPO+DTOS(E5\_DATA)+E5\_CLIFOR+E5\_LOJA+E5\_SEQ    **CTL\_ORDER**: Informa a ordem da chave de busca conforme o ‘Índice da respectiva tabela’  **Exemplo SE5:**Ordem: 2  **Importante:**   |  | | --- | | Para saber qual é a chave e a respectiva ordem de uma determinada tabela, basta acessar a rotina: **Base de Dados** (via configurador), opção: Índices. | |

* [Configurações especiais](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba090_configuracoes_especiais.htm)
