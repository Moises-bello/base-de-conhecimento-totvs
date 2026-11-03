---
article_id: 360053133614
category: MDT - PCMSO
content_hash: f227f856dcb41417f2c1228eaa274c8a2aed842366a0d850eef1187c94addba0
fetched_at: '2026-06-28T22:44:28.543254+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Quais são as amarrações necessárias para que seja
  possível imprimir o relatório Resultados Exames x Agentes
type: support-article
updated_at: '2025-09-03T13:52:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053133614-RH-Linha-Protheus-MDT-Quais-s%C3%A3o-as-amarra%C3%A7%C3%B5es-necess%C3%A1rias-para-que-seja-poss%C3%ADvel-imprimir-o-relat%C3%B3rio-Resultados-Exames-x-Agentes
---

**Dúvida**Quais são as amarrações necessárias para que seja possível imprimir o relatório Resultados Exames x Agentes?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Cadastro de exame do tipo **IBMP,** acesse **Atualizações > PCMSO > Exames**No campo Indica Resultado selecione o tipo 2 - IBMP  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093667094)  
  
Amarre o Exame ao fornecedor na rotina de Fornecedor de Exames, acesse **Atualizações > PCMSO > Fornecedor de Exames**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093667794)  
  
Na rotina de Risco, informe a quantidade do agente de risco no campo **TN0\_QTAGEN**; **Atualizações > PPRA > Riscos**  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093667974)  
  
Vincule o exame por risco, **Atualizações > PCMSO > Exames por risco**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095922573)  
  
Execute a Geração de exames de riscos com o agente, informando a intensidade nos campos **TN1\_DEINTE** e **TN1\_ATEINTE**;  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093668534)  
  
Realize a programação de Exames,  **Atualizações > PCMSO > Gerar Programação**  
Informe o resultado do exame do funcionário, na rotina de Exames por Funcionário; **Atualizações > PCMSO > Exames do Funcionário  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093670374)**Preencha as informações conforme seu cenário e Imprima o relatório, **Relatório > Resultado Exames > Exames por agente.  
  
Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
