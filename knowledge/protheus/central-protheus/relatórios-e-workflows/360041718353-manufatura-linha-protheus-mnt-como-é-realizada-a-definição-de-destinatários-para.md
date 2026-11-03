---
article_id: 360041718353
category: Relatórios e Workflows
content_hash: 24e61e0a6584d7ad4add95dcbc5ff90e2822e9f6d8a7b3c7894809ee490781ae
fetched_at: '2026-06-28T22:42:31.625951+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Como é realizada a definição de destinatários
  para workflows
type: support-article
updated_at: '2026-06-10T15:20:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041718353-Manufatura-Linha-Protheus-MNT-Como-%C3%A9-realizada-a-defini%C3%A7%C3%A3o-de-destinat%C3%A1rios-para-workflows
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18613655194903)*** Tempo aproximado para leitura: **00:04:45 min**  
  
**Dúvida**  
Como é realizada a definição de destinatários para *workflows*?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios de Workflows - Versão 12  
  
**Solução**  
No módulo **Manutenção de Ativos - SIGAMNT**há algumas formas de definir os destinatários de um *workflow*, visto que, cada *workflow* possui sua peculiaridade, assim, várias tabelas podem ser consultadas com intuito de localizar os destinatários de um *workflow*. A rotina **MNTA855 -** **Cadastro de Filiais** possibilita de forma complementar, a definição de destinatários para determinados *workflows*.  
  
A seguir, estão listados todos os *workflows* disponíveis no módulo **Manutenção de Ativos - SIGAMNT** juntamente com os respectivos locais onde o Sistema busca os destinatários para o envio dos mesmos:

* **MNTW005 - Alerta de tendência de falhas de bens**  
  - **Cadastro de Filiais - MNTA855**
* **MNTW010 - Alerta de O.S. - Ordem de serviço atrasada**  
  - **Cadastro de Filiais**
* **MNTW020 - Alerta de O.S. preventiva a vencer com base no campo de tolerância da manutenção**  
  - **Cadastro de Filiais**  
  - **Grupo de Contas E-mail - MNTA225**
* **MNTW025 - Aviso de inclusão de S.S. para o responsável pelo serviço**  
  - **Cadastro de Filiais**  
  - *E-mail* do usuário do Sistema vinculado ao campo **Supervisor** do **Tipo de serviço** da **S.S. - Solicitação de Serviço**, cadastrado na rotina **Tipo de Serviços - MNTA285**  
  - *E-mail*do usuário do Sistema vinculado ao campo **TQB\_CDSOLI - Solicitante da S.S.**
* **MNTW030 - Resumo da S.S. para o executante**  
  - **Cadastro de Filiais**  
  - campo **ST1\_EMAIL - E-mail do funcionário**, vinculado ao campo **TQB\_CDEXEC - Executante da S.S.**  
  - **MV\_RELACNT - Conta a ser utilizada no envio de E-Mail para os relatórios**
* **MNTW035 - Aviso de encerramento da S.S. / Pesquisa de satisfação**  
  - **Cadastro de Filiais**  
  - *E-mail*do usuário do Sistema vinculado ao campo **TQB\_CDSOLI**
* **MNTW040 - Aviso de inclusão de S.S. para o executante**  
  - **Cadastro de Filiais**  
  - *E-mail*do usuário do Sistema vinculado ao responsável pelo tipo de serviço da **S.S.**  
  - *E-mail*do usuário do Sistema vinculado ao campo **TQB\_CDSOLI**  
  - *E-mail*vinculado ao executante da **S.S.** campo **TQ4\_EMAIL1 - E-mail executante S.S.**
* **MNTW045 - Aviso de exclusão de S.S. para o solicitante**  
  - **Cadastro de Filiais**  
  - *E-mail*do usuário do Sistema vinculado ao campo **TQB\_CDSOLI**
* **MNTW055 - Aviso de inclusão de sinistro**  
  - **Cadastro de Filiais**  
  - *E-mail*dos responsáveis por sinistros, parâmetro **MV\_NGRESIN - Emails dos responsáveis por Sinistro**  
  - Conta de *e-mail*do usuário no servidor de *e-mail*, parâmetro **MV\_RELACNT**
* **MNTW060 - Aviso de inclusão de multa**  
  - **Cadastro de Filiais**  
  - Ponto de Entrada [MNTW0601](https://tdn.totvs.com/pages/viewpage.action?pageId=191467066).  
  - *E-mail*dos responsáveis por multas, parâmetro **MV\_NGRESMU - Emails dos responsáveis por Multas**  
  - *E-mail*vinculado ao *leasing* do veículo, campo **TSJ\_EMAIL - E-mail do responsável**
* **MNTW061 - Aviso de inclusão de notificação**  
  - **Cadastro de Filiais**  
  - Ponto de entrada [MNTW0611](https://tdn.totvs.com/display/PROT/DT_PE_MNTW0611_Altera_o_Destinatario_de_email_Notificacao)  
  - *E-mail*dos responsáveis por multas, parâmetro **MV\_NGRESMU**  
  - *E-mail*vinculado ao *leasing* do veículo, campo **TSJ\_EMAIL**
* **MNTW065 - Aviso de geração de advertência de multa**  
  - **Cadastro de Filiais**  
  - *E-mail*dos responsáveis por multas, parâmetro **MV\_NGRESMU**
* **MNTW070 - Apropriação de débito de sinistro**  
  - **Cadastro de Filiais**  
  - *E-mail*dos responsáveis por sinistros, parâmetro **MV\_NGRESIN**  
  - Conta de *e-mail*do usuário no servidor de *e-mail*, parâmetro **MV\_RELACNT**
* **MNTW075 - Aviso de vencimento de taxa**  
  - **Cadastro de Filiais**  
  - Conta de *e-mail* do usuário no servidor de *e-mail*. parâmetro **MV\_RELACNT**
* **MNTW200 - Documentos vencidos/a vencer**  
  - **Cadastro de Filiais**  
  - Conta de *e-mail*do usuário no servidor de *e-mail*, parâmetro **MV\_RELACNT**
* **MNTW205 - Multas vencidas/a vencer**  
  - **Cadastro de Filiais**  
  - *E-mail*dos responsáveis por multas, parâmetro **MV\_NGRESMU**
* **MNTW210 - Garantias vencidas/ a vencer**  
  - **Cadastro de Filiais**  
  - Conta de *e-mail* do usuário no servidor de *e-mail*, parâmetro **MV\_RELACNT**
* **MNTW215 - Liberação de O.S.**  
  - **Cadastro de Filiais**
* **MNW29501 - Inclusão de O.S. vinculada a S.S.**  
  - *E-mail* do usuário do Sistema vinculado ao campo **TQB\_CDSOLI**  
  - Conta de *e-mail* do usuário no servidor de *e-mail*, parâmetro **MV\_RELACNT**
* **MNW29502 - Fechamento de O.S. vinculada a S.S.**  
  - *E-mail* do usuário do Sistema vinculado ao campo **TQB\_CDSOLI**  
  - Conta de *e-mail* do usuário no servidor de *e-mail*, parâmetro **MV\_RELACNT**

**Saiba mais**  
Para informações complementares, verifique os artigos:  
[Configuração do ambiente para recebimento de respostas para Pesquisa de Satisfação da Solicitações de Serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039943893)  
[Configuração Workflow](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026260491)
