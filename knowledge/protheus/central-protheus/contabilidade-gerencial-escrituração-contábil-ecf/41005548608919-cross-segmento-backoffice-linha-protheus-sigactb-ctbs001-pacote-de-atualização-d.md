---
article_id: 41005548608919
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 8bb0491f01e4cafe7d56c350d19e23e7954cb49d7de4be52a28793233f8482df
fetched_at: '2026-06-28T22:40:48.849936+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 - Pacote de atualização
  da ECF 2026, leiaute 12
type: support-article
updated_at: '2026-06-22T17:53:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41005548608919-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-da-ECF-2026-leiaute-12
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41005548593687) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como realizar a atualização da ECF 2026? (leiaute 12)

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Solução:**  
Para a entrega da ECF em 2026, o layout 12 referente ano 2025. É imprescindível que atualize o seu ambiente a fim de garantir a geração adequada do documento.

Passos para atualização:

**1° Preparando a base para a atualização:**

* Faça uma cópia fria (com os serviços parados) da pasta raiz do Protheus (Ex.: C:\TOTVS 12\) e do banco de dados.
* Recomendamos que o processo seja feito inicialmente em ambiente de homologação e que os processos mais importantes para a operação da empresa sejam validados.

**2° Recomendamos efetuar a atualização com as últimas liberações do portal.**

* Para efetuar o procedimento, consulte os passos de atualização em   
  [Atualização básica do Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=271651871)   
  [Atualização de dicionário do Protheus 12.](https://tdn.totvs.com/pages/releaseview.action?pageId=366649057)

* **Link para download:**  
  [**TOTVS S/A - Downloads e Atualizações**](https://suporte.totvs.com/portal/p/10098/download#company/)

**3º As atualizações específicas ECF 2025 estarão disponíveis nos pacotes de atualização:**

* Pacote [CTB\_EXPEDICAO\_CONTINUA](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777#issues-17). Com isso, para atualizar o módulo contábil, é preciso aplicar o 3º passo.
* Pacote [TAF\_EXPEDICAO\_CONTINUA](https://tdn.totvs.com/pages/releaseview.action?pageId=634272553). Com isso, para atualizar o módulo do TAF é preciso aplicar o 4º passo.

  OBS: Para a entrega, é obrigatório a aplicação dos 2 pacotes.

**4° Baixar os artefatos de atualização disponíveis nos pacotes acumulados dos módulos Contabilidade Gerencial e TAF. Estes pacotes contêm:**

* **Pacote ECF Módulo CTB :**  
  [**12.1.2310**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1123867)**-**[**12.1.2410**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1182881)**-**[**12.1.2510**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1223280)

  Copiar o arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e cópia do arquivo novo)

  Copiar os arquivos hlpdfeng.txt, hlpdfpor.txt, hlpdfspa.txt para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e cópia do arquivo novo)

  **Executar o UPDDISTR**

  Arquivo "Config.ZIP" contendo os modelos de visão gerencial utilizados na entrega ECF (Ex: ECF\_RegL300a.cve). Para mais detalhes, clique [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)
* **Pacote Acumulado Módulo TAF:**  
  [**12.1.2310**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1126399)**-**[**12.1.2410**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1174332)**-**[**12.1.2510**](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1228187)

  Copiar o arquivo SDFBRA.TXT para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e cópia do arquivo novo)

  Copiar os arquivos hlpdfeng.txt, hlpdfpor.txt, hlpdfspa.txt para a pasta Systemload (Se existir o arquivo na pasta, proceder com a exclusão do arquivo existente e cópia do arquivo novo)

  **Aplicar o pacote "expedicao\_continua\_12\_1\_2xx\_taf\_tttm120\_hp.ptm"**

  **Executar o UPDDISTR**

  [**Revisar - Parâmetros de Integração CTB/TAF**](https://centraldeatendimento.totvs.com/hc/pt/articles/360006564072-MP-SIGACTB-ECF-Par%C3%A2metros-de-Integra%C3%A7%C3%A3o-CTB-TAF-)

  [**configurar o parâmetro MV\_VAUTCON = deixe o parâmetro EM BRANCO**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017826812-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-atualizar-as-tabelas-autocontidas-no-TAF)**.**

  **para atualizar a autocontida ,acessar sistema para carregar as Autocontidas " Taf atualizações/ Config. TAF / Wizard Configuração" , para que o sistema crie corretamente as tabela TAFST1 e TAFST2**

**Importante: você deve rodar o UPDDISTR do Diferencial (SDFBRA.TXT) tanto do SIGACTB quanto do TAF, e descompactá-los na pasta Systemload, um de cada vez, para que seja substituído e rodado o UPDDISTR corretamente.**

#### **Modificações no layout da ECD**

* [**Modificações Leiaute 12 na Contabilidade**](https://tdn.totvs.com/pages/releaseview.action?pageId=1066108702)
* [**Modificações Leiaute 12 no TAF**](https://tdn.totvs.com/pages/releaseview.action?pageId=1059302421)

**Saiba Mais**  
[Para maiores detalhes sobre o processo de atualização e correções de erros/advertências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pr%C3%A9-requisitos-para-gera%C3%A7%C3%A3o-da-ECF)  
[ECF PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)  
[COMO GERAR O ARQUIVO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005051922-MP-SIGACTB-ECF-COMO-GERAR-O-ARQUIVO-NO-TAF?source=search)  
[ECF em vídeo (Principais processos e configurações para a entrega)](https://tdn.totvs.com/display/public/PROT/ECF#Controladoria-4)  
[Como preencher os dados da escrituração](http://tdn.totvs.com/display/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF)  
[Pagina Cnetralizadora ECF](https://tdn.totvs.com/display/public/PROT/ECF)
