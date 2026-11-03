---
content_hash: 60469ca500cd9d18ba47adc282dfab2466187055ce167acedb8de0c79ee50a94
fetched_at: '2026-06-29T00:10:22.648780+00:00'
page_id: '498448040'
product: rm
source: tdn-rm
title: 5093389 DEDUINTEGRACOES-4608 DT Desconsiderar serviço na geração de NF-e por
  competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498448040
version: 7
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS  Educacional |
| Função: | Geração de movimento (NF-e) |
| Ticket: | 5093389 |
| Requisito/Story/Issue (informe o requisito relacionado) : |  |

## **02. SITUAÇÃO/REQUISITO**

Para os cenários em que o Educacional está parametrizado para gerar movimento (NF-e) no regime de competência não é possível gerar para alguns serviços movimento(NF-e) no regime de caixa, exceto quando a parcela seja do tipo “Parcela Extra”.

Alguns cenários o cliente deseja, por exemplo, que para o serviço de matricula a NF-e seja gerado no regime de caixa e não seja considerada no processamento da NF-e no regime de competência.

## **03. SOLUÇÃO**

Realizamos uma melhoria no Educacional para que seja possível identificar os serviços que devem ser desconsiderados na geração de movimento no regime de competência, e consequentemente as parcelas destes serviços possam posteriormente ser processadas na geração de movimento no regime de caixa.

Foi disponibilizado no cadastro de serviço a opção "Desconsiderar na geração de NF-e por competência".

Quando esta opção estiver marcada ao gerar o movimento no regime de competência o sistema não vai considerar as parcelas cujo o serviço esteja com esta opção marcada.  
  
Se ao marcar a opção "Desconsiderar na geração de NF-e por competência" e o sistema identificar que já existem movimentos gerados considerando estes serviço será apresentada a mensagem de observação abaixo.

Depois que a opção "Desconsiderar na geração de NF-e por competência" estiver marcada serão consideradas as seguintes regras:

* Será possível gerar o movimento no regime de caixa para a parcela correspondente ao serviço parametrizado, mesmo a parcela não sendo do tipo “Parcela Extra”.
* Se houver movimentos gerados no regime de caixa para parcelas desse serviço, não será possível desmarcar a opção ao editar o cadastro do serviço.
* **Agrupamento de Boleto:**Quando for gerado um movimento no regime de caixa para um boleto agrupado, será considerado no movimento somente as parcelas do serviço que estiver com a opção "Desconsiderar na geração de NF-e por competência" marcada, as demais parcelas do agrupamento serão consideradas na geração de movimento no regime de competência.

É importante ressaltar que para o contrato que tiver parcelas do serviço parametrizado, e este serviço já foi processado anteriormente em um movimento gerado no regime de competência (provavelmente ocorreu antes de marcar a opção “Desconsiderar na geração de NF-e por competência”) não será possível gerar o movimento no regime de caixa para a parcela do contrato em questão, neste caso a geração de movimento no regime de caixa para as parcelas com este serviço será possível somente para contratos criados após a habilitação da opção “Desconsiderar na geração de NF-e por competência” no serviço.

Este recurso está disponível oficialmente a partir da versão 12.1.26, porem poderá ser habilitado a partir da versão 12.1.23 através da execução do script "CN.2019.01\_02" e "CN.2019.06\_02" que deverão ser solicitados ao suporte.

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
]]>
