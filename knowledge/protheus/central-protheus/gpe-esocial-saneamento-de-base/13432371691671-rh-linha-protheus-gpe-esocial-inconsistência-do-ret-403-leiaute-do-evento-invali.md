---
article_id: 13432371691671
category: GPE - eSocial - Saneamento de Base
content_hash: 7515b752053e422f285defa4b2d46ed16372a5afb2cf4a013925e200538a9d28
fetched_at: '2026-06-28T22:45:01.515854+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Inconsistência do RET - 403 - Leiaute
  do evento invalido
type: support-article
updated_at: '2024-06-24T11:41:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13432371691671-RH-Linha-Protheus-GPE-eSocial-Inconsist%C3%AAncia-do-RET-403-Leiaute-do-evento-invalido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24318764826647) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao tentar transmitir os eventos S-2206, S-2200, S-1200, entre outros do eSocial, o governo retorna a inconsistência:

Código da Resposta: **403 - Leiaute do evento invalido** ou **Tipo Advertência - Código da ocorrência: Descrição: Leiaute do evento invalido**  
  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24320323551255)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**A partir da data de **21/01/2024**, passa a ser obrigatória a transmissão dos eventos do eSocial no novo **Leiaute S-1.2**. O Governo não aceitará transmissões no antigo **Leiaute S-1.1**.  
  
**Solução**Para solucionar essa ocorrência, será necessário alterar os parâmetros **MV\_VLESOC e MV\_TAFVLES** e atualizar os ambientes conforme documentação abaixo:  
[RH - Linha Protheus - GPE - eSocial - Como se adequar e atualizar o ambiente para o eSocial leiaute S-1.2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8658568031127-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-e-atualizar-o-ambiente-para-o-eSocial-leiaute-S-1-2?source=search)  
  
**Atenção:** Esta atualização possui dicionário de dados, sendo necessário rodar o UPDDISTR.  
  
**Observação:**Se o registro (evento) no TAF, foi integrado no **Leiaute S-1.1**, será necessário excluir o evento no TAF, e após alterar para o **Leiaute S-1.2**, é necessário integrar o registro novamente do GPE para o TAF.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
