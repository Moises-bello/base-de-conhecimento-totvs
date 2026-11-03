---
content_hash: f4ece23c144119ae40651896ca6ff5d2415d636396c4ddfc7d722027446b1f8e
fetched_at: '2026-06-29T00:09:16.933773+00:00'
page_id: '421388525'
product: rm
source: tdn-rm
title: Impressão de Cheque - Pertochek 501S
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388525
version: 10
---

Informações sobre a impressão de cheque na impressora Pertochek 501S. A comunicação com a impressora será apenas serial, não fazendo uso de recursos de comunicação paralela, disponível na impressora. A comunicação com a impressora será direta não fazendo uso de dlls ou qualquer recurso adicional. O número do banco informado no processo de impressão será enviado para impressora de cheques, podendo ocorrer falhas de impressão se o número do banco no cheque contido na linha CMC7 (código de barras do cheque) for diferente. O verso do cheque para esta impressora só permite a edição de 2 linhas com 60 caracteres. Deste modo, serão consideradas as 2 primeiras linhas preenchidas no parâmetro do processo "Verso do Cheque" considerando os 60 caracteres. De acordo com o fabricante, a impressão de cheques pode ser compatível com os seguintes modelos abaixo, porém, o teste de impressão foi realizado no modelo "Pertochek 501S". - Pertochek 501S

* Pertochek 502S (com teclado e display)
* Pertochek 502SM (com teclado, display e consulta a provedores)
* A impressora de cheques, de acordo com o modelo, possui os seguintes recursos que não serão utilizados pelo RM Fluxus: - Lista Negra de cheques
* Informações CMC7 (código de barras do cheque)
* Impressão de Telefone
* Impressão de Cheque Administrativo
* Impressão Cheque Transferência Bancária
* Impressão de Cópia de Cheque
* Interface de Comunicação Paralela
* Uso do PinPad
* Uso do Teclado
* Uso do LCD
* Uso da leitora de cartão

Importante:

É necessário que a porta serial ( COM1, COM2, COM3 ou COM4) esteja ativada no sistema operacional da máquina do usuário.  
 Deverá ser preenchido nos parâmetros do TOTVS Gestão Financeira, todos os itens na opção: "Impressora de Cheque Serial".

Dica de Configuração:

Um exemplo de configuração para PertoCheck 501S

Porta Serial Default = COM1;  
 Velocidade = 4800bps;  
 Paridade = Nenhuma;  
 Bits Dados = 8 bits;  
 Bits Parada = 1 bit;  
    
 Importante ressaltar que as configurações acima podem sofrer alterações conforme ambiente computacional. Maiores informações sobre os valores das configurações devem ser consultadas no Manual Técnico da Impressora.

Dica de Impressão:

Ao imprimir o cheque, a folha de cheque deve ser inserida na impressora somente após apresentar as mensagens abaixo, ou seja, a folha deve ser inserida somente quando estiver piscando luz verde na impressora. O mesmo para impressão do verso do cheque. 

"O cheque ( xxx ) está preparado para impressão. Tecle [Enter] para iniciar a impressora e então posicione-o..."
