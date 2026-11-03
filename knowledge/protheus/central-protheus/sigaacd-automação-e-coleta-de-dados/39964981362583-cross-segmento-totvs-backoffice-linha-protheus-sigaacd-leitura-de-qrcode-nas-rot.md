---
article_id: 39964981362583
category: SIGAACD - Automação e Coleta de Dados
content_hash: c3b702c691700cfd06bba3f1241096c3cb3c735817fc4ef378cc4438ea4c29f6
fetched_at: '2026-06-28T22:39:13.911546+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD - Leitura de QRCode
  nas rotinas padrão
type: support-article
updated_at: '2026-04-23T18:49:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39964981362583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAACD-Leitura-de-QRCode-nas-rotinas-padr%C3%A3o
---

As rotinas padrão do módulo SIGAACD permitem a leitura de QRCode pelo aplicativo Meu Coletor de Dados e por coletores físicos compatíveis. O QRCode deve conter apenas o código do produto (B1\_COD) no app, enquanto coletores físicos reconhecem o código de barras (B1\_CODBAR) para a leitura correta.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39964981353495) Tempo aproximado para leitura: 00:01:00 min  
  
**Dúvida**  
As rotinas padrão do módulo SIGAACD estão preparadas para realizar a leitura de QRCode nas movimentações de estoque e qual o padrão deve ser utilizado?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
As rotinas padrão do módulo ACD permitem a leitura de QRCode tanto pelo aplicativo (App Meu Coletor de Dados) quanto por coletores físicos que possuam hardware compatível com essa tecnologia.

Para que a leitura ocorra corretamente, o QRCode deve seguir as seguintes premissas:

* **Conteúdo do Código**: Atualmente, o sistema espera que o QRCode contenha apenas o código do produto (B1\_COD) no aplicativo Meu coletor de dados.

  Quanto ao coletor fisico, se ele tiver leitor de QRCode, nos campos do produto é esperado que ele reconheça o codigo de barras (B1\_CODBAR).

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[*Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Leitura de QRCode*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028654191-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Leitura-de-QRCode)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como configurar o ACD para imprimir etiquetas?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016771731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-ACD-para-imprimir-etiquetas)
