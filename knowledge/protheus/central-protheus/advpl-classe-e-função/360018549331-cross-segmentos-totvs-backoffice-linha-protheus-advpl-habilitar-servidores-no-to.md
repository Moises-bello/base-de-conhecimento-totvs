---
article_id: 360018549331
category: ADVPL - Classe e Função
content_hash: 21cfe14101b6a8ed8bcfd5f2463036d0bfdb0b0604df32c7484f70d66c597d28
fetched_at: '2026-06-28T22:40:19.370068+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Habilitar servidores
  no totvs developer studio
type: support-article
updated_at: '2022-01-10T15:35:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018549331-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Habilitar-servidores-no-totvs-developer-studio
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como habilitar um servidor no IDE (*Integrated Development Environment*) TOTVS Developer Studio?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Pré-requisitos**  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como instalar o totvs developer studio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018541431)  
  
**Solução**

1. Clique com o botão direito do mouse em Servidores, depois selecione Nova Aplicação, conforme imagem abaixo:  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-4%2017%3A38%3A40.png?version=1&modificationDate=1493931553000&api=v2)
2. Selecione o produto, no qual deseja incluir o novo servidor, e clique em avançar:  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2010%3A15%3A2.png?version=1&modificationDate=1493990163000&api=v2)
3. Antes de preencher as informações do novo servidor que será criado, incie o *Application Server* e execute o *SmartClient* (observe que o ambiente no servidor é o TOTVS 12XBRA):  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2010%3A31%3A19.png?version=1&modificationDate=1493991140000&api=v2)
4. Abra também o arquivo appserver.ini para identificar a porta (observe que a porta utilizada é a 4323 da chave TCP):  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2010%3A55%3A2.png?version=1&modificationDate=1493992563000&api=v2)
5. Preencha no campo Nome, a identificação do seu ambiente como preferir, na imagem abaixo utilizamos o nome do ambiente como TOTVS P12XBRA. No campo Endereço utilize o ip desejado ou então, utilize *localhost*. No campo Porta, preencha conforme o appserver.ini. Depois clique em "Detectar/Validar":  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2010%3A18%3A35.png?version=1&modificationDate=1493990376000&api=v2)
6. Depois de detectado, clique em Concluir:  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2010%3A33%3A54.png?version=1&modificationDate=1493991295000&api=v2)
7. Para se conectar com o serviço, clique com o botão direito sobre o servidor desejado e selecione a opção Conectar:  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2010%3A58%3A1.png?version=1&modificationDate=1493992742000&api=v2)
8. Preencher o campo Ambiente com o nome do servidor, seu usuário e senha:  
   ![](http://tdn.totvs.com/download/attachments/273998184/image2017-5-5%2011%3A16%3A47.png?version=1&modificationDate=1493993867000&api=v2)
