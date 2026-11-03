---
content_hash: adee51e642259f1a1372252de6e713c2f5beb56c77899faaff7e5ac702def25f
fetched_at: '2026-06-28T21:35:19.134088+00:00'
page_id: '192092531'
product: fluig
source: tdn-fluig
title: Eventos de Componentes
type: documentation
url: https://tdn.totvs.com/display/fluig/Eventos+de+Componentes
version: 18
---

No desenvolvimento de um *widget* para o Fluig Plataforma é possível programar certas ações a serem executadas em tempo de instalação, ativação ou desativação.

Importante

Esses eventos estão disponíveis desde que se utilize a [Central de Componentes](http://tdn.totvs.com/display/HF/Central+de+componentes) disponível no agrupador **Aplicativos** do **Painel de controle** ou a [Exportação e Importação de Páginas](http://tdn.totvs.com/pages/viewpage.action?pageId=234455771) disponível no agrupador **Personalização** do **Painel de controle**

Para que isso seja possível, é necessário criar uma classe em seu projeto Fluig que [implemente](https://docs.oracle.com/javase/tutorial/java/IandI/usinginterface.html) a classe "com.fluig.sdk.api.component.activation.ActivationListener". É necessário também inserir uma [annotation](https://docs.oracle.com/javase/tutorial/java/annotations/) de mapeamento, que depois deverá ser referenciada no arquivo [application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info).

Veja abaixo um exemplo dessa classe:

javaActivationClass.java

Em seguida, no arquivo [application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info) deve ser criada a propriedade "activation.class", cujo valor deve ser o mesmo da propriedade *"name"* da [annotation](https://docs.oracle.com/javase/tutorial/java/annotations/) da classe de ativação.

Para o exemplo dado acima a propriedade ficaria assim:

bashapplication.info

Além disso, para que seu artefato seja corretamente gerado, é necessário adicionar algumas dependências ao seu projeto. Caso o seu projeto seja do tipo maven.

Utilize o código abaixo:

xmlpom.xml

com.fluig
foundation-security-authentication-saml
provided

javax
javaee-api
provided

com.fluig
wcm-sdk-service
provided

com.fluig
wcm-common
provided

com.fluig
fluig-sdk-common
provided

com.fluig
fluig-sdk-api
provided

com.fluig
wcm-core
jar

com.fluig
ecm-ejb-api
jar

org.json
json
provided



org.apache.maven.plugins
maven-war-plugin

false


org.slf4j, com.fluig.api, com.fluig.api.common

net.alchim31.maven
yuicompressor-maven-plugin



compress

false
true
-1
false
false
false
true
false
]]>Exemplo Completo

Para uma visão mais completa dessa técnica, é possível visualizar um dos *widgets* disponibilizados pela equipe do TOTVS Fluig Plataforma em nosso repositório de [samples](https://git.fluig.com/projects/SAMPLES/repos/widgets/browse), como por exemplo o *widget* de [convênios.](http://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse/wcm/widget/kit_convenios)
