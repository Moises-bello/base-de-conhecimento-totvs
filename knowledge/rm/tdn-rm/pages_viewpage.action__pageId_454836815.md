---
content_hash: 7e42352d1e207b7f9ec955c5bf3ae70274ceae85370dde9cb700dcb7575c1b2f
fetched_at: '2026-06-29T00:10:13.088107+00:00'
page_id: '454836815'
product: rm
source: tdn-rm
title: 4958445 FISCAL01-7877 Tributo Item - Código de receita com tamanhos diferentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454836815
version: 2
---

# Escrituração de Lançamentos Fiscais

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Escrituração |
| **Situação/Requisito:** | Ao realizar o processo de escrituração de movimentos, é apresentado a seguinte mensagem de erro:  Erros no Serviço de Inclusão de Lançamentos  **---------------------------------------------------------------------------------**  **Erro na Inclusão do Registro**:  String or binary data would be truncated.  **---------------------------------------------------------------------------------**  A origem da demanda em questão se refere ao campo CÓDIGO DA RECEITA para o tributo INSS. O RM Nucleus permite o código da receita com 10 caracteres, sendo que este mesmo campo no RM Liber é apenas 6 caracteres. O código da receita é preenchido no cadastro do cliente/fornecedor, anexos, Defaults de cli/for, abra Outros Dados, que preenche automaticamente no movimento, nos tributos do item de movimento, campo Código de Retenção do Imposto.  Em uma pré análise da equipe de atendimento, o RM Nucleus deveria limitar o preenchimento destes campos com 6 dígitos. |
| **Solução/Implementação:** | Foi alterado no banco o tamanho do campo Código da Receita de 6 para 10 e o “MaxLength” deste campo no formulário de tributo do Item.  Observação: Alteração disponível a partir da versão 12.1.24 |
