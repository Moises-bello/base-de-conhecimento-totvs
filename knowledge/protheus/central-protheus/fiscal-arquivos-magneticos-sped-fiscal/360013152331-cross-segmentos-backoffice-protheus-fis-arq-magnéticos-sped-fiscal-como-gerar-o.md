---
article_id: 360013152331
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d51bb2fb4b9c2d62e0d9f0c677caea33966e3fbe174c8fe5ee6d6481b414066c
fetched_at: '2026-06-28T22:42:01.168255+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro 1010, 1100, 1105 e 1110 no Sped Fiscal?
type: support-article
updated_at: '2023-02-24T13:55:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013152331-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-1010-1100-1105-e-1110-no-Sped-Fiscal
---

#### **Dúvida** Como gerar os registros 1010, 1100, 1105 e 1110 no Sped Fiscal? **Ambiente** Protheus – Livros Fiscais – A partir da versão 12.25.

#### **Solução**

#### **Registro 1010: Obrigatoriedade de Registros do Bloco 1**

Indica a obrigatoriedade dos registros do **bloco 1** gerados no arquivo magnético. Informado pelas perguntas no *Wizard* da rotina.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2014%3A1%3A14.png?version=1&modificationDate=1465142121000&api=v2)

#### **Registro 1100: Registro de Informações sobre Exportação**

Este registro é gerado a partir do livro fiscal, somente para notas de saída modelo **01, 04** ou **55**. As informações complementares de exportação são lançadas pela rotina **Complementos dos documentos Fiscais**.

Verifique os conteúdo do parâmetro **MV\_EECSPED**:

Se **MV\_EECSPED= .T.** , os registros de exportação do SPEDFISCAL serão gerados com dados da integração SIGAEEC.

Se **MV\_EECSPED= .F.** , os registros de exportação do SPEDFISCAL serão gerados com dados da da tabela CDL.

**Cadastro Cliente:**

Para habilitar a tela de exportação nos complementos da NF, o cadastro do cliente deve estar com a seguinte configuração:

 

**Estado** = **EX**

**Tipo** = **X** - exportação

**Município** = 99999 (estrangeiro)

Livros Fiscais / Atualizações / Movimentos/ Nota Fiscal manual de saída / Outras ações – Complementos

Preencher as “Informações complementares – exportações” e salvar.

Parâmetro da *wizard* do SPEDFISCAL para geração do registro 1100

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2014%3A4%3A20.png?version=1&modificationDate=1465142308000&api=v2)

#### **Registro 1105: Documentos Fiscais de Exportação**

Este registro é gerado a partir do livro fiscal, somente para notas de saída modelo 01, 04 ou 55. As informações complementares de exportação são lançadas pela rotina **Complementos dos documentos Fiscais**. Neste registro são informadas as notas fiscais da efetiva exportação. Para os casos de complementos de documentos fiscais de remessa para exportação, o documento da efetiva exportação pode ser lançado pela rotina **Complementos dos documentos.**

Parâmetro da *wizard* do SPEDFISCAL para geração do registro 1105:

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2014%3A4%3A20.png?version=1&modificationDate=1465142308000&api=v2)

#### **Registro 1110: Operações de Exportação Indireta - Mercadoria de Terceiros**

Este registro é gerado a partir do livro fiscal, somente para notas de saída modelo 01 ou 55, sendo exigido apenas quando a mercadoria destinada à exportação não for produzida pelo próprio emitente. As informações complementares de exportação são lançadas pela rotina **Complementos dos documentos Fiscais**. Neste registro são informadas as notas fiscais de entrada com fim específico de exportação, no caso de exportações indiretas.

**1** – Gerar uma NF de saída usando um CFOP de Exportação e um cliente estrangeiro = **EX**.

 

- Usar um CFOP de exportação **indireta**. 

 - O CFOP da nota de saída deve estar nesse parâmetro **MV\_EXPIND**

**2** – Gerar os complementos da NF na tela de NF manual de saída/complementos/exportação:

 - Preencher todos os campos dos complementos, usando uma NF de entrada válida como referência da exportação.

Deixar esse campo CDL\_NATEXP = 1 (Indireta)

Parâmetro da *wizard* do SPEDFISCAL para geração do registro 1110:

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2014%3A4%3A20.png?version=1&modificationDate=1465142308000&api=v2)

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
