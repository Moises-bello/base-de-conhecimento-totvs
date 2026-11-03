---
article_id: 360010169092
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: da6a7fae2f41646491747030cab645530904c3f8aaba0006f40432694c368c5e
fetched_at: '2026-06-28T22:42:02.558654+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPEDFISCAL
  - Registro C176, C177, C178 e C179
type: support-article
updated_at: '2025-02-11T22:03:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010169092-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPEDFISCAL-Registro-C176-C177-C178-e-C179
---

**Dúvida**

Como gerar o registro C176, C177, C178 e C179?

**Ambiente**

Protheus - Livros Fiscais - A partir do 12.1.17

**Solução**

#### **REGISTRO C176: Ressarcimento de ICMS em operações com Substituição Tributária (Código 01, 55)**

Este registro é gerado para cada registro do tipo **C170**, em operações de saída que possuam complemento de ressarcimento de ICMS.

* Nota Fiscal Modelo 1 ou 1-A – Espécie “NF ou NFE”
* Nota Fiscal Eletrônica, Modelo 55 – Espécie “SPED”

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-7%2020%3A6%3A17.png?version=1&modificationDate=1467932777000&api=v2)

**Importante**

**Complemento de nota fiscal Automático**

Existem duas formas possíveis de alimentar a tabela CD0 automaticamente. São eles:

1 - Utilizando a rotina de Ressarcimento de ICMS ST (FISA132) que irá realizar uma apuração dos documentos de entrada e saída do período para gerar as informações da tabela CD0.

A documentação desta rotina está disponivel no link: [FIS0076\_Portaria\_CAT\_158\_de\_2015\_Ressarcimeto\_ICMS\_retido\_por\_Sujeição\_Passiva\_de\_Subs.Tributaria.](http://tdn.totvs.com/pages/viewpage.action?pageId=270103269)

2 - Utilizando o ponto de entrada MATUCOMP para realizar alterações automáticas nos complementos dos documentos fiscais após a emissão dos documentos de saída.

 Para mais informações sobre o processo do Ponto de entrada MATUCOMP, acesse: [MATUCOMP - Alterações automáticas -- 12485](http://tdn.totvs.com/pages/viewpage.action?pageId=6077107)

O parâmetro MV\_ATUCOMP deve ser configurado para que seja possível utilizar o Ponto de Entrada MATUCOMP,  **MV\_ATUCOMP = T.**

**Observação:**

Para maiores informações acessar link TDN

<http://tdn.totvs.com/display/PROT/ARQ0005_Gerar_Registro_C176_Do_SPED_FISCAL>

#### **REGISTRO C177: Operações com Produtos Sujeitos a Selo de Controle IPI**

As informações contidas neste registro são obtidas por documentos fiscais contendo mercadorias sujeitas a controle de selo que serão obtidas pelo cadastro das **Tabelas Guias de Selo (SFN)**,**Saldos Iniciais de Selo (SFO)**e**Cadastro de Produtos (SB1)**.

Esse documento está dividido em quatro seções:

* Seção 1 - Cadastro de Guias de Selos de Controle (MATA907)
* Seção 2 - Saldos de Guias de Selos de Controle (MATA908)
* Seção 3 - Registro de Entrada e Saída do Selo de Controle (MATR909)
* Seção 4 - Procedimentos para implementação

#### **REG****ISTRO C178: Operações com Produtos Sujeitos à Tributação de IPI por Unidade ou Quantidade de Produto**

As informações contidas neste registro são obtidas por documentos fiscais contendo mercadorias tributadas com IPI de Pauta.

#### **REGISTRO C179: Informações Complementares ST (Código 01)**

Este registro não é gerado, pois a informação não é tratada pelo Microsiga Protheus.

Para mais informações sobre o Sped Fiscal acessar:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
