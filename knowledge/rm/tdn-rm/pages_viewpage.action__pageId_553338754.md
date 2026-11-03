---
content_hash: 1945144eb7cdc4c059619744fdd43ca9462a85301e72e0f541fd8f4e601c32ee
fetched_at: '2026-06-29T00:10:45.501185+00:00'
page_id: '553338754'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Como realizar integração de produtos parceiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338754
version: 1
---

5%90%10%100%

O processo de desenvolvimento das integrações de produtos de terceiros com a TOTVS deve ser feito exclusivamente através do consumo de serviços disponibilizados para este fim. Por motivo de segurança e para garantir a qualidade da informação imputada no sistema, é terminantemente proibida o acesso direto a tabelas de banco de dados.

Para consultar os serviços disponibilizados pelos produtos TOTVS, consulte **[API TOTVS](https://api.totvs.com.br/)** ou a FAQ abaixo.

#FF8000#FFF8DCsolid

**FAQ:**

A TOTVS é uma provedora de serviços de negócio em escala mundial e por este motivo, diversas empresas e staturps desejam integrar suas soluções aos produtos TOTVS, bem como complementá-los de forma a gerar valor para o cliente.

Pensando nisto, disponibilizamos a desenvolvedores externos uma plataforma de serviços estruturada e padronizada que permite interagir de forma segura com os produtos  TOTVS. Para saber mais, acesse **[API TOTVS](https://api.totvs.com.br/)**.

A plataforma TOTVS consiste na documentação de serviços disponibilizados através de APIS REST com o conteúdo no formato JSON. Cada API disponibilizada atende a um processo de negócio especifico e portanto, o conteúdo varia de acordo com o negócio, todavia, ainda assim padronizamos a forma e recursos disponibilizados de forma a adiantar o processo de aprendizagem e uso.

       Quais recursos foram padronizados? Vários, entre eles destacamos:

**1) Conteúdo no formato JSON.**

A exceção são as APIs que atendem a legislações que exigem o formato xml. Além disso, o retorno da api pode ser unitário e neste caso o formato será parecido com o abaixo*:*

false

*GET http://[totvs.com.br/api/fluig/fdn/v1/users/1](http://totvs.com.br/api/fluig/fdn/v1/users/1)*

*{*

*name: "John",*

*surname: "Doe"*

*}*

No caso de retorno de múltiplos registros, o retorno será parecido com o abaixo

false

*{*

*hasNext: **true**,*

*items: [*

*{*

*name: "John",*

*surname: "Doe"*

*},*

*{*

*name: "Elvis",*

*surname: "Brito"*

*},*

*...*

*]*

*}*

**2) Pensando em múltiplos registros, posso ordenar o retorno?**

Sim, basta utilizar o designador order precedendo o(s) nome(s) dos campo(s)

false

GET **<https://totvs.com.br/api/fluig/fdn/v1/users?order=name,-age,surname>**

**3) E filtrar?**

Sim, o filtro pode ser feito utilizando o nome do campo=valor ou utilizando o filtro no padrão o Data (opcional). Devido a performance, nem todos os campos permitem filtro, consulte a documentação da API para saber quais campos podem ser filtrados **[API TOTVS](https://api.totvs.com.br/)**.

Estes são apenas alguns recursos, para a listagem completa consulte **[Guia de Implementação das IPIs](https://tdn.totvs.com/x/nDUxE)** e surpreenda-se!

**E o que fazer se não encontrar a API (serviço) que retorne o que preciso?**

Neste caso você deve abrir um ticket para a equipe de produto responsável detalhando a necessidade.

**Ok, abrirei o ticket, mas enquanto isto posso fazer acesso direto a base de dados para retornar ou alterar uma informação?**

Não. APIs foram desenvolvidas para manter perene a assinatura. Assim, se você fizer a leitura direta a base de dados, é provável que tenha problemas nas atualizações de versões em virtude de alteração no dicionário de dados. Além disto, para garantir a qualidade do dado imputado dentro do sistema, é terminantemente proibido gravar qualquer informação diretamente na base de dados sem passar pela API.

Para qualquer dúvida, consulte o fórum de API no [**Ryver**.](https://totvs.ryver.com/index.html#forums/1230269.)

5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
