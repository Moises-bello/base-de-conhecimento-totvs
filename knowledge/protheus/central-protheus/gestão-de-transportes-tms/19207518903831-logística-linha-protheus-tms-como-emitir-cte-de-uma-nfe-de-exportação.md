---
article_id: 19207518903831
category: Gestão de Transportes (TMS)
content_hash: a3e4ba84b26be43f643fe4aa8be389e82f049e3176712ec9234204d0fdea334f
fetched_at: '2026-06-28T22:45:27.425347+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como emitir CTe de uma NFe de exportação?
type: support-article
updated_at: '2026-02-27T20:51:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19207518903831-Log%C3%ADstica-Linha-Protheus-TMS-Como-emitir-CTe-de-uma-NFe-de-exporta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19207535028759) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como emitir **CTe** de uma **NFe** de exportação?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões   
  
**Solução**  
Para emitir um **CTE** de **NFE** de exportação:  
  
1. Em **Estrutura de Regiões - TMSA120**, crie uma região no exterior:

![Screenshot_1.png](https://totvssuporte.zendesk.com/attachments/token/SRTVUVhDMFWZDcdeAE2eFJ9bu/?name=Screenshot_1.png&lotus_request=true)

2. No cadastro de **Cliente - MATA030/CRMA980**, do cliente do exterior com os campos:  
3. Cadastre o cliente exterior como **Solicitante** **- TMSA440:**

* **A1\_EST** = EX,
* **A1\_CGC** = 00000000000000
* **A1\_INSCR** = ISENTO
* **A1\_CDRDES** = Região gerada na estrutura de região

4. Cadastre o [Recebedor](https://atendimento.totvs.com/hc/pt-br/articles/360059341313-Central-Colaborativa-Boas-Pr%C3%A1ticas-do-PO-Product-Owner) no cadastro de **Cliente - MATA030/CRMA980**, exemplo seria Aeroporto de Congonhas.  
5. Na **Entrada de Documentos - TMSA050**, insira o documento preenchendo os campos com:

* **DTC\_CLIREM** = Cliente emitente da **NFe**
* **DTC\_CLIDES** = Cliente do exterior;
* **DTC\_CLIREC** = Cliente que vai receber a mercadoria (Aeroporto/Porto/CLIA)

Exemplo do **XML**:

![Screenshot_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19746912958359)

**Glossário**  
**CLIA - Centro Logístico e Industrial Aduaneiro**  
**CTe - Conhecimento de Transporte Eletrônico**  
**NFe - Nota Fiscal Eletrônica**  
**XML - Extensible Markup Language**
