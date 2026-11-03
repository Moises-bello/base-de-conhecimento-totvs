---
article_id: 37347681866775
category: RH - Dissídio
content_hash: 40ac460280721d98fd0edca7333e726e157a63da5806e371f736bb2a95df0743
fetched_at: '2026-06-28T22:43:43.355176+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Erro argument error in function Len() on FCALCINSSFUN(GPEXCIMP.PRX)
  ao Calcular o Dissídio Retroativo
type: support-article
updated_at: '2025-12-30T19:07:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37347681866775-RH-Linha-Protheus-GPE-Erro-argument-error-in-function-Len-on-FCALCINSSFUN-GPEXCIMP-PRX-ao-Calcular-o-Diss%C3%ADdio-Retroativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37347650260247) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao Processar o Cálculo do Dissídio Retoativo, é apresentado o erro "argument error in function Len() on FCALCINSSFUN(GPEXCIMP.PRX)" no Log de ocorrências, e as verbas de Encargos de Empresa (INSS Empresa, Terceiros e Acidente de Trabalho) não são calculadas.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**  
O erro ocorre quando há Inconsistências no preenchimento d tabela S037.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37347681860119)

**Solução**  
1. Acesse: Atualizações / Definições de Cálculo / Manutenção de Tabelas (GPEA320);  
2. Localize a tabela S037 e clique em Visualizar;  
3. Confirme se os campos da tabela S037 estão preenchidos de forma correta. Para mais informações sobre o preenchimento sa tabela acesse [Cadastro da tabela S037 - Encargos Empresa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053697053-RH-Linha-Protheus-GPE-Cadastro-da-tabela-S037-Encargos-Empresa)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37347681860631)

**Importante:** O campo "Mês/Ano" deve ser preenchido com a competência Final da vigência dos encargos.   
Se houver uma linha para a competência atual com o campo "Mês/Ano" preenchido e outra linha com o campo em branco, o erro pode ser apresentado.

**Saiba Mais:**

[**RH - Dissídio**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
