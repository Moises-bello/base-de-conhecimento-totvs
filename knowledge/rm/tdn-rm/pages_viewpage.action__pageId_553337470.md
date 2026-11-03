---
content_hash: 4bd2875db0c6d07c7e855552ece38d45ce20eb83629d3c406b3013fe2d53c463
fetched_at: '2026-06-29T00:10:44.704544+00:00'
page_id: '553337470'
product: rm
source: tdn-rm
title: Rascunhos04. Processo Desenvolvimento Ágil | Documentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553337470
version: 1
---

5%90%

Na atividade de Documentação devem ser gerados os documentos necessários para o produto, de forma que o cliente possa instalá-lo, entender a sua forma de utilização e conhecer as novidades do *release*.

#2E2E2E#F4F7F71dashed

 **DOCUMENTAÇÃO OBRIGATÓRIA**

**Documentação - Desenvolvimento Padrão**

5%95%

**Documento Técnico:** utilizado para documentar as novas implementações, melhorias e correções importantes de cada requisito, seja ele para versões de *roadmap* ou distintas. Estão disponíveis em dois modelos de *templates* **Documento Técnico Estendido** e **Documento Técnico Simplificado**.

* Em alguns casos, não é necessária a criação do Documento Técnico. São eles:
  + Itens agrupados por afinidade (itens com o mesmo assunto podem ser agrupados e gerar-se uma única documentação. É importante que seja mantida a rastreabilidade de onde essa documentação foi elaborada);
  + Ajuste em acentuação/correção ortográfica no sistema;
  + Programas de Acerto de Base;
  + *Issues* que foram registrados durante Teste Sistêmico.
* **Linha RM:** É utilizada uma automação via robô de expedição para geração do release notes de manutenções em substituição ao Documento Técnico, onde é documentado de forma automatizada o que foi liberado na ***Release** por *****Patch***** e por ****Produto*****. *(Ex.: )*.

  + Informações que devem ser apresentadas ao cliente: a rotina ajustada, o *ticket* e a *issue* relacionada, o texto de descrição do *check-in* no TFS e os arquivos que foram modificados;
  + Importante que algum membro da equipe fique responsável por receber a notificação de criação das páginas quando o robô expedir, para que este fique responsável por auditar uma amostra das páginas criadas e publicá-las, para que as tornem visíveis aos clientes.

**Quando elaborar o Documento Técnico?**

* + Pode ser elaborado em qualquer etapa do processo;
  + Obrigatório na entrega do produto pronto;
  + Documenta novas implementações, melhorias e correções importantes;
  + Cada requisito ou ticket deve ter o seu Documento Técnico.[**Instrução de Trabalho - Documento Técnico**](http://tdn.totvs.com/pages/viewpage.action?pageId=461921735)  
  [**Instrução de Trabalho - Boas Práticas de Documentação**](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)
* [**Instrução de Trabalho - Estrutura de Pastas (Documentação)**](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)

**Documento de Referência:** apresenta os principais procedimentos realizados nos produtos TOTVS, com o objetivo de orientar o cliente na execução das suas rotinas diárias. É   
composto pela ambientação, que expõe os itens de uso geral em todo o produto e as demais pastas que correspondem ao módulo, com um documento para cada programa. **Este artefato deve ser gerado ou revisado de acordo com a necessidade.**

**Quando elaborar o Documento de Referência?**

* + Pode ser elaborado em qualquer etapa do processo;
  + Obrigatório na entrega do produto pronto;
  + Contém os principais procedimentos realizados, com o objetivo de orientar o cliente na execução das suas rotinas diárias;
  + Deve ser atualizado sempre que uma inovação/manutenção modifique a rotina.[**Instrução de Trabalho - Documento de Referência**](http://tdn.totvs.com/pages/viewpage.action?pageId=463798640)
* [**Instrução de Trabalho - Boas Práticas de Documentação**](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)
* [**Instrução de Trabalho - Estrutura de Pastas (Documentação)**](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)

---

**Documentação - Desenvolvimento Mobile**

5%95%

**Guia de uso:** No desenvolvimento Mobile as informações do Documento Técnico e de Referência podem estar documentadas em um único documento, **o Guia de Uso**, que deverá conter informações técnicas e dados de configuração, para que o cliente consiga instalar e utilizar o aplicativo.

**Política de Privacidade:** Para publicação de um aplicativo é preciso respeitar os itens definidos como obrigatórios pelas *stores* (**[Google Play](https://play.google.com/intl/pt-BR/about/privacy-security-deception/)**/**[App Store](https://www.apple.com/legal/privacy/br/)**) e também utilizar a versão da Política de Privacidade em vigência, que previamente foi validada pela área Jurídica da TOTVS. **[Template Política de Privacidade](https://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=6749851)**

Qualquer informação atrelada ao conteúdo do aplicativo precisa estar de acordo com a Política de privacidade, a versão disponibilizada pelo Jurídico não deve ter o seu conteúdo alterado, caso tenha dúvidas, abra um ticket para: ***[eng.corp.desenv@totvs.com.br](mailto:eng.corp.desenv@totvs.com.br)**.*

*\*Para as equipes que disponibilizam aplicativos no **Portal de Mobilidade** ou semelhante, a Política de Privacidade não é necessária.*

* Instruções específicas para Desenvolvimento Mobile:**[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**
#2E2E2E#FBFBEF1dashed

 **DOCUMENTAÇÃO OPCIONAL**

**Documento de Integração:** Descreve os pré-requisitos para a implantação e utilização de determinado módulo que apresenta integração com um ERP e Parceiros. Este artefato é opcional e deve ser criado por ofertas para os requisitos de integração.   
É elaborado por um integrante do *Dev Team* na atividade **Codificação** em **[Processo de Desenvolvimento Ágil | Desenvolvimento](http://tdn.totvs.com/pages/viewpage.action?pageId=458764626)**. Após elaboração, o documento deve ser submetido à aprovação e, na sequência, enviado para revisão ortográfica.

[**Instrução de Trabalho - Documento de Integração**](http://tdn.totvs.com/pages/viewpage.action?pageId=463798677)

[**Instrução de Trabalho - Boas Práticas de Documentação**](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)

[**Instrução de Trabalho - Estrutura de Pastas (Documentação)**](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)

***Vídeo How To***: são pílulas de conhecimento em formato de vídeo, utilizadas para disseminar os processos TOTVS para área de Atendimento, áreas interessadas e Clientes. Estes vídeos tem duração máxima de 3 minutos, e quando necessário demonstrar processos mais complexos, deve-se gravar vídeos separados, para serem exibidos em sequência no *YouTube*. **Este artefato não é obrigatório. No entanto, pode ser criado para todos os itens de inovação e para manutenções relevantes.** Para acessar o tutorial e artefatos necessários para criar um *How To* pelo Camtasia, acessem o [**link**.](https://fluig.totvs.com/portal/p/10097/ecmnavigation?app_ecm_navigation_doc=6616628)

**[Instrução de Trabalho -](https://tdn.totvs.com/x/dwWlGw)[Como criar Vídeos How to?](https://tdn.totvs.com/x/dwWlGw)**

Se necessário realizar a **tradução** **da documentação**, ver tópico "**Tradução de Documentação de Produto ou Sistêmica**".

0solid

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

27px

## 

560px

**ENTRADA(S):**

* Plano de Entregas
* Detalhamentos dos itens de *backlog*
* Subtarefas
* Impedimentos
* Defeitos
* Ambiente de teste disponível
* Fonte alterado e testado
* Dicionário de Dados / Telas criadas / atualizados e traduzidos
* Evidência(s) do Teste de Unidade
* Evidência(s) do Teste Integrado
* Evidência(s) da Correção do Defeito (quando necessário)
* **[Instrução de Trabalho - Documento Técnico](http://tdn.totvs.com/pages/viewpage.action?pageId=461921735)**
* **[Instrução de Trabalho - Boas Práticas de Documentação](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)**
* **[Instrução de Trabalho - Estrutura de Pastas (Documentação)](http://tdn.totvs.com/pages/viewpage.action?pageId=463799452)**
* **[Instrução de Trabalho - Documento de Referência](http://tdn.totvs.com/pages/viewpage.action?pageId=463798640)**
* **[Instrução de Trabalho - Documento de Integração](http://tdn.totvs.com/pages/viewpage.action?pageId=463798677)**
* **[Instrução de Trabalho - Como Criar Vídeos HowTo?](http://tdn.totvs.com/pages/viewpage.action?pageId=463799671)**
* **[Instrução de Trabalho - Plugin Scroll PDF](http://tdn.totvs.com/pages/viewpage.action?pageId=463799477)**
* **[Instrução de Trabalho - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=384584643)**
27px220px

**ENVOLVIDO(S):**

* ***[Dev Team](http://tdn.totvs.com/pages/viewpage.action?pageId=274834451) \****
23px250px

**SAÍDA(S):**

* Documento Técnico elaborado
* Documento de Referência elaborado (quando necessário)
* *How To*elaborado (opcional)
* *Task Board*atualizado
* Indicadores Operacionais atualizados

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

***\* Obrigatório***

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
font-size: 15px !important;
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
hr {
border-bottom: 1px solid #FF8000;
}
]]>
