---
article_id: 360047007414
category: Controle de Documentos (SIGAQDO)
content_hash: 00b98d08252872eed6e5f1a73800c8930898bfd83a2b9d7b954974586e2bc069
fetched_at: '2026-06-28T22:42:29.065585+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Exibição do arquivo txt para aviso
  de documento
type: support-article
updated_at: '2021-05-19T20:31:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047007414-Manufatura-Linha-Protheus-SIGAQDO-Exibi%C3%A7%C3%A3o-do-arquivo-txt-para-aviso-de-documento
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:25 min**  
**Dúvida**Como definir se o aquivo **txt** de aviso de documento será exibido ao usuário?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**A exibição do aviso de documento é definido pelo parâmetro **MV\_QDOGEAV - define se gera avisos no documento (1-SIM / 2-NAO)**. Quando o parâmetro **MV\_QDOGEAV** estiver ativo, gera aviso de:

* Ausência temporária;
* Documento vencido;
* Pendências;
* Referência para o elaborador
* Inclusão de questionário;
* Necessidade de realizar treinamento;
* Solicitação de novo documento;
* Solicitação de alteração de documento;
* Agendamento de treinamento;
* Cancelamento de documento.

**Importante**  
Ao desativar este parâmetro, nenhum dos avisos citados acima será exibido ao usuário.
