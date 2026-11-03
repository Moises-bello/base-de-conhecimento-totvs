---
article_id: 33994987099415
category: Financeiro - Baixas a Receber
content_hash: bde05a5704aa353e4171ec4010598aa7b6e4def105a2ece6173e934892344366
fetched_at: '2026-06-28T22:37:43.806956+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA191 - Como realizar
  a baixa e a devolução de um cheque a receber
type: support-article
updated_at: '2025-12-16T15:01:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33994987099415-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA191-Como-realizar-a-baixa-e-a-devolu%C3%A7%C3%A3o-de-um-cheque-a-receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33994987059607) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como realizar a baixa e a devolução de um cheque a receber?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
1º **Inclusão do registro com cheque**: inclua um título utilizando cheque. Com isso, será gerado automaticamente o registro correspondente na rotina de **Cheques Recebidos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33994964135831)

Observação: o cheque também pode ser incluído no momento da baixa do título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33994964137239)

**2º Compensação do cheque**: Ao realizar a baixa do título, acesse a rotina **Cheques Recebidos (FINA191)**, clique em **Outras Ações** e selecione a opção **Compensar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33994964138391)

**3º Devolução do cheque**: Caso seja necessário realizar a devolução, acesse novamente a rotina de **Cheques Recebidos**, clique em **Outras Ações**, selecione **Est. Comp.** e confirme. Após o estorno da compensação, acesse a rotina **Devolução de Cheques**, clique em **Devolver**, preencha os campos de **alínea** e **data da 1ª devolução**, e confirme. Se necessário, poderá realizar uma nova devolução informando a segunda alínea.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33994964138391)

#### **Importante 📢️:**

Para contabilização dos cheques utilize os lançamentos padrões abaixo:

559 - Compensação de Cheques Emitidos **(rotina FINA191)**  
583 - Estorno da Compensação de Cheques Emitidos **(rotina FINA191 - devolução)**
