---
content_hash: 5d8e7833971fba53a1e61da8e1fe6f7c7014a72517ead634c8d6d49d313c1a07
fetched_at: '2026-06-29T00:06:20.708895+00:00'
page_id: '223152315'
product: rm
source: tdn-rm
title: TSSAXB_Informações_Contexto_Session_EducaMobile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223152315
version: 1
---

# Acesso a informações do Contexto do EducaMobile

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *TOTVS Educacional.* |
| **Módulo:** | **Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Contexto.* | *Contexto do EducaMobile* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Acesso ao Contexto do Aluno e Professor por aplicação externa*.* | *Contexto do Professor e Aluno.* | |  |  | |
| **Cadastros Iniciais:** | *N/A.* |
| **Parâmetro(s):** | *N/A.* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados Relacionados** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | *SQL Server e Oracle.* |
| **Tabelas Utilizadas:** | *N/A.* |
| **Sistema(s) Operacional(is):** | *Windows.* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *12.1.9* |

## Descrição

Foi realizado uma implementação no EducaMobile onde no arquivo Menu.XML do EducaMobile, possa ser cadastrado um novo item de Menu para ser informado um link uma aplicação externa, e seja configurado para que o Contexto seja selecionado pelo aluno ou professor, antes da página ser redirecionada.

Esta alteração força que o contexto seja selecionado antes do redirecionamento, e esta ação preenche as informações do contexto selecionado pelo aluno ou professor em algumas Sessions, no qual podem ser acessadas por aplicações externas, caso estas aplicações também estejam no mesmo diretório virtual no IIS do EducaMobile ou Portal Educacional.

## Procedimento para Utilização

**Exemplo:**

       1.           Editar o arquivo Menu.XML, cadastrando um novo item de Menu com as seguintes TAGs:

```
 <MenuItem>
      <Tag>0</Tag>
      <Caption>Globo Aluno</Caption>
      <Image>Areas/Educacional/Content/images/mn_AppExterna.png</Image>
      <ExternalURL>http://m.aplicacaoexterna.com</ExternalURL>
 <TipoUser>A</TipoUser>
      <SetContext>S</SetContext>
 <Module>S</Module>
    </MenuItem>
```

       2.            Foi criado uma nova TAG chamada "SetContext". Esta TAG especifica se antes do redirecionamento para o endereço especificado na Tag "ExternalURL" será aberto a tela de seleção de contexto.

       3.            Para especificar que o contexto deve ser aberto antes do redirecionamento, a TAG "SetContext" deve conter o valor "S". A tela de seleção de Contexto só será aberta se o aluno ou professor ainda não estiver selecionado nenhum contexto anteriormente, e as variáveis e sessions internas do EducaMobile ainda não estiverem preenchidas.

       4.            Se o valor da TAG SetContexto conter qualquer valor diferente de "S" ou até mesmo não existir, não será exibido a tela de seleção de contexto antes do redirecionamento. Se o contexto do aluno ou professor já tiver sido selecionado antes da utilização deste item de Menu, o contexto não será alterado ou apagado.

       5.            Deverá ser especificado corretamente o Tipo de Usuário através da TAG "TipoUser" como sendo "A" para Aluno e "P" para Professor. O contexto que será exibido para o usuário será baseado nesta informação. Esta Tag é obrigatória conforme os outros itens de Menu.

divs
