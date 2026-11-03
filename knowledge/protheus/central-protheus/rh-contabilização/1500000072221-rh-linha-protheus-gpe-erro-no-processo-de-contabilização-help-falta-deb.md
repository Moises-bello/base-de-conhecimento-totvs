---
article_id: 1500000072221
category: RH - Contabilização
content_hash: 0a953c66f353c1cd2b3321dd5a887ee484493827d884002e33d9f281e51de3c2
fetched_at: '2026-06-28T22:43:46.125156+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro no processo de contabilização - Help: FALTA
  DEB'
type: support-article
updated_at: '2025-07-30T02:20:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000072221-RH-Linha-Protheus-GPE-Erro-no-processo-de-contabiliza%C3%A7%C3%A3o-Help-FALTA-DEB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33810924336663) Tempo aproximado para leitura: 00:01:30 min**

**Ocorrência**Erro no processo de contabilização - Help: FALTA DEB.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois uma ou mais verbas não estão gerando a informação na coluna **Cta Debito** da **Contabilização - GPEM110**, esta informação é gerada pelo **Lançamento Padrão - CTBA080** atribuído a verba no campo **Lcto. Padrão (RV\_LCTOP)** do cadastro de **Verbas - GPEA040**.

**Solução**Erro apresentado:  **![help_falta_deb.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000070682)**

Para solucionar essa ocorrência siga os procedimentos:   
  
1- Identifique na tela de dados da contabilização os lançamentos que não estão gravando a informação de Conta Débito, no print abaixo é possível identificar que vários lançamentos de diferentes verbas estão sem esse conteúdo, possivelmente todas estão atribuídas a um mesmo lançamento.   
![contabiliza__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360098946314)  
  
2 - Verifique a parametrização da verba 001 - Salário Mensal, assim é possível identificar o Lançamento Padrão atribuído a esta no campo **Lcto. Padrão**  
Acesse: **Atualizações** -> **Definições de Cálculo** -> **Verbas**:  na aba **Contabilização** é possível verificar o conteúdo do campo.  
![verbas.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000071322)  
  
3 - Identificado o Lançamento Padrão que esta ocasionando este erro, analise o conteúdo do campo **Cta Debito** da rotina Lançamento Padrão no exemplo abaixo o motivo foi ausência de informação.  
Acesse: **Atualizações** -> **Cadastros** -> **Lançamento Padrão**: na aba **Entidades** valide o conteúdo e ajuste.  
![lan_amento_padrao_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360101162953)  
**Obs.**: No cadastro de Verbas também é possível verificar o conteúdo deste campo, mas o ajuste deve ser realizado diretamente na rotina Lançamento Padrão.  
  
4 - Efetue a Contabilização - GPEM110 novamente e valide se a rotina passou a apresentar conteúdo para a coluna de Cta Debito.  
Acesse: **Miscelânea** -> **Fechamentos** -> **Contabilização**:   
![contabiliza__o_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360098947174)
