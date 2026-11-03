---
article_id: 360027859551
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 94eba3da62d4956231128020a5977bb3bf553e40aeca3324e1b79d60209944ce
fetched_at: '2026-06-28T22:39:57.395585+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Element
  ''MunicipioPrestacaoDescricao": This element is not expected (DSFNET)'
type: support-article
updated_at: '2025-07-08T19:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027859551-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Element-MunicipioPrestacaoDescricao-This-element-is-not-expected-DSFNET
---

**Ocorrência**Na rotina **FISA022** ao realizar a transmissão de uma NFSE é apresentado o erro: **Element 'MunicipioPrestacaoDescricao": This element is not expected. Expected is ( MunicipioPrestacao).**

![aaaaa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360027633212/aaaaa.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**O erro ocorre porque a informação do Código SIAFI na tag MunicipioPrestacao não está sendo montada no XML.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse a APSDU (Tabelas do Protheus);  
  
2. Na tabela CC2, filtre o campo **CC2\_CDSIAF** referente ao município de prestação em questão (campo CC2\_MUN ou CC2\_CODMUN);  
  
3. Preencha-o com o **SIAFI** correspondente:  
-<https://www.cnm.org.br/cms/images/stories/Links/16062014_Codigo_SIAFI_municipio.pdf>  
  
4. Feito isso, também se certificar de estar preenchendo os dados com o mesmo município nos campos abaixo:  
**A1\_EST, A1\_COD\_MUN e A1\_CODSIAF** (Cadastro do Cliente);  
**C5\_ESTPRES e C5\_MUNPRES** (Caso o município de prestação seja diferente do cliente)  
  
5. Feito isso deverá ser gerado uma nova nota e realizar a transmissão da mesma.  
  
**Obs.:** Essa é apenas uma **orientação pontual**. Portanto, deverá entrar em contato com a equipe de Suporte Fiscal para solicitar atualização da tabela de municípios. Dessa maneira a coluna será preenchida para todos os municípios.
