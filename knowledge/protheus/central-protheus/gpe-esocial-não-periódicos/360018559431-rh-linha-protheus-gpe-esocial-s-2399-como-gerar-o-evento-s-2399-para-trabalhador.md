---
article_id: 360018559431
category: GPE - eSocial - Não Periódicos
content_hash: 26d778be4a9ce79f23f3c16a135624777f68fdebd6b7a2fa8e40ae25229a25e8
fetched_at: '2026-06-28T22:45:05.944999+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2399 - Como gerar o Evento S-2399 para
  Trabalhadores Sem Vínculo
type: support-article
updated_at: '2026-06-16T12:56:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559431-RH-Linha-Protheus-GPE-eSocial-S-2399-Como-gerar-o-Evento-S-2399-para-Trabalhadores-Sem-V%C3%ADnculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28088227507479)** Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como gerar o Evento S-2399 para Trabalhadores Sem Vínculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Para gerar o Evento **S-2399** referente ao Término de contrato de Trabalhador Sem Vínculo, a **categoria para o esocial deve ser 721**, no cadastro do Trabalhado do **GPE** pode ser informada a data de demissão e a situação da Folha igual a "**D**".  
  
De acordo com o MOS S-1.1, no evento S-2399 (Trabalhador Sem Vínculo de Emprego/Estatutário - Término), a informação relativa às verbas rescisórias devidas deve ser prestada, neste evento, no grupo [verbasResc] **apenas em relação aos diretores não empregados com FGTS - categoria [721].** Nos demais casos, **as verbas rescisórias devidas devem ser informadas nos eventos S-1200 ou S-1202,****conforme o regime previdenciário do trabalhador.**  
  
Porém, **caso hajam valores a serem pagos no momento do encerramento do contrato sugerimos utilizar uma das opções abaixo:**  
  
**1.** Para **Trabalhadores Sem Vínculos com categoria 721**, há a possibilidade de gerar o **Evento S-2399** através da rotina do cálculo de Rescisão do GPE, para essa parametrização consulte: [MP - GPE - eSocial - S-2399 - Como calcular Rescisão para Trabalhador Sem Vínculos através da rotina de Rescisão do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026463573)  
  
**2.** Para Estagiários, categoria do eSocial **901**, será gerado o evento S-1200 através da rotina do cálculo de Rescisão do **GPE**, para essa parametrização consulte: **[MP - GPE - eSocial - S-1200 - Como calcular Rescisão para Estagiário através da rotina de Rescisão do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466213)** **3.** Para **Trabalhadores Sem Vínculos das demais categorias**, também será gerado os valores rescisórios no evento **S-1200** através da rotina do cálculo de Rescisão do GPE, para essa parametrização consulte: [MP - GPE - eSocial - S-2399 - Como calcular Rescisão para Trabalhador Sem Vínculos através da rotina de Rescisão do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026463573)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
