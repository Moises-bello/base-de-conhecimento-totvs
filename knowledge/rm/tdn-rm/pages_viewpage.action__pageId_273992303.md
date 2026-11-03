---
content_hash: 0713b255d959df9e9f3db167aa561cedc590d4f8dbd24cc44e8dbfecdeea08bb
fetched_at: '2026-06-29T00:08:32.597215+00:00'
page_id: '273992303'
product: rm
source: tdn-rm
title: NFSE0006_Município_não_homologado_para_esta_operação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273992303
version: 4
---

|  |  |
| --- | --- |
| **Produto:** | NFS-e - Nota Fiscal de Serviço Eletrônica (Municipal) |
| **Versões:** | Ambas |
| **Ocorrência:** | Município não homologado para esta operação |
| **Passo a passo:** | **Introdução:**  Ao tentar enviar uma NFS-e o sistema apresenta a seguinte mensagem de erro:  Não foi possível enviar a nota.  Nenhuma NFS-e foi enviada.  Município não homologado para esta operação. Para maiores esclarecimentos procure o suporte Totvs.  **Procedimentos para correção do problema:**  1. Verifique através do link abaixo se o município está homologado:    2. Acesse Ambiente | Parâmetros | Gestão de estoque, compras e faturamento | Integrações | Fiscal | Parâmetros por filial, clica duas vezes em cima da Filial, na etapa "Ambiente NF-e".  No campo “Classificação Município” deve ser selecionada a tabela de classificação de município, esta tabela varia de acordo com cada município que poderá ser IBGE (ABRASF) ou SIAFI (DSFNET).    3 .Verifique se o código IBGE possui 7 dígitos:  Cadastro | Tabelas auxiliares | Municípios – edite o cadastro do município  Anexos | codificação do Município      4 - Caso o município esteja homologado execute a configuração do servidor mashups conforme link abaixo:    5 -  Caso já tenha realizado o configuração do mashups realize o seguinte processo:  Acesse o menu: SPED | NFSe (municipal) em seguida Processos | Atualização de Municípios Homologados      Nesta tela existem duas listagens: ao lado esquerdo corresponde aos municípios em que o sistema RMNucleus já considera como homologados e ao lado direito a listagem de todos os municípios que a TOTVS já disponibilizou utilização remotamente.  Obs: É necessário que o município que esteja parametrizando seja apresentado ao lado esquerdo da imagem, caso contrário a inconsistência continuará a ser apresentada. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
