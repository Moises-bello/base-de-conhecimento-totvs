---
article_id: 360036938913
category: License Sever Virtual
content_hash: 02c4cd4daffc8fbe46144844cc07d468c0f5baff300f2694d514253134c527a5
fetched_at: '2026-06-28T22:42:20.045278+00:00'
product: protheus
section_id: 360000075428
source: central-protheus
title: Framework - Linha Protheus - CONFLITO LSNUMBER.VAL PARA CADA LICENSE SERVER
type: support-article
updated_at: '2026-01-26T19:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036938913-Framework-Linha-Protheus-CONFLITO-LSNUMBER-VAL-PARA-CADA-LICENSE-SERVER
---

**DÚVIDA**  
Tenho dois License Servers, um em cada máquina. Supondo que o LS 1 esteja no ar e o LS 2 desligado, todavia em dado momento o LS 1 fique fora do ar e o LS 2 assume o processamento.

Como será o tratamento do arquivo LSNUMBER.val caso o LS 1 retorne e o LS 2 seja desligado?   
  
**AMBIENTE**  
Protheus – License Server – A partir da versão 12.1.17  
  
**CONFLITO**  
No momento que o LS 1 fica fora do ar, o LS 2 assumirá realizando um SELECT MAX+1 e gerando um novo arquivo LSNUMBER.val.

Contudo, caso novas numerações sejam cedidas no LS 2 e o mesmo saia do ar para entrada do LS 1, o último número disponível no LS 1 será utilizado.

Isto irá gerar conflitos, pois a última numeração do LS 1 não corresponde a um número disponível para utilização em persistência.  
  
**SOLUÇÃO**  
Para evitar a inconsistência de numeração, o arquivo LSNUMBER.val deve ser transportado para o License Server que ficará ativo ou então desabilitar a geração do arquivo por meio da chave `NUMBERVAL` da sessão `LICENSE SERVER`.  
  
**SAIBA MAIS**  
[HABILITADA GERAÇÃO DO ARQUIVO LSNUMBER.VAL](https://tdn.totvs.com/pages/viewpage.action?pageId=353277433)
