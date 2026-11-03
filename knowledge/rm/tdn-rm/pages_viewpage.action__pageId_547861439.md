---
content_hash: 65c004de61a901fa87befed91bb14b156bfb0716c3c1eae8a6d6361f998ba37b
fetched_at: '2026-06-29T00:10:42.840960+00:00'
page_id: '547861439'
product: rm
source: tdn-rm
title: 2.12 Baixa de Lançamento por Arquivo Bancário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547861439
version: 9
---

A importação de arquivos de retorno é um processo que consiste em baixar automaticamente ou atualizar os Lançamentos Financeiros por meio de importação de arquivos disponibilizados pela rede Bancária.

Em se tratando de Cobrança Eletrônica, a baixa será realizada automaticamente desde que o arquivo de retorno possua os dados requeridos, assim como data de crédito, valor do crédito, motivo de ocorrência específica para baixas ou quitações, entre outras informações importantes.

Alguns arquivos de retorno reportam apenas atualizações para o lançamento financeiro, provenientes de transações entre empresa e Banco. Um exemplo dessa transação é o arquivo de retorno que o Banco disponibiliza à empresa informando do processamento dos títulos. Ao importar esse arquivo a única alteração a ser feita é a atualização do STATUS.CNAB do Lançamento para “Registrado” e não produzirá baixas.

Para realizar este procedimento, o usuário deve acessar o Módulo Gestão Financeira e selecionar “*Movimentações Bancárias | Retorno Bancário | Retorno | Cobranç*a” e seguir os passos abaixo:

Neste momento, o Sistema apresenta o assistente para leitura do arquivo de retorno de baixa.

Em seguida, o usuário deve escolher o de retorno bancário:

* **Retorno de cobrança registrada:** Utilizado para cobrança registrada de 400 posições;
* **Retorno de cobrança não registrada:** Utilizado para cobrança não registrada;
* **Retorno de Cobrança CNAB 240:** Utilizado para cobrança registrada de 240 posições. (Mais utilizado pelos DRs).
* **Retorno Cobrança PIX - 750 (layout específico do banco):** Quando o processo é executado com essa opção marcada, será exigido que as linhas do arquivo tenham 750 caracteres.

Ao clicar em “Avançar”, o Sistema disponibilizará a tela para informar os dados para importação do arquivo.

O usuário deve preencher os campos:

* **Arquivo:** É necessário indicar o caminho onde se encontra o arquivo a ser importado (disponibilizado pelo banco);
* **Código Filial:** Informe o código da Filial. Caso o arquivo possua registros de várias filiais, basta não preencher esta informação no ato da importação do arquivo;
* **Conta Caixa:** Informe o Código da Conta Caixa para a baixa dos Lançamentos. Informando a Conta Caixa, o Banco será atualizado (Banco referente ao arquivo que será importado). Este preenchimento é essencial para devida importação;
* **Banco a ser importado:** Será carregada automaticamente ao informar a conta caixa;
* **Evento Contábil:** Informe o Evento para a contabilização da baixa (se não informado, será utilizado o evento parametrizado para o processo de Baixa de acordo com a tabela default para evento);
* **Histórico:** Será carregado automaticamente.

O usuário deve informar alguns parâmetros para leitura do arquivo conforme a seguir:

* **Se diferença a maior:** Informar o campo que receberá os valores a maior do que os calculados pelo Sistema;
* **Se a diferença a menor:** Informar o campo que receberá os valores a menor do que os calculados pelo Sistema;

falseComportamento do sistema para diferença a maior ou menor

* [Baixar e Gerar uma Baixa Parcial](https://tdn.totvs.com/display/LRM/Baixar+e+Gerar+uma+Baixa+Parcial)
* [Baixar e Gerar um Adiantamento](https://tdn.totvs.com/display/LRM/Baixar+e+Gerar+um+Adiantamento)
* [Baixar e informar o valor da diferença em um campo](https://tdn.totvs.com/pages/viewpage.action?pageId=421388648)
* [Não Baixar](https://tdn.totvs.com/pages/viewpage.action?pageId=421388569)

* **Utilizar conta caixa do lançamento:** Marcar esta opção para que o Sistema utilize a conta/caixa do lançamento para realizar a baixa;
* **Cobrança Registrada:** Marcar esta opção se a cobrança é registrada no banco
* **Consistir Nosso Número apenas para Lançamento em aberto:**Essa opção permanece funcional apenas para Cobrança não registrada, pois a numeração do nosso número pode ser reiniciada.  
  Será usada para, ao procurar o lançamento pelo Nosso Número para cobrança não registrada, o sistema procura apenas nos lançamentos em aberto.
* **Usar Data Compensação como data de Contabilização da Baixa:** Marcando essa opção, a "Data de Contabilização de Baixa" dos lançamentos, será a "Data de Compensação" informada no arquivo bancário.
* **Gerar um extrato para todos os Lançamentos:**Com essa opção marcada, ao importar o arquivo de retorno será gerado apenas um registro no Extrato de Caixa pelo valor total dos lançamentos recebidos pelo banco.
* **Contabilizar posteriormente:**Marque esta opção caso a contabilização precise ocorrer em momento diferente do retorno.
* **Exibir no log informações dos lançamentos relacionados a cada boleto:**O sistema irá exibir no log informações de todos os lançamentos que compõem o boleto de cobrança.

Avançar | Executar

Após realizar a leitura do arquivo conforme instruções, todos os lançamentos contidos no arquivo bancário, será quitado no sistema automaticamente.

Ao importar o arquivo de retorno, o sistema identifica os lançamentos de mesmo IDBOLETO e produz a baixa total ou parcial de todos os Lançamentos de mesmo IDBOLETO.

falseDesbloqueio de Arquivo de Retorno

Esse processo tem por objetivo desbloquear o arquivo de retorno, caso tenha ocorrido algum erro ou interrupção do processo de importação do arquivo retorno, deixando assim o seu status como processando.

Nestes casos, o campo STATUSPROCESSAMENTOARQUIVO da tabela FRETORNOBANCARIO recebe o valor 1 (processando), enquanto o campo HASHFILE fica com um valor hash preenchido.

Para que o arquivo seja desbloqueado e os campos da tabela alterados, permitindo a execução do processo de importação, basta executar o processo de desbloqueio no menu *Movimentações Bancárias | Retorno Bancário | Desbloqueio de Arquivo de Retorno*.

Veja também

* [FIN - Retorno Bancário](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=421388702)
* [FIN - Retorno Cobrança Eletrônica](https://tdn.totvs.com/pages/releaseview.action?pageId=421388703)
* [Boletim Técnico - Retorno de Cobrança Eletrônica](https://tdn.totvs.com/pages/viewpage.action?pageId=42043760)
* [Cross Segmentos - Backoffice Linha RM - FIN - Como Importar Arquivo de Retorno de Cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060832094-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-Importar-Arquivo-de-Retorno-de-Cobran%C3%A7a)
* [Cross Segmentos - Backoffice Linha RM - FIN - Parametrizar sistema para baixar lançamentos via retorno bancário com diferença de 1 ou 2 centavos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001976742-Cross-Segmentos-Backoffice-Linha-RM-FIN-Parametrizar-sistema-para-baixar-lan%C3%A7amentos-via-retorno-banc%C3%A1rio-com-diferen%C3%A7a-de-1-ou-2-centavos-)
* [FIN - Desbloqueio de Arquivo de Retorno](https://tdn.totvs.com/display/LRM/FIN+-+Desbloqueio+de+Arquivo+de+Retorno)
* [RM - FIN - Arquivo de retorno XXX está sendo importado pelo usuário YYY](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001097488-RM-FIN-Arquivo-de-retorno-XXX-est%C3%A1-sendo-importado-pelo-usu%C3%A1rio-YYY)
