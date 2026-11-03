---
content_hash: 4279635519ece0c336f01b3d32d506e27d8aabe3ddd97d330f5a015c0131944c
fetched_at: '2026-06-29T00:09:27.147402+00:00'
page_id: '423938440'
product: rm
source: tdn-rm
title: Renumeração de documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938440
version: 2
---

*Atenção!*

Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.

Este processo permite alterar o número dos documentos existentes nos lançamentos contábeis a partir das opções de renumerações existentes na tela. Serão renumerados somente os documentos referentes ao lote, datas e intervalo de lançamentos informados.  
   
**Atenção**  
Uma vez renumerados os documentos, não há como voltar aos números originais!

**Opções de renumeração**

*Documento = Id do lançamento*  
Esta opção permite que o número do documento das partidas seja preenchido com o respectivo id do lançamento contábil.

*Documento = Id da Partida*  
Esta opção permite que o número do documento das partidas seja preenchido com o respectivo id da partida.  
   
**Exemplo**  
O documento da partida 456 está preenchido com o valor '000123', ao rodar o processo, o documento desta partida será alterado para 456 que é igual ao id da partida.

*Reinicia renumeração a cada mês (mês a mês)*  
Esta opção permite que a numeração dos documentos dos lançamentos selecionados seja realizada mensalmente, reiniciando a numeração a cada mudança de mês. Desta forma não haverá continuidade da numeração de um mês para o outro.

*Reinicia renumeração a cada dia (dia a dia)*  
Esta opção permite que a numeração dos documentos dos lançamentos selecionados seja realizada diariamente, reiniciando a numeração a cada mudança de dia. Desta forma não haverá continuidade da numeração de um dia para o outro.

*Renumera por ordem de Data*  
Esta opção permite que os documentos dos lançamentos selecionados sejam renumerados seqüencialmente por ordem de data. Desta forma a numeração será contínua entre os lançamentos selecionados.  
   
**Observação**  
Ao escolher uma das opções "Reinicia renumeração a cada mês (mês a mês)", "Reinicia renumeração a cada dia (dia a dia)" ou "Renumera por ordem de Data" deve-se informar o número inicial a ser considerado pelo sistema para realizar a renumeração.

*Preencher com zeros à esquerda sem alterar o número do documento*  
Com esta opção marcada, o sistema irá completar com zeros à esquerda os números dos documentos existentes, até preencher todo o campo conforme tamanho informado nos parâmetros do sistema, entretanto, sem alterar o seu valor original, apenas completando com zeros o espaço restante.  
Como o sistema não altera o valor original do documento, se o campo Documento estiver vazio, após rodar esta rotina com esta opção marcada, o campo Documento permanecerá vazio.

*Documento = Lote de Origem*  
Ao ativar esta opção os documentos serão renumerados com o mesmo número do código do lote de origem dos lançamentos. Por exemplo, os documentos dos lançamentos originados do lote número 106 passarão a ter o campo documento preenchido com o número 106, mesmo que estes lançamentos já tenham sido integrados ao lote zero.  
   
**Observação**  
Caso o lote esteja bloqueado com um usuário o processo não será executado enquanto o mesmo não for liberado.

*Preencher com zeros à esquerda*  
Esta opção pode se utilizada juntamente com as outras opções de renumeração. Desta forma, além de renumerar conforme a opção desejada, os números dos documentos dos lançamentos selecionados serão preenchidos com zeros à esquerda, até preencher todo o campo conforme tamanho informado nos parâmetros do sistema (opção: Tamanho do Documento).  
Esta opção somente ficará disponível quando o parâmetro do sistema "Preenchimento com zeros à esquerda" estiver desmarcado.

**Executando o processo**  
Para executar o processo deve-se informar o lote e a filial a que os lançamentos pertencem. Caso não seja informada a filial, serão considerados todos os lançamentos.

Informe o período (data inicial e final) e a faixa de lançamentos a partir do número do id dos mesmos, a fim de filtrar apenas os lançamentos desejados.
