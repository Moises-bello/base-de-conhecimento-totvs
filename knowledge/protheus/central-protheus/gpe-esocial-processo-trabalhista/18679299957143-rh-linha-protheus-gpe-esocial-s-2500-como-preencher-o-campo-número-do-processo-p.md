---
article_id: 18679299957143
category: GPE - eSocial - Processo Trabalhista
content_hash: 586f5a3394b9ffdc0510bf8c4cc7b658885a9a913b7d4cb0fb54a9df9caf54cf
fetched_at: '2026-06-28T22:45:00.584793+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Como preencher o campo número
  do processo para o eSocial
type: support-article
updated_at: '2023-10-30T20:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18679299957143-RH-Linha-Protheus-GPE-eSocial-S-2500-Como-preencher-o-campo-n%C3%BAmero-do-processo-para-o-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18679299941399) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como preencher o campo número do processo para o eSocial?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**De acordo com o leiaute do eSocial vigente, o evento S-2500 possui o grupo [infoProcesso](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#r_2500_infoProcesso) onde é necessário preencher a tag nrProcTrab com a seguinte validação:  
  
**Número do processo trabalhista**, da ata ou número de identificação da conciliação.  
**Validação:** Se [origem](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_infoProcesso_origem) = [1], deve ser um processo judicial válido, com 20 (vinte) algarismos. Se [origem](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/#2500_infoProcesso_origem) = [2], deve possuir 15 (quinze) algarismos.  
  
Portanto acesse a rotina Processos (APTA100), localizada em **Atualizações - Processos Trabalhistas - Processos - Processos.**No campo Nº Processo inclua a numeração valida de acordo com a validação do leiaute: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/18679288776983)**Verifique na rotina Dados eSocial (TAFA552D) se o campo foi preenchido corretamente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18679294991383)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
**Próximos Treinamentos**[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
