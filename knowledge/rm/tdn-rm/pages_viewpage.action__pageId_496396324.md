---
content_hash: b72ec1ce3816ac19145bfa19d72ad23a907a0998a40d936d68ff236240689363
fetched_at: '2026-06-29T00:10:22.087125+00:00'
page_id: '496396324'
product: rm
source: tdn-rm
title: 5475008 FOPROTINAS01-8359 DT - Integração TOTVS Folha pagto RM x Outros Backoffices
  (Autônomos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496396324
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Recursos Humanos |
| Módulo: | Folha de Pagamento |
| Função: | Integração |
| Ticket: | 5475008 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FOPROTINAS01-8359 |

## **02. SITUAÇÃO/REQUISITO**

Mesmo com a integração configurada corretamente e os de-para cadastrados de forma adequada, era exibida a mensagem "Coligada no RM não foi mapeada para a Empresa - <código>".

## **03. SOLUÇÃO**

Foi realizado ajuste no source code do *adapter* da entidade EXTERNALAUTONOMOUSPAYMENT versão 1.002 para compor a chave de busca do de-para de filial de acordo com o *backoffice* integrado. Assim, quando o *backoffice* for o Protheus, a chave de busca será apenas o conteúdo do campo CompanyInternalId, que já contém uma concatenação dos códigos da coligada e da filial. Entretanto, para os outros *backoffices*, a regra padrão continua valendo: será feita a concatenação dos valores do campo CompanyInternalId e BranchId, separados pelo caractere '|'.

Caso a integração TOTVS Folha pagto RM x Outros Backoffices (Autônomos) já tenha sido configurada, é necessário reconfigurá-la para que essa alteração tenha efeito. Para isso, basta seguir o passo a passo abaixo:

Passo 01, Passo 02, Passo 03, Passo 04passo1,passo2,passo3,passo4yespasso1

**Apagar o código fonte da mensagem EXTERNALAUTONOMOUSPAYMENT:**

1. Acessar o módulo Integração e ir em Integração \ Mensagem Única \ Integrações \ Anexo Mapeamento de Entidades
2. Selecionar a integração TOTVS Folha pagto RM x Outros Backoffices (Autônomos) na visão
3. No anexo, selecionar o registro com TransactionId "EXTERNALAUTONOMOUSPAYMENT"
4. Editar o registro, no campo Evento acessar o link "Autônomos Adapter" e na janela de "Cadastro de códigos fontes", clicar em Excluir
5. Confirmar a exclusão

nopasso2

**Apagar o mapeamento da mensagem EXTERNALAUTONOMOUSPAYMENT:**

1. Selecionar a integração TOTVS Folha pagto RM x Outros Backoffices (Autônomos) na visão
2. No anexo, marcar o registro com TransactionId "EXTERNALAUTONOMOUSPAYMENT"
3. Clicar em Excluir
4. Confirmar a exclusão

nopasso3

**Executar o Configurador de Integração TOTVS Folha pagto RM x Outros Backoffices (Autônomos):**

1. No módulo Integração acessar Ferramentas \ Ferramentas \ Configurar
2. Avance um passo no assistente e faça login utilizando usuário e senha de acesso ao RM
3. Teste a conexão e avance mais um passo
4. Execute o configurador da integração TOTVS Folha pagto RM x Outros Backoffices (Autônomos)

nopasso4

**Confira se o mapeamento e o respectivo source code da mensagem EXTERNALAUTONOMOUSPAYMENT foram configurados e compile o source code:**

1. Após a execução do processo, clicar em OK na mensagem que instrui a conferir os parâmetros da integração
2. Fechar o assistente de execução do processo
3. Atualizar a visão do anexo de Mapeamento de Entidades
4. Editar o registro com TransactionId "EXTERNALAUTONOMOUSPAYMENT" e clicar no link do source code
5. Clicar em Editor C#
6. Clicar em Build e aguardar a mensagem "Build Succeeded" aparecer no rodapé
7. Clicar em OK
8. Salvar o registro e fechar as janelas abertas
9. Conferir os demais parâmetros da integração

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
