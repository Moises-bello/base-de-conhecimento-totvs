---
article_id: 6295217661847
category: Controle de Não Conformidades (SIGAQNC)
content_hash: bb05825a79f7b665cd15ed4a4e7b9bd780a979df26b305aca102558c9bab8286
fetched_at: '2026-06-28T22:42:28.041442+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - QNCR070 - Não existem dados gerados
  para este Relatório. Verifique os parâmetros do relatório
type: support-article
updated_at: '2022-05-24T17:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6295217661847-Manufatura-Linha-Protheus-SIGAQNC-QNCR070-N%C3%A3o-existem-dados-gerados-para-este-Relat%C3%B3rio-Verifique-os-par%C3%A2metros-do-relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**No módulo **SIGAQNC - Controle de Não Conformidades**, ao tentar listar o relatório **QNCR070 - Diagrama de Causa e Efeito** é exibida a mensagem **Não existem dados gerados para este Relatório. Verifique os parâmetros do relatório**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Essa mensagem ocorre porque o **Plano de ação** selecionado para listagem não possui os requisitos necessários para geração do diagrama de causa e efeito.  
  
**Solução**Para que o relatório do **QNCR070** seja listado com sucesso é necessário ter alguns relacionamentos:  
1. Quando a **FNC - Ficha de Não Conformidade** for cadastrada na rotina **QNCA040 - Cadastro de Ocorrências/Não Conformidades**, o campo **QI2\_CODCAU - Cod Causa** deve ser informado;  
2. No **Plano de ação** relacionado à esta **FNC** na rotina **QNCA030 - Cadastro de Plano de Ação**, em **Outras Ações/Causa** deve ser relacionado o **Código da causa** para este plano, gerando a tabela **QI6 - Causas**;  
3. E ainda nesta rotina **QNCA030**, informar as etapas para este plano, em **Outras Ações/Ação/Etap**.
