---
content_hash: e9df7317193eca6e7965e3b401f903a7f472cab041d6a87670175af293ee4c45
fetched_at: '2026-06-29T00:09:37.856691+00:00'
page_id: '425459634'
product: rm
source: tdn-rm
title: Linha RM x Microsoft Dynamics CRM - Configuração e Parâmetros do Microsoft
  Dynamics CRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459634
version: 7
---

**Configuração e Parâmetros do Microsoft Dynamics CRM**

---

**Configuração do Microsoft Dynamics CRM 4.0**  
    
 Para configurar o MS CRM 4.0 é necessário possuir os arquivos de configuração:

* Extensões de Clientes\_4.0.zip
* Entidades Personalizadas\_4.0.zip

*Observação:* Para obter os arquivos de configuração referente a esta integração, entre em contato com o Suporte da TOTVS-BH no produto Integração. Os arquivos customizados disponíveis são para as versões 4.0 e 2011 do MS CRM.   
    
 Realize os passos a seguir:  
 **1**. No arquivo de configuração "customizations.xml", que se encontra dentro de Extensões de Clientes\_4.0.zip, localize a expressão \*http://\* que deve estar em uma expressão similar a mostrada abaixo:  
 ... url = '**http://**RM0001010:8051/wsPageIndex/MSCRM?DbAlias=AliasRM&idConceito...  
    
 Substitua:

* **RM0001010** pelo hostname ou pelo IP do servidor do TBC.
* **AliasRM** pelo nome do Alias referente a conexão com o banco de dados RM.  
    
   Por exemplo:  
   ... url = 'http://**RM0005533**:8051/wsPageIndex/MSCRM?DbAlias=**CORPORERM**&idConceito...

**2**. Acesse o MS CRM 4.0 e clique na opção **Configurações** na página principal.

**3**. No menu acesse **Personalização,** e após escolha a opção **Importar Personalizações.**

**4**. Clique na opção **Procurar** e selecione um dos arquivos de configuração. Após clique em **Carregar.**

**5**. Selecione as Personalizações e clique em **Importar Personalizações Selecionadas.** Aguarde as customizações serem importadas para o MS CRM. Após clique em ok.

**Observação:**

Repita os procedimentos 3, 4 e 5 para o outro arquivo de configuração.

**6**. Toda customização instalada ou importada deve ser publicada para que as alterações entrem em vigor. Acesse: **Configurações | Personalização | Personalizar Entidades**   
    
 Selecione as entidades e clique em **Publicar.**  
    
**7**. Também é necessário habilitar o MS CRM para que sejam exibidas todas as alterações realizadas no ISV.Config, SiteMap, etc. Para isso acesse: **Configurações | Administração | Configurações do sistema.**

**8**. Na aba **Personalização,** em Menus e Barras de Ferrametnas Personalizados, selecione a opção: **"Web, Outlook Online, Outlook offline".**

Após, clique em ok.

O MS CRM 4.0 está configurado com a Linha RM para esta integração.   
    
 **Configuração do Microsoft Dynamics CRM 2011**  
    
 Para configurar o MS CRM 2011 é necessário possuir os arquivos de configuração:

* Default\_1\_0\_ISV\_2011.zip;
* Default\_1\_0Personalizacao\_2011.zip;

*Observação:* Para obter os arquivos de configuração referente a esta integração, entre em contato com o Suporte da TOTVS-BH no produto Integração. Os arquivos customizados disponíveis são para as versões 4.0 e 2011 do MS CRM.  
    
 Realize os passos a seguir:

**1**. Clique na opção **Configurações** na página principal.

**2**. Acesse: **Personalização | Personalizações.** Após, clique na opção **Soluções.**

**3**. Selecione a opção **Importar.** Clique em **Procurar** e informe um dos arquivos de configuração. referente a integração. Após, clique em **Avançar.**

**4**. Clique em **Avançar** novamente. Os arquivos serão importados para o MS CRM 2011.

**5**. Ao final da importação, clique na opção **Publicar todas as Personalizações.**

*Observação:* Repita os procedimentos 3, 4, e 5 para o outro arquivo de configuração.

**6**. Nos arquivos de configuração que foram importados, é necessário alterar os arquivos de Recursos da Web. Para alterar os arquivos acesse: **Configurações | Personalizações | Personalizar Sistema**

**7**. Clique em **Recursos da Web.** Será exibida a lista de arquivos JavaScript (.js) utilizados para integração. Os arquivos que devem ser alterados são:

* account\_ribbon
* contact\_ribbon
* new\_contratocorpore\_ribbon
* new\_estado\_ribbon
* new\_municipio\_ribbon
* opportunity\_ribbon
* product\_ribbon
* quote\_ribbon
* salesorder\_ribbon

**8**. Selecione o arquivo desejado e dê um duplo-clique no mesmo. Na nova janela, clique em **Editor de Texto.**

**9**. Localize no script a expressão \*http://\* que deve estar em uma expressão similar a mostrada abaixo:  
    
 ... url = '**http://**RM0001010:8051/wsPageIndex/MSCRM?DbAlias=AliasRM&idConceito...  
    
 **Substitua:**

     - **RM0001010** pelo hostname ou pelo IP do servidor do TBC.  
      - **AliasRM** pelo nome do Alias referente a conexão com o banco de dados RM.  
    
 Por exemplo:  
 ... url = 'http://**RM0005533**:8051/wsPageIndex/MSCRM?DbAlias=**CORPORERM**&idConceito...

**10**. Salve todas as configurações e clique em **Publicar.**

O MS CRM 2011 está configurado com a Linha RM para esta integração.

**Recursos Adicionais**

Acesse os boletins técnicos abaixo para ver mais detalhes da configuração:

[Configuração do Microsoft Dynamics CRM 4.0](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-configuracao-do-microsoft)

[Configuração do Microsoft Dynamics CRM 2011](http://totvsconnect.blogspot.com.br/2012/09/como-fazer-configuracao-do-microsoft_13)
