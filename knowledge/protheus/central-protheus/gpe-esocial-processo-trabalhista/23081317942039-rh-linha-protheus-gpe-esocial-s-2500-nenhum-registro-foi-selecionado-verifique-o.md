---
article_id: 23081317942039
category: GPE - eSocial - Processo Trabalhista
content_hash: 4144c38bcf580e526ccb91db855dccc2a1744035efac0412fa6aab8b5734b378
fetched_at: '2026-06-28T22:45:00.521816+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Nenhum registro foi selecionado,
  verifique os parâmetros selecionados
type: support-article
updated_at: '2024-04-29T13:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23081317942039-RH-Linha-Protheus-GPE-eSocial-S-2500-Nenhum-registro-foi-selecionado-verifique-os-par%C3%A2metros-selecionados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23081317911447) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo SIGAGPE, ao tentar realizar a geração e integração do evento S-2500 através da rotina **Eventos Processos Trabalhistas (GPEM038)** é apresentada a mensagem **Nenhum registro foi selecionado, verifique os parâmetros selecionados  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23088394736919)**  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Essa mensagem é apresentada quando os parâmetros e filtros para geração do evento não foram preenchidos corretamente  
  
**Solução**1. Verifique se o número do processo cadastrado está seguindo a regra do eSocial:   
**Número do processo trabalhista, da ata ou número de identificação da conciliação.**  
**Validação: Se [origem](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2500_infoProcesso_origem) = [1], deve ser um processo judicial válido, com 20 (vinte) algarismos.**  
**Se [origem](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/index.html#2500_infoProcesso_origem) = [2], deve possuir 15 (quinze) algarismos  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23081332446871)**2. Verifique se foi realizado o preenchimento dos parâmetros e filtros para geração do evento corretamente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23126058574743)  
Para mais detalhes acesse a documentação abaixo:  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Como realizar a geração dos eventos de processo trabalhista na rotina GPEM038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12412564333719-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Como-realizar-a-gera%C3%A7%C3%A3o-dos-eventos-de-processo-trabalhista-na-rotina-GPEM038?source=search)  
 **Saiba Mais**Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Premissas-para-gera%C3%A7%C3%A3o-dos-eventos-do-eSocial-para-Processos-Trabalhistas?source=search)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
