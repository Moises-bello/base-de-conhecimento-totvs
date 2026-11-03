---
content_hash: 29e1157ed9080c8c2971e88e9ab74f714e390ae1e22ec8539fe0b6579b5451ba
fetched_at: '2026-06-29T00:08:42.821992+00:00'
page_id: '287079669'
product: rm
source: tdn-rm
title: Configurando o RM Multi Tenancy (Multi Alias)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287079669
version: 25
---

# Objetivo

---

O objetivo deste documento é auxiliar na configuração de uma instalação do RM para trabalhar no modelo multi tenancy, ou seja, ter apenas uma instalação e atender várias bases/alias sem a necessidade do usuario selecionar alias no RM.exe e no portal. Alem disso a configuração permite que os web services fornecidos pelo HOST trabalhem sem a configuração de alias default para atender as requisições.

# Pre-requisitos

---

1. Configuração da infraestrutura para fornecer um nome de rede, dominio ou sudominio para cada Tenant.   
   Ex.: cliente1.totvs.com.br, cliente2.totvs.com.br, clienteN.totvs.com.br  
   Todos estes direcionando para o mesmo ambiente de instalação.
2. Utilizar o configurador global.
3. Utilizar o TOTVS Update.

Atenção

Observação

Para a execução de TLS 1.1 e 1.2 no Windows 7 é necessário adicionar os registros abaixo, visto que são os protocolos de comunicação ativos atualmente e que por padrão não são ativos na versão Windows7:

Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]  
"DisabledByDefault"=dword:00000000  
  
[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]  
"DisabledByDefault"=dword:00000000

**Arquivo disponível para download:** [Arquivo.reg](https://tdn.totvs.com/download/attachments/215482828/arquivo.reg?version=1&modificationDate=1590091618463&api=v2)

Importante

As configurações de Portal e HOST são totalmente independentes, ou seja, uma não implica absolutamente nada na outra. Portanto pode-se utilizar somente o multi tenancy do portal, sem nenhuma configuração adicional no host.

# Configurando o HOST como Multi Tenancy

---

1. Fazer a instalação do Server do RM no servidor e configurá-lo como servidor de atualização conforme documentação disponível [neste link.](http://tdn.totvs.com.br/display/LRM/Configurando+o+Smart+Client+RM+e+TOTVS+Update)
2. Criar um alias de banco para cada Tenant e dar um nome que possa ser inserido em um domínio, subdomínio ou nome de recurso de rede.
3. Criar o arquivo de configuração global contendo a tag SubDomainMask respeitando os seguintes critérios:  
   Vamos supor que você possui dois Tenants onde seus respectivos Alias são: **cliente1** e **cliente2**.  
   - Se o seus subdomínios forem: **cliente1.empresa.com** e **cliente2.empresa.com** então a tag SubDomainMask deve ser **[ALIAS].empresa.com**  
   - Se o seus domínios forem: **www.[cliente1.com](http://cliente1.empresa.com)**e **www.[cliente2.com](http://cliente2.empresa.com)** então a tag SubDomainMask deve ser **www.[ALIAS].[com](http://empresa.com)**  
   - Se o seus nomes de rede forem: **[cliente1](http://cliente1.empresa.com/)**e **[cliente2](http://cliente2.empresa.com/)**então a tag SubDomainMask deve ser somente **[ALIAS]**
4. Os arquivos de **.config** de cada aplicação devem conter apenas a tag configpath, conforme documentação acima relacionada.
5. Seguem exemplos de como devem ficar os arquivos de configuração: ,  , , .  
   A partir da versão 12.1.28, o Multi Tenancy pode ser configurado com o novo formato de configuração global, em JSON:    
   Exemplo dos arquivos de configuração em formato JSON:  , , , .
6. As tags **UpdateServer** e **ServicesHostName** devem direcionar para um endereço padrão válido, pois não faz nenhuma diferença, por ser uma tag relacionada à ambiente e infraestrutura.

   Atenção

   Especificamente para a tag **ServicesHostName** recomendamos utilizar um endereço válido que exponha os serviços, mas sem um tenant específico.

   Exemplo: **tenant.dominio.com**

   Ao utilizar o WSDL é importante que o cliente de consumo, SOAP UI por exemplo, consiga obter uma resposta deste endereço, mas o cliente deverá obrigatoriamente trocar o tenant pelo nome correto do seu Alias para consumir o serviço.

   Ao adicionar o WSDL no SOAP UI, por exemplo teremos o seguinte nas requisições:

   O trecho ***tenant***deve ser trocado pelo nome do Alias que representa o tenant do cliente.  

   Não é possível expor WSDLs específicos por tenant.

   false

   Atualmente para o consumo do WebServices via Host através do software SoapUI, foi criada uma tag opcional que pode ser acrescentado no host (com a porta de escuta do WebApi no TGM):

   **<add key="SERVICESPORT" value="9001" />**
7. Os arquivos acima devem ficar no diretório de instalação do RM (RM.Net) no servidor.
8. Feito isso os domínios, subdomínios ou nomes de rede devem ser criados de forma compatível com a configuração acima.
9. Feito isso basta acessar normalmente as URLs de serviço, como por exemplo:
   1. [http://empresa1.totvs.com.br:8051/wsUpdate](http://empresa1.totvs.com.br/wsUpdate)  - Este para baixar o SmartClient e utilizar já com o alias correto de forma transparente.
   2. [http://empresa1.totvs.com.br:8051/w](http://empresa1.totvs.com.br/wsUpdate)sReport  - Este para gerar relatórios via web service.
   3. Após baixar o Smart Client, basta executá-lo que ele já estará configurado corretamente para o Tenant correto.  
      Obs.: Ao baixar o Smart Client de ambiente Multi Tenancy, as telas de gerenciamento de Alias se comportam da seguinte forma:  
         - Se baixado na mesma máquina onde está o ambiente server: É possível visualizar e editar apenas o cadastro do Alias do Tenant.  
         - Se baixado em máquina diferente de onde está o ambiente server: É possível apenas visualizar o cadastro do Alias do Tenant.  
         Em ambos os casos, na tela de login não é possível alterar o Alias, pois ele carrega apenas o Tenant correto.

# Configurando o Portal Corpore.NET e FrameHTML como Multi Tenancy

---

1. Fazer a instalação do Portal RM no servidor.
2. Criar um alias de banco para cada Tenant e dar um nome que possa ser inserido em um domínio, subdomínio ou nome de recurso de rede.
3. **Em todos os alias será necessário deixar em branco o parâmetro URL do Portal em Parâmetros Globais.**
4. Configurar a tag SubDomainMask nos arquivos **Web.config** dos diretórios **Corpore.Net e FrameHTML** respeitando os seguintes critérios:  
   Vamos supor que você possui dois Tenants onde seus respectivos Alias são: **cliente1** e **cliente2**.  
   - Se o seus subdomínios forem: **[cliente1.empresa.com](http://cliente1.empresa.com)** e **[cliente2.empresa.com](http://cliente2.empresa.com)** então a tag SubDomainMask deve ser **[ALIAS].[empresa.com](http://empresa.com)**  
   - Se o seus domínios forem: **www.[cliente1.com](http://cliente1.empresa.com/)**e **www.[cliente2.com](http://cliente2.empresa.com/)** então a tag SubDomainMask deve ser **www.[ALIAS].[com](http://empresa.com/)**  
   - Se o seus nomes de rede forem: **[cliente1](http://cliente1.empresa.com/)**e **[cliente2](http://cliente2.empresa.com/)**então a tag SubDomainMask deve ser somente **[ALIAS]**
5. A Tag dos arquivos **web.config** devem ficar desta forma, por exemplo:  <add key="SubDomainMask" value="[ALIAS].totvs.com" />
6. A Tag **FrameHtmlUrl** do **web.config** do **Corpore.Net** deve ser preenchida normalmente, sem se preocupar com o tenant, por exemplo: **<add key="FrameHtmlUrl" value="http://localhost:8080/RM" />**
7. Feito isso basta acessar os portais normalmente. O seletor de alias não estará mais disponível para selecionar o Tenant, pois o mesmo será resolvido de forma transparente.

Facilidade!

## Para adicionar um novo tenant no ambiente de instalação, basta criar o Alias de banco e criar um dominio, subdomínio ou nome de rede que respeite as regras definidas no parâmetro SubDomainMask!!

Importante

As configurações de Portal e HOST são totalmente **independentes,** ou seja, uma não implica absolutamente nada na outra. Portanto pode-se utilizar somente o multi tenancy do portal, sem nenhuma configuração adicional no host.

# Como funciona?

---

Com o ambiente configurado, o Portal Corpore.NET, FrameHTML, Web Services (somente expostos pelo HOST, conforme recomendado) e RM.exe farão a escolha do Tenant de forma transparente. Exemplo:

* Criamos apenas UMA instalação do RM e configuramos a tag **SubDomainMask** com a informação**[ALIAS].totvs.com.br** nos arquivos de confguração, confirme orientação acima.
* Neste exemplo considero que temos os portais e o servidor de aplicação (HOST) instalado no ambiente.
* O primeiro cliente vai utilizar o ambiente, então chamaremos ele de **cliente1**.
* Criamos um alias de nome **cliente1**no ambiente.
* Criamos um subdomínio público, direcionado para o ambiente de instalação, chamado **cliente1.totvs.com.br**.
* O cliente agora pode acessar o endereço **<http://cliente1.totvs.com.br:8051/wsUpdate>** para baixar o SmartClient.
* O SmartClient não dará opção para selecionar alias, pois será resolvido de forma transparente.
* Os WebServices podem ser listados através do endereço **[http://cliente1.totvs.com.br:8051](http://cliente1.totvs.com.br:8051/wsUpdate)/wsPageIndex.**
* Não será necessário configurar nenhum alias Default.
* O portal pode ser acessado pelo endereço**[http://cliente1.totvs.com.br/Corpore.](http://cliente1.totvs.com.br/Corpore.NET)Net** e também não terá opção para selecionar alias.
* O segundo cliente vai utilizar o ambiente, então chamaremos ele de **cliente2**.
* Criamos um alias de nome **cliente2**no ambiente.
* Criamos um subdomínio público, direcionado para o ambiente de instalação, chamado**[cliente2.totvs.com.br](http://cliente1.totvs.com.br).**
* Basta isso e o cliente2 pode acessar da mesma forma que o cliente1, porem com o endereço **[cliente2.totvs.com.br](http://cliente1.totvs.com.br/).**
* Em resumo, os dois clientes estão utilizando o mesmo ambiente de forma tranparente e sem a necessidade de se preocupar em selecionar o alias.

Os servidores de portal e servidor de aplicação (HOST) não precisam ser os mesmos, basta fazer as configurações devidas em ambientes separados e criar os sudomínios dirrecionando-os corretamente.

Ao realizar a configuração no arquivo "**hosts**", é necessário que o "**Nome do Alias"** seja adicionado juntamente ao subdomínio.

Exemplo: **[ALIAS].empresa.com**
