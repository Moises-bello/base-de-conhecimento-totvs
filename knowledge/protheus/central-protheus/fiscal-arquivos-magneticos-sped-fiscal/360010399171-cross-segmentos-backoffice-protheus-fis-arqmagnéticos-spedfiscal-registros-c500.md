---
article_id: 360010399171
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 6bb594df1540dbb2d508c42468fde9248523a69eee404cb784bec3557a549637
fetched_at: '2026-06-28T22:42:03.670492+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPEDFISCAL -
  Registros C500, C510 e C590
type: support-article
updated_at: '2024-06-18T19:50:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010399171-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registros-C500-C510-e-C590
---

**Dúvida**

Como gerar os registros C500, C510 e C590 do Sped Fiscal?

**Produto**

Protheus - Livros Fiscais - A partir da 12.1.17

**Solução**

#### **REGISTRO C500: Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento D'água Canalizada (Código 29) e Nota Fiscal Consumo Fornecimento de Gás  (CÓDIGO 28)**

Este registro é gerado a partir do livro fiscal e é composto de notas fiscais dos seguintes modelos:

* Nota Fiscal/Conta de Energia Elétrica, Modelo 6 - Espécie = "NFCEE".
* Nota Fiscal Consumo de Gás, Modelo 28 - Espécie ="NFCFG".
* Nota fiscal de fornecimento de agua, Modelo 29 - Espécie ="NFFA”.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A17%3A10.png?version=1&modificationDate=1467933431000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A22%3A25.png?version=1&modificationDate=1467933745000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A27%3A57.png?version=1&modificationDate=1467934076000&api=v2)

**Configuração Produto**

Campo:

Origem (B1\_ORIGEM) =?

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A28%3A23.png?version=1&modificationDate=1467934106000&api=v2)

**Configuração de TES**

Campos:

Calcula ICMS (F4\_ICM) =?

Calcula IPI (F4\_IPI)=?

Livro ICMS, IPI = diferentes de Não ->“Deve ser configurado campo de um dos livros com opção diferente de não para geração dos valores nas tabelas SF3 e SFT”

Sit. Trib. ICM (F4\_SITTRIB)=?

Cod. Trib. IPI (F4\_CTIPI)=?

**- Se  existir calculo de PIS COFINS**

PIS/COFINS (F4\_PISCOF) = Ambos   
Cred. PIS/COF (F4\_PISCRED) = Debita(Saída)/Credita (Entrada)

Sit. Trib PIS (F4\_CSTPIS) = Entrada (50 a 66) / Saída (01 a 49) lembrando que as CST de credito estão no intervalo 50 a 66

Sit. Trib COFINS (F4\_CSTCOF) = Entrada (50 a 66) / Saída (01 a 49) lembrando que as CST de crédito estão no intervalo 50 a 66

**-Se não for existir calculo de PIS COFINS**

PIS/COFINS (F4\_PISCOF) = Não considera

Cred. PIS/COF (F4\_PISCRED) =Não Calcula

Sit. Trib PIS (F4\_CSTPIS) = Entrada (70) / Saída (49)

Sit. Trib COFINS (F4\_CSTCOF) = Entrada (70) / Saída (49)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A29%3A0.png?version=1&modificationDate=1467934139000&api=v2)

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A30%3A20.png?version=1&modificationDate=1467934219000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A30%3A33.png?version=1&modificationDate=1467934233000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A30%3A45.png?version=1&modificationDate=1467934244000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A30%3A56.png?version=1&modificationDate=1467934256000&api=v2)**

**Importante**

Cadastro de TES (SF4)

**Código da Situação tributária do ICMS (F4\_SITTRIB).**

**Código da Situação tributária do IPI (F4\_CTIPI).**

**Código da Situação tributária do PIS**, caso seja um TES que **calcule PIS(F4\_CSTPIS).**

**Código da Situação tributária do COFINS**, caso seja um TES que **calcule COFINS(F4\_CSTCOF).**

Para todos os registros no qual é necessário informar a classificação fiscal do item, com relação aos impostos ICMS, IPI, PIS e COFINS, existe a possibilidade de alterar a classificação fiscal padrão apresentada pelo sistema (composta pelo produto e pelo TES). Caso exista esta necessidade, deve-se customizar o **Ponto de Entrada SPDFIS03.** Para mais detalhes sobre este Ponto de Entrada, acesse: [SPDFIS03 - Altera a Situação Tributária dos Impostos ICMS, IPI, PIS e COFINS](http://tdn.totvs.com/pages/releaseview.action?pageId=6077157)

**Complementos que devem ser realizados após lançamento das notas fiscais:**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A31%3A14.png?version=1&modificationDate=1467934274000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A31%3A27.png?version=1&modificationDate=1467934287000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A31%3A37.png?version=1&modificationDate=1467934297000&api=v2)**

**Complemento de nota fiscal Automático**

Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais.

Para mais informações sobre o processo do Ponto de entrada MATUCOMP, acesse: [MATUCOMP - Alterações automáticas -- 12485](http://tdn.totvs.com/pages/viewpage.action?pageId=6077107)

O parâmetro MV\_ATUCOMP deve ser configurado para que seja possível utilizar o Ponto de Entrada MATUCOMP,  **MV\_ATUCOMP = T.**

#### **REGISTRO C510: Iten do Documento Nota Fiscal/Conta Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento D'água Canalizada (Código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28)**

Este registro é gerado a partir do livro fiscal tabela SFT, contendo as especificações do serviço de energia elétrica ou de gás, sendo exigido apenas para saída. É composto de notas fiscais dos seguintes modelos:

* Nota Fiscal/Conta de Energia Elétrica, Modelo 6 - Espécie = "NFCEE"
* Nota Fiscal Consumo de Gás, Modelo 28 - Espécie ="NFCFG"
* Nota fiscal de fornecimento de agua, Modelo 29 - Espécie ="NFFA”

#### **REGISTRO C590: Registro Analítico do Documento - Nota Fiscal/Conta de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento D'água Canalizada (Código 29) e Nota Fiscal Consumo Fornecimento de Gás (Código 28)**

Este registro é gerado a partir do livro fiscal, contendo as especificações do serviço de energia elétrica ou de gás, sendo exigido apenas para saída. É composto de notas fiscais dos seguintes modelos:

* Nota Fiscal/Conta de Energia Elétrica, Modelo 6 - Espécie = "NFCEE"
* Nota Fiscal Consumo de Gás, Modelo 28 - Espécie ="NFCFG"
* Nota fiscal de fornecimento de água, Modelo 29 - Espécie ="NFFA”

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
