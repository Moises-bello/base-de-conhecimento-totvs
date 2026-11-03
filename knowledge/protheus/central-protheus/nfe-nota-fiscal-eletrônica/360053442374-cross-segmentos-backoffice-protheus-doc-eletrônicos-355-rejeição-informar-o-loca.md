---
article_id: 360053442374
category: NFe - Nota Fiscal Eletrônica
content_hash: c07a74cca5105365026f6cf5f04c522fe261a259940d6e53cbbcdf8528eaca63
fetched_at: '2026-06-28T22:40:01.405169+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 355 Rejeição :
  Informar o local de saída do Pais no caso da exportação '
type: support-article
updated_at: '2021-11-24T14:33:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053442374--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-355-Rejei%C3%A7%C3%A3o-Informar-o-local-de-sa%C3%ADda-do-Pais-no-caso-da-exporta%C3%A7%C3%A3o
---

**Dúvida**Como solucionar a rejeição abaixo:

355 Rejeição : Informar o local de saída do Pais no caso da exportação  ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para notas de exportação a **Sefaz** valida alguns campos e tornando o seu preenchimento obrigatório no **Complemento de Exportação** no modulo **Livros Fiscais.**

1- Acesse a rotina **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099707813/20201117_103818.gif)

2- Preencha os **campos abaixo:**

Prod NF (**CDL\_PRODNF**)  
Item NF (**CDL\_ITEMNF**)  
UF Emb (**CDL\_UFEMB)**Loc Emb (**CDL\_LOCEMB**)

3- No configurador preencha o parâmetro **MV\_EECFAT**=.**F**. para que as informações do complemento da exportação seja da tabela **CDL**.

4- Após, o preenchimento dos campos clique no campo **Salvar** para confirma a operação. Ao terminar a inclusão do complemento de exportação transmita a nota.

* **Exemplo do XML:**

![EXPORTACAO_1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360096282413/EXPORTACAO_1.PNG)

* **Validação da Sefaz:**

![EXPORTACAO_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360094018474/EXPORTACAO_2.PNG)
