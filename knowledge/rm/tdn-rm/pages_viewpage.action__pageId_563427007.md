---
content_hash: 945c715c4f7610939266fefb93aa2143d5f10534598e07271f8441113f07fde2
fetched_at: '2026-06-29T00:10:50.784302+00:00'
page_id: '563427007'
product: rm
source: tdn-rm
title: Validação Procedimento em Período de Retorno
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563427007
version: 18
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas**
   1. **Parâmetros Gerais**
   2. **Condições Contratuais com Convênios**
4. **Tela Parcial**
   1. **Principais Campos e Parâmetros**
5. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Ao executar o processo "Encerramento de Parcial", será retornada a mensagem "Procedimento de Consulta está no período de retorno." caso:

* O parâmetro "Mostrar relatório com mensagens não impeditivas" esteja marcado;
* E o procedimento está dentro da faixa de codificação do Retorno de Consulta do convênio;
* E o tempo entre o encerramento da parcial e data de realização do procedimento está dentro do período de Retorno de Consulta (Exemplo: um procedimento foi realizado há 40 dias e Período de Retorno é de 50 dias);

Por ser apenas um alerta, não cancela o encerramento da parcial.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Telas

## **03. TELAS**

filhosParâmetros Gerais

### **3.1****Parâmetros Gerais**

É possível alterar o valor do parâmetro "Mostrar relatório com mensagens não impeditivas" em Ambiente→ Parâmetros Gerais→ Faturamento

Condições Contratuais com Convênios

### **3.2****Condições Contratuais com Convênios**

É possível alterar o período de Retorno de Consulta em Condições Contratuais de Convênio → Retorno de Consulta. Para mais informações sobre esse anexo, acesse sua documentação .

Tela Parcial

## **04. TELA PARCIAL**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| Mostrar Relatório com Mensagens não impeditivas | Se marcado, ao encerrar a parcial os alertas também vão ser listados no relatório. |

## **05. TABELAS UTILIZADAS**

* SZCONDCONTRATRETORNO
* SZATENDIMENTO
* SZATENDHONORARIO
* SZPARCIALATEND
* SZFAIXACODIFICACAO
