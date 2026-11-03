---
article_id: 1500000077482
category: RH - Contabilização
content_hash: 9db2399872966c1a297524d93a788a3bd9030779454a06656c328bbec399814b
fetched_at: '2026-06-28T22:43:46.129537+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro no processo de Contabilização - O Item Contábil
  da Filial não foi encontrado no: CTD'
type: support-article
updated_at: '2025-07-30T02:19:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000077482-RH-Linha-Protheus-GPE-Erro-no-processo-de-Contabiliza%C3%A7%C3%A3o-O-Item-Cont%C3%A1bil-da-Filial-n%C3%A3o-foi-encontrado-no-CTD
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33810955058327) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Erro no processo de Contabilização - O Item Contábil da Filial não foi encontrado no: CTD.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois uma ou mais verbas não estão gerando a informação nas colunas **Item Debito e/ou Item Credito** da **Contabilização - GPEM110**, esta informação é gerada pelo **Lançamento Padrão - CTBA080** atribuído a verba no campo **Lcto. Padrão (RV\_LCTOP)** do cadastro de **Verbas - GPEA040**.

**Solução**  
Erro apresentado:  **![log_item_contabil.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101167453)**

Para solucionar essa ocorrência siga os procedimentos:   
  
1- Identifique na tela de dados da contabilização os lançamentos que não estão gravando a informação de Item Débito e/ou Item Crédito, no print abaixo é possível identificar os lançamentos sem esse conteúdo.  
![contabiliza__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360101167613)  
  
2 - Verifique a parametrização dos campos **Item Debito** e/ou **Item Credito** na rotina **Lançamento Padrão** das verbas que estão apresentando este problema, no exemplo abaixo o motivo foi ausência de informação.  
Acesse: **Atualizações** -> **Cadastros** -> **Lançamento Padrão**: na aba **Entidades** valide o conteúdo e ajuste.  
![lan_amento_padrao_ITEM_DEBITO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360101167893)  
**Obs.**: No cadastro de Verbas também é possível verificar o conteúdo destes campos, mas o ajuste deve ser realizado diretamente na rotina **Lançamento Padrão**.  
  
Outro situação que pode provocar esse erro é a ausência de conteúdo no campo **RD\_ITEM** da tabela **SRD - Acumulados,** este campo é preenchido na execução do cálculos **Por Roteiros - GPEM020** ou **Cálculo Múltiplos - GPEM020A,** a rotina coleta a informação do campo **Item (RA\_ITEM)** do cadastro de **Funcionários - GPEA010**![funcionarios.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000078101)  
  
4 - Efetue a Contabilização - GPEM110 novamente e valide se a rotina passou a apresentar conteúdo para as colunas **Item Debito e/ou Item Credito**.  
Acesse: **Miscelânea** -> **Fechamentos** -> **Contabilização**:   
![contabiliza__o_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000076701)
