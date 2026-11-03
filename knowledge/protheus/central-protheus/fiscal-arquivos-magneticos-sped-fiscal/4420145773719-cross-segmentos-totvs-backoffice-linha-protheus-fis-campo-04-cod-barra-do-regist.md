---
article_id: 4420145773719
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e196f887b82d0c6cc2bb41b7d6af81d9828ea28ab181f881d45664654aea3dab
fetched_at: '2026-06-28T22:42:03.737313+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- campo 04 - COD_BARRA
  do registro 0200 no SPED FISCAL
type: support-article
updated_at: '2022-01-24T19:42:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420145773719-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-campo-04-COD-BARRA-do-registro-0200-no-SPED-FISCAL
---

**Dúvida**

Campo **04 - COD\_BARRA** do registro **0200** no **SPED FISCAL**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução**

Foi implementado uma tratativa no arquivo para que quando for preenchido os dois campos (**B1\_ CODGTIN e B1\_CODBAR**), seja atribuído ao registro 0200 para o campo 04 - COD\_BARRA, o conteúdo do campo **B1\_CODGTIN** ao invés do conteúdo do campo **B1\_CODBAR**.

Também implementado a tratativa da leitura do campo **B1\_ CODGTIN**para o registro 0200 do SPED FISCAL.

Para que o sistema considere o conteúdo do campo **B1\_ CODGTIN ou B1\_CODBAR**no arquivo, é necessário que o mesmo esteja com quantidade compatível com o padrão GTIN (8, 12, 13, ou 14 números).

Deve-se levar em consideração que o sistema adiciona um número no final para composição:

**Exemplo:**

Para GTIN de 14, o usuário digitará 13 números, e o sistema complementará com o 14° número. Se o campo não estiver dentro da quantidade padrão, o sistema não levará para o arquivo.

**Assuntos relacionados:**

* [FIS0009\_Manual\_Utilização\_SPEDFISCAL](https://tdn.totvs.com/x/VSEwDg)
* [DSERTSS1-7561 Novo campo na SB1 referente ao código GTIN para atender quem utiliza o ACD](https://tdn.totvs.com/x/3gR8FQ)
* [DSERTSS1-68/ DSERTSS1-10670 -DT NF-e Implementação da versão 4.00](https://tdn.totvs.com/x/KoP9Eg)
* [FIS0005\_SPED\_FISCAL](https://tdn.totvs.com/x/MYGUD)
