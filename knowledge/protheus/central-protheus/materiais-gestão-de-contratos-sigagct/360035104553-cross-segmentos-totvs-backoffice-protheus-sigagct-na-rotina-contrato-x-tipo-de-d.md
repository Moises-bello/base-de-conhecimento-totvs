---
article_id: 360035104553
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 975e8687ebe8e05361e74f5e5f042d44011e703c431ffbdb6fc979ef9da1b67b
fetched_at: '2026-06-28T22:37:23.925946+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Na rotina Contrato
  X Tipo de Documento X Situação (CNTA210) ao visualizar a consulta padrão do campo
  Tipo Doc (CNJ_TPDOC) a linha está duplicada e não está trazendo o código opcional
  do cadastro
type: support-article
updated_at: '2022-05-19T21:25:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035104553-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Na-rotina-Contrato-X-Tipo-de-Documento-X-Situa%C3%A7%C3%A3o-CNTA210-ao-visualizar-a-consulta-padr%C3%A3o-do-campo-Tipo-Doc-CNJ-TPDOC-a-linha-est%C3%A1-duplicada-e-n%C3%A3o-est%C3%A1-trazendo-o-c%C3%B3digo-opcional-do-cadastro
---

**Ocorrência**

Na rotina ***Contrato X Tipo de Documento X Situação (CNTA210)*** ao visualizar a consulta padrão do campo ***Tipo Doc (CNJ\_TPDOC)*** a linha está duplicada e não está trazendo o código opcional do cadastro  
  
**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
  
**Solução**

Ajustada a consulta padrão para que não haja duplicidade dos registros. A exibição do **Código Opcional** (**CN5\_CODOPC**) não é necessária, pois a amarração do **Tipo de Documento** é realizada pelo campo **Código** (**CN5\_CODIGO**).

**Importante:**Esta atualização estará disponível a partir da **release 12.1.28.**

Para surtir o efeito desejado em releases anteriores, deve-se alterar a consulta padrão seguindo o procedimento abaixo:

Acesse: **SIGACFG** > **Base de Dados** > **Dicionário** > **Base de Dados**, selecione **Consulta padrão,** pesquise pela consulta **CN5**(**Tipo de Documento**) e clique em **Editar**.

Avance até chegar na tela de inclusão de filtro.

Digite o filtro conforme a imagem:

**Filtro: CN5->CN5\_SEQ = '00'**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045756573/mceclip0.png)

Clique em **Finalizar**.

Sua consulta padrão será atualizada com sucesso.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
