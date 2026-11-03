---
article_id: 21539474578455
category: Originação de Grãos (OG)
content_hash: b673254a524c671c04e4d4c9046065994862f1f83a27d44d49ee99b7eba46235
fetched_at: '2026-06-28T22:45:44.946006+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Status do Fardo - Atualizações do Compatibilizador
type: support-article
updated_at: '2025-06-25T11:15:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21539474578455-Agro-Linha-Protheus-AGR-Status-do-Fardo-Atualiza%C3%A7%C3%B5es-do-Compatibilizador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21539474525847) Tempo aproximado para leitura: **00:00:50 min****Dúvida**  
Em Status do Fardo. Como realizar as o Atualizações**do Compatibilizador** ?

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Para solucionar essa dúvida, siga o seguinte passo:

**1.** Verifique, será preciso realizar a criação de **Campos** no arquivo **SX3 – Campos**;

* Tabela DXI - Fardos de Algodão em Pluma:

|  |  |
| --- | --- |
| **Campo** | DXI\_STATUS |
| **Tipo** | C |
| **Tamanho** | 3 |
| **Decimal** | (X3\_DECIMAL) |
| **Formato** | @! |
| **Título** | Filial |
| **Descrição** | Filial do Sistema |
| **Nível** | (X3\_NÍVEL) |
| **Usado** | Sim |
| **Obrigatório** | Sim |
| **Browse** | Não |
| **Opções** | (X3\_CBOX) |
| **When** | (X3\_WHEN) |
| **Relação** | (X3\_RELACAO) |
| **Val. Sistema** | (X3\_VALID) |
| **Help** | Filial do Sistema |
