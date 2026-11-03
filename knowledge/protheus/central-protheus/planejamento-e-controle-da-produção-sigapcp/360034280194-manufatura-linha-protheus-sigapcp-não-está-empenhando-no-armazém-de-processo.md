---
article_id: 360034280194
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3f25e0393d8a6d93c77736ed31e84d3e6b92c7ea93f8443ee2f3c788ce76e383
fetched_at: '2026-06-28T22:42:44.582206+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Não está empenhando no armazém de processo
type: support-article
updated_at: '2022-04-01T13:13:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034280194-Manufatura-Linha-Protheus-SIGAPCP-N%C3%A3o-est%C3%A1-empenhando-no-armaz%C3%A9m-de-processo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:44 min**  
**Dúvida**Qual o motivo de não estar empenhando o componente no armazém de processo, ou seja, quando o campo **B1\_APROPRI - Apropriação** está como **Indireto** no **MATA010 - Cadastro de Produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Essa situação ocorre porque o parâmetro **MV\_LOCPROC - Local padrão a ser enviado os materiais indiretos em processo** está igual ao parâmetro **MV\_CQ - Local (Almoxarifado) Controle de Qualidade.**  
Quando esses parâmetros estão com o mesmo armazém, o Sistema realizará o empenho no armazém padrão.
