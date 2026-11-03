---
content_hash: deb381e5e26d7e5d3462cacfc8d3fced1cbc4861a895461e3dc45c411a6eaf73
fetched_at: '2026-06-29T00:06:26.534296+00:00'
page_id: '225951102'
product: rm
source: tdn-rm
title: Ferramenta Analisa Conversão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225951102
version: 2
---

|  |
| --- |
| **Produto:**Analisa Conversão                                                                           **Versão****:4.0.0.18** |
| **Processo: Conversão RM Classis Básico / Superior para TOTVS Educacional (RM Classis Net)** |
| **Subprocesso:***Analise e validação da base de dados* |

***Analisa conversão***

O “Analisa conversão” é uma ferramenta para auxiliar no processo de migração. A ferramenta permite validar a base de dados indicando possíveis inconsistências, alterações na tabela CONTROLECONVERSOR, limpa os dados do Totvs Educacional para migrar os dados novamente e auxilia na análise do log.

***Conexão***

Obs. As inconsistências encontradas devem ser ajustadas antes de processo de conversão.

O “Analisa conversão” pode ser utilizado em banco de dados SQL Server e Oracle, sendo necessário informar o Servidor, Banco, Usuário e Senha e clicar no botão “Conectar”.

 ***Guia “Verificar base (Pré-Conversão)”***

 Antes de realizar o teste de conversão ou a conversão é necessário à validação da base de dados. Clique no botão Analisar e selecionar a coligada, a ferramenta validará a base e listará possíveis inconsistências vão impedir a migração / conversão dos registros (dados).

Leia atentamente cada mensagem e as instruções ou sugestões para correção da falha. O ajuste dos dados é de responsabilidade da instituição e devem ser feitos por um DBA com conhecimento das estruturas das tabelas do RM Classis Ensino Básico / Superior.

***Guia “Limpa conversão”***

Este recurso limpa os dados das tabelas do TOTVS Educacional. O objetivo é que as tabelas sejam limpas para eliminar dados permitindo refazer uma migração sem ter que restaurar um novo backup. Você pode marcar a opção para “Manter tabelas do processo seletivo”, caso contrário todas as tabelas serão selecionadas.

**As tabelas no Processo Seletivo não são reconstruídas após a limpeza, portanto a sua exclusão resultará na perda dessas informações.**

Ao clicar no botão “Limpa conversão”, o sistema seleciona as tabelas do TOTVS Educacional e tabelas criadas na conversão que possuam registros e exibe para o usuário.

**O usuário deverá marcar as tabelas que *NÃO* devem ser limpas.**

Tabelas com valores padrões do TOTVS Educacional já vem marcadas como sugestão para que os valores sejam mantidos. É necessário que verifique a lista e marque as tabelas que deseja manter.

Clique no botão “Continuar” para limpar as tabelas.

O sistema tentará truncar a tabela. Caso não seja possível truncar será executado um delete para limpar a tabela.

O tempo de exclusão dos dados varia de acordo com o tamanho da tabela.

O ícone de notificação exibirá balões com informações sobre o processo de exclusão. No término da exclusão, o sistema exibirá a tela abaixo para corrigir a GAUTOINC.

Você poderá remover os campos que possuem valor registrado clicando no botão “Remover marcados”.

É aconselhável, marcar todos os registros e clicar em "Corrigir marcados", principalmente para bases que possuam mais de 1 (uma) coligada.

Após corrigir a GAUTOINC, clique no "X" para fechar a tela.

No próximo passo você poderá excluir os campos complementares criados. Basta marcar os campos e clicar no botão “Remove campos complementares”.

Após excluir os Campos Complementares clique no "X" para fechar a tela.

Na próxima tela o sistema exibirá as tabelas que possuem lote de conversão.

É necessário marcar as tabelas e clicar no botão “Remove lotes” para que seja possível executar novamente o conversor que utiliza o campo de lote desta tabela.

Somente serão exibidos os lotes, quando o financeiro estiver Convertido.

Após excluir os Lotes clique no "X" para fechar a tela. O sistema apresentará um log, listando as tabelas que foram limpas, os campos da GAUTOINC que foram ajustados e os lotes que foram removidos.

Com todos estes processos executados, a migração poderá ser executada novamente.

***Guia “Acompanhar Conversão”***

Ao clicar no botão “Atualizar” o sistema verifica a tabela CONTROLECONVERSOR e exibe o status da conversão.

Ao clicar no botão “Remover marcados” todos os registros marcados no grid serão removidos da tabela CONTROLECONVERSOR.

Ao clicar no botão “Setar status para:” todos os registros marcados no grid receberão o status indicado na tabela CONTROLECONVERSOR.

Ao clicar no botão “Cancela última conversão” os registros com status “Convertendo” receberão o status “Pendente”, para executar os conversores novamente.

Lembrando que estas operações apenas alteram a tabela CONTROLECONVERSOR, não desfazendo alterações em outras tabelas que podem ter sido feitas por algum conversor.

***Guia “Log de migração”***

Caso a conversão esteja em andamento ou já tenha sido executada, basta clicar no botão “Atualizar” para que o grid exiba os detalhes do que foi registrado pelo log.

Ao encontrar alguma situação que precisa ser analisada, como “porque todas as disciplinas da grade não foram convertidas”, você poderá dar um duplo clique no registro para verificar os detalhes desta conversão. Lembrando que é comum não bater exatamente a quantidade de registros devido a alterações de regras entre os sistemas Classis e o TOTVS Educacional. Um registro do TOTVS Educacional pode representar vários registros do Classis Ensino Superior, por exemplo.

O sistema irá solicitar a coligada e o sistema que receberão os dados do log. Informe os dados e clique em “Selecionar”.

Caso não haja nenhuma informação no log texto, execute a consulta utilizada para selecionar os registros. O registro que não foi inserido poderia estar “duplicado” ou ser inconsistente. Como informamos no início deste documento, vários registros podem não ser convertidos devido a inconsistências na base ou pelo TOTVS Educacional ter um comportamento diferente dos sistemas básico e superior.

Em caso de dúvidas, entre em contato com o nosso suporte técnico. Para facilitar o atendimento, disponibilize a base de dados no ponto em que o problema da conversão ocorreu. Lembrando que certos problemas podem ocorrer em um cliente e não ocorrer em outros devido à forma que o ensino básico e superior são utilizados e parametrizados.

***Guia “Mensagens Comuns”***

São mapeadas algumas mensagens de erro já encontradas no conversor.
