---
article_id: 1500004324601
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 3e83e4881d654d5dd23dd47804dbb9e98813baca33fd0b6cc975795690fa16fc
fetched_at: '2026-06-28T22:42:27.968380+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Help QN030NEETA no QNCA030
type: support-article
updated_at: '2021-05-12T21:00:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004324601-Manufatura-Linha-Protheus-SIGAQNC-Help-QN030NEETA-no-QNCA030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQNC - Controle de Não Conformidades**, ao tentar finalizar a inclusão de um plano de ação na rotina **QNCA030 - Cadastro de Plano de Ação** é exibido o *help* **QN030NEETA**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**O *help* **QN030NEETA** é exibido quando o parâmetro **MV\_QNCACOB - Define se e possível finalizar o plano com o cadastramento obrigatório das ações/etapas** está com conteúdo igual à **1 - Sim** e não foram informadas as etapas para este plano em **Outras Ações/Ação/Etap** na rotina **QNCA030**.  
  
**Solução**Para solucionar essa ocorrência, verifique se o conteúdo do parâmetro **MV\_QNCACOB** está correto.  
Se o parâmetro estiver com conteúdo igual à **1 - Sim**, para finalizar a inclusão do plano, deve-se informar as etapas deste plano, por meio da opção **Outras Ações/Ação/Etap** na rotina **QNCA030**.  
Mas, se o parâmetro estiver com conteúdo igual à **2 - Não**, as etapas não são obrigatórias e é possível finalizar a inclusão do plano de ação sem informá-las.
