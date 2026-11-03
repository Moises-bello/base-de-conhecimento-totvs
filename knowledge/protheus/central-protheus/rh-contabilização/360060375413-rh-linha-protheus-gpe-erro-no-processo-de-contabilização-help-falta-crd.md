---
article_id: 360060375413
category: RH - Contabilização
content_hash: 4e224866e44dbac843e414c129e2f2f8cb5391fa0d703e5f75a29c6c272db9be
fetched_at: '2026-06-28T22:43:46.120793+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro no processo de Contabilização - Help: FALTA
  CRD'
type: support-article
updated_at: '2025-07-30T02:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060375413-RH-Linha-Protheus-GPE-Erro-no-processo-de-Contabiliza%C3%A7%C3%A3o-Help-FALTA-CRD
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33810958882583) Tempo aproximado para leitura: 00:01:30 min**

**Ocorrência**Erro no processo de Contabilização - Help: FALTA CRD.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois uma ou mais verbas não estão gerando a informação na coluna **Cta Credito** da **Contabilização - GPEM110**, esta informação é gerada pelo **Lançamento Padrão - CTBA080** atribuído a verba no campo **Lcto. Padrão (RV\_LCTOP)** do cadastro de **Verbas - GPEA040**.

**Solução**Erro apresentado:  **![HELP_FALTA_CRD.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101165293)**

Para solucionar essa ocorrência siga os procedimentos:   
  
1- Identifique na tela de dados da contabilização os lançamentos que não estão gravando a informação de Conta Crédito, no print abaixo é possível identificar que o lançamento sem esse conteúdo.  
![contabiliza__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360101165393)  
  
2 - Verifique a parametrização da verba 520 - Mensalidade Sindical, assim é possível identificar o Lançamento Padrão atribuído a esta no campo **Lcto. Padrão**  
Acesse: **Atualizações** -> **Definições de Cálculo** -> **Verbas**:  na aba **Contabilização** é possível verificar o conteúdo do campo.  
![verbas.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000074881)  
  
3 - Identificado o Lançamento Padrão que esta ocasionando este erro, analise o conteúdo do campo **Cta Credito** da rotina **Lançamento Padrão** no exemplo abaixo o motivo foi ausência de informação.  
Acesse: **Atualizações** -> **Cadastros** -> **Lançamento Padrão**: na aba **Entidades** valide o conteúdo e ajuste.  
![lan_amento_padrao_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000074882)  
**Obs.**: No cadastro de Verbas também é possível verificar o conteúdo deste campo, mas o ajuste deve ser realizado diretamente na rotina **Lançamento Padrão**.  
  
4 - Efetue a Contabilização - GPEM110 novamente e valide se a rotina passou a apresentar conteúdo para a coluna de **Cta Credito**.  
Acesse: **Miscelânea** -> **Fechamentos** -> **Contabilização**:   
![contabiliza__o_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360098949914)
