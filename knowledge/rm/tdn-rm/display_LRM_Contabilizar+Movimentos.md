---
content_hash: cb7206dbb3696b3b3c099e8baebf31332b4f306902b8bb0b4f7bb625882215b8
fetched_at: '2026-06-29T00:09:25.931296+00:00'
page_id: '423938208'
product: rm
source: tdn-rm
title: Contabilizar Movimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Contabilizar+Movimentos
version: 7
---

Esta opção somente será visualizada se o tipo de movimento for parametrizado para Utilizar Evento Contábil (Parâmetros do Tipo de Movimento | etapa Contabilização).   
O processo de contabilizar movimentos executa os cálculos de fórmulas e configurações de defaults contábeis, cadastrados dentro do Evento Contábil parametrizado para este tipo de movimento.   
Com estes dados, são gerados lançamentos contábeis em Lotes específicos, criados pelo próprio sistema, para facilitar a conferência dos dados no momento da integração dos lançamentos para o Lote Contábil.  
Ao selecionar os movimentos para serem contabilizados, o sistema verificará se, no tipo de movimento, existe um Evento Contábil default.   
Se existir, o sistema irá utilizar este Evento para a geração da contabilidade deste movimento.   
Caso contrário, o sistema apresentará uma tela, solicitando a seleção de um Evento Contábil para a execução do processo.  
***Observação***: Caso o (s) movimento (s) selecionado (s) já estiver (em) contabilizado (s), o sistema executará novamente o processo de Contabilização, como se entendesse que o movimento não tivesse sido contabilizado.

---

Informações Adicionais

* [Contabilização de Movimentação de Baixa de Estoque](http://tdn.totvs.com/pages/viewpage.action?pageId=4813674)

A partir da versão/patch **12.1.2605.275**, os processos de Contabilizar Movimentos poderá ser configurados para utilizar o fracionamento de jobs, utilizando a classe à seguir:

* MovContabilizarMovimentosProc

Os processos de Contabilizar Movimentos poderão ser executados com ou sem fracionamentos de jobs. 

Para informações detalhadas sobre o fracionamento de jobs, consultar a documentação [Configuração de fracionamento de jobs.](https://tdn.totvs.com/x/lpR-I)
