---
article_id: 6744161821335
category: Gestão de Distribuição (SIGAOMS)
content_hash: 0e639d0461da696ceb4cf4a48bd9a15e66b97516ff2efec7c43dfba536f9525a
fetched_at: '2026-06-28T22:45:49.533273+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Associação dos Códigos de Clientes e Códigos
  Operadores Logísticos - DLGA270
type: support-article
updated_at: '2022-07-12T20:55:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6744161821335-Log%C3%ADstica-Linha-Protheus-OMS-Associa%C3%A7%C3%A3o-dos-C%C3%B3digos-de-Clientes-e-C%C3%B3digos-Operadores-Log%C3%ADsticos-DLGA270
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:12 min** **Dúvida**Como utilizar o cadastro de **Associação ao Código do Operador Logístico - DLGA270**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Quando se utiliza os Ambientes de Logística em modo de **Operador Logístico**, todo o cadastramento de **Clientes** deverá ser submetido a aprovação da **Filial do Operador Logístico**.  
  
A rotina **Associação ao Código do Operador Logístico - DLGA270** poderá ser acessada somente quando o Sistema estiver com a seguinte parametrização:

* **MV\_APDLFOP**: a utilização dos Ambientes de Logística, em modo de **Operador Logístico**, deve estar ativa.
* A Filial do Operador Logístico - Centralizadora em uso, deve ser a mesma da definida no parâmetro **MV\_APDLOPE**.
* A inclusão de um **Código de Operador Logístico** é efetuada por meio da rotina de **Cadastro de Clientes** quando o parâmetro de **Operador Logístico** estiver ativo. Assim, esta rotina permite somente a **alteração** e **visualização pela Filial do Operador Logístico.**

**Exemplo:**Filial do Operador Logístico - Centralizadora: **01**   
Filial - Não Centralizadora: **02**

* Por intermédio do **Cadastro de Cliente - MATA030**, um usuário logado na **Filial 02** efetua o cadastro de um cliente com o código **JOIN01**
* O cadastro efetuado é registrado na tabela **DCK - Código Cliente x Operador Logístico** e poderá ser utilizado somente depois de aprovado pela **Filial 01**.
* O **Operador Logístico** pode, inclusive, alterar o código digitado, sugerindo um novo código para impedir que existam códigos repetidos entre as diversas Filiais do Sistema.
* Com este cadastro evita-se que existam vários cadastros repetidos para o mesmo cliente na base de dados.
* Na **Filial** **01**, apresentará o cadastro do cliente  no cadastro **DLGA270** com o código **JOIN01**
* Ao incluir **Pedidos de Venda - MATA410** para cliente **JOIN01**, caso desejar que os **Pedidos de Venda** sejam visualizados somente na **Filial 02**, no cadastro **DLGA270,** os campos **Cod Cliente - DCK\_CODOPL** e **Loja Cliente - DCK\_LOJOPL** não deverão ser preenchidos.
* A funcionalidade do cadastro **DLGA270** poderá ser utilizada para **restringir** ou **bloquear** os **Pedidos de Venda** do cliente **JOIN01,** para que sejam **criadas as Cargas somente na Filial 02**.
* Para que os **Pedidos de Venda** do cliente **JOIN01** criados na **Filial 02**, sejam apresentados na rotina de **Montagem de Carga - OMSA200** da **Filial 01**, terá que ocorrer a aprovação do cadastro **DLGA270** do cliente **JOIN01**, preenchendo os campos **Cod Cliente -** **DCK\_CODOPL** e **Loja Cliente - DCK\_LOJOPL.** Dessa forma, os **Pedidos de venda** do cliente **JOIN01** serão considerados na **Montagem de Carga Filial 01**.

**Saiba mais**Mais informações poderão ser acessadas nos *links*:  
[Códigos Clientes x Códigos Operadores Logísticos - DLGA270](https://tdn.totvs.com/pages/viewpage.action?pageId=572227579)  
[Logística - Linha Protheus - OMS - Montagem de carga compartilhada com pedidos de múltiplas filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027375872-Log%C3%ADstica-Linha-Protheus-OMS-Montagem-de-carga-compartilhada-com-pedidos-de-m%C3%BAltiplas-filiais)
