---
article_id: 360043091874
category: ADVPL - Rotina Automática
content_hash: 57c6ad136c8cfe1ead96313b159a7ddc5017ec941e9ca08b67a81dd95bfa61b0
fetched_at: '2026-06-28T22:40:25.046981+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  para manutenção do cadastro de instruções
type: support-article
updated_at: '2021-08-30T14:24:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043091874-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-para-manuten%C3%A7%C3%A3o-do-cadastro-de-instru%C3%A7%C3%B5es
---

**Dúvida**Na rotina **FINA040** (Rotina FINA040->Outras ações->Manutenção) em títulos borderô temos a opção instruções conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058177094/mceclip0.png)

Existe algum recurso ou alguma forma de realizarmos esse procedimento e preenchermos esses dados nessa tabela de maneira automática ou ***via ExecAuto***?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12  
  
**Solução**A rotina para manutenção do cadastro de instruções não está preparada para ser executada automaticamente.  
É possível customizar, porém é responsabilidade do cliente:

1) A rotina de customização do cliente pode executa a rotina automática ***FINA040*** com a opção de alteração.

2) Após o retorno OK da rotina automática **FINA040** de alteração, a customização do cliente deve chamar uma função de usuário(próprio cliente deverá desenvolver) para incluir as instruções de cobrança a serem cadastrados para o título (tabela FI2). Porém só devem ser cadastradas instruções para títulos que estejam em banco e com *ID* cnab preenchido (E1\_IDCNAB <> ' ' .And. E1\_PORTADO <> ' ').

3) Para incluir dados de instruções de cobrança para o titulo (tabela FI2), a rotina do usuário deverá consistir se o código da ocorrência enviada para inclusão existe previamente cadastrada na tabela de ocorrências (tabela SEB) para o banco do título desejado (E1\_PORTADO).

4) Se o código de ocorrência existir na SEB, o registro pode ser incluído na FI2, onde deverão ser preenchidos os campos: FI2\_FILIAL (filial da tabela FI2), FI2\_OCORRE (código da ocorrência que deve existir na SEB para o banco utilizado), FI2\_DESCOC (descrição da ocorrência cadastrada na SEB), FI2\_PREFIX (prefixo do titulo), FI2\_TITULO (numero do titulo), FI2\_PARCEL (parcela do titulo), FI2\_TIPO (tipo do titulo), FI2\_CODCLI (código do cliente do titulo), FI2\_LOJCLI (loja do cliente do titulo), FI2\_GERADO (gravar sempre com o conteúdo "2"), FI2\_NUMBOR (numero do borderô do titulo), FI2\_CARTEI (carteira do titulo), FI2\_DTOCOR (data da inclusão).
