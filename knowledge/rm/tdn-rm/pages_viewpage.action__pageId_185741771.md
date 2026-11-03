---
content_hash: 5f5a5b437872c0a1b4d728f0ae02868a2b6336528199ca75900c5537b40d65c5
fetched_at: '2026-06-29T00:05:58.165772+00:00'
page_id: '185741771'
product: rm
source: tdn-rm
title: O relatório não está parametrizado para ser executado através de JobServer
  - Totvs Gestão de Estoque, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185741771
version: 4
---

|  |  |
| --- | --- |
| Produto | RM |
| Versões | 11.52 ou superior |
| Sintoma | "Erro na execução do relatório: O relatório não está parametrizado para ser executado através de JobServer.  Para que esse relatório seja executado no ambiente .Net é necessário que esteja parametrizado para ser executado através de JobServer (3 camadas).    Se tiver dúvidas sobre como efetuar essa parametrização entre em contato com o suporte. "  ou  "Erro na execução do relatório: Violação de chave estrangeira" |
| Causa | Os relatórios impressos na Nova MDI agora são gerados pelo servidor de JobServer e não mais por BDE. Se a impressão for realizada pelo modelo antigo funcionará, mas se for pelo modelo novo, a mensagem será arpesentada. |
| Solução | - Acessar o RM Nucleus | Menu Relatórios | Gerador  - Localize o relatório em questão  - Selecione o relatório e clique no botão "Editar" (Não dê duplo click pois abrirá uma página diferente)  - Localizado a direita da tela existem 3 flags ("Visível a todas as Coligadas", "Executa em Job Server" e "Executa em BDE")  - Desmarque a opção "Executa em BDE" (se estiver marcada)  - Marque a opção "Executa em JobServer"  - Salve o relatório |
