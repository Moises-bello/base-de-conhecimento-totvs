---
content_hash: b15709565614f34b67bde7ec8f75376e056118e6d7f086497e6f51347a539fed
fetched_at: '2026-06-29T00:12:16.339545+00:00'
page_id: '985663167'
product: rm
source: tdn-rm
title: DT - S-2206 - Geração do gatilho em lote com campo data efetiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=985663167
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | S-2206 - Geração do gatilho em lote com campo data efetiva |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-12055](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12055 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410.298
* 12.1.2502.205
* 12.1.2506.148 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Garantir que o evento S-2206 seja gerado com as informações de função e salário conforme o histórico vigente nas datas de alteração e data efetiva, garantindo a correta atualização da CTPS Digital do colaborador.

**Exemplo:**

O funcionário exercia a função de "Operador de Loja" e teve uma alteração de função registrada com data de 01/11/2022, passando para a função "Pesquisador". Essa alteração foi corretamente integrada ao eSocial.

Em seguida, foi realizada uma alteração salarial, com data de histórico em 01/11/2022 e data efetiva em 01/09/2022, no valor de R$ 2.043,00.

Porém, ao gerar o evento S-2206, o XML foi enviado com a função anterior ("Operador de Loja"), o que resultou na sobrescrição indevida da função correta no eSocial.

## **04.****SOLUÇÃO**

Foi criado o parâmetro **“Dissídio”**. Ao marcá-lo, o sistema habilita o novo campo **"Data Efetiva"**, permitindo que o usuário preencha conforme necessário.

Com isso, o gatilho do evento S-2206 será gerado com o campo Data Efetiva devidamente informado.

**Exemplo da Situação Atual**

Acesse o menu eSocial | Outros Processos | Gerar gatilho em lote e cadastre a data de alteração, marcando o parâmetro "Dissídio" e digite a data efetiva.

Selecione  a coligada desejada:

Após a execução do processo, o sistema gerou corretamente o gatilho para o funcionário na data de 01/09/2025 com a data efetiva para 01/08/2025.

Após a geração do XML o sistema gerou corretamente.

## **05. DOCUMENTAÇÃO**
