---
content_hash: 0bc4eb4a18aa675b2621c41e7e283bb8acc2d01ecad5d98dfd2b2273b121a921
fetched_at: '2026-06-29T00:09:49.736656+00:00'
page_id: '435105354'
product: rm
source: tdn-rm
title: Definir Aluguel Complementar - Exemplo de Aluguel Complementar com % Taxa de
  Participação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105354
version: 5
---

**Exemplo de Aluguel Complementar com % Taxa de Participação**

Abaixo vamos mostrar um passo a passo exemplificando o Cálculo do Aluguel Complementar com o campo **% Taxa de Participação no Faturamento:**

**1º Passo:** Cadastrar uma fórmula. Vamos mostrar abaixo uma fórmula que serve exemplo, utilizando as funções de fórmula necessárias.  
(FATURAMENTOALGCOMPLEMENTARVALOR(COMPETENCIAALGCOMPLEMENTAR) \* PERCENTUALFATURAMENTOALGCOMPLEMENTAR(COMPETENCIAALGCOMPLEMENTAR)/100) \* (ALGTABELACONTRATOLOCACAO('TAXAPARTICIPACAOFATURAMENTO','V')/100)

**2º Passo:** No cadastro de Contrato de Locação preencher as informações obrigatórias do contrato, assim como as informações dos Parâmetros do Aluguel Complementar. Veja o exemplo abaixo:

Veja que o campo de **% Taxa de Participação no Faturamento** foi preenchido com 9,99. Esse valor não equivale à 9,99 %, para converter esse valor em porcentagem a fórmula deve ter uma divisão do campo TAXAPARTICIPACAOFATURAMENTO por 100, isso foi feito na fórmula acima no trecho final da fórmula: **('TAXAPARTICIPACAOFATURAMENTO','V')/100**. O usuário pode também inserir o valor já convertido para porcentagem. Neste caso o valor seria, **0,0999**.

**3º Passo:** Efetivar o Contrato de Locação.  
**4º Passo:** Preencher as informações de Medição  
   
   
   
**5º Passo:** Realizar o processo de **Geração do Aluguel Complementar** em **Contrato de Locação | Processos Gerar Aluguel Complementar.**   
   
   
   
**6º Passo:** Após a execução do processo acima os campos Código do evento e Ref. lançamento são preenchidos, possibilitando ver a parcela de Aluguel Complementar e seu Log, para isto basta clicar no link do Evento, localizado no **Código do Evento**.  
    
   
   
**7º Passo:** Já no Evento Financeiro na aba Parcelamento, basta dar um clique duplo na parcela ver maiores detalhes da mesma.  
    
   
   
**8º Passo:** Abaixo temos o Log gerado para este caso.   
   
   
   
**Log do Processo de Aluguel Complementar:**

Valor do faturamento na competência de 03/2016: 800000  
Percentual do faturamento na competência de 03/2016: 15%  
Cálculo do valor do aluguel complementar realizado por fórmula   
Cálculo do valor do aluguel complementar (valor do aluguel complementar - valor do aluguel base): 11988 - 1000 = 10988  
   
**9º Passo:** E por fim, na aba de Lançamentos Financeiros da Parcela é possível conferir o lançamento de Aluguel Complementar gerado.   
 

Voltar
