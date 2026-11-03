---
article_id: 25471272246423
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: bc548c8a5bb8ca652468545b184b33ade9599cba7ef6103093e3d96fc2e125a7
fetched_at: '2026-06-28T22:42:03.602634+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPED FISCAL
  - Erro código do item inválido campo 02 do registro 1400
type: support-article
updated_at: '2024-08-07T17:27:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25471272246423-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Erro-c%C3%B3digo-do-item-inv%C3%A1lido-campo-02-do-registro-1400
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25471241305367) Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência:**

Erro no campo **02** do registro **1400 - Código do item inválido**.

**Ambiente:**

Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.2210

**Causa:**

Com base no **Guia prático**, o campo **02** do registro **1400** possui a seguinte critério de validação:

“Campo **02** (**COD\_ITEM\_IPM**) - Preenchimento: Consulte a Secretaria de Fazenda de cada UF quanto ao município a ser informado.

a) Se o município no campo **03** (**MUN**) pertencer à UF informada no campo **09** do Registro **0000**, o código informado deve existir na **Tabela 5.9.1** de Itens UF Índice de Participação dos Municípios, ou deve existir no campo **COD\_ITEM** do registro **0200**.

b) Se o município no campo **03 (MUN)** pertencer a uma UF informada no campo **02** do Registro **0015**, a **Tabela 5.9.2** de Itens UF\_ST Índice de participação dos Municípios dessa UF deve conter o código informado.”

Desta forma, mesmo com o código válido de acordo com a **tabela 5.9.1**, após à atualização disponibilizada pela Receita Feral do PVA para **Versão 4.0.4**, o programa validador passou a apontar erro no registro **1400** campo **02:**

![1400.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25471272230423)

Devido à apresentação do registro **0015** com a mesma UF contida no registro **0000** campo **09 (IE)**. Com esta nova validação do PVA para que o erro **não** ocorra, **não** deverá ser informado no registro **0015**a inscrição estadual da empresa na unidade federativa que a empresa estiver situada.

**Solução:**

Para a correção do erro, basta **não** informar no parâmetro **MV\_SUBTRIB** a inscrição estadual da empresa na unidade federativa que estiver situada.

**Observação**: O parâmetro **MV\_SUBTRIB** deve ser configurado a UF + Inscrição Estadual, nos estados que o contribuinte houver inscrição estadual. O parâmetro deverá ser informado conforme o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25471272232215)

Documentações complementares:

<http://sped.rfb.gov.br/pagina/show/7449>

<http://sped.rfb.gov.br/estatico/38/22C37BE2CE82F67C1A161538F27551C2D8E7E9/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.1.6.pdf>

<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

<https://tdn.totvs.com/pages/releaseview.action?pageId=642623935>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/5384293565463-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-Registro-0015-do-Sped-Fiscal-gerado-indevidamente?source=search>
