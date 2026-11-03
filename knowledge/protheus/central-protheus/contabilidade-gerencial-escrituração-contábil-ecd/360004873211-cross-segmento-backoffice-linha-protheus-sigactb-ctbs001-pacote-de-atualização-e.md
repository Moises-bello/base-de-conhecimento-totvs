---
article_id: 360004873211
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 51d01a397ba41e2969c5a1427804304f1beddb9f03940c57efc4bf3a1e4a3932
fetched_at: '2026-06-28T22:40:44.409603+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - Pacote de atualização
  e como realizar a atualização da ECF 2022, leiaute 8
type: support-article
updated_at: '2023-06-09T20:27:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECF-2022-leiaute-8
---

**Duvida:**

Pacote de atualização e como realizar a atualização da ECF 2022, leiaute 8?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução:**

Para deixar seu ambiente atualizado para entrega do ECF, realize os seguintes passos:

**Passo 1** - Recomendamos efetuar a atualização com as últimas liberações do portal. Para efetuar o procedimento, consulte os passos de atualização em [Atualização básica do Protheus 12](http://tdn.totvs.com/pages/viewpage.action?pageId=271651871) e [Procedimento para efetuar a atualização básica do Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=366649057)

* para atualização do **módulo TAF (utilizado apenas para a entrega ECF)** seguir os passos a seguir:[Atualização TAF Completo](https://tdn.totvs.com/pages/releaseview.action?pageId=374311673) e [Parâmetros de Integração CTB/TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-?source=search)

**Acesse aqui as ultimas expedições Pacote ECF**

* **Acesse aqui as ultimas expedições Pacote ECF:**

  **[Pacote Acumulado Contabilidade + Dicionário + Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**

**Acesse aqui as ultimas expedições Pacote TAF**

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1097863> ;

12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1097864> ;

12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1097865> ;

**[Pacote Acumulado Contabilidade + Dicionário + Procedure](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**

* Aplicar Procedure  responsáveis pela atualização de saldos (Ex: p12\_01.sps) Para mais detalhes veja [Atualização de Procedures](https://tdn.totvs.com/display/PROT/Stored+Procedures)
* Realizar a execução do UPDDISTR em seu ambiente

Links para download:

* [Pacote Acumulado Módulo Contabil](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/CTB_EXPEDICAO_CONTINUA)idade Gerencial
* [Pacote Acumulado Módulo TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=374311673)
* [Pacote LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)
* [Pacote DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)
* [Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)
* [Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)
* [Dicionário Diferencial e Dicionário Completo](https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125DD/)

**Obs. Caso não encontre no portal do cliente ou o sistema apresente algum erro ao aplica-los necessário abertura de um ticket junto ao time de Framework**

Importante:

Você deve baixar tanto o arquivo de dicionário completo (SXSBRA.TXT, por exemplo) quanto o dicionário diferencial (SDFBRA.TXT, por exemplo), e descompactá-los na pasta Systemload. Embora a atualização de release utilize apenas o arquivo diferencial, o arquivo completo também deve ser baixado para a pasta, pois futuramente, quando for criar uma nova empresa ou filial, por exemplo, o arquivo que será utilizado será o COMPLETO.

**Passo 2** - Baixar os artefatos de atualização disponíveis ná pagina [Pacotes de Atualização](https://tdn.totvs.com/pages/viewpage.action?pageId=544733422). Este pacote  contem:

* Patch para atualização das rotinas envolvidas na entrega ECD/ECF
* Arquivo "Contents.txt" contendo o detalhe dos fontes envolvidos neste pacote
* Arquivo "Config.ZIP" contendo os layouts atualizados para a criação do arquivo texto. (Ex: ecdlivro\_g.xml). Para mais detalhes veja  [Pasta do Layout para criação do arquivo texto](https://tdn.totvs.com/pages/releaseview.action?pageId=536725577)
* Arquivo "Config.ZIP" contendo os modelos de visão gerencial utilizado na entrega ECF (Ex: ECF\_RegL300a.cve). Para mais detalhes clique [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)
* Arquivo "Config.ZIP" contendo os arquivos base  para atualização das procedures  responsáveis pela atualização de saldos (Ex: p12\_01.sps)

**Passo 3** - Copiar o arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)

**Passo 4** - Copiar os arquivos *hlpdfeng.txt, hlpdfpor.txt, hlpdfspa.txt* para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)

**Passo 5** – Aplicar  pacote referente as entregas ECD/ECF 2022 em seu ambiente.

**Passo 6** - Excluir os arquivos de log abaixo:

Dentro da pasta system:

* mpupdlog.log
* mpupdlog.fpt
* mpwizard.hlp
* mpwizardhlp.lck

Dentro da pasta Appserver:

* mpupddistri.tsk

**Passo 7** - Realizar a execução do UPDDISTR em seu ambiente: [Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=366649057)

                Caso deseje executar uma única vez o UPDDISTR do TAF e ECD/ECF utilize: [Atualizador de dicionário UPDBATCH](https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=635982000)

**Passo 8** - Atualizar os arquivos bases responsáveis pela criação do arquivo texto do ECD.  Para mais detalhes veja [Pasta do Layout para criação do arquivo texto](https://tdn.totvs.com/pages/releaseview.action?pageId=536725577)

**Passo 9** - Atualizar as procedures responsáveis pela atualização de saldos contábeis. Para mais detalhes veja [Atualização de Procedures](https://tdn.totvs.com/display/PROT/Stored+Procedures)

**Passo 10** - Os passos anteriores referem-se a atualização do **Protheus módulo Contábil**, para atualização do **módulo TAF (utilizado apenas para a entrega ECF)** seguir os passos a seguir: [Atualização TAF Completo](https://tdn.totvs.com/pages/viewpage.action?pageId=374311673) e [Parâmetros de Integração CTB/TAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-?source=search)

O link acima contem orientação para download do pacote de atualização e procedimentos de atualização do sistema

## A não atualização do ambiente conforme procedimentos descritos acarretará em erros na execução do processo.

**Saiba Mais**

* [Relatório de Checklist para geração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008351187-MP-SIGACTB-ECD-ECF-Relat%C3%B3rio-de-Checklist-para-gera%C3%A7%C3%A3o?source=search) **[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008351187-MP-SIGACTB-ECD-ECF-Relat%C3%B3rio-de-Checklist-para-gera%C3%A7%C3%A3o?source=search)**e venha como utilizar e qual sua finalidade
* Para maiores detalhes sobre o processo de atualização e correções de erros/advertências consulte [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-)
* [ECF PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)
* [COMO GERAR O ARQUIVO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005051922-MP-SIGACTB-ECF-COMO-GERAR-O-ARQUIVO-NO-TAF?source=search)
* Pagina Centralizadora ECD (Documentações e Atualizações centralizadas): [Clique Aqui](http://tdn.totvs.com/display/PROT/ECD)
* KCS Contabilidade (principais dúvidas documentadas): [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001492708-Contabilidade-Gerencial)
* ECF em vídeo (Principais processos e configurações para a entrega)[Clique aqui](https://tdn.totvs.com/display/public/PROT/ECF#Controladoria-4)
* Realizar a escrituração do ECF conforme o link: [Como preencher os dados da escrituração](http://tdn.totvs.com/display/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF)
* Página Centralizadora: <http://tdn.totvs.com/display/PROT/ECF>
