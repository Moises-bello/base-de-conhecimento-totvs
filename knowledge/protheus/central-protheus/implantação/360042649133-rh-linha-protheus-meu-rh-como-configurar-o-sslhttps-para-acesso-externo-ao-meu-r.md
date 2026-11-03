---
article_id: 360042649133
category: IMPLANTAÇÃO
content_hash: 491461c816b7bf3d6a10bd7c91d80ae76bbeafe0abe68d5250583b9bf12810f7
fetched_at: '2026-06-28T22:44:33.446654+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar o SSL/HTTPS para acesso externo
  ao MEU RH
type: support-article
updated_at: '2026-01-09T19:14:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042649133-RH-Linha-Protheus-MEU-RH-Como-configurar-o-SSL-HTTPS-para-acesso-externo-ao-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17378891104535) Tempo aproximado para leitura: 00:04:00 min**  
  
**Dúvida**  
Como configurar o SSL/HTTPS para acesso externo ao MEU RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Para configurar o **SSL/HTTPS** para o **MEU RH** e utilizar uma conexão segura é obrigatório que realize todos os passos indicados nos artigos relacionados abaixo:  
  
[**Informações adicionais para configuração do APPSERVER.INI**](https://tdn.totvs.com/pages/releaseview.action?pageId=550322262)**:**

1. [**Certificados SSL**](https://tdn.totvs.com/display/NPR/Certificados+SSL)
2. [**Caso de uso de certificado SSL/TLS**](https://tdn.totvs.com/pages/viewpage.action?pageId=550326944)
3. [**Validação de certificados**](https://tdn.totvs.com/pages/viewpage.action?pageId=550327608)
4. [**Informações Relevantes sobre HTTP/REST no MeuRH**](https://tdn.totvs.com/pages/viewpage.action?pageId=550327736)

Segue abaixo um exemplo de configuração do **MEU RH** no **APPSERVER.INI** com a utilização de **SSL/HTTPS:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17378557418007)**  
  
**Sessão [HTTPREST] e [SSLCONFIGURE]**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25692451173271)**  
  
**Observação:** A *tag* *PassPhrase* refere-se a senha do certificado utilizado.   
Caso não tenha senha mantenha a *tag* no padrão ou em branco.  
  
**Sobre o certificado,** se houver erros no momento de subir o serviço do REST, será necessário validar junto à certificadora da Empresa, os certificados apontados, onde para a aplicação do Appserver é importante que o **certificado, e a chave privada** estejam codificados no **formato Apache (Base 64) com extensão (\*.PEM) ou (\*.CRT).**  
Entre em contato com sua certificadora para que seja fornecido o certificado neste formato.  
  
Mais informações nos *links* abaixo:  
<https://tdn.totvs.com/display/tec/KeyServer>    
<https://tdn.totvs.com/display/tec/CertificateServer>  
  
**ATENÇÃO :** [**Não é recomendado uso dos certificados totvs para o meu rh.**](https://tdn.totvs.com/pages/viewpage.action?pageId=548376390)  
O certificado padrão da TOTVS foi criado para comunicação Segura da Porta Multiprotocolo da conexão *SmartClient Desktop* com *Appserver* (Aplicação Protheus).   
Não serve para o *Rest* Meu Rh, recomendamos que seja feito a compra com uma certificadora de sua preferência.  
  
**IMPORTANTE:**  
**Para versões de Android abaixo da 14, é necessário aplicar os procedimentos da documentação a seguir:**  
**https://tdn.totvs.com/pages/viewpage.action?pageId=961003106**  
  
**IP ou URL para acesso externo:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17378851770007)**  
  
Abaixo, segue o modelo de Configuração do arquivo ***properties.json*** deste exemplo:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17378668923799)**  
  
**Importante:** Ao configurar o MEU RH para um **acesso externo**, primeiramente certifique-se de que os acessos através de **endereço e porta interno** estão funcionando corretamente, após funcionar realize os direcionamentos de IP e porta para o acesso externo, tanto do serviço do Meu RH quanto do serviço REST.  
  
**Vale ressaltar que, a alteração do acesso ao Meu RH de** ***HTTP*** **para** ***HTTPS***, ou seja, de protocolo inseguro para seguro, faz-se necessário a geração de um novo *QR Code* para acesso ao Meu RH, pois a URL do Meu RH e a URL do REST serão alteradas.  
  
Para geração de um novo *QR Code*, verificar o vídeo *How-To* abaixo:  
<https://www.youtube.com/watch?v=Flt-LKPEyBY>   
  
Após a geração do novo *QR Code*, **será necessário em TODOS os celulares dos funcionários da Empresa, adicionar um novo Ambiente e ler o novo acesso gerado.**  
  
- como ler o novo *QR Code*, para celulares ***Android***, [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058394613)  
- como ler o novo *QR Code*, para celulares ***iOS***, [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058394333)  
  
**Obs.:** Vale ressaltar que o **Suporte Padrão** não tem como auxiliar nos processos relacionados à configuração de **Endereços Externos,** ***DNS*****,** ***Firewall*****/Antivírus e Certificado Digital**, pois tratam-se de questões internas e de infraestrutura particular de cada Empresa.  
  
Caso tenha alguma falha nos processos indicados nos artigos acima os erros mais comuns são:

1. Falha no Acesso ao MEU RH ou mensagem abaixo:  
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096026934)
2. Mensagem de erro no Console.log:  
     
   [ERROR][SSL] SSL Accept method error '3333333333'.  
   [ERROR][SSL] SSL Accept method '6'.
3. Rotina de Geolocalização do MEU RH apresenta mensagens de erro relacionadas abaixo:  
     
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098322293)  
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098322213)

**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
