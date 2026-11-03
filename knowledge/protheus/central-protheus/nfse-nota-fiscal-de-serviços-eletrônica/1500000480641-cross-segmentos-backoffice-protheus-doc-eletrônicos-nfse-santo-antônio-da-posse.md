---
article_id: 1500000480641
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7167627e0d882f0d5491ff68521756c783cdd08512a0672090d06d38531c4994
fetched_at: '2026-06-28T22:39:58.492888+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Santo Antônio
  da Posse - SP: Fault occurred while processing (Homologação)'
type: support-article
updated_at: '2025-06-10T17:52:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000480641-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Santo-Ant%C3%B4nio-da-Posse-SP-Fault-occurred-while-processing-Homologa%C3%A7%C3%A3o
---

**Dúvida**Ao transmitir uma nota fiscal de serviços para o município de Santo Antônio da Posse - SP, **em ambiente de homologação**, o status da nota na SPED051 permanece em 2, no monitor "Aguardando transmissão do lote" e no rcv ocorre o retorno abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000546441)  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**Pontualmente nesse caso, o erro ocorre quando o mesmo número de lote já foi transmitido anteriormente.  
Para correção, acesse essa entidade na tabela SPED000 e localize o parâmetro **MV\_NFEIDLT.**Ajuste o conteúdo do parâmetro fazendo um salto na numeração, ou verifique o sequencial do lote correto na prefeitura para ajuste.  
Como o status da nota está pendente no TSS, para retransmitir esse mesmo número será necessário os acertos abaixo:  
**No TSS**, deletar o registro da nota nas tabelas SPED051, SPED053, SPED055 e TSSTR1.  
**No Protheus**, limpar o conteúdo dos campos F3\_CODRET e F3\_CODRSEF da nota em questão.  
  
Após execução do processo acima, basta retransmitir e monitorar a nota.
