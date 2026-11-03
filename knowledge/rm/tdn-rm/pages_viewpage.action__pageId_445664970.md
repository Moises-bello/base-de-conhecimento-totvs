---
content_hash: 55130e8ae93cf0d0f15116809ea9360cac7b58f6c7935e0eaba8455673ca82e1
fetched_at: '2026-06-29T00:09:54.924713+00:00'
page_id: '445664970'
product: rm
source: tdn-rm
title: DT Função de Fórmula DIASAFT2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445664970
version: 6
---

Tempo aproximado para leitura:**00 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Plataforma RH |
| Módulo: | Folha de Pagamento |
| Função: | Função de fórmula DIASAFT2 |
| Ticket: | 2160193 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FOPCALCULO01-2716 |
| Versões Afetadas | 12.1.22.142 ou superior |

## **02. SITUAÇÃO/REQUISITO**

O cliente necessita saber dentro de um período, quantos dias de afastamento são pagos pela empresa e quantos são pela empresa. Hoje a função de fórmula DIASAFT retorna a quantidade de dias afastado do funcionário não separando a quantidade que é paga pela empresa e a quantidade que é paga pela previdência.

## **03. SOLUÇÃO**

Para atender esta demanda, foi criada a função de fórmula DIASAFT2. Com esta função de  fórmula, será feito o cálculo de dias de afastamento, discriminando os que foram pagos pela empresa e os que foram pagos pela previdência durante o período informado.

Para a fórmula, será considerado quando utilizar o controle manual de continuidade de afastamento com atestado médico, onde os afastamentos deverão ser ligados através do campo 'Dt. Inicial da Continuidade de Aft.' disponível no cadastro de afastamentos do anexo do funcionário.

Para utilizar a fórmula, é necessário informar: Data Inicial, Data Final, e o indicativo de quem pagou (1 - afastamentos pagos pela previdência; 2 - afastamentos pagos pela empresa)

Exemplo:

1. Afastamento ligados pelo campo 'Dt. Inicial da Continuidade de Aft.':  
   Funcionário esteve afastado por 10 dias (01/11/2018 a 10/11/2018)  
   Funcionário esteve afastado por 15 dias (16/11/2018 a 30/11/2018)  
   DIASAFT2('01/11/2018', '30/11/2018', 1) = 10 (como foi o indicativo 1, retornou os 10 dias que foram pagos pela previdência)  
   DIASAFT2('01/11/2018', '30/11/2018', 2) = 15 (como foi o indicativo 2, retornou os 15 dias que foram pagos pela empresa)
2. Afastamento sem ligação pelo campo 'Dt. Inicial da Continuidade de Aft.':  
   Funcionário esteve afastado por 10 dias (01/11/2018 a 10/11/2018)  
   Funcionário esteve afastado por 10 dias (16/11/2018 a 25/11/2018)  
   DIASAFT2('01/11/2018', '30/11/2018', 1) = 0 (como foi o indicativo 1, retornou os 0 dias que foram pagos pela previdência, pois os afastamentos não tinham continuidade entre si)  
   DIASAFT2('01/11/2018', '30/11/2018', 2) = 20 (como foi o indicativo 2, retornou os 20 dias que foram pagos pela empresa)

## **04. DEMAIS INFORMAÇÕES**

**Esta função só retorna os dias de afastamento quando o parâmetro de controle manual de afastamentos está marcado no parametrizador. Quando o parâmetro está desmarcado retorna valor 0 (zero) para ambos indicativos de quem pagou e no cálculo retorna mensagem no log informando que o o parâmetro de controle de continuidade manual está desmarcado.IMPORTANTE!**

Tipos de Afastamentos

Esta função de fórmula só é válida para os tipos de Afastamentos:

P - Previdência

T - Acidente de Trabalho

O - Doença Ocupacional
