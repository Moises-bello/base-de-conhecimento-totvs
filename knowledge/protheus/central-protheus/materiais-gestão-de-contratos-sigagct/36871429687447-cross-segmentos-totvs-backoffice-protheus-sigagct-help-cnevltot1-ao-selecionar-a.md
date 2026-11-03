---
article_id: 36871429687447
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fee10e8c4a863735e111e53c1830d88563ac0c7b539060ee8ea2fc0698629538
fetched_at: '2026-06-28T22:37:22.907154+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNEVLTOT1 ao selecionar
  a Planilha ao incluir uma Medição de Contrato
type: support-article
updated_at: '2025-12-09T10:45:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36871429687447-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNEVLTOT1-ao-selecionar-a-Planilha-ao-incluir-uma-Medi%C3%A7%C3%A3o-de-Contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36871429670423) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Ao Confirmar a inclusão de uma medição está apresentando o "Help CNEVLTOT1 - Problema: Existe inconsistência no item 001 - O valor Total informado é maior do que o saldo do item"

ao tentar selecionar a planilha onde serão gatilhados os itens para a medição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36871495357463)

**Ambiente**

Protheus – Gestão de Contratos – A partir da versão 12.1.23

**Solução**

A mensagem CNEVLTOT1 em questão o selecionar uma planilha na inclusão de medição, possui ocorrência da validação conforme abaixo:  
   
*"a validação "CNEVLTOT1" normalmente ocorre quando o valor total (CNE\_VLTOT) informado na medição/item da planilha é maior do que o saldo existente do item em questão (CNE\_QTAMED \* CNE\_VLUNIT) da medição."*  
   
   
Além dessa informação, um teste que pode ser realizado para o contrato em específico que ocorre a mensagem, é a execução em ambiente de homologação do recalculo dos saldos do contrato conforme as instruções do artigo abaixo, verificando se é modificado alguma informação ou ainda persiste:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Ajuste de Saldos em Contratos, Planilhas e Cronograma Financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Ajuste-de-Saldos-em-Contratos-Planilhas-e-Cronograma-Financeiro-?source=search)  
 

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[SIGAGCT - Como realizar medições com valores maior que o previsto no Cronograma Financeiro do Contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051964674-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-medi%C3%A7%C3%B5es-com-valores-maior-que-o-previsto-no-Cronograma-Financeiro-do-Contrato-?source=search)
