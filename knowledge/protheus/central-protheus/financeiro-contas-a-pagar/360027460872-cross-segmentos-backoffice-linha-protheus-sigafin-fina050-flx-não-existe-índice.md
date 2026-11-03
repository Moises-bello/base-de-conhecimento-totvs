---
article_id: 360027460872
category: Financeiro - Contas a Pagar
content_hash: cb29e8fe35892accbfb41362711ad73af24bd3e4e392fe01a52175cb8f281004
fetched_at: '2026-06-28T22:38:08.556124+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - FLX: NÃO
  EXISTE ÍNDICE PARA ESSE ALIAS NO SINDEX'
type: support-article
updated_at: '2022-08-05T16:59:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027460872-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-FLX-N%C3%83O-EXISTE-%C3%8DNDICE-PARA-ESSE-ALIAS-NO-SINDEX
---

**Ocorrência**No módulo **Financeiro**, ao tentar realizar um inclusão (**FINA050**), caso apresente a mensagem: "**FLX : Não existe índice para esse alias no SINDEX**", como mostrado abaixo:

![Tela_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360027348911/Tela_1.PNG)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA050 - Todas as versões

**Solução**Realize o seguinte procedimento demonstrado abaixo:

No **Configurador: Ambiente -> Dicionário -> Base de Dados**

Abra a Tabela **FLX** e confira se todos os campos da tabela estão criados, como mostrado:  
![tela_4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360027343972/tela_4.PNG)

Valide também se os índices estão criados, como descritos:

Segue linha para visualização: **FLX\_FILIAL+FLX\_FORNEC+FLX\_LOJA+FLX\_ITEM**

Detalhes da Tela:

![tela_3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360027343932/tela_3.PNG)![tela_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360027343952/tela_2.PNG)
