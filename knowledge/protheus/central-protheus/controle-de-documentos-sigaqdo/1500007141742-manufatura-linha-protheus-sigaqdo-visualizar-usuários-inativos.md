---
article_id: 1500007141742
category: Controle de Documentos (SIGAQDO)
content_hash: a6359a84c440f236a4e5701e1100bd1273c35c419ce63267ddedf59689956a40
fetched_at: '2026-06-28T22:42:29.976014+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Visualizar usuários inativos
type: support-article
updated_at: '2022-04-26T20:15:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007141742-Manufatura-Linha-Protheus-SIGAQDO-Visualizar-usu%C3%A1rios-inativos
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**É possível visualizar os usuários inativos na rotina **QAXA010 - Cadastro de Usuários**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para que seja possível visualizar os usuários inativos na rotina **QAXA010** é necessário que o parâmetro **MV\_QUSRINA - Define se deverá aparecer no Browser os Usuários Inativos** tenha conteúdo igual à **S-Sim**. Desta forma, ao acessar a opção **Outras Ações/Mostrar Inativos** da rotina **QAXA010**, os usuários inativos serão exibidos.  
  
**Importante**  
À partir da *release* 12.1.2210 ou a rotina **QAXA010** com data superior à 29/03/2022, não será mais validado o conteúdo do parâmetro **MV\_QUSRINA**. Será necessário apenas acessar a opção **Outras Ações**/**Mostrar Inativos** da rotina **QAXA010**.
