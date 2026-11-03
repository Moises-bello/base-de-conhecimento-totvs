---
article_id: 23051105781783
category: GPE - eSocial - Processo Trabalhista
content_hash: cbeaa69a1c549df2527999f0dd0fe6ed49b7d259dc8f885cbcce8e1eeb0503a7
fetched_at: '2026-06-28T22:45:00.529361+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Como corrigir a ocorrência 8
  Grupo 'Grau de Exposicao a Agentes Nocivos' deve ser preenchido
type: support-article
updated_at: '2024-04-25T18:16:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23051105781783-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-corrigir-a-ocorr%C3%AAncia-8-Grupo-Grau-de-Exposicao-a-Agentes-Nocivos-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23051105761687) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como corrigir o Codigo da ocorrência: 8 para o evento S-2500?  
Localização: /eSocial/evtProcTrab/ideTrab/infoContr/ideEstab/infoVlr/idePeriodo[1]/baseCalculo  
Descrição: Grupo 'Grau de Exposicao a Agentes Nocivos' deve ser preenchido. Verifique as condicoes de preenchimento no leiaute.  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando existir o lançamento das bases de cálculo de contribuição previdenciária decorrentes de processo trabalhista e ainda não declaradas, é necessário o preenchido da *tag* [infoAgNocivo](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s-1-2-cons-nt-02-2024-rev-29-02-2024/index.html#2500_ideTrab_infoContr_ideEstab_infoVlr_idePeriodo_baseCalculo_infoAgNocivo).  
  
Para que o sistema gere as informações corretamente no xml do evento S-2500, é necessário acessar a rotina Dados eSocial (TAFA552D):  
- Clicar em Editar   
- Acessar aba Contrato de Trabalho  
- Clicar em Editar  
- Selecionar Identificação de Período  
- Editar o periodo   
- Selecionar a opção desejada no campo Grau de exposição a agentes nocivos  
- Para salvar a edição do periodo clique em Atualizar Periodo  
  
![smartclient_64dpgkLfs7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/23051112334359)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos do eSocial para Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847-RH-Linha-Protheus-GPE-eSocial-Processos-Trabalhistas-Premissas-para-gera%C3%A7%C3%A3o-dos-eventos-do-eSocial-para-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
