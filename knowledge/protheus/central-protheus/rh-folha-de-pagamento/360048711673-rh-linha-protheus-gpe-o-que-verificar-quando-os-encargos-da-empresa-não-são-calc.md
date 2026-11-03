---
article_id: 360048711673
category: RH - Folha de Pagamento
content_hash: 03a7af27a72934b13c84681b86bf1efc3a6b544aa376593d13df7c27348abc9e
fetched_at: '2026-06-28T22:44:16.091236+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando os encargos da empresa não
  são calculados
type: support-article
updated_at: '2024-09-10T19:05:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048711673-RH-Linha-Protheus-GPE-O-que-verificar-quando-os-encargos-da-empresa-n%C3%A3o-s%C3%A3o-calculados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26278495932695) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Ao calcular a folha, os encargos da empresa (INSS parte empresa, INSS acidente de trabalho, INSS terceiros) não são calculados, o que pode ser verificado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução** **1.** Verificar se para o **Tipo de Contrato** do Funcionário (aba Funcionais do cadastro de Funcionário) tem registro relacionado nas **Tabelas S037 e S038** da rotina Manutenção Tabelas:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071915513)  
  
Tabelas S037 e S038 da rotina Manutenção Tabelas caminho: **>Atualizações >Definições de Cálculo >Manutenção Tabelas**.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070780314)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071915813)  
  
**2.** Na rotina **Histórico de Contrato**, o campo **Encargos Emp** deve estar com SIM ou em branco, pois quando esta em branco o sistema assume que deve ser calculado os encargos:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071916073)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
