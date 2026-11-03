---
article_id: 25140398856599
category: Financeiro
content_hash: e187eb4f8e97d39b38f1e59ba7cb315e5a7b6f6a4570877424299084b330b934
fetched_at: '2026-06-28T22:38:03.125406+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como realizar
  a alteração do vencimento no título
type: support-article
updated_at: '2024-09-19T19:21:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25140398856599-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-realizar-a-altera%C3%A7%C3%A3o-do-vencimento-no-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25140602366359)Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como realizar a alteração do vencimento no título?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Importante**

Apenas os bancos **Banco do Brasil** e **Itaú** contemplam a alteração dos boletos para determinados campos.

**Banco do Brasil** - Apenas a data de vencimento **(E1\_VENCTO ou E1\_VENCREA)** pode ser modificada.

**Itaú** - É permitida a alteração apenas da data de vencimento **(E1\_VENCTO ou E1\_VENCREA)** e/ou do valor **(E1\_VALOR)**. Essas modificações devem ser feitas em ambiente de produção, seguindo a regra do banco que permite alterar apenas boletos que foram previamente transmitidos nesse ambiente.

As alterações nos campos permitidos para cada banco serão reconhecidas pelo sistema como boleto online para transmissão via **job FINA713**. No entanto, se houver alteração em algum outro campo do título, não sendo os permitidos, o sistema não considera essa modificação via job. Em vez disso, será tratado como uma alteração normal de **CNAB**, verá essas ocorrências na tela de ocorrências **CNAB** do sistema.

**Solução**

Para alterar um boleto registrado, siga estes passos:

1. Acesse a rotina de **Contas a Receber (FINA040)** via: **atualização** > **Contas a Receber** > **Contas a Receber.**
2. Posicione-se sobre o título transmitido via API **(EA\_BORAPI = S, EA\_TRANSF = S)**.
3. Clique em "**Alterar**" e faça a modificação desejada, como, por exemplo, o vencimento. Confirme a alteração.
4. Após a confirmação, um registro será gravado na tabela **FI2** para o título em questão, onde os campos **FI2\_BORAPI** = S e **FI2\_OPEAPI** = A indicam que a operação foi realizada com sucesso.

**Outro aspecto relevante é que o banco aceitará a alteração do título através do job FINA713 somente após um intervalo de 30min ou 24h dependendo do banco.****Para validar se foi enviado a instrução de cobrança o campo FI2\_TRANSF deve ser igual a C.**

**Saiba mais**

[Contas a receber (Comunicação bancária online) - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392#Contasareceber(Comunica%C3%A7%C3%A3obanc%C3%A1riaonline)-Altera%C3%A7%C3%A3o/cancelamentodeboletosareceber)

[SIGAFIN - FINA590 - Manutenção de títulos em borderô](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028291032-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA590-Manuten%C3%A7%C3%A3o-de-t%C3%ADtulos-em-border%C3%B4)

[Monitor de Boletos com Pendências - FINA710](https://tdn.totvs.com/pages/releaseview.action?pageId=619123545#A%C3%A7%C3%B5es-passo2)
