---
article_id: 360058472673
category: SIGAEST - SALDOS
content_hash: 44ce9ddf06e9f2b9ed60542d8579b9bd1dcdefe8e5d75175113218a0581368e1
fetched_at: '2026-06-28T22:39:14.912797+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_A175VLD habilitado
  como alterar a Data de Validade de Produtos com controle de Lote
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058472673-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-A175VLD-habilitado-como-alterar-a-Data-de-Validade-de-Produtos-com-controle-de-Lote
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28807627152919)**Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Quais os passos para alterar a data de validade dos produtos quando o MV\_A175VLD está habilitado?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões

**Solução:**Quando o parâmetro **MV\_A175VLD = .T.** não será possível efetuar a manutenção da data de validade dos Lotes pela rotina MANUTENÇÃO DE LOTES (MATA390). Nesse caso, todo produto que estiver nesse cenário deve ser transferido para o Armazém de Qualidade para que o responsável pela qualidade efetue a alteração da Data de Validade conforme necessário.

**Obs:** Esse cenário, é padrão mesmo para os produtos que não controlam Qualidade. Ou seja, é necessário o envio para a qualidade efetuar a alteração da Validade do Lote, também será necessário efetuar a Baixa do Armazém CQ ([Ver artigo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025518774--SIGAEST-MATA175-Instru%C3%A7%C3%B5es-sobre-Controle-de-Qualidade?source=search)).

Na rotina MANUTENÇÃO DE LOTES (MATA390) ao tentar alterar a Data de Validade apresenta o Help A390DTVAL alertando sobre esse cenário.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098431293)

Caso o Lote esteja vencido e deseja alterar a Data de Validade do Lote, é necessário primeiramente liberar o saldo do lote na rotina BLOQUEIO DE LOTES (MATA275) para em seguida efetuar a transferência para o Armazém de Qualidade.

Para os produtos que originaram através da Baixa de Qualidade e o Lote venceu no Armazém padrão, deve-se estornar todas as movimentações até a chegada do saldo no Armazém CQ. Veja o passo a passo no exemplo abaixo:

***- Atualização -> Movimentações -> Internas -> Endereçamento -> Endereçar (MATA265)***

***- Acessar a rotina Endereçar e estornar o endereçamento no armazém destino (Armazém padrão);***

***- Atualizações -> Movimentos -> Internos -> Qualidade (MATA175)***

***- Acessar a rotina Qualidade e estornar a liberação do CQ;***

***- Incluir o campo na tabela (SD7)  D7\_DTVALID como usado.***

***- Incluir um registro do tipo 5 (Data de validade) e alterar a data do lote conforme desejado;***

***- Após esse processo seguir com a liberação do produto do CQ com a nova data de validade.***

![MATA175_VALIDADE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/6272506269463)

Um outro detalhe, para esse cenário, conforme a imagem de exemplo abaixo, o campo D3\_LOTECTL deve ser digitado manualmente, o saldo do lote liberado não é apresentado pela consulta F4.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096137634)

**Observação importante:**

Para alterar a Data de validade do Lote utilizando o CQ, deve manter o parâmetro F12 da rotina **MANUTENÇÃO DE LOTES (MATA390)**, conforme o Print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19544177236247)

Dessa forma altera a data de validade do lote, conforme demostra na rotina MATC060:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19543334515863)

Saiba Mais:

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
