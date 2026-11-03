---
article_id: 360061981174
category: Financeiro - Contas a Pagar
content_hash: af45739be53641220ab84a6df2bad0b0805959a5fda318c4380dd671521aad35
fetched_at: '2026-06-28T22:38:09.624869+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340  - Ao estornar
  apresenta o help M340VALID - Não foi possível cancelar compensação
type: support-article
updated_at: '2022-08-05T00:21:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061981174-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Ao-estornar-apresenta-o-help-M340VALID-N%C3%A3o-foi-poss%C3%ADvel-cancelar-compensa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Na rotina de **Compensação CP (FINA340)** ao estornar apresenta a mensagem o help M340VALID - Não foi possível cancelar compensação  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Divergência no conteúdo dos campos chaves das tabelas **SE5** e **FK2.**   
**E5\_FILIAL+E5\_IDORIG e FK2\_FILIAL+FK2\_IDDOC** devem apresentar o mesmo conteúdo.

**Cenário**

Ao estornar a compensação **Contas a Pagar**

![tela_1_Soraia.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360102432694/tela_1_Soraia.PNG)

Clicar no botão **Ok**

![imagem_2_So.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102432714/imagem_2_So.png)

Selecionar os  títulos a serem estornado (pois pode ser mais de 1 título)

![imagem_3_So.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003552542/imagem_3_So.png)

Neste momento  que irá apresentar a mensagem "M340VALID - Não foi possível cancelar compensação, verifique compartilhamento **SE5** e **FK2**"

![imagem_4_So.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003552562/imagem_4_So.png)

**Solução**Verificar o conteúdo da filial ou do ID não encontrado, e validar:

- Nível de compartilhamento da **FK2** que pode estar diferente da **SE5** (precisa ser o mesmo ou E ou C);

- Conteúdo do campo **E5\_IDORIG** de algum título não foi preenchido

- Conteúdo no campo **FK2\_IDDOC** não existe pois por algum motivo foi realizada a limpeza das **FK´s**.

O sistema irá conferir todos os campos acima dos títulos que estão no processo, tanto o título posicionado (que pode ser uma **NF**) para estornar, e os títulos compensados (que podem ser do tipo:**NDF**), e se 1 dos títulos estiverem com algum campo que possui o seu conteúdo diferente, vai apresentar a mensagem de erro.

**Exemplo :**   
Se a empresa compensou 10 títulos **NDF** com 1 único **NF**, deverá ser avaliado os 11 títulos para saber se todos estão com o **E5\_FILIAL+E5\_IDORIG** correspondentes ao conteúdo **FK2\_FILIAL+FK2\_IDDOC**
