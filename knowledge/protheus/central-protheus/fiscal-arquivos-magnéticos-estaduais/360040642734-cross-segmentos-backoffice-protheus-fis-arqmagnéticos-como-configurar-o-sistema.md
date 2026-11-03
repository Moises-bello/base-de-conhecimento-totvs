---
article_id: 360040642734
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 187a757ad8392675e6a90b1278ca1600c8adda729ecf2d1a14a85b114a598cba
fetched_at: '2026-06-28T22:42:10.296049+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como configurar
  o sistema para transmissão das guias de recolhimento pela rotina GNRE WS?
type: support-article
updated_at: '2024-06-13T18:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040642734-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-configurar-o-sistema-para-transmiss%C3%A3o-das-guias-de-recolhimento-pela-rotina-GNRE-WS
---

**Dúvida**Como configurar o sistema para transmissão das guias de recolhimento pela rotina **GNRE WS (FISA095)**?   
  
**Ambiente**TOTVS Backoffice (Linha Protheus) – Livros Fiscais –  Todas as versões**.**  
  
**Solução**

Para configurar o sistema para transmissão das guias de recolhimento pela rotina **GNRE WS** (**FISA095**) é preciso seguir o processo abaixo:

**1 - Atualização dos fontes e do TSS:**

 - Fontes **FISA095** e **GNREXMLENV**:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-Cross-Segmentos-Backoffice-Protheus-FIS-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-Livros-Fiscais>

- Atualização do **TSS** (RPO , Schemas, URLs e Appserver):

Para realizar a atualização do repositório do **TSS**, faça o download em um dos links abaixo de acordo com sua release:

**RPO:** [MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

**Schemas :** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)

**URLs:** [TSS - Atualização das URLs do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS)

**Binário:**- [MP - TSS - Atualização do Appserver (binário) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062416694-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Appserver-bin%C3%A1rio-do-TSS)

**2 -  Configuração** completa da rotina **FISA095 - GNREWS:**

**GNREWS :**<https://tdn.totvs.com/display/public/PROT/GNREWS+-+Guia+Nacional+de+Recolhimento+de+Tributos+Estaduais+via+Webservice>

**Informações extras :** <https://tdn.totvs.com/pages/releaseview.action?pageId=700503940>

(CSV do ambiente de homologação da GNRE em anexo)

Portal **GNRE** nacional :

Ambiente produção da **GNRE** : <https://www.gnre.pe.gov.br:444/>

Ambiente homologação da **GNRE** : <https://www.testegnre.pe.gov.br:444/gnre/portal/GNRE_Principal.jsp>

**3 - Preenchimento automático** dos campos da guia de recolhimento exigidos pelas UFs/portal GNRE **:**

\* Para preencher os campos da guia de recolhimento de forma automática foi disponibilizado o **Ponto de Entrada MA960GREC** conforme link e pacote abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=607040232>

**4 - Particularidades das UF's de ES e SP:**

As UFs de ES e SP não aderiram ao programa GNRE nacional , porém também conseguimos transmitir as guias para essas UFs pela rotina **FISA095** conforme processos abaixo:

- **GNRE WS** para o estado do **Espirito Santo (DUA ES)**:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/12635308849047-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DUA-ES-Como-transmitir-e-imprimir-as-guias-de-recolhimento-de-Espirito-Santo-ES?source=search>

**- GNRE** para o estado de São Paulo **(DARE SP)**:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/10378843633687-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DARESP-Como-gerar-o-arquivo-XML-e-imprimir-as-guias-de-recolhimento-de-SP-?source=search>
