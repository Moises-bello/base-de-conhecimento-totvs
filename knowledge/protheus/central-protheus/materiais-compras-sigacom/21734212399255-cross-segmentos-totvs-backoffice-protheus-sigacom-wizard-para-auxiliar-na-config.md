---
article_id: 21734212399255
category: Materiais - Compras (SIGACOM)
content_hash: 0c8a5a9f220537b99c950d4e656782fadc5da764c48de3ce86f3b1fea8e91779
fetched_at: '2026-06-28T22:41:25.430191+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Wizard para Auxiliar
  na Configuração do Importador XML e Integração com o Totvs Transmite (Novo Modelo).
type: support-article
updated_at: '2026-01-21T18:59:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21734212399255-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Wizard-para-Auxiliar-na-Configura%C3%A7%C3%A3o-do-Importador-XML-e-Integra%C3%A7%C3%A3o-com-o-Totvs-Transmite-Novo-Modelo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21734173147031) Tempo aproximado para leitura: **00:05:00min**  
  
**Dúvida**  
Como Configurar o novo Wizard do Importador XML para integração com TOTVS Transmite?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - A partir da Versão 12  
  
**Solução**

Crie no menu do módulo compras o wizard adicionando a função WIZIMP conforme abaixo:

![d105beae-d862-4dbd-9bfd-d07d432765f8.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22885288884631)

**Sugestão de caminho:** Miscelânea → Importador XML → Wizard

Caso esteja no modelo antigo do Wizard seguir a documentação: [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Wizard para auxiliar na configuração do Importador XML e da integração com o Totvs Transmite (Modelo Antigo).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15777953925655-Cross-Segmentos-Totvs-Backoffice-Protheus-Wizard-para-auxiliar-na-configura%C3%A7%C3%A3o-do-Importador-XML-e-da-integra%C3%A7%C3%A3o-com-o-Totvs-Transmite)

Acesse o menu criado através do modulo compras e siga as orientações abaixo:

* **Parâmetro utilizado no Wizard de configuração do Importador XML**

**MV\_WIZCFG = .T.**

Caso queira configurar apenas o Importador XML, precisa utilizar o parâmetro como **.F.**

**1) Boas Vindas**

Ao acessar o Wizard é apresentado a tela de boas vindas e os primeiros passos da configuração:

* Tipo de configuração: Selecionar o tipo de configuração será executada.
  + Importador XML - Configurar apenas o importador xml;
  + Importador XML x Transmite - Configurar integração do Importador XML x TOTVS Transmite.

* Tipos de documentos importados: Selecionar os tipos de documentos que serão considerados na importação.
  + NFE - Nota Fiscal Eletrônica;
  + NFSE - Nota Fiscal de Serviço Eletrônica;
  + CTE - Conhecimento de Transporte Eletrônico;
  + CTEOS - Conhecimento de Transporte Eletrônico para Outros Serviços.

* Tipo de integração: Selecionar como será processada a geração automática de documentos do Importador XML. 
  + Monitor XML - Somente importado e visualizado no monitor de importação de XML;
  + Pré-Nota - Importado e gerar pré-nota;
  + Documento Classificado - Importado e gerar documento de entrada classificado.

**![](https://tdn.totvs.com/download/attachments/821198053/smartclient_yXMs77akpT.gif?version=1&modificationDate=1706648871777&api=v2)**

* Documentações:

Em todas as etapas de configuração é apresentado a opção de **Documentações**, que é apresentado os links recomendados com orientações do processo.

Segue abaixo a lista de documentos disponíveis:

**Guia de referência - Importador XML:** Toda documentação sobre o Importador XML.

**Integração Importador XML x Totvs Transmite:**Toda documentação sobre a integração entre o Importador XML x Totvs Transmite.

**Expedição Continua - Compras:**Caso tenha divergência de programas ou dicionário, já possui link para baixar as ultimas atualizações do modulo de Compras.

**Expedição Continua - Documentos Eletrônicos:**Caso tenha divergência do programa **ColAutoRead** ,já possui link para baixar as ultimas atualizações.

**Estrutura de pastas:** Informações sobre estrutura(Pastas/Parâmetros) dos arquivos XMLs.

![](https://tdn.totvs.com/download/attachments/821198053/Uhn9spsn0x.gif?version=1&modificationDate=1706648893917&api=v2)

**2) Credenciais**

Na Segunda Etapa são apresentados os Campos de Credenciais para preenchimento com Informações obtidas no TOTVS Transmite.

* Client ID - Client ID do TOTVS Transmite;
* Client SECRET - Client Secret do TOTVS Transmite.

![](https://tdn.totvs.com/download/attachments/821198053/smartclient_O4kk3Feaxm.gif?version=1&modificationDate=1706641636227&api=v2)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22509488053399)

**3) Configurações**

Na Terceira Etapa de Configuração é apresentado a opção **Configurar**, que realiza todas as verificações e configurações necessárias automaticamente para facilitar/agilizar todo o processo.

Tipo de configuração:

* **Importador XML**

![](https://tdn.totvs.com/download/attachments/821198053/PiiW61GR2Q.gif?version=1&modificationDate=1706641798937&api=v2)

No processo de configuração automática as empresas e filiais serão todas configuradas para integração com o TOTVS Transmite.

* Caso seja necessário alterar as configurações realizadas automaticamente existe a opção de configurações avançadas.
* Caminho dos Arquivos XML: Definir o caminho(diretório) de onde os XMLs serão lidos e importados;
* Parâmetros Importador XML: Definir parâmetros utilizados para o importador XML;

![](https://tdn.totvs.com/download/attachments/821198053/smartclient_8FUO8RMSlC.gif?version=1&modificationDate=1706641877603&api=v2)

* **Importador XML x Transmite**

**![](https://tdn.totvs.com/download/attachments/821198053/smartclient_m5vMP9Pd05.gif?version=1&modificationDate=1706044113750&api=v2)**

Caso seja necessário alterar as configurações realizadas automaticamente existe a opção de **configurações avançadas**.

* Caminho dos Arquivos XML: Definir o caminho(diretório) de onde os XMLs serão lidos e importados;
* Parâmetros Importador XML: Definir parâmetros utilizados para o importador XML;
* Parâmetros Integração TOTVS Transmite: Definir parâmetros utilizados para integração com TOTVS Transmite;
* Empresas e Filiais: Definir quais Empresas e Filiais serão Integradas com o TOTVS Transmite.

![](https://tdn.totvs.com/download/attachments/821198053/smartclient_HviMDColjh.gif?version=1&modificationDate=1706044112440&api=v2)

**Saiba Mais:**

Documentação Completa do Novo Wizard: [Wizard Configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=821198053)

[Integração Importador Xml x Totvs Transmite](https://tdn.totvs.com/pages/viewpage.action?pageId=678583195)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
