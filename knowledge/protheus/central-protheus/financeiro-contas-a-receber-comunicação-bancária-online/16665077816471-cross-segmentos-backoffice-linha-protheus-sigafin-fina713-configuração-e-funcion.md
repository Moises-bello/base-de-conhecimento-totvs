---
article_id: 16665077816471
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 0b4b3f759a0a63797708e6bee5c9769f646eda008d8530459563ca510e801467
fetched_at: '2026-06-28T22:37:49.225336+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Configuração
  e Funcionalidade da transmissão de boletos API
type: support-article
updated_at: '2025-04-07T20:34:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16665077816471-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Configura%C3%A7%C3%A3o-e-Funcionalidade-da-transmiss%C3%A3o-de-boletos-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16665018127127) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Configuração e Funcionalidade da transmissão de boletos API.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713 - A partir da versão 12.1.33  
  
**Solução**Para a utilização da rotina de transmissão de boletos online é necessário que o ambiente esteja configurado a chave de multiprotocolo. Para mais informações acesse a documentação abaixo:

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Configura%C3%A7%C3%A3o-e-Funcionalidade-do-Novo-Gestor-Financeiro)

O **Job FINA713** é responsável pela transmissão dos títulos e envio de boletos por e-mail.

O Job deve ser configurado com o código do "Grupo de Empresa" passando por parâmetro. Exemplo:  Grupo de empresas com o código = 01 **FINA713('01')**

#### **CONFIGURAÇÃO**

No módulo configurado **SIGACFG**acesse o menu **Schedule**>**Schedule.**

Em agendamentos selecione a opção cadastro e adicione o agendamento do job.

No exemplo do Grupo de empresa 01, configure a rotina como **FINA713('01')**para transmissão ou **FINA715('01')**para o retorno.

Configure o módulo como **Financeiro 06** e configure o ambiente e recorrência conforme a necessidade.

![configuração.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16665062780311)

**How to | - SIGAFIN - NGF - Como Config. Envio de Boletos FINA710 | [#TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/hashtag/totvs_backoffice_linha_protheus)**

**Webinar TOTVS|MP-SIGAFIN FINA713 Funcionamento Novo Boleto Online [#TOTVS](https://www.youtube.com/hashtag/totvs) BackOffice Linha Protheus**

**1 - ) Bancos homologados para Transmissão, Certificados e pastas:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Quais os Bancos Homologados para registro online de boletos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8019944849303)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - O que fazer quando o Banco faz o envio dos arquivos CRT e o KEY do Certificado Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12119318485015)

[Cross Segmentos  - Backoffice Linha Protheus - SIGAFIN - FINA713 - Caminho padrão para a gravação dos certificados dos bancos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15671908709911)

**2 - ) Configurações de Layout e principais cadastros:**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Configuração do novo layout de boleto do Novo Painel do Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413850994711)

#### [Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como ajustar a informaçao de clientes no Boleto gerado via API](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16506619056279)

[Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAFIN - FINA713 - Como incluir mais de um e-mail na Carta de Cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14498726442519)

[Parametrização de Carta de Cobrança - FINA810](https://tdn.totvs.com/pages/viewpage.action?pageId=615384255)

[Carta de Cobrança - Financeiro - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=492706741)

**Outras Documentações:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Personalização de boleto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5716138818327)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Extensão .PDF no Download de Boletos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10505539182743)

[Cross Segmentos - Linha BackOffice Protheus - Financeiro - FINA713 - Como transmitir novamente o Borderô via Boleto Online](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10993470739351)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713: Erro 412: arquivo key ou certificado não encontrado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12128505420183)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Boleto sendo impresso sem código de barras e sem linha digitável](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14397141247639)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Erro de comunicação - Problema ao assinar a mensagem com o certificado. Verifique se o certificado utilizado é válido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11983196240279)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como buscar as informações do Json após executar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451382489495)

### Saiba mais

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/viewpage.action?pageId=612548392)

[Comunicação bancária online - FINA710](https://tdn.totvs.com/pages/viewpage.action?pageId=734394374)
