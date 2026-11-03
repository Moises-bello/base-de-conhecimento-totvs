---
article_id: 39601316380695
category: Materiais - Compras (SIGACOM)
content_hash: 81a1c33e5fac4f84a015d95f7dfe4c36caaa59fc1d720a3d5e248e2e52b64514
fetched_at: '2026-06-28T22:41:21.837165+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Mensagem "Processo
  IGNORADO. FINALIZADO anteriormente." ao responder formulário da cotação via Workflow
type: support-article
updated_at: '2026-04-08T14:59:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39601316380695-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Mensagem-Processo-IGNORADO-FINALIZADO-anteriormente-ao-responder-formul%C3%A1rio-da-cota%C3%A7%C3%A3o-via-Workflow
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39601316363287) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Ao preencher o formulário da proposta da cotação e clicar em Enviar, é gerada a mensagem de erro Processo IGNORADO. FINALIZADO anteriormente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39601534698263)

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310  
  
**Solução**  
Para corrigir esse erro, efetue os procedimentos abaixo:

**1º passo:**Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112215) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168420)  
- Smartclient - [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112221)  
- Smartclient WebApp - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)  
- DBAccess - [MP - FRAME - Atualização do DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033789713-MP-FRAME-Atualiza%C3%A7%C3%A3o-do-DBAccess?source=search)

Obs: Recomendamos backup e validação primeiramente em ambiente teste.

**2º passo:** Verifique como estão preenchidos os parâmetros MV\_WFDIR e MV\_WFDHTTP

Nesses parâmetros devem ser informados o Diretório de trabalho do Workflow - o local (pasta) onde os arquivos físicos do wizard serão gravados no servidor. Por exemplo, se os arquivos serão gravados na estrutura Protheus\_Data\workflow, informe \workflow nesses parâmetros. Segue abaixo print da sugestão de preenchimento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39601325598231)

A pasta Workflow deve conter a pasta *Messenger* e os arquivos HTML do Novo Fluxo de Compras, conforme mostrado no print abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39601316364951)

**3º passo:** Caso os parâmetros do passo anterior não estejam preenchidos corretamente, execute novamente o WIZARD do WORKFLOW do Novo Fluxo de Compras seguindo a documentação abaixo,

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow através do Wizard no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25128258571287-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-atrav%C3%A9s-do-Wizard-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

Se as configurações estiverem corretas e o erro continuar, será necessária uma análise por parte do Suporte. Abra um ticket com a equipe de Suporte Compras e, para agilizar o atendimento, é essencial anexar as seguintes informações:

* Arquivo de **Inspetor de Objetos**.
* Print do conteúdo dos parâmetros de configuração de e-mail   
  ('MV\_WFDIR', 'MV\_WFDHTTP', 'MV\_WFBRWSR', 'MV\_PGCWF', 'MV\_PGCPISV', 'MV\_PGCPIPO', 'MV\_PGCSMSR', 'MV\_PGCSMPO', 'MV\_PGCTAUT','MV\_WFSNDAU','MV\_WFMLBOX')
* Por gentileza, peço que adicione as chaves abaixo **no appserver.ini do serviço protheus e do WORKFLOW:**  
  [General]  
  rest\_log\_level=4  
     
  [Sessão Ambiente]  
  tracestack=1  
  FWTRACELOG=1  
  FWLOGMSG\_DEBUG=1  
    
  Limpe o console.log do appserver.ini > Gere o erro novamente no NFC > Separe o novo console.log e nos encaminhe para analise!

***Saiba Mais:***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow através do Wizard no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25128258571287-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-atrav%C3%A9s-do-Wizard-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o WorkFlow no Novo Fluxo de Compras - NFC (PGCA010)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-WorkFlow-no-Novo-Fluxo-de-Compras-NFC-PGCA010)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
