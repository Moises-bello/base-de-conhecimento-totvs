---
article_id: 360053334173
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: b4082e83de1d7ac5f74888b2303d9013bc73a033fc1e84a9286a4fe71944e530
fetched_at: '2026-06-28T22:36:58.087901+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Ao retirar a
  data de embarque apresenta a mensagem: Não é possível retirar a data de embarque
  pois existem parcelas de câmbio contratadas.'
type: support-article
updated_at: '2022-01-20T19:20:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053334173-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Ao-retirar-a-data-de-embarque-apresenta-a-mensagem-N%C3%A3o-%C3%A9-poss%C3%ADvel-retirar-a-data-de-embarque-pois-existem-parcelas-de-c%C3%A2mbio-contratadas
---

**Dúvida**Ao retirar a data de embarque apresenta a mensagem: Não é possível retirar a data de embarque pois existem parcelas de câmbio contratadas. , como corrigir?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões.  
**Solução**A mensagem é apresentada quando na rotina de Cambio (EECAF200) , a parcela encontra-se liquidada.   
Sendo assim, realize o procedimento abaixo:  
1. Acesse no módulo SIGAEEC em Atualizações \ Financeiro \ Cambio (EECAF200);  
2. Posicione no processo , selecione alterar;  
3. Posicione em Outras Ações \ Estorno da Liquidação;  
4. Selecione salvar e salvar novamente para gravação.  
5. Posicione novamente no processo , selecione alterar;  
6. Posicione na parcele e selecione alterar , e apague o conteúdo de Dt.Cred.Ext. e Sol.Cambio:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085498614/mceclip0.png)  
7. Selecione o salvar, e salvar novamente para gravação do processo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086668193/mceclip1.png)  
8. O status do processo ficará como Embarcado:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360086668233/mceclip2.png)  
9. Após acesse a rotina Embarque \ Manutenção (EECAE100), posicione no processo e selecione Alterar;  
10. Na aba Transporte , retire o conteúdo do campo Dt.Embarque (EEC\_DTEMBA), após selecione o salvar para retirar a data de embarque.   
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085498854/mceclip3.png)
