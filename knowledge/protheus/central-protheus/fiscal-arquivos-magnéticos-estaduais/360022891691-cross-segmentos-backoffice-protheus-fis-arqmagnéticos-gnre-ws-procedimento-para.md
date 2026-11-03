---
article_id: 360022891691
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 4f998d74e59650ecffbc51aa3e63fe3e02456e6906d70513ac4137a401292b09
fetched_at: '2026-06-28T22:42:11.728210+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - Procedimento
  para transmissão e impressão de guias
type: support-article
updated_at: '2022-08-17T19:37:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022891691-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-Procedimento-para-transmiss%C3%A3o-e-impress%C3%A3o-de-guias
---

**Dúvida**

Como transmitir e imprimir as guias por meio da **GNRE WS** rotina **FISA095.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão 11.80  
  
**Solução**  
1. Com as Guias já cadastradas na **SF6** - **Guia Nacional de Recolhimento** e com o **TSS** instalado acesse a rotina de Transmissão e Monitoramento da **GNREWS** conforme abaixo:  
No módulo **Livros Fiscais (SIGAFIS)** acesse **Miscelânea / Arq. Magnéticos / GNREWS (FISA095)**;

2. Defina o filtro das **GNRE's** a serem processadas:

 -  **Data Inicial ->** Informe a Data Inicial para Processamento **GNRE** via Web Service;   
 -  **Data Final ->** Informe a Data Final para Processamento **GNRE** via Web Service;   
 -  **Filtro ? ->** Defina o filtro de apresentação das **GNREs**. 1 - Sem filtro / 2 - Transmitidas / 3 - Não Transmitida / 4 - Autorizadas / 5 - Não Autorizadas;          
 -  **Estado ->** Informe o Estado destino do recolhimento.

3. Em Ações Relacionadas selecione a opção desejada:

**Ambiente:**Configure o Ambiente de Transmissão da **GNRE** - Produção ou Homologação  
Obs. O que for configurado neste momento será gravado no parâmetro **MV\_AMBGNRE**  
  
![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A8%3A11.png?version=1&modificationDate=1459537783000&api=v2)![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A14%3A20.png?version=1&modificationDate=1459538152000&api=v2)

**Wiz.Config** : Wizard de Configuração do **TSS**

**Transmissão** : Wizard de transmissão da **GNRE** onde deverá ser informado:

* Número Inicial da **Gnre**
* Número Final da **Gnre**

 ![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A15%3A25.png?version=1&modificationDate=1459538217000&api=v2)![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A15%3A36.png?version=1&modificationDate=1459538228000&api=v2)![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A15%3A43.png?version=1&modificationDate=1459538235000&api=v2)

**Importante**  
Para o Estado do Rio de Janeiro está disponível apenas o Ambiente de Produção;

4. **Monitor** : Monitoramento das **GNRE's** transmitidas.  
  
![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A16%3A7.png?version=1&modificationDate=1459538259000&api=v2)

![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A16%3A16.png?version=1&modificationDate=1459538268000&api=v2)

Ao clicar no Botão Mensagens dentro da rotina de Monitoramento será possível obter maiores detalhes da **GNRE** transmitida;

![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A17%3A28.png?version=1&modificationDate=1459538340000&api=v2)

5. **Impressão**: Nesta rotina é possível imprimir em PDF - Modo Retrato as **GNREs** a serem pagas.   
Obs.  Somente as que tiveram o retorno do Código de Barras no momento da Transmissão que serão impressas.  
  
![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A20%3A56.png?version=1&modificationDate=1459538548000&api=v2)![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A21%3A9.png?version=1&modificationDate=1459538561000&api=v2)

![](http://tdn.totvs.com/download/attachments/235312112/image2016-4-1%2017%3A23%3A23.png?version=1&modificationDate=1459538695000&api=v2)
