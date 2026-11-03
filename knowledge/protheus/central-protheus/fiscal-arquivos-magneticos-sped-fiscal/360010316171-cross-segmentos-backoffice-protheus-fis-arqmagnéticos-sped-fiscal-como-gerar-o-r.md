---
article_id: 360010316171
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 697687cb4ba287eb57d44d30483b483b487d368d075aac167ef4083f37b2cdd2
fetched_at: '2026-06-28T22:42:03.566403+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar o registro C113 - Documento Fiscal Referenciado?
type: support-article
updated_at: '2023-04-06T19:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316171-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-registro-C113-Documento-Fiscal-Referenciado
---

**Dúvida**Como gerar o registro C113 do arquivo magnético SPEDFISCAL?  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.25  
  
**Solução**Neste registro, são apresentados todos os documentos fiscais relacionados. A associação de outros documentos ao documento fiscal original pode ser feita pela rotina **Complementos dos documentos Fiscais - "Documentos Fiscais"**

Para solucionar essa dúvida, realize os seguintes passos:

1.Acesse o módulo Livros Fiscais> Atualizações> Movimentos> NF. Entrada Manual ou NF. Manual de Saída;

2. Selecione a nota de Devolução/ Beneficiamento/ Complemento de Preço

3. Clique em Ações Relacionadas> Complemento > **Documentos Fiscais (Tabela CDD);**

4. Preencha manualmente o campo **Inf. Compl (CDD\_IFCOMP).**Importante: Os principais campos serão preenchidos automaticamente.  
Dessa forma será gerado no arquivo SPEDFISCAL os registros C113. Lembrando que na tabela **SFT,** os campos da nota onde a origem foi referenciado conforme exemplo abaixo:

Campos referentes a nota fiscal de origem na tabela **SFT****(FT\_NFISCAL, FT\_ITEM** e **FT\_SERIE):**Deve ser preenchido na nota fiscal (Tipo= Normal, Devolução, Beneficiamento ou Complemento etc.) que será complementada na **tabela CDD,** os campos abaixo referem-se à nota de origem para liberação dos campos da **CDD**.

**Exemplo para gerar o registro C113:**

**DOCUMENTO DE ENTRADA** - Tipo da Nota = Normal, Devolução, Beneficiamento, Complemento.

1. Preencha os campos com as informações da nota de origem **D1\_NFORI, D1\_SERIORI e D1\_ITEMORI**, conforme exemplo abaixo:  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-6%2017%3A44%3A34.png?version=1&modificationDate=1467837915000&api=v2)

**DOCUMENTO DE SAÍDA -** Tipo do Pedido = Normal, Devolução, Beneficiamento, Complemento.

1. Preencha os campos com as informações da nota de origem **C6\_NFORI, C6\_SERIORI e C6\_ITEMORI**, conforme exemplo abaixo:  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-6%2017%3A45%3A2.png?version=1&modificationDate=1467837943000&api=v2)  
  
2. Após realizar a escrituração da NF de Devolução, Beneficiamento, Complemento, de referência à nota de origem, os campos da tabela **SFT** (**FT\_ITEMORI, FT\_SERORI e FT\_NFORI**) serão preenchidos para nota fiscal referenciada que deve gerar C113**.**

3. Preencha o complemento na rotina **MATA910** ou **MATA920**.

Documentos fiscais da nota onde documento de origem foi referenciado para geração do registro C113.  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-6%2017%3A45%3A15.png?version=1&modificationDate=1467837956000&api=v2)

Após adicionar informações na aba "**Documentos Fiscais"**, adicione também informações na aba **"Informações Complementares"** conforme o print abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/xyHZJbsDkNWD7J0bQMJDQ8VAk/?name=image.png)

Atenção: Para a geração do registro C113, será gerado um registro Pai C110 - Informações complementares.

**Complemento de Nota Fiscal Automático**   
Utilizado para alterações automáticas nos complementos dos documentos fiscais, após a emissão das Notas Fiscais.   
Para informações sobre o Ponto de entrada MATUCOMP, acesse:

<https://tdn.totvs.com/pages/releaseview.action?pageId=642645988>

 O parâmetro MV\_ATUCOMP deve ser configurado para que seja possível utilizar o Ponto de Entrada MATUCOMP,  MV\_ATUCOMP = T .
