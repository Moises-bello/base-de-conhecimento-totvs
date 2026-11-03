---
article_id: 7019775569047
category: Financeiro - Novo Gestor Financeiro
content_hash: 1204d41e3f8314534d7780730ae9b6606fcb2f9182af13ea21a42090dfbf2feb
fetched_at: '2026-06-28T22:37:41.367585+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração
  e Funcionalidade do Novo Gestor Financeiro
type: support-article
updated_at: '2026-03-25T12:49:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Configura%C3%A7%C3%A3o-e-Funcionalidade-do-Novo-Gestor-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15366436067991) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Configuração e Funcionalidade do Novo Gestor Financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA710 - A partir da versão 12.1.33  
  
**Solução**  
Na seção GENERAL, deve-se incluir a chave “**App\_Environment”**, cujo valor deve ser o nome do ambiente que os serviços rodarão.   
Na seção **DRIVERS**, deve-se habilitar a porta multiprotocolo na chave **“MultiProtocolPort”** com o valor = 1.  
Por padrão a conexão SSL está ativa na porta multiprotocolo, os detalhes das configurações estão disponíveis na documentação **Application Server** - Porta Multiprotocolo.  
Para desabilitar a conexão por SSL é necessário informar a chave **“MultiProtocolPortSecure = 0”**  
  
[Application Server - Porta Multiprotocolo](https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo)  
  
A configuração do *Job* é realizada de forma automática pelo *Wizard* de configuração**.**

### **Vídeo How To**

**1-** ***) Wizard*** **para configuração de Job e validação do dicionário para utilização do Novo Gestor Financeiro.**  
[Wizard de configuração - FINA711](https://tdn.totvs.com/pages/releaseview.action?pageId=602610545)

**Wizard Novo Gestor Financeiro (FINA711)**

<https://www.youtube.com/watch?v=-lRP79XlSRg&t=27s>

**2-) Como gerar agendamento da Rotina FINA710 (Novo gestor Financeiro)**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Agendamento da Rotina (WIZARD configuração)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410339101591-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Agendamento-da-Rotina-WIZARD-configura%C3%A7%C3%A3o-?source=search)  
   
**3-) Registro online de boletos tem por finalidade automatizar o processo de geração e registro dos boletos gerados pelas empresas, juntos aos bancos, utilizando comunicação com APIs.**  
[Comunicação Bancária via API - FINA710](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=612548392)

**4-) A transmissão de boleto registrado e envio de E-mail ao cliente de forma aglutinada.**  
[JOB Transmissão e Envio de E-mail - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=619130482)  
  
**5-) Cadastro responsável pela manutenção das Espécies do Boleto Registrado.**  
[Cadastro de Espécies do Boleto Registrado - FINA714](https://tdn.totvs.com/pages/releaseview.action?pageId=619130710)

***6-)*** **As movimentações financeiras apresentam todo o fluxo de entrada e saída de títulos.**  
[Movimentações Financeiras - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=622668231)  
  
**7-) É possível personalizar o boleto pela rotina FINA710?**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Personalização de boleto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5716138818327-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Inclus%C3%A3o-de-QRCODE-no-boleto?source=search)

**8-) Como realizar a configuração para apresentação do novo layout de boleto do Novo Painel do Gestor Financeiro** ?  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração do novo layout de boleto do Novo Painel do Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413850994711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Configura%C3%A7%C3%A3o-do-novo-layout-de-boleto-do-Novo-Painel-do-Gestor-Financeiro?source=search)  
  
**9-)** **Painel Gestão apresentando “FINA710REST A Configuração da porta multiprotocolo não está habilitada no ambiente. Verifique a configuração para o uso do Novo Gestor Financeiro”**  
[Cross Segmento - Backoffice linha Protheus - SIGAFIN – FINA710 - Mensagem FINA710REST ao acessar o Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441032963735-Cross-Segmento-Backoffice-linha-Protheus-SIGAFIN-FINA710-Mensagem-FINA710REST-ao-acessar-o-Novo-Gestor-Financeiro-?source=search)  
   
**10-) No módulo Financeiro  ao acesso a rotina FINA710 mensagem** **HELP: FINA710JOB**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - HELP:FINA710JOB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410336871575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-HELP-FINA710JOB?source=search)  
   
**11-) Como buscar as informações do Json após executar o schedule?**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como buscar as informações do Json após executar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451382489495-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-buscar-as-informa%C3%A7%C3%B5es-do-Json-ap%C3%B3s-executar-o-schedule?source=search)

**12-) Ao Finalizar o processo de configuração é apresentado o Help ERRO! Tente novamente.**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - Help ERRO! Tente novamente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5449356330007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Help-ERRO-Tente-novamente?source=search)

**13-) Na rotina Novo Gestor Financeiro é considerado Vencimento ou Vencimento Real?**  
[Cross Segmento Backoffice Linha Protheus SIGAFIN - FINA710 - Na rotina Novo Gestor Financeiro é considerado Vencimento ou Vencimento Real](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410118752791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Na-rotina-Novo-Gestor-Financeiro-%C3%A9-considerado-Vencimento-ou-Vencimento-Real?source=search)

**14-) O Novo Gestor Financeiro está disponível para qual versão?**  
[Cross Segmento Backoffice Linha Protheus SIGAFIN - FINA710 - O Novo Gestor Financeiro está disponível para qual versão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410112400023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-O-Novo-Gestor-Financeiro-est%C3%A1-dispon%C3%ADvel-para-qual-vers%C3%A3o?source=search)

**15-) No módulo Financeiro, ao tentar realizar a configuração do Layout de Banco, o banco não está aparecendo.**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Banco não aparece na configuração de Layout do Boleto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6923644526743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Banco-n%C3%A3o-aparece-na-configura%C3%A7%C3%A3o-de-Layout-do-Boleto?source=search)

**16-) Quais Pontos de Entrada disponíveis na rotina Novo Gestor Financeiro - FINA710 ?**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Ponto de Entrada Novo Painel Gestor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24298133233175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Ponto-de-Entrada-Novo-Painel-Gestor)

**17-) É possível alterar a data base do sistema para trazer informações de determinado dia do Novo Painel Financeiro (FINA710) ?**  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710 - Alteração da data base do novo Painel do Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413641008791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Altera%C3%A7%C3%A3o-da-data-base-do-novo-Painel-do-Gestor-Financeiro?source=search)

**18-) Como gerar arquivos .PEM para utilização no registro de boletos por API do banco Bradesco?**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como gerar arquivos .PEM para utilização no registro de boletos por API do banco Bradesco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6983602488343--Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-gerar-arquivos-PEM-para-utiliza%C3%A7%C3%A3o-no-registro-de-boletos-por-API-do-banco-Bradesco?source=search)

**19-) Não apresenta os valores na coluna de Saldo nos títulos de inclusão no Contas a Receber.**  
[Cross Segmento Backoffice Linha Protheus SIGAFIN - FINA710 - Não apresenta os valores na coluna de Saldo nos títulos de inclusão no Contas a Receber](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410108902167)

**20-) Ao tentar realizar a transmissão de boletos pela FINA710, ocorre a mensagem pelo Monitor de Pendencias:  Erro CPF/CNPJ Beneficiário Inválido!**

[Cross Segmentos - Linha BackOffice Protheus - SIGAFIN - Transmissão Boletos - Erro CPF/CNPJ Beneficiário Inválido!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7114654592279)  
  
**21) Como preparar um título para envio de Boleto Online - API Banco do Brasil (FINA713)?**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Preparar um título para envio de Boleto Online - API Banco do Brasil (FINA713)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7927092298903)  
  
**22) Ao tentar realizar o Download do Boleto na rotina FINA710 - Novo Gestor Financeiro, não sai automaticamente com a extensão .PDF**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Extensão .PDF no Download de Boletos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10505539182743)  
  
23)  Bancos Homologados para pagamentos via API

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Bancos Homologados para pagamentos via API](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24455747356439-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Bancos-Homologados-para-pagamentos-via-API)

### **Eventos**

### [Acompanhe nossos Eventos Totvs Backoffice linha Protheus](https://eventos.totvs.com/webinars/fique-por-dentro-dos-principais-conceitos-e-tratativas-do-novo-gestor-financeiro/)

**Saiba Mais**

[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)
