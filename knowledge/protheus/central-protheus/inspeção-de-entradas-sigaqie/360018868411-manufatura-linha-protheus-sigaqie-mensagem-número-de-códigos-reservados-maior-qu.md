---
article_id: 360018868411
category: Inspeção de Entradas (SIGAQIE)
content_hash: 46afbdca8d0b728b0815e0d1809a918d8401cfa559bda21e6b44ac2db0828ff9
fetched_at: '2026-06-28T22:42:27.075071+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIE - Mensagem: Número de códigos reservados
  maior que 20'
type: support-article
updated_at: '2021-05-27T11:05:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018868411-Manufatura-Linha-Protheus-SIGAQIE-Mensagem-N%C3%BAmero-de-c%C3%B3digos-reservados-maior-que-20
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:20 min  
  
Ocorrência**Ao realizar a inspeção de entrada, por meio da rotina de **QIEA215 - Resultados**, informando uma **FNC - Ficha de Não Conformidade**, o Sistema apresenta mensagem **Numero de códigos reservados maior que 20**.  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
 **Causa**Geralmente a mensagem é apresentada devido a registros deletados na tabela **QI2 - Não Conformidades**. O controle de numeração automática, por conceito, consegue reservar até 20 números na montagem do código da **FNC**.  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verificar em ambiente homologação a existência de registros deletados na tabela de não conformidades - **QI2**, realizando *pack* via **APSDU**.   
  
2. Validar o campo **Chave** - **QE\_CHAVE** se preenchido com o ano corrente. Exemplo: 2019;  
  
3. O campo **Tamanho** - **QE\_TAMANHO** deve estar preenchido com 11;  
  
4. Verificar se o campo **Numero** - **QE\_NUMERO** já existe no Sistema. Caso sim, ajustar manualmente para o próximo número.  
**Exemplo:** Na tabela **QNSXE** a próxima numeração está como 00000000174, porém a última **FNC** que consta no Sistema é a 00000000175. Neste exemplo seria necessário alterar na **QNSXE** para 00000000176 para resolver o erro. Na tabela **QNSXF** não é necessária alteração.
