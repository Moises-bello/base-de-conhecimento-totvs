---
article_id: 360054292814
category: GPE - eSocial - Não Periódicos
content_hash: 0460bf2e5fe48ee542370601161d9cac05c0cc43747ea851e133fbb8570311d4
fetched_at: '2026-06-28T22:45:05.856488+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Inconsistência do RET - 191
  - Não e permitido o desligamento do trabalhador. Verificar se o trabalhador encontra-se
  ativo
type: support-article
updated_at: '2026-06-16T10:56:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054292814-RH-Linha-Protheus-GPE-eSocial-S-2299-Inconsist%C3%AAncia-do-RET-191-N%C3%A3o-e-permitido-o-desligamento-do-trabalhador-Verificar-se-o-trabalhador-encontra-se-ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26176289556247) Tempo aproximado para leitura:**00:01:00 min**  
  
**Ocorrência**  
S-2299 - Código da ocorrência: 191  
Descrição: Não é permitido o desligamento do trabalhador. Acões Sugeridas:- Verificar se o trabalhador encontra-se ativo. Verificar se o motivo do desligamento do trabalhador e compatível com o desligamento sem retorno do afastamento ou sem o fim da cessao/exercicio em outro orgão.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Esse incidente tem várias causas as mais conhecidas estão relacionadas com a data fim de afastamento não preenchidas no RET, ou seja, o usuário esta tentando transmitir o desligamento para um funcionário que ainda esta afastado.  
Somente **é permitido** o envio de evento de Desligamento para trabalhador afastado temporariamente ou cedido/em exercício em outro órgão se o **motivo de desligamento for igual a (07, 09, 10, 11, 12, 13, 14, 16, 21, 22, 23, 24, 25, 26, 29, 30, 32, 34, 36, 37, 38, 39, 40, 43, 44, 47, 48, 49)**. Para essa regra, considerar como data de desligamento a maior data entre {dtDeslig} e {dtProjFimAPI} do evento S-2299. Para os demais tipos de afastamentos temporários, obrigatoriamente deverá haver o retorno antes do envio do desligamento.  
  
**Solução**  
Verificar no RET se o afastamento esta sem data fim, deverá ser transmitido o retorno do afastamento para desligamentos diferentes dos informados no paragrafo anterior.  
[RH - Linha Protheus - GPE - eSocial - S-2230 - Como consultar no site do eSocial dados do evento S-2230 (Afastamento Temporário)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040817794-RH-Linha-Protheus-GPE-eSocial-S-2230-Como-consultar-no-site-do-eSocial-dados-do-evento-S-2230-Afastamento-Tempor%C3%A1rio)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
