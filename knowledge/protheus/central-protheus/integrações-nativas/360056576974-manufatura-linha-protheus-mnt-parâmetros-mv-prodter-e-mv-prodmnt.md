---
article_id: 360056576974
category: Integrações Nativas
content_hash: 349e892d2e4a5f4fe0e1e164d1ce22fce57894dced0173b09046eb7bbee2cc2d
fetched_at: '2026-06-28T22:42:35.484195+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Parâmetros MV_PRODTER e MV_PRODMNT
type: support-article
updated_at: '2024-09-03T16:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056576974-Manufatura-Linha-Protheus-MNT-Par%C3%A2metros-MV-PRODTER-e-MV-PRODMNT
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26092772951447)*Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Qual a utilização dos parâmetros **MV\_PRODMNT** e **MV\_PRODTER** no **SIGAMNT - Manutenção de ativos**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**A utilização dos parâmetros no módulo **SIGAMNT** é:

* **MV\_PRODMNT - Item de estoque para ordem de produção do SIGAMNT**: ao incluir uma **OS - Ordem de serviço** no **Manutenção de Ativos** é gerado automaticamente uma **Ordem de Produção - SC2**. O **Código do produto** usado para gerar a **OP - Ordem de Produção** é o conteúdo definido no parâmetro **MV\_PRODMNT**.
* **MV\_PRODTER -** **Item de estoque que indica Terceiros no SIGAMNT**: ao incluir um insumo previsto de uma **OS** do tipo terceiro, é gerado automaticamente uma **SA - Solicitação de armazém** e o **Código do produto** usado para gerar essa movimentação é o conteúdo definido no parâmetro **MV\_PRODTER**.

**Importante**É possível definir apenas um código para cada um dos parâmetros.  
Exemplo:

* **MV\_PRODMNT = MANUTENCAO**
* **MV\_PRODTER = TERCEIRO**
