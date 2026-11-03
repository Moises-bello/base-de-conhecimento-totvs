---
article_id: 32551679139735
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 5e012494aa5b891b8e3014d383c9a133bd59224dcaddecb8a8b7425704f25c85
fetched_at: '2026-06-28T22:40:48.839924+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - Pacote de atualização
  da ECF 2025, leiaute 11
type: support-article
updated_at: '2025-07-14T12:29:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32551679139735-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-da-ECF-2025-leiaute-11
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32551679121303) Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como realizar a atualização da ECF 2025? (leiaute 11)

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Solução****:**Para a entrega da ECF em 2025, o layout 11 referente ano 2024.

Portanto, é imprescindível que atualize o seu ambiente a fim de garantir a geração adequada do documento.

Preparando a base para a atualização  
- Faça uma cópia fria (com os serviços parados) da pasta raiz do Protheus (Ex.: C:\TOTVS 12\) e do Banco de Dados  
- Recomendamos que o processo seja feito inicialmente em ambiente de homologação e que os processos mais importantes para a operação da empresa sejam validados

**1º**Recomendamos efetuar a atualização com as últimas liberações do portal. Para efetuar o procedimento, consulte os passos de atualização em [Atualização básica do Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=271651871) e [Atualização de dicionário do Protheus 12.](https://tdn.totvs.com/pages/releaseview.action?pageId=366649057)

**Links para download:**

[Pacotes LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)  
[Pacotes DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)  
[Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)  
[Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)  
[Dicionário Diferencial e Dicionário Completo](https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125DD/)

Aplicar Procedure responsáveis pela atualização de saldos, para mais detalhes veja [Atualização de Procedures](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)

**2º**As atualizações ECF 2025 estarão disponíveis no pacote de atualização:

* Data prevista a partir do dia 20/06 estará [disponível CTB\_EXPEDICAO\_CONTINUA ( clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777#issues-17)), com isso , para atualizar o modulo contabil é preciso aplicar o 3º passo  .
* Ja está liberado no 4º passo  pacote [acumulado do  TAF\_EXPEDICAO\_CONTINUA (clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=634272553) em nossa central de downloads.

Para a entrega é necessário atualizar os 2 pacotes .

Baixar os artefatos de atualização disponíveis nos pacotes acumulados dos módulos Contabilidade Gerencial e TAF. Estes pacotes contem::

**3º** Pacote ECF Módulo CTB :

12.1.2210:<https://r.totvs.io/p/1196343> ; 12.1.2310:<https://r.totvs.io/p/1196344> ; 12.1.2410:<https://r.totvs.io/p/1196342> ;

* Copiar o arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)
* Copiar os arquivos hlpdfeng.txt, hlpdfpor.txt, hlpdfspa.txt para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)
* **Executar o UPDDISTR**
* Arquivo "Config.ZIP" contendo os modelos de visão gerencial utilizado na entrega ECF (Ex: ECF\_RegL300a.cve). Para mais detalhes clique [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)

**4º**[Pacote Acumulado Módulo TAF (Clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=634272553)

* Copiar o arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)
* Copiar os arquivos hlpdfeng.txt, hlpdfpor.txt, hlpdfspa.txt para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e copia do arquivo novo)
* **Aplicar o pacote " expedicao\_continua\_12\_1\_2xx\_taf\_tttm120\_hp.ptm"**
* **Executar o UPDDISTR**
* [**Revisar - Parâmetros de Integração CTB/TAF**](https://centraldeatendimento.totvs.com/hc/pt/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-)
* **configurar o parâmetro MV\_VAUTCON = deixe o parâmetro EM BRANCO.**
* **para atualizar a autocontida ,acessar sistema para carregar as Autocontidas " Taf atualizações/ Config. TAF / Wizard Configuração" , para que o sistema crie corretamente as tabela TAFST1 e TAFST2**

**Importante: Você deve rodar o UPDDISTR do Diferencial (SDFBRA.TXT) tanto do SIGACTB quanto do TAF, e descompactá-los na pasta Systemload, um de cada vez, para que seja substituído e rodado o UPDDISTR corretamente.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32551691871127)Modificações

* **[Modificações Leiaute 11 na Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=918398193)**
* **[Modificações Leiaute 11 no TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=933145345)**

**Saiba Mais**

* [Para maiores detalhes sobre o processo de atualização e correções de erros/advertências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pr%C3%A9-requisitos-para-gera%C3%A7%C3%A3o-da-ECF)
* [ECF PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)
* [COMO GERAR O ARQUIVO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005051922-MP-SIGACTB-ECF-COMO-GERAR-O-ARQUIVO-NO-TAF?source=search)
* [Pagina Centralizadora ECD (Documentações e Atualizações centralizadas)](https://tdn.totvs.com/display/public/PROT/ECD)
* [ECF em vídeo (Principais processos e configurações para a entrega)](https://tdn.totvs.com/display/public/PROT/ECF#Controladoria-4)
* [Como preencher os dados da escrituração](http://tdn.totvs.com/display/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF)
* <https://tdn.totvs.com/display/public/PROT/ECF>
