---
article_id: 9173632088343
category: eSocial - Gerar XML/ Integração Evento
content_hash: 95a7b9e54e3d00d0f80ae3182479f1b7143c3afa22e1e90b9cb3cf9b92dd84db
fetched_at: '2026-06-28T22:47:12.162330+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 675 na integração com governo: Não é permitida
  a exclusão de evento de Admissão S-2200, Trabalhador Sem Vínculo S-2300 e Registro
  Preliminar S-2190 quando já existirem outros eventos trabalhistas para o mesmo vínculo'
type: support-article
updated_at: '2025-12-29T14:24:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9173632088343-RH-RM-FOP-eSocial-Erro-675-na-integra%C3%A7%C3%A3o-com-governo-N%C3%A3o-%C3%A9-permitida-a-exclus%C3%A3o-de-evento-de-Admiss%C3%A3o-S-2200-Trabalhador-Sem-V%C3%ADnculo-S-2300-e-Registro-Preliminar-S-2190-quando-j%C3%A1-existirem-outros-eventos-trabalhistas-para-o-mesmo-v%C3%ADnculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24346855147799) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao encaminhar a exclusão de um evento S-2190, S-2200 ou S-2300 ocorre o erro **675: Não é permitida a exclusão de evento de Admissão S-2200, Trabalhador Sem Vínculo S-2300 e Registro Preliminar S-2190 quando já existirem outros eventos trabalhistas para o mesmo vínculo/contrato.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9173244948375)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Ao encaminhar um evento de exclusão do **2200 (Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhador), S-2300 (Trabalhador Sem Vínculo de Emprego/Estatuário - Início) ou S-2190 (Admissão Preliminar)**, porém no portal do governo já constam eventos posteriores a admissão, o que ocasiona o erro.  
  
**Solução**  
Para correção da ocorrência siga os seguintes passos:  
1. Será necessário encaminhar o S-3000 - [exclusão dos eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos) posteriores à admissão e que constam no portal do governo.   
2. Após não possuir mais nenhum evento para o funcionário, a exclusão do S-2200, S-2300 ou S-2190, poderá ser realizada.
