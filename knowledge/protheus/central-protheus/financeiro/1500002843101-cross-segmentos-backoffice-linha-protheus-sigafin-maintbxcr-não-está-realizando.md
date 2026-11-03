---
article_id: 1500002843101
category: Financeiro
content_hash: 06c4ec4a1f15b067dcdbca5583047c60007a39f36c0557b2b4de00bd9784a503
fetched_at: '2026-06-28T22:38:03.393278+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MaIntBxCR - Não está
  realizando a compensação
type: support-article
updated_at: '2022-06-15T00:47:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002843101-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MaIntBxCR-N%C3%A3o-est%C3%A1-realizando-a-compensa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Já estou utilizando a função **MaIntBxCR** conforme link mencionado  ([FIN0023\_CREC\_Compensacao\_receber\_execauto](https://tdn.totvs.com/display/public/PROT/FIN0023_CREC_Compensacao_receber_execauto)), a questão é que na contabilização o título posicionado é do RA (Recebimento Antecipado) e não na NF (Nota Fiscal), para constar como compensação e não como baixa.

**Exemplo**O campo **E5\_TIPODOC** gravado **CP** (compensação) e não **BA** (Baixa Automática ou Baixa que não tenha movimentação bancária), igual quando a compensação parte da NF para a RA.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA330 - Todas as versões  
  
**Solução**Na rotina **FINA330** quando a compensação entre uma **NF** e a **RA**.  
  
1 - Processo quando parte da **NF** o sistema grava o campo **CT2\_KEY** com os dados da **RA** com a informação do campo **E5\_TIPODOC = CP**.  
  
Porque quando você faz a compensação e parte da **NF**, é informado ao sistema que está compensando a **NF**.  
Grava **E5\_TIPODOC = CP** e não gera Saldo.  
  
**Saiba Mais**  
[FIN0006\_MBAN\_Descrição E5\_TIPODOC](https://tdn.totvs.com/pages/releaseview.action;jsessionid=45260149A813E2728B4CC229DF85C28F?pageId=207357394)  
![](https://totvssuporte.zendesk.com/attachments/token/7kX5EkpdKSMauWOHMx1gqgzwO/?name=inline1153279313.png)​  
  
2 - Processo quando parte da **RA** o sistema grava o campo **CT2\_KEY** com os dados da **NF** com a informação do campo **E5\_TIPODOC =  BA**.  
  
Porque quando você faz a compensação e parte do **RA**, é informado ao sistema que está efetuando uma baixa do **RA**.  
Grava **E5\_TIPODOC = BA** e não gera Saldo.  
  
  
**Saiba Mais**  
**[FIN0006\_MBAN\_Descrição E5\_TIPODOC](https://tdn.totvs.com/pages/releaseview.action;jsessionid=45260149A813E2728B4CC229DF85C28F?pageId=207357394)**  
![](https://totvssuporte.zendesk.com/attachments/token/uNuk0jRG8Snn0PJHgn9otXecE/?name=inline-1869010192.png)​  
  
Como o execauto (**MaIntBxCR**) sempre vai compensar e parti do **RA**, gravação do **E5\_TIPODOC = BA**

**Importante**  
Esse comportamento é padrão do sistema e o conceito da gravação **E5\_TIPODOC**.
