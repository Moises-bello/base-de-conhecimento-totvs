---
article_id: 18077120018967
category: IMPLANTAÇÃO
content_hash: 6a972e5252fd646767bf2ad481f32abd39a19a5533cdb2bdf4e00606e25a71ca
fetched_at: '2026-06-28T22:44:33.344259+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível configurar um Timeout nos serviços
  do Meu RH
type: support-article
updated_at: '2026-06-15T19:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18077120018967-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-configurar-um-Timeout-nos-servi%C3%A7os-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18077148831639) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
É possível configurar um *Timeout* nos serviços do Meu RH?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
No serviço *REST* do App Meu RH, é possível incrementar a **chave** ***TimeOut*** e a quantidade de milissegundos necessários, para que uma requisição seja cancelada para o serviço do REST, que pode ter algum tipo de efeito em seu ambiente.

**Sobre a chave** ***TIMEOUT***  
Esta chave tem **influência direta na** ***comunicação HTTPS***.  
  
Durante o SSL *handshake*, cliente e servidor negociam protocolo e cifra para a realização de comunicação segura.   
  
Se o servidor não recebe uma resposta do cliente, ele deve aguardar um tempo máximo.  
  
Esta chave configura este tempo.  
  
Exemplo de chave TIMEOUT na sessão [SSLCONFIGURE]  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18076990879383)  
  
**Documentação de Referência:** [**Timeout na Chave [SSLCONFIGURE]**](https://tdn.totvs.com/x/-I_EIg)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
