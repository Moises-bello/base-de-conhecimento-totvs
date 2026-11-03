---
content_hash: 3bd9a10653f0bd95da8c9c975cbf13ba0ad27103ae64eee393f67e9dd9157330
fetched_at: '2026-06-29T00:08:34.299753+00:00'
page_id: '274659352'
product: rm
source: tdn-rm
title: RSP0002_Produto_Nao_Exibido_no_Ressuprimento
type: documentation
url: https://tdn.totvs.com/display/LRM/RSP0002_Produto_Nao_Exibido_no_Ressuprimento
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Produtos não são apresentados no “Processo” e na “Analise” do Ressuprimento. |
| **Ambiente:** | Ressuprimento |
| **Passo a passo:** | Ao realizar o "Processo" e a "Análise" do Ressuprimento, determinado produto não é exibido. CAUSA 1 - O Produto não é de último nível;  2 - O Produto está Inativo;  3 - Não existe “Informações de Estoque” para o produto compatível com o Nível de Gestão parametrizado;  4 - O Tipo de Aplicação não esta informada no cadastro de produto;  5 - O Tipo de Aplicação informado no produto esta com a opção “Usa Gestão de Materiais” desmarcada.   SOLUÇÃO 1 - Se o produto estiver como Inativo, verificar se realmente irá ser utilizado no Ressuprimento e habilitá-lo se for o caso;  2 - Se o produto não for de último nível, verificar se realmente irá ser utilizado no Ressuprimento e colocar o mesmo para ser de último nível;  3 - No cadastro do produto, Anexo, Informações de Estoque, deverá cadastrar conforme necessidade da empresa;  4 - Informar um Tipo de Aplicação dentro do(s) produto(s) correspondente(s);  5 - Marcar a opção “Usa Gestão de Materiais” do Tipo de Aplicação amarrado ao produto ou então alterar o tipo de aplicação do produto para um que tenha a opção marcada. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
