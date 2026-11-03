---
content_hash: ced0d480100415ebe57607a16074cd708b291970fb8a8609d7f8ae6432682858
fetched_at: '2026-06-29T00:08:33.031762+00:00'
page_id: '274002636'
product: rm
source: tdn-rm
title: NFSE0008_Substituição_NFS-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274002636
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | NFS-e - Nota Fiscal de Serviço Eletrônica (Municipal) |
| **Versões:** | A partir da 11.40 |
| **Ocorrência:** | Substituição NFS-e |
| **Passo a passo:** | **Introdução:**  Há casos em que o contribuinte necessita simplesmente trocar a NFS-e ainda que válida, mas emitida com algum dado incorreto. Nesses casos, o contribuinte poderá simplesmente substituir a NFS-e emitida com erros por outra NFS-e.  A original será cancelada pela Prefeitura e a nova NFS-e tomará o seu lugar, registrando um vínculo entre a NFS-e substituta e a NFS-e substituída.  **IMPORTANTE: Estes procedimentos não se aplicam a NFS-e BH.**  **Procedimentos:**  1 - Acessar | Ambiente | Parâmetros | Gestão de estoque, compras e faturamento | Parametrizar o tipo de movimento (O tipo de movimento a ser parametrizado deve ser o do tipo 2.1.xx, uma vez que o movimento enviado para  prefeitura é o 2.1.xx e não o 2.2.xx.) | etapa “Mov – Outros Dados”, marcar o parâmetro “Edita Movimento Relacionado”.           2 - Após realizar as parametrizações do tipo de movimento, acesse o menu Movimentos, Vendas / Faturamento e selecione o tipo de movimento parametrizado. No menu Novo, gere o movimento a ser transmitido para substituição da NFS-e (Lembrando que o movimento a ser substituído deve ser o 2.1.xx e**não** o 2.2.xx).   Na aba identificação do novo movimento, realize o preenchimento do numero do movimento (RPS) que será substituído junto a prefeitura, realizando as correções necessárias e envie a NFS-e.          3 - Ao realizar o envio da NFS-e, o movimento enviado ficará com status “Pendente” e a NFS-e que esta sendo substituída, ficará com status “Cancelamento Pendente”.      Realize a consulta autorização das duas NFS-e e confirme a nota a ser substituída com status “Cancelada” e a NFS-e que substituiu com status “Autorizado”. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
