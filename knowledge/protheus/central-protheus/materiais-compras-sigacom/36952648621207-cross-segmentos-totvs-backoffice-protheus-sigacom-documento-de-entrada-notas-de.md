---
article_id: 36952648621207
category: Materiais - Compras (SIGACOM)
content_hash: c93df29b507dfc9e20f34c7beb6f24108830e5d41f80554251d3d932dac14941
fetched_at: '2026-06-28T22:41:17.352601+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de Entrada
  - Notas de Débito e Crédito - Reforma Tributária
type: support-article
updated_at: '2026-06-26T13:31:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36952648621207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-Entrada-Notas-de-D%C3%A9bito-e-Cr%C3%A9dito-Reforma-Tribut%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36952664785175) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência :**

A NT 2025.002, publicada no contexto da Reforma Tributária, institui as **Notas de Crédito (finNFe = 5)** e **Notas de Débito (finNFe = 6)** na NF-e/NFC-e.

Esses novos tipos de documento têm como finalidade formalizar ajustes tributários referentes aos novos impostos IBS (Imposto sobre Bens e Serviços) e CBS (Contribuição sobre Bens e Serviços), aplicando correções sobre operações fiscais já realizadas.

* + A **Nota de Crédito (finNFe=5)** representa uma **redução** no imposto devido, na ótica do emitente.
  + A **Nota de Débito (finNFe=6)** representa um **acréscimo** no imposto devido, na ótica do emitente.

**Importante:**

-> Essas notas não substituem notas complementares ou de devolução do regime anterior (ICMS/IPI) e são exclusivas para ajustes relacionados ao IBS e à CBS.

-> Incluir e transmitir **Nota de débito com formulário próprio igual a SIM**, não é um processo válido para ser realizado no módulo de Compras, devendo ser incluído e transmitido através do módulo Faturamento.

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) – A partir da versão 12.1.24  
  
  
**Solução:**

1- ) Para efetuar as atualizações e implementações legais sobre a reforma tributária é necessário atualizar o sistema, conforme link abaixo :

[**https://tdn.totvs.com/pages/releaseview.action?pageId=522011099**](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

Além de atualização dos fontes, é necessário também atualizar o dicionário contido no pacote e realizar a execução do UPDDISTR, para que as novas opções e campos dentro do documento de entrada sejam devidamente criados.

Seguem abaixo documentos sobre os processos envolvendo o documento de entrada e o módulo do compras.

[**Notas de Entrada de débito e crédito**](https://tdn.totvs.com/pages/releaseview.action?pageId=1010253803#Reformatribut%C3%A1riaNotadeD%C3%A9bitoeCr%C3%A9dito-exref)

[**Compra Governamental**](https://tdn.totvs.com/pages/releaseview.action?pageId=1010245647)

[**Parecer consultoria de segmentos finalidade notas de debito e credito**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=1039513743)

[**Parecer consultoria de segmentos reforma tributária e Sinief 49/2025**](https://tdn.totvs.com/pages/releaseview.action?pageId=982919844#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosPSCONSEG18561ReformaTribut%C3%A1riaNovasFinalidadesdeEmiss%C3%A3odaNFe-4.Conclus%C3%A3o)

**2-) Implementação do ajuste Sinief 49/2025 conforme itens 3.5 e 3.8, do documento abaixo :**

[**Ajuste Sinief 49/2025 .**](https://tdn.totvs.com/pages/releaseview.action?pageId=982919844#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosPSCONSEG18561ReformaTribut%C3%A1riaNovasFinalidadesdeEmiss%C3%A3odaNFe-4.Conclus%C3%A3o) Bem como a criação do tipo de complemento 6 para as notas de entrada de crédito ( devolução por recusa parcial ), atendendo [**Ajuste Sinief 08/2026**](https://tdn.totvs.com/pages/viewpage.action?pageId=1013620273)

Onde na entrada de uma nota de crédito com o tipo de complemento 3, devolução por recusa ou não localização, será emitida uma única nota de entrada, e com a utilização do TES, configurado para gerar financeiro e alimentar o estoque. Bem como, por se tratar de um processo de recusa, o campo [**F1\_DEVMERC**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029087332-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Recusa-de-Mercadoria-n%C3%A3o-Entregue-Processo-do-m%C3%B3dulo-Compras) será habilitado para preenchimento.

Documento sobre a implementação :

<https://tdn.totvs.com/pages/releaseview.action?pageId=1061180512>

Pacote a ser aplicado :  **( para releases já expirados, necessário verificar se há garantia estendida para utilização do mesmo ).**

**12.1.2310:**[**https://r.totvs.io/p/1250615**](https://r.totvs.io/p/1250615)**;**

**12.1.2410:**[**https://r.totvs.io/p/1250616**](https://r.totvs.io/p/1250616)**;**

**12.1.2510:**[**https://r.totvs.io/p/1250614**](https://r.totvs.io/p/1250614)**;**

**3-) Notas de entrada de débito e crédito, referente a operações de vendas de serviços.**

[**Parecer da consultoria de segmentos/tributária referente a situação.**](https://tdn.totvs.com.br/display/public/ConSeg/NFS-e+Nacional+x+DPS)

**4-) Parecer da consultoria de segmentos/tributária referente ao processo de vendas de serviços, e posterior ajuste do IBS/CBS nas notas de entrada.**

[**https://tdn.totvs.com.br/display/ConSeg/NFS-e+Nacional+x+DPS**](https://tdn.totvs.com.br/display/ConSeg/NFS-e+Nacional+x+DPS)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
