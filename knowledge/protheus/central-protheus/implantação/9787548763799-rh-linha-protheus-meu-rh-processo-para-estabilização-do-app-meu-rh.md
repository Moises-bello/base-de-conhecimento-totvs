---
article_id: 9787548763799
category: IMPLANTAÇÃO
content_hash: 13f6bffac5632325b621ae57ce80dfdb55198ee6258eddbf0b5503d476ee0492
fetched_at: '2026-06-28T22:44:33.368136+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Processo para estabilização do app MEU RH
type: support-article
updated_at: '2026-01-14T18:05:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9787548763799-RH-Linha-Protheus-MEU-RH-Processo-para-estabiliza%C3%A7%C3%A3o-do-app-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23083990934807) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Presença de Lentidão, Quedas do serviço REST e/ou instabilidade durante o uso do Meu RH  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Causa**  
Falta de atualização e inclusão de chaves de estabilização no appserver.ini do MEU RH  
  
**Solução**  
  
**-> Passo 1**  
**ATUALIZAÇÃO DAS BIBLIOTECAS DE FRAMEWORK (LIB) e BINARIO:**  
Atualizar as bibliotecas de framework (LIB):  
Onça: <https://suporte.totvs.com/portal/p/10098/download#detail/1168735>   
Harpia: <https://suporte.totvs.com/portal/p/10098/download?e=1050526>  
  
**-> Passo 2**  
**ATUALIZAÇÃO DO APPSERVER.INI:**  
Adicionar as seguintes informações abaixo no appserver.ini do serviço REST:  
**EnableKeepAlive=0** -> Adicionar na seção **HTTPENV**. Esta chave pode estar configurado também como **HTTPURI**.   
  
**Exemplo:**  
[HTTPENV]  
URL=/restT1  
PrepareIn=T1  
Instances=2,5,1,1  
CORSEnable=1  
AllowOrigin=\*  
Public=fwjwt/refresh\_token,auth,setting/companySettings  
**EnableKeepAlive=0**  
  
A função da tag **EnableKeepAlive** é indicar que a conexão será encerrada depois da resposta à requisição.  
  
**Stateless=1**-> Adicionar na seção **HTTPV11**. Com essa **TAG** só haverá consumo de licença quando a thread estiver em uso.  
  
Abaixo segue os links das documentações de referência das TAG's mencionadas:  
**EnableKeepAlive:** <https://tdn.totvs.com/pages/releaseview.action?pageId=567770418>  
**Stateless:** <https://tdn.totvs.com/pages/viewpage.action?pageId=527852596>  
  
**Compression**=1 -> Adicionar na seção **HTTP** (caso não possua SSL) ou **HTTPS** (caso possua SSL).  
  
Exemplo:  
[HTTP]  
ENABLE=1  
**COMPRESSION=1**

Para saber mais sobre a tag Compression, acesse: [Compression](https://tdn.engpro.totvs.com.br/display/tec/Compression)  
  
Em casos de ambientes que utilizam HTTPS/SSL, revisem as configurações com base no artigo: [Informações adicionais para configuraçao de appserver](https://tdn.totvs.com/x/VkDNI)  
  
Caso utilize **Broker** no seu ambiente:  
Adicione na chave do Broker **HTTP/HTTPS** a tag: **USING\_COOKIES=0**  
  
Na versão **2410** para quem usa broker é obrigatório o uso da chave:  
**MONITORING\_TYPE = CONNECTION no** ***Rest*** **do** ***Broker*** **conforme documentação abaixo:**  
<https://tdn.totvs.com/display/tec/Balanceamento+entre+Clientes+HTTP+e+servidor+Application+Server>   
  
Para apps nas versões de ***Android***menores que **14** validar **documentação referente a compatibilidade de certificado SSL**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=961003106>  
  
**-> Passo 3:**  
**ATUALIZAÇÃO DOS ARQUIVOS DO PORTAL MEU RH:**  
Os Arquivos do Portal sofrem atualizações periódicas e devem sempre estar de acordo com a versão dos fontes que está utilizando para evitar qualquer tipo de comportamento indesejado, inclusive quanto à performática do ambiente, portanto estar atualizado em todos os termos é extremamente recomendável e necessário para garantir a estabilidade do serviço.  
Acessar o link a seguir e realizado o download conforme a release:  
<https://tdn.totvs.com/display/NPR/Passo+1%3A+Atualizando+os+arquivos>  
  
Importante: Deixar um *backup* do arquivo *properties.json*. Após a atualização da pasta, copiar o arquivo de backup para dentro dessa pasta.  
  
**-> Passo 4:**  
**INFORMAÇÕES IMPORTANTES:**  
É comum que o MEU RH possua uma configuração separada do ERP com RPO e binários exclusivos.  
Portanto, como esse processo de atualização envolve bibliotecas de *framework* (**Lib**), tanto o **repositório** do Meu RH quanto **todos os demais repositórios** (RPOs) que apontam para o mesmo ambiente (Protheus\_data e banco de dados) devem ser atualizados. Isso garante a integridade do produto.  
Caso o problema de instabilidade persistir, abra um ticket ao time de suporte técnico, grupo de Meu RH com as informações listadas abaixo:  
  
**1.** Arquivo com **data das suas rotinas do RPO do Meu RH**, conforme artigo: [Como gerar arquivo com a data de todos os fontes do RPO?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024518391)  
**2.** **Data** dos **arquivos do portal** Meu RH  
**3.** Arquivos **appserver.ini** e **properties.json**atuais, após os procedimentos deste artigo  
**4. c*****onsole.log*** demonstrando a tentativa de autenticação, conforme artigo: [Como gerar o Console.log para análise de erros do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751)  
**5.** **QRCode** ou print da configuração do App no Celular (caso utilize via aplicativo mobile)  
**6.** Informe se o erro ocorre apenas em dispositivos IOS, Android, ambos e/ou via browser  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
