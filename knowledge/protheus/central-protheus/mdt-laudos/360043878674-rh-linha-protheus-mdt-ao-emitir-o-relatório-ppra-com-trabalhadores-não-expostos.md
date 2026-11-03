---
article_id: 360043878674
category: MDT - Laudos
content_hash: 49d96253ee511d47a4cdd7e5fcc2eb281d2f697e13201b1205f62695d1064f31
fetched_at: '2026-06-28T22:44:26.176500+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Ao emitir o relatório PPRA com trabalhadores Não Expostos
  a Riscos está sendo gerado funcionários desligados que estavam em exposição ao risco
  até a sua data de saída
type: support-article
updated_at: '2025-09-03T14:29:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043878674-RH-Linha-Protheus-MDT-Ao-emitir-o-relat%C3%B3rio-PPRA-com-trabalhadores-N%C3%A3o-Expostos-a-Riscos-est%C3%A1-sendo-gerado-funcion%C3%A1rios-desligados-que-estavam-em-exposi%C3%A7%C3%A3o-ao-risco-at%C3%A9-a-sua-data-de-sa%C3%ADda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27597489867415)**Tempo aproximado para leitura: 00:01:00 min  
  
**Dúvida**Ao emitir o relatório **PPRA** (Programa de Prevenção de Riscos Ambientais) com trabalhadores **Não Expostos a Riscos** está sendo gerado funcionários **desligados** que estavam em exposição ao risco até a sua **data de saída.**  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Verifique no cadastro do laudo o campo **Data Fim** se ela estiver preenchida com uma data incorreta pode apresentar trabalhadores desligados.  
  
Obs: Esse artigo aplica-se a geração de PPRA para trabalhadores não expostos a riscos. Para saber como gerar esse relatório consulte: [MP - MDT - Como emitir um relatório PPRA com trabalhadores não expostos a Riscos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044355793)  
  
**Exemplo:**  
**1.** Rotina Laudos.  
Caminho SIGAMDT: atualizações > laudos > laudos![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060047733)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059187134)  
  
**2.** Rotina Riscos.  
Caminho SIGAMDT: atualizações > PPRA > riscos  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060047933)  
  
Funcionários expostos ao risco  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059187174)  
  
**3.** Rotina Laudos x Risco.  
Caminho SIGAMDT: atualizações > laudos > laudos x risco  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060048173)  
  
**4.** Exemplo de trabalhador desligado.  
Caminho SIGAMDT: atualizações > cadastros gerais> funcionários  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060048893)  
  
**5.** Relatório PPRA para funcionário não expostos a riscos.  
Caminho SIGAMDT: atualizações > relatórios > PPRA > rel. geral PPRA  
  
Note que não é gerado o trabalhador desligado.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059187374)  
  
**Saiba Mais:**  
[Artigos Laudos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360012070273-MDT-Laudos)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[ChatBot Carol](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
[Documentação Laudos Completa](https://tdn.totvs.com/x/6NybFg)
