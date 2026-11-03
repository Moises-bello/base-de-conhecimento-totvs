---
article_id: 360050190553
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 7ea561d4e703e707b3cb345885fc9cbd57df5976042e77467798f3474048a489
fetched_at: '2026-06-28T22:39:58.604908+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - TSS: WSCERR044
  / Não foi possível POST 999 : Invalid HTTP Connection (WebIss)'
type: support-article
updated_at: '2021-10-06T19:08:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050190553-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-TSS-WSCERR044-N%C3%A3o-foi-poss%C3%ADvel-POST-999-Invalid-HTTP-Connection-WebIss
---

**Ocorrência**Ao realizar a transmissão de um RPS para municípios do provedor WebIss o RPS fica com STATUS = 2 (Aguardando Transmissão do Lote) por conta do erro abaixo:  
  
WSCERR044 / Não foi possível POST : URL https://feiradesantanaba.webiss.com.br/servicos/wsnfse/nfseServices.svc ( 999 : Invalid HTTP Connection )  
  
Obs.: Nesse caso foi usado Feira de Santana como exemplo.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse problema ocorre pelo fato do TSS não estar conseguindo realizar uma comunicação de POST com a prefeitura em questão. Isso pode ser bloqueio de rede (local ou da própria prefeitura) ou requisições feitas em excesso pelo TSS.  
  
**Solução**1ª Verificação  
Pegar a URL da prefeitura (através do erro no console) e tentar abri-la no navegador da mesma máquina onde o TSS está instalado. Caso utilize servidor, deverá abrir dentro do navegador do mesmo.  
  
Nesse caso usado como exemplo a URL seria:   
- <https://feiradesantanaba.webiss.com.br/servicos/wsnfse/nfseServices.svc>Importante lembrar que deverá realizar a importação do Certificado Digital dentro do navegador que irá realizar o teste. Se tudo estiver correto será aberto a URL em questão, exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075227593/mceclip0.png)  
  
2ª Verificação  
Caso a URL esteja acessível corretamente, deverá incluir a linha abaixo no Appserver.ini do TSS, reiniciar o serviço e realizar novos testes.  
  
disableCipher=RC4  
  
![](https://totvssuporte.zendesk.com/attachments/token/2z7NC0pFHHMxVgdelz2yDHKFV/?name=inline2092543156.png)  
  
Essa linha habilitada reduz a quantidade de cifras enviadas para o servidor da prefeitura, onde no caso essas cifras (de criptografia e troca de chaves) são utilizadas na comunicação SSL/TLS.   
As cifras são divididas em grupos, no caso o RC4 como possui uma grande quantidade e não é aproveitado por esse provedor, é aconselhável desabilitar ele especificamente.  
De uma forma resumida, é uma maneira do TSS evitar enviar requisições em excesso e causar o erro de POST.
