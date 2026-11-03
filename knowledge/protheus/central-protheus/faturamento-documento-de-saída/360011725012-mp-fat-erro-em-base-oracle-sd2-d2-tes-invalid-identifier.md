---
article_id: 360011725012
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c1ce61c800f0e2ef3c2ee717431cb82775690b0d048301e534602cbbb10595b5
fetched_at: '2026-06-28T22:38:45.221563+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP-FAT-Erro em base oracle SD2 - D2_TES - invalid identifier
type: support-article
updated_at: '2021-04-28T15:13:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011725012-MP-FAT-Erro-em-base-oracle-SD2-D2-TES-invalid-identifier
---

**Ocorrência**

Ao excluir a nota fiscal de saída está gerando o erro: **Error : 904 - ORA-00904: "SD2"."D2\_TES": invalid identifier**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17  
   
 **Causa**

A causa do erro foi a falta do alias da Tabela na chamada de query da função B2ATUCOMD2 de atualização do saldo da SB2 com a SD2 em ambiente de Dados Oracle  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote de correção - **ocorrência 48**: **[Error : 904 - ORA-00904: "SD2"."D2\_TES": invalid identifier ( From tOracleConnection::GetQueryFile ) na Exclusão do Documento de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=235334710)**

2. Via TDS (Totvs Developer Studio), aplique o pacote de correção em um ambiente de homologação para validar o processo e correção;

3. Após validar em ambiente de homologação, aplique em base de produção.

Obs: Aplicação de pacotes no ambiente requer conhecimento técnico de configuração de ambientes e da ferramenta TDS, em caso de dúvida no processo consulte a equipe de Frame WORK para auxiliar.
