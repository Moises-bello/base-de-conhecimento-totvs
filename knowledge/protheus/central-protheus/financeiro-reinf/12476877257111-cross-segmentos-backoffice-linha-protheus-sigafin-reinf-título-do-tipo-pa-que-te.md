---
article_id: 12476877257111
category: Financeiro - Reinf
content_hash: 491e9fcb98723d0110e1e47e659f648038b25d3dc540d22036730cce95222a67
fetched_at: '2026-06-28T22:37:51.859010+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Título do tipo
  PA que tem retenção de IRF/PIS/COFINS/CSLL como será enviado para REINF
type: support-article
updated_at: '2023-10-31T13:45:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12476877257111-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-T%C3%ADtulo-do-tipo-PA-que-tem-reten%C3%A7%C3%A3o-de-IRF-PIS-COFINS-CSLL-como-ser%C3%A1-enviado-para-REINF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18680013842455) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Títulos do tipo PA que tem retenção de IRF/PIS/COFINS/CSLL apresentam para o REINF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O processo de envio do REINF segue o mesmo processo que era enviado na **DIRF** ou seja ao incluir um **PA** e sendo gerado um titulo **TX** ou seja quando o **MV\_BX10925** esta = **1** **Baixa** após inclusão do registro é gravado a tabela **FKW** com isso as informações é enviado para o REINF.  
  
Exemplo da pergunta na rotina da DIRF, esse mesmo processo segue para o REINF   
![](https://totvssuporte.zendesk.com/attachments/token/PoXkBPGNFuI08zm1WL8bjzGYe/?name=image.png)  
Ao incluir um titulo **PA** quando é gerado o **TXA** não é gerado a tabela **FKW** com isso essa informação não ira para o REINF.

Quando se incluir um registro do tipo **PA** que gera o **TXA** nesse processo, o envio para o REINF é quando se realiza a compensação exemplo do titulo do tipo **NF** x **PA** no período da compensação é enviado o layout **T158** referente ao titulo principal NF.  
  
**Pagina centralizadora**  
[Protheus REINF Suporte Financeiro](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro)
