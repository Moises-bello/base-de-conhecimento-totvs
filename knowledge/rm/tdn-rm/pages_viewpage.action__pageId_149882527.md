---
content_hash: dafdfd48418c43fb5bf705a7bf9b13ce78e7981aa87a8ceefd8783393e549c78
fetched_at: '2026-06-29T00:05:56.416278+00:00'
page_id: '149882527'
product: rm
source: tdn-rm
title: Compensação de Tributos Federais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149882527
version: 1
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                         **Versão:** 11.52/11.82 |
| **Processo** | **:** | Compensação de Tributos Federais |
| **Subprocesso** | **:** | Apuração de Tributos |
| **Data da publicação** | **:** | 25/07/2014 |

**O objetivo deste documento é apresentar como é feita a compensação de tributos federais no aplicativo TOTVS Gestão Fiscal e os parâmetros e cadastros necessários para isto.**

Qualquer tributo administrado pela SRF passível de restituição poderá ser compensado com DÉBITOS PRÓPRIOS. A compensação deverá ser comunicada previamente à SRF através de Declaração de Compensação feita na PER/DCOMP.O sistema de Gestão Fiscal foi alterado de modo a proporcionar o controle de Compensações de Tributos Federais pagos a maior e a geração das fichas correspondentes da DCTF.

O processo de utilização do Controle de Compensações se dará o seguinte:

1.Nos Parâmetros 03.01.10, Etapa 6 “Compensação de Tributos Federais”, informe qual será a Taxa utilizada para ajustar o valor do crédito no momento da compensação.

2.Crie a taxa (SELIC) no menu CADASTROS\ MOEDAS e ÍNDICES e informe seus índices.

3. O primeiro passo é reconhecer o crédito. Nesse primeiro momento, foi implementada apenas a compensação por pagamento indevido ou a maior.

Acesse o menu *Cadastros | Tabelas Auxiliares | Obrigações Federais | Compensação de Tributos Federais, clique em inlcuir*e informe os dados do crédito.

O registro do crédito pode ser feito de duas formas:

1. 1. Digitando os dados:

   B. Vinculando uma guia dos Períodos de Apuração:

             

4. No encerramento dos Períodos de Apuração o sistema irá avisar da existência de créditos cadastrados.

5. As Guias DARF do Período devem ser geradas normalmente. 

6. O próximo passo é associar os débitos (Guias geradas) aos créditos a serem compensados.

OBS: Só poderão ser vinculadas Guias de Débito que NÃO estiverem Baixadas.

7. Decidindo por utilizar o crédito naquele período, a pedido de compensação deve ser feito e enviado para a RFB. Acrescente a Data de Transmissão da DCOMP no cadastro do crédito.

8.Execute o Processo “**Cálculo das Compensações de Tributos Federais**”. Esse processo irá atualizar o valor do crédito de acordo com a taxa informada nos parâmetros (item 1).

OBS: O cálculo somente será realizado se o campo Data de Transferência estiver informado. Este campo é utilizado para realizar o cálculo da Taxa SELIC acumulada. O Processo de Cálculo poderá ser realizado diversas vezes, desde que o Processo de Finalização não tenha sido realizado. Após a Finalização do Processo o cálculo não poderá ser realizado.

9. Para conclusão da compensação, execute o Processo “**Finalização do Cálculo da Compensação**”. Após esse processo não serão permitidas mais alterações.

Se houver saldo residual do crédito, o sistema incluirá um novo registro de compensação para posterior utilização.

10.Depois de concluído o processo de Compensação, o Sistema irá registrar o Valor Compensado nas Guias utilizadas como Débito.

- Guia totalmente compensada

- Guia com saldo residual para pagamento

11. Quando solicitada a geração da DCTF, o sistema irá gerar os registros da Compensação da seguinte forma:

1. 1. **Ficha R10:** Será gerada normalmente, independente se a guia foi totalmente compensada ou não;
   2. **Ficha R11:** Será gerada somente se houver saldo residual para pagamento;
   3. **Ficha R12:** Será gerada para todas as Guias do período que sofreram Compensação, seja total ou parcial.
