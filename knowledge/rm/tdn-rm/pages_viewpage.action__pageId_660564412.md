---
content_hash: 097a41a48348afd2d273936412462fc713b30c60f3dbd399f31944262845ae95
fetched_at: '2026-06-29T00:11:13.413642+00:00'
page_id: '660564412'
product: rm
source: tdn-rm
title: Integração TAS (TOTVS API Services) RM (Parâmetros Globais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=660564412
version: 33
---

true

A partir das versões informadas abaixo, para utilização dos serviços pagos do TOTVS API Services é preciso informar a API-KEY (Chave de autenticação - Token) disponibilizada no painel do Manager, [link](https://manager.totvs.app/). A utilização dos demais serviços é independente do token.

Mais informações sobre os serviços pagos acesse: <https://www.totvs.com/totvs-api-services/>

Mais informações sobre o TOTVS API Services, acesse a página da solução no .

Para exemplo de utilização do TOTVS API Services no RM, acesse: <https://tdn.totvs.com/x/LDUmDg>

### **Alteração disponível nas seguintes versões e patches:**

12.1.31, a partir do Patch 294

12.1.32, a partir do Patch 241

12.1.33, a partir do Patch 177

12.1.34, a partir do Patch 100 e versões mais atuais

### **Configuração para versão 12.1.2306 e superiores**

A partir da versão 12.1.2306, não será mais necessário informar manualmente o nome de usuário e senha, pois o RM enviará automaticamente essas informações para o TOTVS API Services. Os campos relevantes agora podem ser encontrados nos Parâmetros Globais.

**Url de serviços do TOTVS API Services,** É TOTVS API SERVICES que possui o domínio <http://totvsapiservices.totvs.com.br>

**Chave de autenticação (Token)**, É uma chave para utilização dos serviços pagos do TOTVS API SERVICES. Mais detalhes de onde obter o token podem ser encontradas neste .

Atenção

Na versão 12.1.2306, houve uma mudança nos nomes dos menus que antes eram referentes ao Mashup. Agora, esses menus foram renomeados para TOTVS API Services. Caso tenha alguma dúvida ou precise de ajuda para encontrar os menus que procura, nossa equipe de suporte estará pronta para ajudá-lo.

### **Configuração para versão 12.1.2302, 12.1.2209, 12.1.2205:**

Para configurar o recurso de Mashup nos Parâmetros Globais, vá na tela principal do RM selecione o Aba, Ambiente → Parâmetros → Parâmetros Globais.

paramGlobais

Na tela de Parâmetros Globais, selecione a Aba, Integração Mashup.

Informe a Url do endereço de serviço do Mashup, o usuário e senha para autenticação. Neste caso, o novo serviço disponibilizado pela TOTVS é o TOTVS API SERVICES que possui o domínio <http://totvsapiservices.totvs.com.br>

Chave de autenticação (Token), É uma chave para utilização dos serviços pagos do TOTVS API SERVICES. Mais detalhes de onde obter o token podem ser encontradas neste .

Caso seja necessário criar uma nova conta, acesse ,

Após realizar a configuração e clicar em Salvar, será necessário aguardar o tempo informado na mensagem de aviso, para que as novas configurações tenham efeito.

   
   
  
**Tela de gerenciar do Mashup:**

Quando todas as configurações estiverem preenchidas no Parâmetros Globais, o ícone de alterar as conexão desta tela não será exibido e o login será realizado automaticamente.  
  
  
Caso as configurações de Url do serviço, Usuário e senha, não estiverem preenchidas na tela de , o ícone será novamente exibido e as configurações poderão ser informadas nesta tela. trueRedNão é recomendado usar dessa forma

IMPORTANTE

A partir de agora a parametrização do login deve ser informada exclusivamente na tela de .
