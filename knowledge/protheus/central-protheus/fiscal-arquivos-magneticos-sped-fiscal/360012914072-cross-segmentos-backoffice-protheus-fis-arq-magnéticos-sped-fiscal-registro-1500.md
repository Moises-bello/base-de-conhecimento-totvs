---
article_id: 360012914072
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: daa9e04b752e234618ca0f371aa56bdc772364050d6cb6646762fdb9dc0dc123
fetched_at: '2026-06-28T22:42:02.396100+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - REGISTRO 1500 e 1510
type: support-article
updated_at: '2025-02-11T21:25:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012914072-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-REGISTRO-1500-e-1510
---

#### **Dúvida** Como gerar o registro 1500 e 1510? **Ambiente** Protheus – Livros Fiscais – A partir da versão 11.80 **Solução**

#### **Registro 1500: Nota Fiscal/Conta de Energia Elétrica Código 06 - Operações Interestaduais**

1 -Lançar documento fiscal com espécie NFCEE onde fornecedor ou cliente com estado diferente do informado no parâmetros MV\_ESTADO.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A53%3A31.png?version=1&modificationDate=1465156058000&api=v2)

**Configuração Produto**

Campo

Origem (B1\_ORIGEM) =?

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A53%3A52.png?version=1&modificationDate=1465156079000&api=v2).

**Configuração de TES**

Campos

Calcula ICMS (F4\_ICM) =?

Calcula IPI (F4\_IPI)=?

Livro ICMS, IPI = diferentes de Não ->“Deve ser configurado campo de um dos livros com opção diferente de não para geração dos valores nas tabelas SF3 e SFT”

Sit. Trib. ICM (F4\_SITTRIB)=?

Cod. Trib. IPI (F4\_CTIPI)=?

**->Se for existir calculo de PIS COFINS**

PIS/COFINS (F4\_PISCOF) = Ambos   
Cred. PIS/COF (F4\_PISCRED) = Debita(Saída)/Credita (Entrada)

Sit. Trib PIS (F4\_CSTPIS) = Entrada (50 a 66) / Saida (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66

Sit. Trib COFINS (F4\_CSTCOF) = Entrada (50 a 66) / Saida (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66

**->Se não for existir calculo de PIS COFINS**

PIS/COFINS (F4\_PISCOF) = Não considera

Cred. PIS/COF (F4\_PISCRED) =Não Calcula

Sit. Trib PIS (F4\_CSTPIS) = Entrada (70) / Saida (49)

Sit. Trib COFINS (F4\_CSTCOF) = Entrada (70) / Saida (49)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A54%3A14.png?version=1&modificationDate=1465156101000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A54%3A27.png?version=1&modificationDate=1465156114000&api=v2)![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A54%3A38.png?version=1&modificationDate=1465156125000&api=v2)![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A54%3A48.png?version=1&modificationDate=1465156135000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A54%3A59.png?version=1&modificationDate=1465156146000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A55%3A11.png?version=1&modificationDate=1465156158000&api=v2)

**2 -Complemento que devem ser realizados após lançamento das notas fiscais**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A55%3A40.png?version=1&modificationDate=1465156187000&api=v2)**

3 -Ao gerar arquivo SPEDFISCAL configurar pergunta da WIZARD

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A56%3A1.png?version=1&modificationDate=1465156208000&api=v2)

#### **Registro 1510: Itens do Documento Nota Fiscal/Conta Energia Elétrica Código 06**

Este registro será gerado para as informações do item tabela SFT dos Livros fiscais  da nota de energia elétrica conforme processo do registro 1500.

 Dessa forma para geração desse registro deverá ser seguindo orientações do registro 1500.

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
