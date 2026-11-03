---
article_id: 360020286552
category: Gestão de Transportes (TMS)
content_hash: d1a3e7a5a7c89a0ecb9f57061883fb2260851bc7873614fc8d7fcb874c82141c
fetched_at: '2026-06-28T22:45:27.280227+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Averbação Eletrônica AT&M
type: support-article
updated_at: '2026-06-19T13:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020286552-Log%C3%ADstica-Linha-Protheus-TMS-Averba%C3%A7%C3%A3o-Eletr%C3%B4nica-AT-M
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23717692035095)*** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Como fazer a integração com a **AT&M** para permitir realizar a **averbação eletrônica**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Essa integração vai permitir que seja efetuada a averbação eletrônica de **CT-e - Conhecimento de Transporte eletrônico** e **NFS-e - Nota Fiscal de Serviço eletrônica.**  
  
No **Cadastro de Fornecedores - MATA020**, cadastre a seguradora que será informada no parâmetro **MV\_FORSEG**. E na aba **TMS**, deve ser preenchido o número da apólice no campo **Num.Apolice - A2\_APOLICE.**

* Caso algum cliente seja responsável pelo seguro, deve ser cadastrada também a seguradora utilizada pelo cliente.  
  Para tal, em **Atualizações**/**Seguro**/**Averbação Cliente**, devem ser informados os clientes que são responsáveis pelo seguro. Devem ser preenchidos a **seguradora**, **número da apólice** e o campo **Averb. Elet.** O campo**Averb. Elet.** indica se o registro deve ser considerado para fins de **Averbação Eletrônica.** Caso esteja marcado como **1-Sim** ou não esteja preenchido, a averbação do conhecimento será realizada via seguradora do cliente. Caso esteja marcado como **2-Não**, será realizada via seguradora da transportadora - **MV\_FORSEG**.
* Em **Atualizações**/**Seguro**/**Seguradoras** - **TMSA295**- **Menu novo**, deve ser cadastrada a seguradora utilizada pela transportadora, bem como as seguradoras dos clientes que são responsáveis pela geração do seguro.  
  Também devem ser informados os tipos de documentos a serem averbados. Para tal, na inclusão ou alteração da seguradora, selecione **Outras Ações**/ **Docs. Averbados** e marque os tipos de documentos.   
  Para realizar a averbação é necessário o **XML - Extensible Markup Language** do **CT-e** aprovado pela **SEFAZ - Secretaria de Estado da Fazenda**. Portanto, mesmo que o tipo do documento esteja marcado para averbação, ele só será averbado caso exista um **CT-e** válido.  
  Devem ser preenchidos os dados para integração com a **AT&M** - *login,* senha, código da empresa e endereço **SOAP - Protocolo Simples de Acesso a Objetos**.  
  Para testes em ambiente de homologação, deve ser informado o endereço **SOAP** do ambiente de testes da **AT&M**.

Os **CT-es** e **NFS - Nota Fiscal de Serviços Eletrônica** aprovadas anteriormente não serão averbados.

* Gerar conhecimento e transmitir para a **SEFAZ**. No momento da aprovação do **CT-e**, o Sistema irá gravar um registro na tabela **DL5**, com o *status* = **0-Aguardando averbação**.
* Caso seja aprovado um cancelamento de **CT-e**, o Sistema irá alterar o *status* do **CT-e** na tabela **DL5** para **4-Aguardando cancelamento** caso o conhecimento já tenha sido averbado anteriormente ou **8-Cancelamento realizado antes da averbação** caso o **CT-e** ainda não esteja averbado.
* Caso estornado o cálculo do frete para **Notas Fiscais de serviço**, o Sistema irá alterar o *status* do **CT-e** na tabela **DL5** para  **8-Cancelamento realizado antes da averbação.**
* Para averbação via agendamento automático, no módulo **SIGACFG**/**Ambiente**/**Schedule**/**Schedule**, cadastrar um agendamento para a rotina **TMSAVBE - Averbação Eletrônica**, definindo a frequência de tempo que a averbação eletrônica deve ser executada. É necessário cadastrar o agendamento apenas para uma Filial, os documentos de todas as filiais serão averbados na execução do agendamento, independente da filial configurada.
* Após a execução da s*chedule* ou averbação via **TMSA296 - Monitor Averbação**, conferir se os conhecimentos foram averbados.
* O campo ***Status*** **da Averbação** - **DL5\_STATUS**, indica a situação atual da averbação: **0=Aguardando Averbação**, **1=Falha de comunicação com o WebService**,**2=Averbado**,**3=Recusado**, **4=Aguardando Cancelamento da averbação**, **5=Falha de comunicação do cancelamento da averbação**,**6=Averbação cancelada**, **7=Cancelamento da averbação recusado**,**8=Documento cancelado antes da averbação**.
* O campo **Mensagem de Erro - DL5\_MSERRO** armazena o código e mensagem de erro, caso a **AT&M** recuse o **CT-e**.
* Para identificar se o conhecimento foi averbado tendo o cliente como responsável pelo seguro, verificar se o campo **Tipo de Movimento da Averbação** - **DL5\_TPMOV** está com o valor **4**. **1=Normal, 2=Cancelado, 3=Cortesia, 4=Resp. de Terceiros, 5=CTe** **complementar**.
* Caso o **status** dos conhecimentos não mudem após a execução da s*chedule* ou averbação via **Monitor Averbação - TMSA296**, verificar no **console.log** se está ocorrendo alguma inconsistência quando o Sistema tenta se conectar com o **WebService** da **AT&M**.
* Acessar a rotina de **Manifesto** - **TMSA190** e acionar a tecla **F12** para configurar como devem ser tratados os conhecimentos sem averbação na geração do manifesto:
  + **Apenas avisar.**
  + **Bloquear emissão do Manifesto.**
  + **Nenhuma ação.**
* Gerar o manifesto e transmitir para a **SEFAZ**.
* Abrir o **XML** do manifesto para conferir as informações referente ao seguro de carga.

Se o conhecimento foi averbado com sucesso, os dados enviados pela **AT&M** serão exportados no **MDF-e - Seguradora,** **Apólice** e **Número da Averbação**.

* Caso tenha ocorrido alguma inconsistência na averbação ou o conhecimento ainda não tenha sido averbado, será exportado o número de apólice vinculado a seguradora e o número de averbação 99999, conforme previsto na **nota técnica 2017/002** do **MDF-e – Manifesto Eletrônico de Documentos Fiscais.**
* Caso o conhecimento não exista na tabela **DL5** - **Averbação Eletrônica**, o seguro será tratado como anteriormente.

**Monitor de averbação MDF-e**  
A rotina **Monitor Averbação** **MDF-e -** **TMSAE74,** permite visualizar e transmitir os eventos do **MDF-e** via **AT&M**.  
  
**Importante**  
**Não existe parâmetro para iniciar a averbação eletrônica.** A chave para iniciar a averbação é cadastrar a seguradora informada no parâmetro**MV\_FORSEG**no cadastro de seguradoras. Assim que a seguradora estiver cadastrada, todos os novos **CT-es** aprovados pela **SEFAZ** serão gravados na tabela **DL5 - Averbação eletrônica** com o *status* **Aguardando averbação.** No caso de averbação de **NFS-e**, os registros serão gravados na tabela **DL5 - Averbação eletrônica**com o *status***Aguardando averbação**após o cálculo do frete, mas a transmissão da averbação de **NFS-e** depende da autorização na prefeitura, considerando o preenchimento do campo **F3\_NFELETR.**  
  
**Saiba mais**  
[DT Averbação Eletrônica AT&M](https://tdn.totvs.com/pages/viewpage.action?pageId=312155060)  
[Monitor de Averbação MDF-e (TMSAE74 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=461911898)   
[HOW TO SIGATMS AVERBAÇÃO](https://www.youtube.com/playlist?list=PLc53uWgxEXo_EN97KWzT8yMqGXcdifnUD)  
[Ponto de Entrada TMAVBGRV](https://tdn.totvs.com/display/public/PROT/Ponto_de_Entrada_TMAVBGRV)
