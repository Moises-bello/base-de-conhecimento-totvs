---
article_id: 24007459694871
category: Recrutamento e Seleção de Pessoas (SIGARSP)
content_hash: a3a1d8e5a595c14610de097e3fb0ade7068f1791c16c156513c462f473544c0f
fetched_at: '2026-06-28T22:43:00.826034+00:00'
product: protheus
section_id: 206960907
source: central-protheus
title: 'RH - Linha Protheus -  RSP - Como configurar Entradas Automatizadas: Download
  de Currículos, Importação e Configurações'
type: support-article
updated_at: '2024-06-07T11:07:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24007459694871-RH-Linha-Protheus-RSP-Como-configurar-Entradas-Automatizadas-Download-de-Curr%C3%ADculos-Importa%C3%A7%C3%A3o-e-Configura%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24007439194519) Tempo aproximado para leitura: 00:10:00 min  
  
Dúvida**Como configurar Entradas Automatizadas: Download de Currículos, Importação e Configurações?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recrutamento e Seleção de Pessoas - Todas as versões  
  
**Solução**A rotina de Entradas Automatizadas permite ser feito o *Download* de Currículos a partir de um servidor de arquivos (FTP), a Configuração dos campos de mesmo padrão e a Importação de dados dos currículos que utilizará o padrão XML. O próprio sistema fará um relacionamento dos campos do arquivo padrão XML com os campos do arquivo de currículos, onde deverá ser indicado cada campo do XML para os campos destino, no cadastro de currículos do módulo Recrutamento e Seleção de Pessoal.

Em Miscelânea / Entradas Automatizadas / Download de Currículos a rotina realiza o download dos currículos cadastrados disponíveis no servidor, possibilitando baixar os arquivos em formato XML.  
  
**Referente as questões relacionadas ao Download de Currículos, deve ser configurado os parâmetros abaixo:****MV\_RSPFTPD - Identifica o Diretório do servidor FTP que contém os arquivos de currículos (XML) para baixar. Ex: \curriculo\  
MV\_RSPFTPP - Informa a Senha de acesso ao Servidor FTP.   
MV\_RSPFTPS - Identifica o Servidor FTP que contém os arquivos de currículos (XML) para baixar. Ex.: ftp.microsiga.com.br   
MV\_RSPFTPU - Identifica o Usuario para login no Servidor FTP. Ex.: john**![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_9-54-4.png?version=1&modificationDate=1698240185153&api=v2)  
Quando os parâmetros supracitados forem preenchidos no módulo SIGACFG e estiverem corretos, os arquivos disponibilizados pelo servidor FTP ficarão disponíveis para baixar e aparecerão na parte indicada abaixo.  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_9-55-6.png?version=1&modificationDate=1698240184933&api=v2)

Se algum dos parâmetros: **MV\_RSPFTPS, MV\_RSPFTPU, MV\_RSPFTPP** estiver com conteúdo inválido irá mostrar a mensagem "**Falha de conexão ao servidor FTP. Verifique se os parâmetros MV\_RSPFTP... estão configurados corretamente**"  
  
Para o parâmetro: **MV\_RSPFTPD** deve-se atentar ao diretório que será informado, exemplo, caso os arquivos fiquem de um diretório raiz, como “C:\Temp” (Diretório do FTP) deve-se informar apenas o valor “/” no parâmetro. Caso trabalhe com subdiretórios, deve-se informar o diretório que se encontra os arquivos, ou seja, caso o diretório seja “C:\Temp\Teste”, deve ser informa do o valor “/Teste/” **(sem as aspas)** no parâmetro. Caso esse parâmetro seja informado de forma incorreta, o sistema não encontra os arquivos e retorna a mensagem “**Falha de conexão. Verifique se o parâmetro MV\_RSPFTPD esta configurado corretamente.**”.

Os arquivos têm que seguir omodelo de XML abaixo.   
**Observação:** Modelo aqui anexado é um exemplo de configuração. Ficando o cliente responsável pela configuração e formatação conforme sua necessidade.  
  
[![](https://tdn.totvs.com/s/ougqdk/8804/xgjkrn/17.19.9/_/download/resources/com.atlassian.confluence.plugins.confluence-view-file-macro:view-file-macro-resources/images/placeholder-small-code.png)curriculoModelo.xml](https://tdn.totvs.com/download/attachments/799267719/curriculoModelo.xml?version=1&modificationDate=1698242961063&api=v2)  
  
Em Miscelânea / Entradas Automatizadas / Configuração permite a configuração dos campos do XML para a Importação de Currículos, é necessário fazer este processo para que os campos do XML correspondam aos campos do sistema na hora da importação. A Configuração só será possível ser realizada após o download de um currículo em formato XML, pois é através deste arquivo que o processo será feito.  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-13-14.png?version=1&modificationDate=1698240184837&api=v2)  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-13-34.png?version=1&modificationDate=1698240184733&api=v2)  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-13-51.png?version=1&modificationDate=1698240184630&api=v2)  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-14-13.png?version=1&modificationDate=1698240184527&api=v2)  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-15-5.png?version=1&modificationDate=1698240184093&api=v2)  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-14-51.png?version=1&modificationDate=1698240184297&api=v2)  
![](https://tdn.totvs.com/download/attachments/268802103/image2016-11-8%209%3A45%3A38.png?version=1&modificationDate=1478609183000&api=v2)  
  
Após efetuar o Download e a Configuração, em Miscelânea / Entradas Automatizadas / Importação será feita a importação dos dados dos currículos.  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-21-11.png?version=1&modificationDate=1698240183487&api=v2)  
![](https://tdn.totvs.com/download/attachments/799267719/image-2023-10-25_10-21-25.png?version=1&modificationDate=1698240183383&api=v2)

**Saiba Mais****[Artigo Relacionado](https://tdn.totvs.com/pages/releaseview.action?pageId=799267719)  
[Artigos sobre Recrutamento e Seleção de Pessoas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960907-Recrutamento-e-Sele%C3%A7%C3%A3o-de-Pessoas-SIGARSP-)**
