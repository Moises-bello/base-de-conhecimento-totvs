---
content_hash: 5d6c02f137037811bf0ac8b01fa449b1c6fc304719db3686c7d98cbb491491c5
fetched_at: '2026-06-29T00:12:06.367953+00:00'
page_id: '915174425'
product: rm
source: tdn-rm
title: Padrão Multi Tenancy
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=915174425
version: 6
---

# **1) Configurando os hosts em: C:\Windows\System32\drivers\etc\hosts**

---

Abra o arquivo "C:\Windows\System32\drivers\etc\hosts"  com privilégio Administrador e adicione os urls desejados, exemplo:

127.0.0.1            [tenancy1.rm.totvslocal.com.br](http://tenancy1.rm.totvslocal.com.br)  
127.0.0.1            [tenancy2.rm.totvslocal.com.br](http://tenancy2.rm.totvslocal.com.br)

**Após alterar, favor fechar e salvar para que as configurações façam efeito!**

# **2) Configurando o arquivo Web.config em: C:\RM\Atual\Release\FrameHTML\Web.config**

---

Abra o arquivo "C:\RM\Atual\Release\FrameHTML\Web.config"  e adicione os seguintes parâmetros para configuração do ambiente multi Tenancy

    <add key="SubDomainMask" value="[ALIAS].[rm.totvslocal.com.br](http://rm.totvslocal.com.br)" />  
    <add key="MULTITENANCY" value="true" />  
    <add key="TenantPathEnabled" value="true" />  
    <add key="LoginSecurityCache" value="false" />

**Após alterar, favor fechar e salvar para que as configurações façam efeito!**

# **3) Configurando o arquivo Alias.dat em: C:\RM\Atual\Release\Bin\Alias.dat**

---

Adicione os alias ao "C:\RM\Atual\Release\Bin\Alias.dat" com as respectivas bases Tenancy, exemplo:

  <DbConfig>  
    <Alias>**tenancy1**</Alias>

    ...  
  </DbConfig>

  <DbConfig>  
    <Alias>**tenancy2**</Alias>  
    ...  
  </DbConfig>

O arquivo Alias.dat ficará com o seguinte formato:

**Após alterar, favor fechar e salvar para que as configurações façam efeito!**

# **4) Configurando o Parâmetro Global FrameHTML em C:\RM\Atual\Release\Bin\RM.exe**

---

Abra o RM.exe "C:\RM\Atual\Release\Bin\RM.exe" e adicione os seguintes parâmetros para configuração do ambiente multi Tenancy

Em sua respectiva base de dados

    <Alias>**tenancy1**</Alias>

Defina o endereço do FrameHTML: [http://tenancy1.rm.totvslocal.com.br](http://tenancy1.rm.totvslocal.com.br/)

    <Alias>**tenancy2**</Alias>

Defina o endereço do FrameHTML: [http://tenancy2.rm.totvslocal.com.br](http://tenancy1.rm.totvslocal.com.br/)

**Após alterar, favor fechar e salvar para que as configurações façam efeito!**

# **5) Acesse o Portal do cliente através dos hosts multi Tenancy**

---

Abra o Portal do Cliente pelos seguintes hosts multi Tenancy configurados

[http://tenancy1.rm.totvslocal.com.br/FrameHTML/web/app/Imb/PortalCliente/#/](http://tenancy1.rm.totvslocal.com.br/FrameHTML/web_src/app/Imb/PortalCliente/#/)

[http://tenancy2.rm.totvslocal.com.br/FrameHTML/web/app/Imb/PortalCliente/#/](http://tenancy2.rm.totvslocal.com.br/FrameHTML/web_src/app/Imb/PortalCliente/#/)
