---
article_id: 360025484213
category: Controle de Documentos (SIGAQDO)
content_hash: d1412cc916a1127b14236b3769ddfa5d46f34b30ecda130dfbb69a7929f3c9ec
fetched_at: '2026-06-28T22:42:29.078939+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Falha de integridade de base na rotina
  Status Gerais
type: support-article
updated_at: '2021-09-08T12:58:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025484213-Manufatura-Linha-Protheus-SIGAQDO-Falha-de-integridade-de-base-na-rotina-Status-Gerais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**  
**Ocorrência**Na rotina **Status Gerais - QDOM020**, a linha **Integridade Base** apresenta um alerta. Ao clicar no botão **Mostra log**, é apresentada a mensagem que o **CC - Centro de Custo** ou **Matrícula** estão inválidos.   
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Este alerta é apresentado devido à inconsistência de informações entre a tabela **QAD - Departamento/Setor** e as tabelas **QDJ - Destinos**, **QDG - Destinatários** e **QD1 - Distribuição por usuário**.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Abra a tabela **QDJ** através do **APSDU** e filtre pelo campo **QDJ\_DEPTO - Código do Departamento** igual ao departamento exibido no **log** de integridade de base.  
2. Verifique qual é o conteúdo do campo **QDJ\_FILMAT - Filial do Sistema** deste registro.   
3. Abra a tabela **QAD** através do **APSDU** e filtre pelo **QAD\_CUSTO - Código do Departamento** igual a departamento filtrado no passo 1. O campo **QAD\_FILIAL - Filial Sistema** precisa ser igual ao **QDJ\_FILMAT**.  
4. Repetir esta verificação para os demais campos abaixo:  
**QDJ\_FILMAT = QAD.QAD\_FILIAL**  
**QDJ\_DEPTO = QAD.QAD\_CUSTO**  
**QD1\_FILMAT - Filial do Sistema = QAA.QAA\_FILIAL - Filial**  
**QD1\_MAT - Código do Usuário = QAA.QAA\_MAT - Código do Usuário**  
**QDG\_FILMAT - Código da Filial do Usuário = QAA.QAA\_FILIAL**  
**QDG\_MAT - Código do Usuário = QAA.QAA\_MAT**  
  
**Importante**  
Caso o alerta indicar inconsistência com a **matrícula**, os campos abaixo devem serem iguais entre as tabelas:  
**QDG\_FILMAT = QAA.QAA\_FILIAL**  
**QDG\_MAT = QAA.QAA\_MAT**
