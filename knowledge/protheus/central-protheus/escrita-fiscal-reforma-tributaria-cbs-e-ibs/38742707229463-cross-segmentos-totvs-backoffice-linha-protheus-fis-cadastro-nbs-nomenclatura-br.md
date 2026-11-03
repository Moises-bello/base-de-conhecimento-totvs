---
article_id: 38742707229463
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 9c21c751b7bf2e5106c50323440f23bf84ce3826e7454d83e884cb23e75d6e17
fetched_at: '2026-06-28T22:39:15.762311+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Cadastro NBS – Nomenclatura
  Brasileira de Serviços
type: support-article
updated_at: '2026-03-02T16:17:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38742707229463-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Cadastro-NBS-Nomenclatura-Brasileira-de-Servi%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38742685233943) Tempo aproximado para leitura: **10:00 min**  
  
**Dúvida**  
Como cadastrar novos códigos do NBS no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

**Como Incluir uma NBS**

**Passo a Passo:**

1. Acesse o módulo de **SIGAFIS > Ambiente > Cadastros > NBS** (pode variar conforme parametrização do menu).
2. Se ainda não estiver visível, inclua o menu de cadastro de NBS via o módulo **SIGACFG** (Configuração de Menus). Documentação de exemplo de como incluir no menu:

   [Cross Segmentos - Backoffice Linha Protheus - Como adicionar um novo menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25803711858071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-adicionar-um-novo-menu)
3. Utilize a rotina **EASYNBS** para incluir o cadastro.
4. Informe o **Código NBS** e a **Descrição** associada ao serviço.
5. Salve o cadastro.

A documentação oficial informa que a tabela **SB5 – Dados Adicionais do Produto** contém os dados utilizados pelo cadastro de NBS no Protheus, campo NBS (B5\_NBS).

**Documentações relacionadas:**

[Cadastro NBS - Nomenclatura Brasileira de Serviços](https://tdn.totvs.com/pages/releaseview.action?pageId=1032866219)

[Cross Segmentos - Backoffice Linha Protheus - Como adicionar um novo menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25803711858071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-adicionar-um-novo-menu)
