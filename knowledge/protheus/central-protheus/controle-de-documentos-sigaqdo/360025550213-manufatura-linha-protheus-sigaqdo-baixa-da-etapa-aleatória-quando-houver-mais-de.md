---
article_id: 360025550213
category: Controle de Documentos (SIGAQDO)
content_hash: 335392fc659f9b761c7752de4d70b211de5ee5116faf3312b25b3d090782ecfd
fetched_at: '2026-06-28T22:42:28.950026+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Baixa da etapa aleatória quando houver
  mais de um responsável
type: support-article
updated_at: '2023-11-03T14:16:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025550213-Manufatura-Linha-Protheus-SIGAQDO-Baixa-da-etapa-aleat%C3%B3ria-quando-houver-mais-de-um-respons%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16793199074455) Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Durante a **revisão do documento**, quando determinada etapa possui mais de um responsável, é possível que apenas um dos usuários faça a **baixa da pendência** para prosseguir para a próxima etapa?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Para obrigar a baixa da pendência por apenas um dos usuários da etapa, o parâmetro **MV\_QDBXALE - Define se a baixa da Etapa devera ser aleatória quando houver mais de um responsável na etapa**, deve ser preenchido como **S - Sim**.  
Desta forma, são geradas as pendências para todos os responsáveis das etapas e quando um usuário realizar a baixa, a **revisão do documento** segue para a próxima etapa.  
  
**Importante**  
Para o correto funcionamento da baixa aleatória, as configurações do **QDOA020 - Tipo de Documento** devem estar de acordo com a **Dica** do documento [Finalizar Documento](https://tdn.totvs.com/x/EypKEg).
