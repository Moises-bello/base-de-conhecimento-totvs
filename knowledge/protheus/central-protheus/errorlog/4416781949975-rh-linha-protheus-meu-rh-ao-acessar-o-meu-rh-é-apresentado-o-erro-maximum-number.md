---
article_id: 4416781949975
category: ERRORLOG
content_hash: 0c205ec6b4c023fc2f7f29f7eca0ed90304bbe04cb1cef5a382be6f9ed7ab0a0
fetched_at: '2026-06-28T22:44:39.487056+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Ao acessar o MEU RH é apresentado o erro Maximum
  Number of http Threads exceed 10
type: support-article
updated_at: '2026-06-23T21:29:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416781949975-RH-Linha-Protheus-MEU-RH-Ao-acessar-o-MEU-RH-%C3%A9-apresentado-o-erro-Maximum-Number-of-http-Threads-exceed-10
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24769277136535) Tempo aproximado para leitura: **00:04:00 min****Dúvida**MEU RH - Ao acessar o MEU RH é apresentado o erro Maximum Number of http Threads exceed 10  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Ao acessar o MEU RH é apresentado o erro **Maximum Number of http Threads exceed 10** no *console.log* conforme imagem abaixo: **![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416795281431)**No **appserver.ini** do MEU RH na seção do **[HTTPENV]** recomenda-se aumentar os ***Instances*** conforme artigo abaixo, porém atentar-se com relação ao consumo de licenças.   
  
**Consumo de Licenças e Configuração Apropriada**  
[https://tdn.totvs.com/pages/viewpage.action?pageId=65409813](https://tdn.totvs.com/pages/viewpage.action?pageId=654098131)[1](https://tdn.totvs.com/pages/viewpage.action?pageId=654098131) ***Instances*:**<https://tdn.totvs.com/display/tec/Instances>  
  
Abaixo segue um exemplo da configuração dos ***Instances*,** lembrando que não se trata de uma indicação para alterar dessa forma, e sim, cada ambiente deve ser avaliado conforme documentação pois irá consumir licença.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33555192795287)  
  
Ainda na mesma seção **[HTTPENV]**também recomenda-se colocar as duas ***TAGS*** abaixo:  
 **EnableKeepAlive=0 >** Indicar que a conexão será encerrada depois da resposta à requisição. **Stateless=1** > Com essa ***TAG*** só haverá consumo de licença quando a *thread* estiver em uso.  
  
Abaixo segue os *links* das documentações de referência das *TAG's* mencionadas:  
***EnableKeepAlive*:** <https://tdn.totvs.com/pages/releaseview.action?pageId=567770418> ***STATELESS*:** <https://tdn.totvs.com/pages/viewpage.action?pageId=527852596>  
  
**Saiba Mais  
[RH - Linha Protheus - MEU RH - Como gerar o Console.log para análise de erros do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751)**  
**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
