---
content_hash: 80e8264c2afe3c2ebf308592b9f8d04f47c07788cfbfe759e48dd7903567e549
fetched_at: '2026-06-29T00:11:51.433312+00:00'
page_id: '848369699'
product: rm
source: tdn-rm
title: Lançamento de Permanência a maior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848369699
version: 1
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Para realizar um lançamento de permanência maior é  necessário realizar o cadastro de procedimentos a informação de quantidade de permanência maior.

Desta forma, no encerramento da conta o sistema, o sistema irá realizar os lançamentos de permanências a maior da definida no procedimento principal.

        O calculo da permanência é a quantidade multiplicada por 2, retirando as UTI´s. Calcula-se quantidade de diárias do atendimento e realiza os lançamentos necessários caso a quantidade real ultrapasse a calculada para permanência do procedimento principal. 

Ela só será lançada para atendimento internos e o tipo de atendimento for diferente de  internação clínica.

## **02. EXEMPLO DE UTILIZAÇÃO**

Será necessário lançar uma diária de permanência maior de código "99003015", o lançamento deverá ser realizado  no menu acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços.

Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços, realize o cadastro do procedimento principal informando a quantidade de dias de permanência.

No registro de atendimento, lançar uma guia de autorização com o procedimento que foiinformando a quantidade de dias de permanência.

Na Elaboração de Contas do Paciente  selecionar a parcial que será encerrada e iniciar o processo de encerramento da parcial.

Após o encerramento da parcial, será lançada na conta a diferença do valor calculado, caso  a quantidade real ultrapasse a calculada para permanência  
 do procedimento principal.

No exemplo abaixo, a internação durou 30 dias e foi lançada uma permanência de 3 dias

Quantidade = Dias internação - total permanência \* 2 - dias UTI;

24= 30 -3\*2 -0
