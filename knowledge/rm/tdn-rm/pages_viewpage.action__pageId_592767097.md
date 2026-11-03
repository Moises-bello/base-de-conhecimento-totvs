---
content_hash: e1f6f6491901544dd60f6f9e9149e394b39f2dd4f9c983459367d7dc8a59a24f
fetched_at: '2026-06-29T00:10:56.758276+00:00'
page_id: '592767097'
product: rm
source: tdn-rm
title: DT- Segurança Dataserver - webservice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592767097
version: 19
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | Segurança dataserver |
| País: | Brasil |
| Ticket: | 10668324 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FOPCALCULO01-12663](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-12663) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar uma chamadas webservice (ReadView, ReadRecord, DeleteRecord e SaveRecord) nos DataServers, mesmo o funcionário tendo acesso apenas a uma coligada, estava sendo retornado informações das demais coligadas.

## **03. SOLUÇÃO**

A restrição de acesso a uma coligada se dá por duas estratégia, por coligada ou por subordinação

**Por coligada:** Se dá quando a tabela master do DataServer possui o campo de vínculo com a coligada, mas não possui vínculo direto com o funcionário, ou seja, não possui campos relativos à CHAPA.

**Por subordinação:** Se dá quando a tabela master do DataServer possui vínculo direto com funcionário, tendo o campo relativo à CHAPA. O usuário terá acesso aos seus subordinados que é chefe e ou aos funcionários que está diretamente vinculado.

Os DataServer via WebServer passam a estar restritos as coligadas que o usuário tem acesso. Veja [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=545647849) os DatasServers que atendem as regras de restrição.

Para efetuar a restrição de coligada, via webservice a opção de perfil "Desconsiderar filtro de produto em WebService" deverá estar desmarcada e o usuário para webservice deverá ser um chefe na seção raiz do cadastro de Chefe/Supervisor.

Para o correto funcionamento da restrição, o usuário deverá marcar o parâmetro 'Valida regras via Web Service', disponível em **RM | RH | Folha de pagamento | Configurações | Parametrizador | Funcionário | Restrições Cadastrais**, conforme imagem abaixo:

**Parâmetro 'Marcado'**

O sistema irá considerar as regras de restrição de acesso a uma coligada, conforme uma das duas estratégias, por coligada ou por subordinação.

**Parâmetro 'Desmarcado'**

Não serão consideradas as regras de restrição de acesso por coligada ou por subordinação, deixando a restrição de acesso a critério do cliente.

**Observações:**

O sistema irá apresentar as mesmas validações de campos obrigatórios da interface nas chamadas cliente ou servidor dos dataserver observando as regras de validações.

O sistema irá exibir alerta de confirmação para permitir o cadastramento de férias mesmo sem período aquisitivo pela interface, mas pela chamada do serviço do datasever (FopFuFeriasPerData) não será realizada devido já que existem empresas que podem trabalhar com cenários distintos (permitindo férias somente com o período aquisitivo ou permitindo férias independente do período aquisitivo completado). Será importante que a interface do sistema que consome nossos serviços seja adequada para exibir o mesmo tipo de confirmação. A regra no caso fica a critério de quem está realizando a chamada via servidor.

O sistema irá exibir um um alerta de data de nascimento maior que a data de admissão pela interface do produto. Ajustado nas chamadas via cliente e servidor apresentar a regra de validação de data de nascimento maior que a admissão.

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2yespasso1

O usuário não deverá ter permissão de acesso ao perfil  "Desconsiderar filtro de produto em WebService", ou seja, opção desmarcada.

nopasso2

O usuário deverá ser chefe ou chefe externo (cadastro Chefe/Supervisor) na seção raiz da coligada que deseja acesso.

## **04. ASSUNTOS RELACIONADOS**

* [Exemplo de utilização de dataserver via webserver](https://tdn.totvs.com/pages/releaseview.action?pageId=545647849)
* [Serviços Via WebService](https://tdn.totvs.com.br/pages/viewpage.action?pageId=425459227)

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
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
