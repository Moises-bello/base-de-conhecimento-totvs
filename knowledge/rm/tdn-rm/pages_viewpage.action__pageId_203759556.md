---
content_hash: 5e7c7152ed4cf36d496d2f96ebc3ec381a38400f531c2e997d74ee61ac38a1b9
fetched_at: '2026-06-29T00:06:10.255278+00:00'
page_id: '203759556'
product: rm
source: tdn-rm
title: ER_Melhorias na Importação /Exportação de Movimentos e Produtos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203759556
version: 8
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Gestão de Estoque, Compras e Faturamento | **Módulo** | Integração |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_C&P\_MOV006 | **IRM1** | * [PCREQ-2235](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-2235 "PCREQ-2235") |
| **Requisito1** | * [PCREQ-7757](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7757 "PCREQ-7757") | **Subtarefa1** | 1. [PDR\_CP\_MOV008-60](http://jira.totvs.com.br/browse/PDR_CP_MOV008-60) |
| **Chamado2** | N/A | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Implementar melhorias identificadas nos arquivos de conceito de Importação / Exportação de Movimentos e  Importação / Exportação de produtos liberados na 12.1.4.

### (Obrigatório)

## Definição da Regra de Negócio

 

1. As informações sobre a formatação padrão dos campos contidos nos arquivos para importação será a mesma definida para a exportação podendo ser verificada através da edição do Gerador de Saídas pela opção “Gerar Documentação”.

   Por exemplo como deve ser feito o preenchimento dos campos quando a informação não ocupar todo o espaço a ela reservado por tipo de campo ou preencher com 0(zeros) a esquerda para campos do tipo INT.
2. A exportação / importação da contabilidade do movimento foi disponibilizado na versão release 12.1.6.
3. Os arquivos de Conceito serão atualizados para que a mensagem  “Cliente/Fornecedor identificado pelo CGCCFO” seja a seguinte: “Cliente/Fornecedor identificado pelo CNPJ/CPF”.
4. O campo DTCADASTRO, da tabela TPRDCODIGO nos layouts de exportação de produtos não será importado, sendo este desconsiderado na importação mesmo que estiver informado no arquivo, pois o mesmo é setado automaticamente com a data do sistema na inclusão. Na exportação não haverá alterações e o campo ainda será exportado mantendo assim o legado no layout.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
