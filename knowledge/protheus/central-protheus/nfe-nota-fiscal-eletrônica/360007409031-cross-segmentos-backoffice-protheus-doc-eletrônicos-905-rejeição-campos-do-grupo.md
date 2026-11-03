---
article_id: 360007409031
category: NFe - Nota Fiscal Eletrônica
content_hash: 1cda893bd68a59d94fab1c4dbd8878681aca81882206fa13efaa20daa0189d1f
fetched_at: '2026-06-28T22:40:00.054853+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 905 Rejeição :
  Campos do grupo Fatura não informados'
type: support-article
updated_at: '2025-06-26T14:45:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007409031-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-905-Rejei%C3%A7%C3%A3o-Campos-do-grupo-Fatura-n%C3%A3o-informados
---

**Dúvida**Como solucionar a rejeição 905 : Campos do grupo Fatura não informados

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

* **A Sefaz espera que o XML** seja gerado assim com o grupo fatura completo, por padrão se gerado o grupo de cobrança e gerado os dados da fatura.

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**[Pacotes de Atualização - Documentos Eletrônicos (NFE | NFSE | MDE | MDFE (FAT))](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

     2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:    
[RDMAKES SPED NFE](https://suporte.totvs.com/portal/p/10098/download#detail/1152113%20)

   3. Após isso, **exclua a nota e gere** novamente.

* **Importante:**

**Para não gerar a rejeição, pode ser realizada a configuração abaixo:**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar alterar o **parâmetro MV\_GRUPCOB = .F. no XML não será apresentadas as duplicatas.**

![20201117_154307.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071597202455)

* **Validação da Sefaz:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404571556119)
