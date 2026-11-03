---
article_id: 40096135957015
category: RH - Transferência
content_hash: 46a069a7314c7e4462eee10b34b2b1f22903f51c2e33cf8004b5e3fd85072f5b
fetched_at: '2026-06-28T22:43:23.397170+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Transferência de funcionário - Tabela RUM
type: support-article
updated_at: '2026-04-29T14:03:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40096135957015-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-funcion%C3%A1rio-Tabela-RUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40096140711063) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao realizar transferência de funcionário é gerado log com mensagem: Não foi possível efetuar a transferência para a matrícula. Ahgora: Registro do funcionário está na tabela RUM (Lote de integração Ahgora), porém não foi integrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40096140711447)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
A mensagem é gerada quando encontra pendencia de integração do funcionário com a Ahgora (tabela RUM).   
Para prosseguir é necessário confirmar a integração com a Ahgora via rotina GPEM929.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40096140711959)

**O que gera registros de Funcionário na RUM?:**  
Registros gravados pelas rotinas de Funcionário (GPEA010/GPEA265), Transferência (GPEA180), GPEM040 (Rescisão) ou Troca de Turno (PONA160).

**Saiba Mais**  
[Protheus x Ahgora - Integração funcionários e afastamentos](https://tdn.totvs.com/pages/viewpage.action?pageId=866520387)  
[Ahgora: Criação de API - Resultados](https://tdn.totvs.com/pages/viewpage.action?pageId=861541135)
