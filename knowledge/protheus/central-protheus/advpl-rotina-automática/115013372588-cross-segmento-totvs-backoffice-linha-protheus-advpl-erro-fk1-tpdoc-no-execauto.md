---
article_id: 115013372588
category: ADVPL - Rotina Automática
content_hash: 518add07e4dcdb848db8b9e6a708ce0369bc26862effdcc878d65bcebed1ec5f
fetched_at: '2026-06-28T22:40:24.246220+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro FK1_TPDOC no
  execauto fina070
type: support-article
updated_at: '2021-12-29T12:59:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013372588-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-FK1-TPDOC-no-execauto-fina070
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Erro ao executar a ExecAuto FINA070 - FK1\_TPDOC - REGNOIS - Não existe registro relacionado a este código.

![](https://tdn.totvs.com/download/attachments/306840101/image2017-10-11_9-26-16.png?version=1&modificationDate=1507724941000&api=v2)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Neste caso não é um erro, trata-se  um help. Verifique em sua base se a tabela FKB tem dados [FIN0006\_MBAN\_Descrição E5\_TIPODOC](https://tdn.totvs.com/pages/viewpage.action?pageId=207357394)  
Verifique se manualmente é possível fazer o cadastro, pois a mesma função que é chamada manualmente é também chamada na ExecAuto.  
A FKB grava essas informações desta tabela, se der um TRUNCATE TABLE FKB010 e reiniciar o APPSERVER, DBACCESS e entrar em uma rotina do financeiro exemplo: FINA750 ou FINA740  
A tabela FKB será criada com o TIPODOC.  
Ao baixar um registro no financeiro é gravado o E5\_TIPODOC com o mesmo tipo da tabela FKB010.

**Saiba mais**  
[ADV0038 Rotina FINA070](http://tdn.totvs.com/display/PROT/ADV0038_ROT_FINA070)
