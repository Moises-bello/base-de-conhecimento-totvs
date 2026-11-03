---
article_id: 360010382871
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 86b1181cd81d9af68e18c08777af25f8f5e8843e287b605b0487dbaa3aca1cce
fetched_at: '2026-06-28T22:42:03.661968+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPEDFISCAL -
  Como gerar o registro C112 no arquivo txt?
type: support-article
updated_at: '2022-12-07T13:19:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010382871-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Como-gerar-o-registro-C112-no-arquivo-txt
---

**Dúvida**  
Como gerar o **registro C112**: Documento de Arrecadação Referenciado.  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Neste registro serão relacionados todos os documentos de arrecadação referenciados no documento fiscal. As informações serão retiradas da **Tabela de Guias de Recolhimentos (SF6)**. A associação de documentos de arrecadação ao documento fiscal, pode ser feita por meio da rotina de **Complementos dos Documentos Fiscais**. Na geração deste registro são consideradas as **Nota de Espécie NF, NFA, NFP, NFCE e SPED.**Para solucionar essa dúvida, realize o seguinte procedimento:  
1. Acesse a rotina de **Complemento dos Documentos Fiscais (MATA926);**2. Acesse e preencha todos os campos das abas grifadas abaixo:

**![pag3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8366166520471/pag3.png)**3. Realize a associação da nota fiscal com a guia de arrecadação preenchendo os campos habilitados pelo sistema.

Após isso, salve e faça um novo teste gerando um novo arquivo do SpedFiscal.

O registro será gerado com sucesso:

![pag4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8366221402391/pag4.png)

**Complemento de Nota Fiscal Automático:**  
Ponto de Entrada MATUCOMP: Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais. Para informações sobre o Ponto de entrada MATUCOMP, acesse:   
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

O parâmetro **MV\_ATUCOMP** deve ser configurado para que seja possível utilizar o **Ponto de Entrada MATUCOMP (MV\_ATUCOMP = T)**.
