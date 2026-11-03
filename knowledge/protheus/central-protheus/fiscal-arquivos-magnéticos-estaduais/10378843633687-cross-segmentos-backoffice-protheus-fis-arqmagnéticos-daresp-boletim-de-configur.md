---
article_id: 10378843633687
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: de2a59ac3eabdd5d111a8909db6cf71227e88d0f60cbc6101e9e07d2c4cc2d64
fetched_at: '2026-06-28T22:42:10.686388+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DARESP -  Boletim
  de configuração para gerar o arquivo XML e imprimir as guias de recolhimento de
  SP
type: support-article
updated_at: '2024-06-14T12:39:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10378843633687-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DARESP-Boletim-de-configura%C3%A7%C3%A3o-para-gerar-o-arquivo-XML-e-imprimir-as-guias-de-recolhimento-de-SP
---

**Dúvida** **DARESP** - Como gerar o arquivo **XML** e imprimir as guias de recolhimento de **SP** ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – Todas as versões.  
**Solução**

**1.** Gere os **arquivos XML** referente as **Guias de recolhimento de SP** pela rotina **FISA095.PRW** conforme manual abaixo:

Boletim **GNREWS**:  
<https://tdn.totvs.com/display/public/PROT/GNREWS+-+Guia+Nacional+de+Recolhimento+de+Tributos+Estaduais+via+Webservice>

Abaixo segue o procedimento para enviar guias da **DARESP** utilizando o *layout* **GNRE** em lote na **versão 2.00**.

* Com as Guias já cadastradas na **SF6** - **Guia Nacional de Recolhimento** acesse a rotina para exportar o **XML** da **GNREWS** conforme abaixo:
* No módulo **Livros Fiscais (SIGAFIS)** acesse **Miscelânea / Arq. Magnéticos / GNREWS (FISA095)**.

**Pergunte Inicial da Rotina GNREWS**

* **Data Inicial ->** Informe a Data Inicial para Processamento **GNRE**.
* **Data Final ->** Informe a Data Final para Processamento **GNRE**.
* **Filtro ? ->** Defina o filtro de apresentação das **GNREs**. 1 - Sem filtro / 2 - Transmitidas / 3 - Não Transmitida / 4 - Autorizadas / 5 - Não Autorizada
* **Estado ->**Para acessar a **DARESP** utilizar o parâmetro "**SP**"
* **Filtro ? ->** Defina o filtro de apresentação das GNREs. 1 - Sem filtro / 2 - Transmitidas / 3 - Não Transmitida / 4 - Autorizadas / 5 - Não Autorizada
* **Tipo GNRE ? ->**Deixar a opção Simples  
    
    
  ![image2022-12-23_16-21-47.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-21-47.png?version=1&modificationDate=1671823307317&api=v2)

Após a confirmação dos parâmetros, aparecerá o *browse* com a relação das guias a serem geradas:

![image2022-12-23_16-23-17.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-23-17.png?version=1&modificationDate=1671823397640&api=v2)

Importante: As guias com **legenda em verde** são as que já foram processadas e para evitar duplicidade de pagamento as mesmas não são processadas caso seja necessário gerar novos arquivos. Caso seja necessário reprocessar uma guia, o usuário terá que entrar no cadastro de "**Guia Nac de Recolhimento**" (**SF6**) e editar o campo **F6\_PROCESS** com o conteúdo igual a "**Não**".

A rotina irá apresentar a mensagem abaixo:

![](https://tdn.totvs.com/download/attachments/700501699/image2022-12-23_17-54-22.png?version=1&modificationDate=1671828862657&api=v2)

As guias com **legenda em azul** são as que estão pendentes de processamento.

Na tela acima temos a opção de "**Exportar XML GNRE**" , na qual irá gerar o arquivo em formato **XML** para importação no site da **SEFAZ-SP**.

![image2022-12-23_16-29-34.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-29-34.png?version=1&modificationDate=1671823775017&api=v2)

Siga os parâmetros conforme imagem abaixo:

![image2022-12-23_16-30-44.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-30-44.png?version=1&modificationDate=1671823845047&api=v2)

![](https://tdn.totvs.com/download/attachments/700501699/image2022-12-23_17-52-45.png?version=1&modificationDate=1671828765610&api=v2)

Após, clique em finalizar o arquivo **XML** estará na pasta selecionada para gravação.

![image2022-12-23_16-32-11.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-32-11.png?version=1&modificationDate=1671823931977&api=v2)

![image2022-12-23_16-35-10.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-35-10.png?version=1&modificationDate=1671824110900&api=v2)

**2.** Gere o **arquivo XML**, basta importar no site da **DARESP**:

 <https://www4.fazenda.sp.gov.br/DareICMS/GnreLote>

![image2022-12-23_16-38-33.png](https://tdn.totvs.com/download/attachments/728648062/image2022-12-23_16-38-33.png?version=1&modificationDate=1671824313177&api=v2)

![](https://tdn.totvs.com/download/attachments/700501699/image2022-12-23_17-48-29.png?version=1&modificationDate=1671828510183&api=v2)

![](https://tdn.totvs.com/download/attachments/700501699/image2022-12-23_17-49-24.png?version=1&modificationDate=1671828564250&api=v2)

![](https://tdn.totvs.com/download/attachments/700501699/image2022-12-23_17-50-8.png?version=1&modificationDate=1671828608847&api=v2)
