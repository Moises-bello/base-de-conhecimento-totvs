---
article_id: 360015722272
category: esocial - Atualização Status Integração
content_hash: 7135bc54b8e555705685df8929dc7fd3f30adf3b936aa4b237b3b492ff7564eb
fetched_at: '2026-06-28T22:47:11.197502+00:00'
product: rm
section_id: 1500000860962
source: central-rm
title: RH - RM - FOP- eSocial- Status do evento no RM divergente do status do evento
  no TAF
type: support-article
updated_at: '2024-06-17T11:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015722272-RH-RM-FOP-eSocial-Status-do-evento-no-RM-divergente-do-status-do-evento-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24189028498199)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Qual procedimento deve ser executado quando encontro diferença entre os status dos XMLs no RM em comparação com o TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir da versão 12.1.22  
  
**Solução**Para identificar e posteriormente igualar os status dos eventos entre os produtos será necessário seguir os passos abaixo:  
1. Executar o processo de [limpeza de inconsistências](http://tdn.totvs.com/pages/releaseview.action?pageId=394211644) no TAF;  
2. Gerar o relatório de [**Integridade RM x TAF**](http://tdn.totvs.com/x/iDF-Fw);  
3. Analisar as diferenças apresentadas no *LOG* da geração do relatório de integridade;  
4. Executar a atualização de status no RM selecionando **eSocial | Atualizar Status Integração TAF**.  
  
**Importante**  
Caso existam arquivos XML's no Labore com status igual a **3- Enviado TAF** e que não foram encontrados no TAF, sugerimos a [exclusão dos mesmos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017738251-RH-RM-FOP-eSocial-Exclus%C3%A3o-de-eventos-da-fila-independente-do-status?source=search).  
  
**Saiba mais**  
[Atualização TAF/TSS](http://tdn.totvs.com/pages/releaseview.action?pageId=374311673)
