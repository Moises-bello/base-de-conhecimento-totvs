---
content_hash: 58dbeede8bc219e706b41386b7872431b483b892621ffb8cc4fa3b3f1d53bcd9
fetched_at: '2026-06-29T00:10:44.991964+00:00'
page_id: '553338449'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Documento Técnico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553338449
version: 1
---

5%90%10%100%

### **DOCUMENTO TÉCNICO (NOVA VERSÃO - REVITALIZAÇÃO DO TDN)**

No processo de desenvolvimento ágil, temos um artefato de documentação que precisa ser produzido: **Documento Técnico,** este é um artefato para documentar novas implementações, melhorias e correções importantes de cada requisito ou ticket, seja ele para versões de *Roadmap* ou versões distintas.

**Artefato obrigatório na entrega do produto pronto;**

**Pode ser elaborado em qualquer etapa do Processo de Desenvolvimento Ágil.**

Para criação deste documento, você precisar estar logado no **TDN (TOTVS Developer Network)** e na *space* do seu Produto.

O template pode ser encontrado a partir do botão  e o documento está identificado como "**Documento Técnico (New)**".

---

#### **Campos do documento e como preencher cada um deles:**

falsetruefalsetrue1documento\_tecnicofalse1100autohidden871

10%70%

Os campos **01. DADOS GERAIS**, **02. SITUAÇÃO/REQUISITO** e **03. SOLUÇÃO** são **obrigatórios**.

Os campos **04. DEMAIS INFORMAÇÕES** e **05. ASSUNTOS RELACIONADOS** são **opcionais**, fica a critério do documentador, pois são informações que não impactam o entendimento do documento.

No item **01. DADOS GERAIS**, foi adicionado o campo **Produto** com as macros *Soluções TOTVS*, *Soluções Cross*, *Soluções Parceiros* e *Solução Parceiros Expedidas TOTVS*. Essas macros contêm os nomes dos produtos de acordo com o **[Guia de Nomenclatura de Produtos](https://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=8803843)**. Você deve preencher escolher uma das macros e selecionar o produto em apenas uma delas, as outras devem permanecer em branco, sem preenchimento, assim elas não aparecem no documento publicado.

No item **01. DADOS GERAIS**, o campo **Linha de Produto** com a macro *Linhas TOTVS* contêm os nomes das linhas de produtos de acordo com o **[Guia de Nomenclatura de Produtos](https://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=8803843)**. Caso não seja aplicável para o seu Produto, selecione a opção "**-**".

No item **03. SOLUÇÃO**, há um modelo de passo a passo com a macro *TOTVS CUSTOM TABS BOX*. Esse modelo foi desenvolvido para padronizar a apresentação de passo a passo para exemplificar funcionalidade mais complexas. Caso não for utilizar, pode ser excluída a macro e utilizar apenas a descrição da solução.

No item **04. DEMAIS INFORMAÇÕES**, há um modelo para box **IMPORTANTE**. Ele é muito útil para evidenciar alguma informação que o cliente deve se atentar. Caso não seja necessário, pode ser excluído.

---

#### **Regras para título do Documento Técnico (título da página):**

Documento técnico para novas implementações:

Quando o documento técnico for elaborado para uma réplica, deve ser informada a versão.

Em casos de localizações: inserir a sigla do país.

***Exemplos:***

DT Fatura Eletrônica (sem localização)

DT Fatura Eletrônica ARG (com localização)

Documento técnico para correções ou melhorias:

Quando tratar-se de uma *issue* interna, não se deve informar o número do *ticket*.

Em casos de localizações: inserir a sigla do país.

***Exemplos:***

122828 MRH-631 DT Erro Integração SAP (*Issue* Externa, sem localização)

MRH-631 DT Erro Integração SAP (*Issue* Interna, sem localização)

---

#### **Labels (tags/rótulos):**

As *tags* têm duas funções muito importantes para os documentos no TDN:

Garantir o funcionamento do *workflow* de aprovação das páginas, cujo fluxo é determinado pelas *tags* de artefato;

São utilizadas no mecanismo de busca da Central de Ajuda;

A utilização de *labels* é **obrigatório**, mas caso queira utilizar outras *labels* que possam facilitar a busca de páginas, é permitido, desde que sigam os padrões de construção de *labels* obrigatórias.

Para construí-las, é preciso seguir algumas regras:

Use apenas letras minúsculas;

Utilize \_ entre as palavras;

Não utilize caracteres especiais;

Não acentue as palavras;

Não insira espaços entre palavras.

| LABEL | EXEMPLOS |
| --- | --- |
| Artefato\*  Disponibilizada nos templates | documento\_tecnico  base\_de\_conhecimento |
| Segmento | manufatura  construcao\_e\_projetos  totvs\_logistica\_recintos\_aduaneiros   Conforme **[Guia de Nomenclatura de Produtos](https://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=8803843)**  ***Importante:*** Manter a nomenclatura antiga, a nova e variações do nome para facilitar a localização do conteúdo. |
| Módulo | sigagpe, sigacom |
| Versão/Release | versao\_12\_1\_17  versao\_11\_80 |
| Entrada (programa) do menu (rotina/action) | mata010  ctbcontaaction |
| País | todos\_paises  bra |
| *Squad*  (apenas nas *spaces* RM, Protheus, SARA, Logix e Datasul) | sp\_guild-protheus\_sj\_totvs\_saude\_engenharia\_pls |

**Importante:** Documentos que não possuem entrada de menu (por exemplo, *mobile*), não precisam da *tag* de rotina. Já os documentos que possuem mais de uma entrada de menu (por exemplo, documentos de integração), colocar uma *label* para cada rotina descrita no documento.

**[Instrução de Trabalho | Boas Práticas de Documentação](https://tdn.totvs.com/x/nASlGw)**

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
