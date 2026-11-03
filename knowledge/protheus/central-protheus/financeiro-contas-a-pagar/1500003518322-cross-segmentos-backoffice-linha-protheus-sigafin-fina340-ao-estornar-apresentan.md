---
article_id: 1500003518322
category: Financeiro - Contas a Pagar
content_hash: 147d5a359a322c7c03cee83764e2f76bc09d55e7f0b51f56d12b2f265d3d62f0
fetched_at: '2026-06-28T22:38:09.628827+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - Ao estornar
  apresentando o help M340VALID - Não foi possível cancelar compensação
type: support-article
updated_at: '2022-08-05T00:23:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003518322-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Ao-estornar-apresentando-o-help-M340VALID-N%C3%A3o-foi-poss%C3%ADvel-cancelar-compensa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Na rotina de **Compensação CP (FINA340)** ao estornar apresentando o help M340VALID - Não foi possível cancelar compensação  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FIINA340 - Todas as versões  
  
**Causa**

Divergência no conteúdo dos campos chaves das tabelas **SE5 e FK2.**

**E5\_FILIAL+E5\_IDORIG e FK2\_FILIAL+FK2\_IDDOC** devem apresentar o mesmo conteúdo.

**Cenário**

Ao estornar a compensação Contas a Pagar

**![image.png](https://mail.google.com/mail/u/0?ui=2&ik=fcbba98911&attid=0.1&permmsgid=msg-f:1693664861133078982&th=17811b37c06601c6&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ906Ki1yP8ZokjrCu0fLqBDdbVGEQ7WJyus_NvIXKp-GtlxnuWZ_Ikx5NijdP-VDUbssOJlYKclzYtGlJbDxl6z-jTImwVY-tVoMAcPLSz3tsJ8UZuy6R04vh8&disp=emb&realattid=ii_kkofa1wp0)**

**Clicar no botão Ok**

**![image.png](https://mail.google.com/mail/u/0?ui=2&ik=fcbba98911&attid=0.2&permmsgid=msg-f:1693664861133078982&th=17811b37c06601c6&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ_5FFlBB93vaqYyvd2kjxc8UEHUXq4of9MdOPL10j4QcrV6qiNdUm8J0MgdWg6rXRX-J749SGVKtPK9lp5X7Li0SA_15Bv0ZmJPkDo06_h7gx7_LLh2ByZI0Ag&disp=emb&realattid=ii_kkofayi41)**

Selecionar os  títulos a serem estornado (pois pode ser mais de 1 título)

![image.png](https://mail.google.com/mail/u/0?ui=2&ik=fcbba98911&attid=0.3&permmsgid=msg-f:1693664861133078982&th=17811b37c06601c6&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ9sT8-r7xYXm-3O_7MsBlgRpBYF_6L-BNaDpNLaUVNgPh6RzfVk4PkWSzyhosAXPam8DOCK8AmLMV0WNtppe6jSfBNBU1sfjINN6UjEknNlaOZ6VSb5Bk-Nvkc&disp=emb&realattid=ii_kkofcz3d2)

Neste momento  que irá apresentar a mensagem "M340VALID - Não foi possível cancelar compensação, verifique compartilhamento SE5 e FK2"

![image.png](https://mail.google.com/mail/u/0?ui=2&ik=fcbba98911&attid=0.4&permmsgid=msg-f:1693664861133078982&th=17811b37c06601c6&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ9QC9BbR55G0OUBm5vX8pnOqcFm8fIrMK8CmJTLaiK25nEUEXhv6Wd03FU6r-H773fJpTilDp0cLjPqm6dcTcCCoh48XxVGCZM-kUr5mmoWXBk2sXzuZ4E9__w&disp=emb&realattid=ii_kkofei6r3)

**Solução**Verificar o conteúdo da filial ou do ID não for encontrado, e validar:

- Nível de compartilhamento da FK2 que pode estar diferente da SE5 (precisa ser o mesmo ou E ou C);

- Conteúdo do campo E5\_IDORIG de algum título não foi preenchido

- Conteúdo no campo FK2\_IDDOC não existe pois por algum motivo foi realizada a limpeza das FK´s.

O sistema irá conferir todos os campos acima dos títulos que estão no processo, tanto o título posicionado (que pode ser uma NF) para estornar, e os títulos compensados (que podem ser do tipo:NDF), e se 1 dos títulos estiverem com algum campo que possui o seu conteúdo diferente, vai apresentar a mensagem de erro.

Exemplo : Se a empresa compensou 10 títulos NDF com 1 único NF, deverá ser avaliado os 11 títulos para saber se todos estão com o E5\_FILIAL+E5\_IDORIG correspondentes ao conteúdo FK2\_FILIAL+FK2\_IDDOC
