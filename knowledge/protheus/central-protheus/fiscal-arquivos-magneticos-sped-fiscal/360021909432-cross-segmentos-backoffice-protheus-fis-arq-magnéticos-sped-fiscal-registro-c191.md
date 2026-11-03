---
article_id: 360021909432
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: a879d14b1392bc82f3ca003921224d39b8cc87467b7f03b87cb61add300bf7cb
fetched_at: '2026-06-28T22:42:02.423780+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C191 - Informações do Fundo de Combate à Pobreza – FCP – na NF-e (Código
  55)
type: support-article
updated_at: '2025-02-11T21:30:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021909432-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C191-Informa%C3%A7%C3%B5es-do-Fundo-de-Combate-%C3%A0-Pobreza-FCP-na-NF-e-C%C3%B3digo-55
---

**Dúvida**De onde o sistema irá buscar os valores para compor o novo registro C191 da EFD ICMS/IPI que será obrigatório no novo layout?  
  
**Ambiente**Protheus - Livros Fiscais - A partir da versão 12.1.17

Observação: Disponível na versão 11.80 apenas para clientes com garantia estendida.  
  
**Solução**Este Registro tem por objetivo apresentar os valores de **FECP** do documento fiscal (apenas notas fiscais modelo 55).

Neste registro não serão apresentados os valores de **FECP** sobre o Diferencial de alíquota (**EC/87**), que já são apresentados no **registro C101**.

Os valores deste registro são meramente informativos e não são contabilizados na apuração dos **registros no bloco E**. A obrigatoriedade e forma de apresentação de cada campo deste registro deve ser verificada junto às unidades federativas.

Para gerar registro é necessário processar arquivo **SPED Fiscal** a partir de janeiro de 2019 e habilitar na *wizard* **SPED Fiscal**, na Guia**"Parâmetros para geração"** a pergunta **"Gera Registro C191 - FECP"**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089508714/mceclip0.png)

**Composição do registro:**

Campo 1 - **VL\_FCP\_OP**é gerado com valor do campo**FT\_VALFECP**(Valor FECP)

Campo 2**- VL\_FCP\_ST** é gerado com valor do campo**FT\_VFECPST**(Valor FECP ST)

Campo 3**- VL\_FCP\_RET** é gerado com valor do campo**FT\_VFCPANT** (Vlr. FCP Ant)

**Importante:**Notas de entrada com ICMS recolhido Anteriormente com **FECP**:

Para nota de entrada onde já foi recolhido **ICMS ST** anteriormente, a base e o valor  recolhido devem estar em informações complementares da nota de entrada emitida pelo fornecedor.

Ao entrar com nota no sistema devem ser preenchidos manualmente o campo **D1\_VFCPANT**(**Valor do FCP Rec. Ant.**) com valor calculado e recolhido anteriormente.

Para criação do campo **D1\_VFCPANT** é necessário aplicar o dicionário do link abaixo através do **UPDDISTR:**

**[https://suporte.totvs.com/portal/p/10098/download#detail/706704](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download%23detail/706704&sa=D&source=hangouts&ust=1544213009076000&usg=AFQjCNGeFQladh_fqToBxTeAWLBh6QfGAQ)**
