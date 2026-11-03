---
article_id: 11979978992919
category: Gestão de Transportes (TMS)
content_hash: dba44eb5cc4aa614d73e685b4fa6e7afa5f39d7162a8d0037950d23dea6f8c63
fetched_at: '2026-06-28T22:45:32.537693+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Regras de regiões de origem, destino e cálculo
type: support-article
updated_at: '2025-03-25T19:14:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11979978992919-Log%C3%ADstica-Linha-Protheus-TMS-Regras-de-regi%C3%B5es-de-origem-destino-e-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30918509846423) Tempo aproximado para leitura: **00:01:05 min** **Dúvida**Como funcionam as regras de regiões de origem, destino e cálculo no **TMS - Gestão de Transportes?**  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**No TMS, as regiões de origem, destino e cálculo possuem a seguinte regra:

* **Reg. Origem**: Por padrão o TMS considera o que for definido no campo **Selec.Origem - DTC\_SELORI**.  
  + **Selec.Origem = 1** **- Transportadora:** Considera a região da transportadora, definida no parâmetro **MV\_CDRORI** da filial corrente.
  + **Selec.Origem = 2** **- Cliente Remetente:** Considera a região do cliente remetente, preenchido no campo **DTC\_CLIREM**.
  + **Selec.Origem = 3 - Local Coleta ou Expedidor:** Considera a região do cliente expedidor, preenchido no campo **DTC\_CLIEXP**.
* **Reg. Destino**: Campo **DTC\_CDRDES,** considera a região do cliente destinatário **DTC\_CLIDES**.
* **Reg. Cálculo**: Campo **DTC\_CDRCAL,** considera a região de destino da carga, considerando a região do cliente destinatário **DTC\_CLIDES**. Caso o documento possua um cliente recebedor **DTC\_CLIREC**, considera a região do cliente recebedor.

**Importante**Utilize regiões que possuam **Categoria do Grupo -** **DUY\_CATGRP = 3 - Região** no cadastro dos clientes, campo **A1\_CDRDES**, para evitar problemas na emissão de **CTe - Conhecimento de Transporte eletrônico** e **MDFe - Manifesto de Documentos Fiscais eletrônico**.
