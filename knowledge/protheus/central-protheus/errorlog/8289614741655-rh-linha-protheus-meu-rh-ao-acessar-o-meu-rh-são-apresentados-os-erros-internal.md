---
article_id: 8289614741655
category: ERRORLOG
content_hash: e39513933e84405284e188c952789198396449ef1036ec195a737a84eebed91b
fetched_at: '2026-06-28T22:44:39.470000+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Ao acessar o MEU RH são apresentados os erros
  "Internal Server Error" e "object Object"
type: support-article
updated_at: '2026-06-18T18:14:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8289614741655-RH-Linha-Protheus-MEU-RH-Ao-acessar-o-MEU-RH-s%C3%A3o-apresentados-os-erros-Internal-Server-Error-e-object-Object
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27597178109975) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao acessar o MEU RH são apresentados os erros ***"Internal Server Error" e "object Object"***  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8289614047767)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Ao acessar o MEU RH são apresentadas as mensagens de erro "*Internal Server Error" e "object Object*". Geralmente estes erros estão relacionados com alguma **configuração incorreta no appserver.ini do MEU RH.**  
  
**O App Meu RH é um serviço em Tecnologia REST,** quando é disparado um erro *"Object Object",* haverá falhas no REST em si, sendo assim será necessário realizar a depuração e análise de qual API teve resposta com erro ou não subiu no serviço.  
  
Para entender sobre, o processo de depuração do browser e como coletar as evidências, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4461070844567).  
  
Da mesma forma, quando no App Meu RH, surge um "*INTERNAL SERVER ERROR*", será gerado o ***THREAD ERROR* no *console.log* do serviço *WS REST*.**Para coletar o console.log, siga as instruções do artigo, [clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035487834).  
  
Com estes dois arquivos, conseguirão analisar juntamente à área do TI interno da Empresa, ou então, poderão solicitar o Suporte em um ticket aberto junto à TOTVS, para que nossos analistas analisem as evidências, e forneçam o retorno mais assertivos às inconsistências geradas.  
 **Saiba Mais  
[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514)  
[RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
