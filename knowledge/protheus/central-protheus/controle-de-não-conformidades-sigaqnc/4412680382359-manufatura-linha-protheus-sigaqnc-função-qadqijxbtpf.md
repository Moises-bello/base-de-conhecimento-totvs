---
article_id: 4412680382359
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 43d04cd1a60a104140bfdc2565276e8384f581e63281b167cfc8fc971a1c9ca8
fetched_at: '2026-06-28T22:42:27.954506+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Função QADQIJXBTPF
type: support-article
updated_at: '2021-11-09T17:53:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412680382359-Manufatura-Linha-Protheus-SIGAQNC-Fun%C3%A7%C3%A3o-QADQIJXBTPF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min** **Ocorrência**Na inclusão de uma **FNC - Ficha de Não Conformidade** na rotina **QNCA040 - Cadastro de Ocorrências/Não Conformidades** é exibido o *help* **NOFUNCW - Opção não disponível no Protheus Função: QADQIJXBTPF Called By {((QAD\_FILIAL+QAD\_CUSTO>=QadQIJXBTpF(). And. QAD\_FILIAL+QAD\_CUSTO**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus)  - Controle de Não Conformidades (SIGAQNC) - Todas as versões  
  
**Causa**Este *help* ocorre devido uma inconsistência na consulta padrão dos campos **QI2\_ORIDEP - Departamento Origem** e **QI2\_DESDEP - Departamento Destino**.  
  
**Solução**  
Para correção deste *help* é necessário aplicar o pacote de atualizações do módulo **SIGAQNC - Controle de Não Conformidades** disponível no *link* [Pacotes de Atualização - QNC - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=566491913) e também atualizar o dicionário de dados conforme documentado no *link* acima.
