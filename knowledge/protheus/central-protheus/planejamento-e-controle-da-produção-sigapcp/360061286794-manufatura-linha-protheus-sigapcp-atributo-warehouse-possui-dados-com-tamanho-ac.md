---
article_id: 360061286794
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 93758f6463a2b77e43d277deb136ded517e6322bf938bd287f5c91de343d60ed
fetched_at: '2026-06-28T22:42:40.875146+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Atributo warehouse possui dados com
  tamanho acima do máximo suportado
type: support-article
updated_at: '2021-08-13T12:37:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061286794-Manufatura-Linha-Protheus-SIGAPCP-Atributo-warehouse-possui-dados-com-tamanho-acima-do-m%C3%A1ximo-suportado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min**  
**Ocorrência**Ao tentar integrar os dados para a execução do **PCAP712 -** **MRP** **M****emória** apresenta a mensagem **Atributo 'warehouse' possui dados com tamanho acima do máximo suportado** para os **Armazéns** no **PCPA142 - Pendencias de Integração do MRP**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**O campo **HWY\_COD - Código** difere do tamanho dos outros campos de **Armazém**.  
  
**Solução**Ajustar o tamanho do campo **HWY\_COD** para o mesmo tamanho do campo **NNR\_CODIGO - Código**.
