---
article_id: 31671861798295
category: TAF - GIA
content_hash: 4187a562aacd6f0bc831a28b47aa255df1ada7b248017d20e3afb75a6bca0975
fetched_at: '2026-06-28T22:41:32.392917+00:00'
product: protheus
section_id: 1500001547982
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - GISS ABRASAF - Como gerar a GISS
  ABRASF no TAF.
type: support-article
updated_at: '2026-06-16T21:22:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31671861798295-Cross-Segmentos-Backoffice-Protheus-TAF-GISS-ABRASAF-Como-gerar-a-GISS-ABRASF-no-TAF
---

**Dúvida**  
Como realizar a geração do XML da GISS ABRASF no TAF.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal- Todas as versões.

**Solução**

**Integração**

**Um dos pre requisitos para integração dos dados da GISS ABRASAF, é a utilização do TSI, em integrações realizadas pelo extrator fiscal será preciso ajuste manuais em campos que não são alimentado pelo Extrator.**

**Processo realizado pelo extrator:** [**Cross Segmentos - Backoffice Protheus - TAF - GISS ABRASAF - Extrator fiscal - GISS ABRASAF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31670844301591-Cross-Segmentos-Backoffice-Protheus-TAF-GISS-ABRASAF-Extrator-fiscal-GISS-ABRASAF)

Doc complementar: <https://tdn.totvs.com/pages/releaseview.action?pageId=878920036>

# **Configurações iniciais**

 No módulo 84 (Totvs Automação Fiscal) configurar no menu o complemento cadastral.

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671861762711)

Selecionar o código **000021** GISS modelo ABRASF

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671861763223)

# **Documentos envolvidos**

Os documentos envolvidos na geração do arquivo são:

* Documentos de entrada com espécie NFS e RPS que incidem ISS (Tributo 01 ou 16)
* Documentos de ISS que possuem cadastro de obras

# **Geração do arquivo**

Selecionar no menu a Central de Obrigações

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671861763863)

Selecionar a esfera Municipal

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671861765527)

Selecionar o código **000021**- Giss Modelo ABRASF

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671861766807)

Clicar em avançar

Na tela de wizard, preencher os campos:

**Diretório do arquivo destino**-  Refere-se ao caminho onde será gerado o arquivo da GISS modelo ABRASF.

**Nome do arquivo destino** - Trata-se do nome do arquivo que será gerado. 

**Data inicial** - Início do período considerado no processamento. 

**Data final** -  Término do período considerado no processamento. 

**Seleciona filiais** - permite selecionar diversas filiais para o processamento.  A utilização do parâmetro Aglutina, depende que este seja selecionado com Sim.

**Aglutina** - Caso outras filiais sejam selecionadas, utilizando este parâmetro, será possível, não aglutinar, aglutinar a seleção de filiais por CNPJ ou ainda aglutinar por CNPJ e por Inscrição Estadual.

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671847707031)

No diretório de destino, será criado o arquivo XML.

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31671861769367)

# **Opções de Geração**

  Na Wizard, há os campos **"Seleciona Filiais"** e **"Aglutina"**, esses campos influenciam na forma como os arquivos são gerados.

* Nos casos em que forem selecionadas as opções "Seleciona Filiais **-Não** e Aglutina **-Não"**

Será gerado um arquivo xml para a **Filial** **logada**.

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673887786647)

* Nos casos em que forem selecionadas as opções "Seleciona Filiais **-Sim** e Aglutina **-Não"**

Será gerado um arquivo xml para cada **Filial Selecionada**.

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673887788055)

* Nos casos em que forem selecionadas as opções "Seleciona Filiais **-Sim** e Aglutina **-Por CNPJ"**

Será gerado um arquivo xml para as filiais que tenham o **mesmo CNPJ**.

![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673910841239)

* Nos casos em que forem selecionadas as opções "Seleciona Filiais **-Sim** e Aglutina **-Por CNPJ + IE"**

Será gerado um arquivo xml para as filiais que tenham o **mesmo CNPJ e a mesma IE**.

![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673887791767)

Cada arquivo será gerado com até 50 Notas Fiscais por lote. Caso a quantidade supere esse valor, um novo arquivo de lote será gerado.

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673910849815)
