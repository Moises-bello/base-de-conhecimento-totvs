---
content_hash: fcd86c032cc118d3ec842e4f1abaa417b458565f3393778b7b25c319166839c7
fetched_at: '2026-06-29T00:10:38.799575+00:00'
page_id: '545227686'
product: rm
source: tdn-rm
title: 8569936 FISCAL01-12745 DT NF-e - Tag cBenef -Mais de uma origem do benefício
  fiscal para o mesmo item
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545227686
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Enviar NF-e |
| Ticket: | 8569936 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12745 |

## **02. SITUAÇÃO/REQUISITO**

Um mesmo produto possui códigos de benefícios fiscais diferentes, para a mesma UF e mesma CST. O que identifica qual código que deverá ser usado é a CFOP. Porém, podemos observar a partir da release 12.1.27, o ERP RM não considera a CFOP que está sendo utilizada no item de movimento.  
  
Neste cenário, o ERP não saberá qual o código de benefício fiscal deverá ser gerado no arquivo XML da nota fiscal.   
  
Portanto o ERP deverá ser adequado para que seja possível realizar tal emissão.

## **03. SOLUÇÃO**

Vamos passar a considerar na Emissão da NF-e tag cBenef da NFe 4.00, conforme a seguinte sequencia:

**1º - Código de Ajuste associado ao Item do Movimento, considerando a UF da Filial emitente e o CST do CFOP**

**Exemplo**

Considerando:

* Que o Código de Ajuste RJ801001 é aplicável aos CST's 30 e 40 e
* Que o Produto 01.01 possui o Código de Ajuste RJ801001 associado, então:

1. Na Filial do Rio de Janeiro, ao movimentar o Produto 01.01 com um CFOP que possui CST 30 ou 40, a tag cBenef deve ser preenchida com o "RJ801001".  
Se for qualquer outro CST, a tag não deve ser gerada.

2. Se a movimentação desse produto foi na Filial de Minas Gerais, como não há nenhum Código de Ajuste que seja de MG associado ao Produto, a tag também não deve ser gerada.

---

Ou, se não estiver preenchido:

**2º - Cadastro do Produto - Anexo Dados Fiscal por UF - Campo Código Fiscal.**

---

Ou, se não estiver preenchido:

**3º - A tag será preenchida com o Código de Ajuste associado ao CFOP informado no Item do Movimento se o campo Registro estiver com a opção "E115" selecionada e o Estado do respectivo cadastro for igual à UF da Filial emitente do documento eletrônico, além disso deve estar marcado um flag no Anexo de Dados Fiscais por UF do Cadastro do Produto, informando que o mesmo possui benefício fiscal.**
