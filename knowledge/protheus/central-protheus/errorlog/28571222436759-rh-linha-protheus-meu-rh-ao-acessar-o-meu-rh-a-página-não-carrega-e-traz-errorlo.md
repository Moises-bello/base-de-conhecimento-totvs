---
article_id: 28571222436759
category: ERRORLOG
content_hash: 05c888c4e263a1c1bd9e673a3d1d744ec807e44e4d63f7f460584ca03f57160b
fetched_at: '2026-06-28T22:44:39.419850+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - Meu RH - Ao acessar o Meu RH, a página não carrega e
  traz errorlog SX6 not open for GetMV on REST_AUTH:POST(RHNP05.PRW)
type: support-article
updated_at: '2026-06-23T21:11:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28571222436759-RH-Linha-Protheus-Meu-RH-Ao-acessar-o-Meu-RH-a-p%C3%A1gina-n%C3%A3o-carrega-e-traz-errorlog-SX6-not-open-for-GetMV-on-REST-AUTH-POST-RHNP05-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28571222396311) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao acessar o Meu RH, a página não carrega e traz errorlog SX6 not open for GetMV on REST\_AUTH:POST(RHNP05.PRW)  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
No ini do Rest tem a chave PrepareIn que indica qual o grupo de empresa será acionado, exemplo: PrepareIn=01, grupo de empresa 01 será solicitado para fazer a leitura das tabelas do módulo. Se tiver apontando para o grupo errado pode ser uma das causas do erro.  
  
Diante deste *errorlog*, é necessário realizar a atualização da versão do *Appserver* utilizado, pois ele **complementa as funcionalidades disponibilizadas no pacote de** ***LIB***, à nível de arquitetura e também o arquivo de comunicação com a **versão do** ***DBAccess*****, o** ***dbapi.dll.***   
  
O erro indica que o acesso não conseguiu realizar a abertura de nenhum dicionário **SX6 (Parâmetros)** para executar o procedimento, podendo ser um erro à nível de estrutura, em que há a falta da atualização da versão do ***appserver***, dado que as funcionalidades das bibliotecas estão mais atualizadas.  
  
Deste modo, será necessário realizar as atualizações conforme indicado:  
- atualização LIB e appserver:  <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>  
e <https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/>  
- atualização do arquivo dbapi.dll: [TEC - APPSERVER - Instruções para atualização da dbapi](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020264351-TEC-APPSERVER-Instru%C3%A7%C3%B5es-para-atualiza%C3%A7%C3%A3o-da-dbapi)  
  
Exemplo do *errorlog*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28571222397719)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
