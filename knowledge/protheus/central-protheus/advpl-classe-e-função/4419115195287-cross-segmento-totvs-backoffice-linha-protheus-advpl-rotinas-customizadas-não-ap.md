---
article_id: 4419115195287
category: ADVPL - Classe e Função
content_hash: 9d2f4233c1758f72fd3dbd305a946c7970c22ffb7455cb1b862ce22d3f70be1f
fetched_at: '2026-06-28T22:40:21.543038+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL- Rotinas customizadas
  não aparecem no RPO após migração?
type: support-article
updated_at: '2024-06-20T17:28:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419115195287-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotinas-customizadas-n%C3%A3o-aparecem-no-RPO-ap%C3%B3s-migra%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20892141922967) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao migrar para release 12.1.33 as customizações não estão sendo apresentadas no RPO?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Causa**A partir da release 12.1.33 a utilização do [RpoCustom](https://tdn.totvs.com/display/tec/RpoCustom) passou a ser obrigatória.  
  
**Solução**Necessário validar os seguintes pontos:  
1 -Verifique se está na última atualização do binário: APPSERVER (ou mais recente) - Acesso ao [Binário Download](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
2- Verifique se não está configurado no appserver.ini a chave [IXBLOG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292-MP-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus) que desabilita as customizações.  
3- Veja se o [RpoCustom](https://tdn.totvs.com/display/tec/RpoCustom) está devidamente configurado em seu ambiente, compile novamente suas customizações.  
4- Verifique no Módulo configurador→ ambiente→ cadastros→ catálogo de personalização, se está habilitado a sua customização.  
  
![](https://totvssuporte.zendesk.com/attachments/token/3Teo6HGs0VUTa2W1pdKs5U59i/?name=inline1499798000.png)​
