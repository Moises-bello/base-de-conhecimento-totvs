---
article_id: 115001376647
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e86aa7ccbf33f9269d5141a805660d9a258832bf878af6ed380315dfc55f6b9e
fetched_at: '2026-06-28T22:38:43.860341+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como ajustar o
  Controle de Numeração no Documento de saída MATA461
type: support-article
updated_at: '2024-01-10T13:32:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001376647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-ajustar-o-Controle-de-Numera%C3%A7%C3%A3o-no-Documento-de-sa%C3%ADda-MATA461
---

**Dúvida**Como ajustar o Controle de Numeração no Documento de saída **MATA461**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Solução**Siga os passos para tratar o controle de numeração de nota:  
1- Identifique o parâmetro **MV\_TPNRNFS** no Configurador em: *Dicionario > Base de Dados > Parâmetros* qual o controle de numeração utilizado.

Opções:  
    1. Controle de numeração pelo **SX5** - Tabelas Genéricas.

    2. Controle de numeração pelo **SXE / SXF** (Hardlock ou Disco System)

    3. Controle de numeração dos documentos de entrada e saída por **SD9** / Cadastro manual via rotina de atualização de documentos (**MATA012**).

2- Após identificar o controle utilizado, siga as instruções para tratar o tipo de controle de numeração, através do link do documento técnico abaixo.

**OBSERVAÇÃO 1:** O controle de numeração do documento de saída não se baseia na numeração do pedido de vendas.

**OBSERVAÇÃO 2:** A numeração durante o faturamento, principalmente quando (MV\_TPNRNFS = 1), pode ficar irregular caso seja preenchido títulos a receber (Tabela SE1, campo E1\_NUM). Ao faturar, o mesmo número do documento de saída tende a ir ao título (E1\_NUM), e ao encontrar um já existente, pode gerar inconsistências.

Em caso de erro de numeração, verifique se a numeração que quer salvar e não consegue existe na tabela SE1, campo E1\_NUM.

**Saiba Mais:**  
[Ajuste Controle de Numeração automática para Documento de Saída](http://tdn.totvs.com/pages/viewpage.action?pageId=329024579)

[FAT0284 A461NUMNF - Falha na reserva do próximo número disponível da SD9](https://tdn.totvs.com/x/qAEwGg)

[Geração Documento Saída - SD9](https://tdn.totvs.com/x/XyekKQ)
