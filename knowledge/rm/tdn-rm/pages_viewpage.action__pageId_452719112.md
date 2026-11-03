---
content_hash: bdbb772fe4b98b51499e5ea1faa28ebe7fc2ddc51492c2ac70b2a107b6d966ae
fetched_at: '2026-06-29T00:10:03.650028+00:00'
page_id: '452719112'
product: rm
source: tdn-rm
title: Definir Período Ativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719112
version: 12
---

Selecione um período no histórico e execute esse processo para definir o período que será utilizado no RM Chronus. Lembrando que a utilização de períodos anteriores não é uma boa prática, pois toda movimentação já foi liberada e lançada para o RM Labore.

Ao alterar qualquer movimentação de funcionário em períodos anteriores temos que ficar atentos também a movimentação do sistema de folha de pagamento, pois qualquer alteração de extras e atrasos que deveriam ser enviadas para o sistema RM Labore irá afetar no cálculo de encargos como o INSS e o FGTS, sem falar em valores já contabilizados no balanço patrimonial da empresa.

**Transferir registros para tabela de produção/arquivo morto de todos os funcionários:**Selecionando esta opção, ao definir um período como ativo, todos os registros dos funcionários serão transferidos para tabela de produção, bem como, ao definir outro período como ativo, todos os registros dos funcionários serão transferidos para tabela de arquivo morto. Caso não seja selecionada, o sistema irá considerar o valor preenchido no parâmetro "Quantidade de meses que não serão migrados para o arquivo morto", do parametrizador.

É importante ressaltar que o processo de definir período ativo sempre irá considerar o valor preenchido no parametrizador. Neste campo é informado a quantidade de meses que serão considerados para manter os dados na Tabela de Produção.

Caso o parâmetro esteja zerado, todos os períodos anteriores ao período que será ativo, serão movidos para o arquivo morto. E também, os meses que já estavam em arquivo morto não serão alterados.

Mais detalhes sobre o parâmetro: [DT\_Transferência de Período com mais de 6 meses](https://tdn.totvs.com/pages/releaseview.action?pageId=372548518)

Exemplo do processo de definir período ativo:

Definindo o período 9 como ativo marcando o parâmetro, os registros são transferidos para a tabela de produção:

Voltando o período 10 para ativo com o parâmetro marcado, os registros do período 9 são transferidos novamente para tabela de arquivo morto:

**OBSERVAÇÃO:** Para transferir apenas os registros de funcionários específicos para tabela de produção ou para a tabela de arquivo morto, é necessário criar um filtro para que seja considerado apenas estes funcionários selecionados.

Períodos  
HelpWiki - RH - Automação de Ponto
