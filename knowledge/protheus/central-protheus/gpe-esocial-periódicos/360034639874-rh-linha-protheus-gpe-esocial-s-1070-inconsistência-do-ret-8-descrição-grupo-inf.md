---
article_id: 360034639874
category: GPE - eSocial - Periódicos
content_hash: 080d1456c72d182f92f9c5acb3ec6458246d4b163a539a012fa4e9162630158b
fetched_at: '2026-06-28T22:45:07.640229+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1070 - Inconsistência do RET 8 - Descrição:
  Grupo ''Informacoes da Suspensao'' deve ser preenchido. Verifique as condicoes de
  preenchimento no leiaute'
type: support-article
updated_at: '2025-07-28T18:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034639874-RH-Linha-Protheus-GPE-eSocial-S-1070-Inconsist%C3%AAncia-do-RET-8-Descri%C3%A7%C3%A3o-Grupo-Informacoes-da-Suspensao-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33773500103575) Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**Inconsistência do RET 8 - Descrição: Grupo '**Informações da Suspensão'** deve ser preenchido. Verifique as condições de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**   
Esse retorno ocorre devido a existir uma **divergência** entre o compartilhamento (modo de acesso) das tabelas relacionadas ao evento **S-1070**, ou devido ao usuário não preencher as informações de suspensão do processo responsável por alimentar o grupo de **TAGs** do XML **infoSusp** (Informações de suspensão de exigibilidade de tributos em virtude de processo administrativo ou judicial.)  
  
**​​****Solução**Para correção efetue os seguintes procedimentos:  
  
1. Verifique se o compartilhamento (modo de acesso) das tabelas do evento **S-1070** estão iguais. Todas as tabelas utilizadas no evento devem ter o mesmo compartilhamento.  
Para verificar as tabelas do evento **S-1070** acesse o ***Link*:** [Relação das rotinas x Eventos x Tabelas do TAF para o eSocial](https://tdn.totvs.com/x/M6m1F).  
  
2. Caso esteja tudo correto verifique no modulo SIGATAF (84) se as Informações de Suspensão estão preenchidas para o processo cadastrado.  
**Caminho**: Atualizações > Eventos eSocial > Tabelas > Processos Administrativos/Judiciais*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045881173)***Abaixo de descrição e regra dos campos:****Código Susp.:** Código do Indicativo da Suspensão **(Esse código é o usuário que defini, não existe um código especifico).****Id.Ind.Susp.:**Indicativo de suspensão da exigibilidade **(existe varias opções que deve ser preenchida de acordo com o processo).**Observação:

* Se o tipo de processo for 1 (Administrativo) só pode ser escolhida a opção [03, 14, 92] nesse campo;
* Se o tipo de processo for 2 (Judicial) só pode ser escolhida a opção [01, 02, 04, 05, 08, 09, 10, 11, 12, 13, 90, 92] nesse campo;
* Se o tipo de processo for 4 (Processo FAP) só pode ser escolhida a opção [14] nesse campo;

**Dt. Decisão:** Data da decisão, sentença ou despacho administrativo.  
 **Ind. Depósito:** Indicativo de Depósito do Montante Integral.  
  
Observação:

* Se **Id.Ind.Susp** for = [90], preencher obrigatoriamente deve ser [N].
* Se **Id.Ind.Susp**for = [02, 03] preencher obrigatoriamente deve ser [S].

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-1070](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052499193)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
  
  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
