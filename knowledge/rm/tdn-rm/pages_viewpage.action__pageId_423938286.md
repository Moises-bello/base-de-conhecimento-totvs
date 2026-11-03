---
content_hash: 8a7bcd67c3a1a33c10f5658b2b3ca229f64f1c4675a4529c08f034b1cd3dc8ab
fetched_at: '2026-06-29T00:09:26.167926+00:00'
page_id: '423938286'
product: rm
source: tdn-rm
title: Integrar Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938286
version: 4
---

Responsável por realizar a integração entre o sistema patrimonial e o sistema contábil, este processo envia os lançamentos contábeis referentes à aquisição, ocorrências (Baixa , Acréscimo  e Transferência Monetária), transferência de controle , depreciação e correção  criados a partir da contabilização destes recursos para um lote contábil.

**A integração contábil não será realizada nas seguintes situações:**

* Data posterior ao período de cálculo do sistema patrimonial. A data a ser informada durante o processo de integração contábil não poderá ser maior que a data do período de cálculo (data definida nos parâmetros do sistema patrimonial);
* Código do lote, informado durante a parametrização do processo, igual a de lote já existente no sistema contábil. Nesta situação caso o código do lote informado seja igual a um lote já existente no sistema contábil, com origem diferente a do patrimônio, o sistema não permitirá a integração;
* Quando existir contabilização pendente no período informado a ser integrado. Somente contabilizações já realizadas, sejam elas de aquisição, ocorrência, transferência de controle, depreciação ou correção serão integradas ao sistema contábil.

**Passos para realização da integração contábil**  
Antes de realizar a integração com o sistema contábil é importante que os lançamentos contábeis sejam conferidos a de conferir se as informações a serem contabilizadas estão de acordo como desejado.

**Observação**  
Os lançamentos contábeis (de aquisição, ocorrências, transferência de controle, depreciação e correção) serão criados respeitando as informações definidas no evento contábil  associado ao cenário informado no grupo de patrimônio. Desta forma, caso as informações contidas nos lançamentos não estejam de acordo com o desejado é interessante rever itens como o evento contábil associado ao cenário.

Para integração com o sistema contábil é necessário que se informe o período de contabilização definindo o mês e ano inicial e o mês e ano final. Ao informar este período todas as contabilizações existentes nesta faixa de data serão integradas (enviadas para o lote no sistema contábil).

Por padrão será exibido o mesmo código do lote definido no parâmetro do sistema patrimonial, porém o número do lote pode ser alterado, na tela do processo de integração (opção Código do Lote de Gestão Contábil), de forma que se possam salvar os lançamentos contábeis no lote desejado.

**Observação**  
Caso o código do lote informado seja igual a de lote já existente no sistema contábil e este lote não seja de origem do patrimônio o sistema não realizará a integração contábil.

A integração contábil será realizada por Cenário de Cálculo, desta forma a cada execução do processo deve-se informar um cenário por vez.   
  
**As opções (Operações) existentes para envio dos lançamentos contábeis para o lote definido anteriormente são:**

* Aquisição: todas as contabilizações de aquisições de patrimônios não pendentes serão integradas. Para conferência das contabilizações de aquisição pode-se editar o patrimônio (visão de patrimônios cadastrados), acessar a aba Cenários para Cálculos, editar o cenário contabilizado e acessar a opção "Visualizar a contabilização da aquisição";
* Depreciações e Correções: as contabilizações de depreciações e correções podem ser conferidas a partir do menu Contabilização/Visualizar contabilizações. Serão exibidas somente contabilizações referentes ao Período de Cálculo (definido nos parâmetros do sistema patrimonial);
* Ocorrências: as contabilizações não pendentes das ocorrências de Baixa, Acréscimo e Transferência Monetária  são integradas sendo que, para conferência das mesmas antes da integração, pode-se acessar o menu Operações Patrimoniais, Consulta/Cancela, editar a ocorrência desejada e acessar a opção "Visualizar a Contabilização da ocorrência".
* Transferências de Controle: seguindo a mesma linha da Aquisição e das Ocorrências, todas as contabilizações não pendentes referentes a transferência de controle serão integradas. Para conferência das contabilizações pode-se acessar o menu Operações Patrimoniais/Transferência de Controle/Consulta, editar a transferência desejada e acessar a aba contabilização;
* Todas: esta opção permite que todas as contabilizações (de aquisição, depreciação e correção, ocorrências e transferências de controle) sejam integradas ao sistema contábil lembrando que os lançamentos serão armazenados no mesmo lote informado no campo "Código do Lote de Gestão Contábil".

**Log de Integração**

Após a execução da integração contábil será exibido um log com informações referentes ao processo. Caso o processo não tenha executado com sucesso é importante que o log seja conferido.

**Lote de Integração**  
Uma vez realizada a integrado pode-se verificar a contabilizar acessando o lote (diretamente no sistema contábil) informado durante o processo de Integração Contábil.

**Exclusão das contabilizações integradas**

Para desfazer a integração contábil deve-se seguir os seguintes passos, respeitando cada tipo de operações selecionada durante a integração:

* Para a exclusão de contabilizações (integradas) de Aquisição deve-se selecionar o(s) patrimônio(s), a partir da visão de patrimônios cadastrados , e escolher a opção Desfazer Contabilização de Aquisição em Processos/Contabilização;
* O cancelamento da integração da contabilização das Ocorrências será realizado ao selecionar a(s) ocorrência(s) e acessar a opção Desfazer Contabilização em Processos na visão de Ocorrências realizadas;
* Para as contabilizações da(s) Transferências(s) de Controle deve-se selecionar, na visão de transferências realizadas, o histórico referente a transferência desejada e  acessar a opção Desfazer Contabilização em Processos;
* Em relação ao cancelamento da integração de contabilização de depreciação e correção deve-se executar o processo de "Exclusão de Contabilização da Depreciação/Correção". Este processo permite que sejam excluídas as contabilizações de Depreciação, Correção ou as duas ao mesmo tempo.

Caso os lançamentos integrados ao sistema contábil estejam em lote n (não oficial) a exclusão da contabilização realizada no sistema patrimonial irá excluí-los do lote. Ficando a contabilização pendente.  
Caso os lançamentos já estejam integrados ao lote oficial (lote 0) do sistema contábil, ao excluir a contabilização o sistema patrimonial irá gerar lançamentos de esterno no lote definido nos parâmetros do sistema patrimonial. Lançamentos estes que podem ser, posteriormente, integrados ao lote oficial (0) do sistema contábil.

Veja Também

* BaixaAcréscimo
