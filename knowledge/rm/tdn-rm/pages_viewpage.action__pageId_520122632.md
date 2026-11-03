---
content_hash: 745e8956e2f6899f61b16dacb542b2f250b2662537a4a44b3d82836888c08876
fetched_at: '2026-06-29T00:10:30.929090+00:00'
page_id: '520122632'
product: rm
source: tdn-rm
title: FISCAL01-11261 DT Registro T154 - IRRF Pessoa Física (Origem do Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520122632
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | TAF |
| Ticket: | FISCAL01-11261 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11261 |

## **02. SITUAÇÃO/REQUISITO**

**1.** Criar o contexto para a seleção dos lançamentos fiscais.

**2.** Buscar dados  
Devem ser selecionados os lançamentos que atendam aos seguintes requisitos:

●Cliente/Fornecedor seja Pessoa Física  
●Status "Normal"  
●Data esteja dentro do período selecionado para integração \*  
●Possuam um tributo do tipo IRRF "OU" IRRFPJ associado

Verificar se a apuração do IRRF/IRRFPJ está "olhando" para o parâmetro de data base do Financeiro. Se estiver,  
fazer a seleção das datas de acordo com este parâmetro. Ou seja, a seleção dos dados deve ser coerente com a  
apuração do tributo.

**3.** Ligar os campos no layout do Registro T154

## **03. SOLUÇÃO**

Foi criado o contexto Registro T154B, baseado nos lançamentos fiscais para a geração do do Registro T154. Todos os campos obrigatórios do Layout foram implementados:  
REGISTRO, NUMERO, SERIE, COD\_PARTICIPANTE, EMISSAO, NATUREZ, VLR\_BRUTO e TIPO\_RECIBO\_FATURA. Além dos campos não obrigatórios: CODMOD\_DOC, NUM\_DOC, SER\_DOC, SUBSER\_DOC, COD\_SERV\_MUN.  
    
Para a geração deste registro, o cliente fornecedor deverá ser Pessoa Física, o Lançamento deverá estar com Status Normal, a apuração do IRRF deverá está parametrizada como Emissão (obs: se estiver como Data de Baixa ou Vencimento, não será tratada nessa issue) e deve possuir o tributo IRRF.
