---
article_id: 24320445523863
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 9d7e02782fe1caf92bfc94c42c20e29984b9b3da8ea43fa1dc79299d1a2089b6
fetched_at: '2026-06-28T22:42:05.009433+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro F700 Deduções Diversas?
type: support-article
updated_at: '2025-01-23T20:37:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24320445523863-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-F700-Dedu%C3%A7%C3%B5es-Diversas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24320445504791) Tempo aproximado para leitura: **00:03:00 min****Dúvida**

Como gerar o registro **F700** - **Deduções Diversas** no **EFD Contribuições**?

**Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão **12.1.25**  
  
**Solução:**

No menu da apuração da **EFD Contribuições (FISA001)** existe a opção **"Deduções Diversas Pis/Cofins"**, que tem objetivo de controlar os valores de Deduções Diversas de **PIS** e **COFINS**, para que sejam considerados para a geração do **registro F700** do **EFD Contribuições**. Os valores de deduções deverão ser informados (se houver) pelo usuário nesta rotina.

No módulo de Livros Fiscais (SIGAFIS), acesse **Miscelânea/Apurações/Apuração EFD Contribuições:**

**![](https://tdn.totvs.com/download/attachments/718438184/DEDUCAO_PIS_COF.gif?version=1&modificationDate=1666374428280&api=v2)**

Detalhamento dos campos disponíveis e informações para preenchimento:

* **Per (MM/AAAA)**: Informar neste campo, o período de processamento onde serão considerados os valores de dedução para o **SPED PIS COFINS**, digitar no formato Mês e Ano.
* **Orig. Dedução**: Indicar neste campo qual a origem da dedução, conforme os seguintes códigos:

- 01=Cred.Presu.Medicamentos – Crédito Presumido Medicamentos

- 02=Cred.Admit.Beb.Fria Créditos Admitidos no Regime Cumulativo – Bebidas Frias

- 03=Contrib.ST.ZFM. - Contribuição Paga pelo Substituto Tributário - ZFM

- 04=ST.Não Ocor.Fato Gerador - Substituição Tributária – Não Ocorrência do Fato Gerador Presumido

- 99=Outras Deduções – Outras Deduções.

* **Ind.Natureza**: Indicador da Natureza da Dedução:

- 0=Dedução de Natureza Não Cumulativa

- 1=Dedução de Natureza Cumulativa

* **Dedução PIS**: Informar neste campo o valor da parcela de dedução referente à PIS.
* **Dedução Cof**: Informar neste campo o valor da parcela de dedução referente à COFINS.
* **Base Cálculo**: Informar neste campo a base de cálculo da operação.
* **CNPJ da PJ**: Informar o CNPJ da Pessoa Jurídica relacionada à operação de Dedução.
* **Inf. Compl**: Informação complementar da operação.

Abaixo link com mais detalhes da rotina:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=718438184>
