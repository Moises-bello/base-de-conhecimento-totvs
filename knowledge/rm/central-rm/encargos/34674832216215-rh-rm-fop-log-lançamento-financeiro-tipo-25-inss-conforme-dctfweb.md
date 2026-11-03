---
article_id: 34674832216215
category: Encargos
content_hash: 57bab866124946cd4c7edee3c5a20de0c5e79c6605edcb1ba0eafe85b162d053
fetched_at: '2026-06-28T22:46:52.185970+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Log lançamento financeiro Tipo 25 INSS conforme DCTFWEB
type: support-article
updated_at: '2026-03-20T18:37:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34674832216215-RH-RM-FOP-Log-lan%C3%A7amento-financeiro-Tipo-25-INSS-conforme-DCTFWEB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34674832190359) Tempo aproximado para leitura: 00**:02:00 min**  
  
**Dúvida**  
Como realizar conferencia e identificação de possíveis divergências no lançamento financeiro tipo 25 INSS conforme DCTFWEB?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2502.180  e 12.1.2506.122 e superiores  
  
**Solução**  
O lançamento financeiro passou a contar com uma nova aba de debug que detalha os valores calculados para cada lançamento. Com essa melhoria, os usuários terão acesso a informações mais completas e maior visibilidade sobre os dados registrados, facilitando a identificação e correção de eventuais inconsistências.

Os valores apresentados na aba incluem: Empresa, Segurados, Acidente de Trabalho, Terceiros e Deduções

## Geração de Lançamentos Financeiros INSS DCTFWeb ##  
Lançamentos Financeiros gerados:  
-----------------------------------------------------------------------------------------------------------------------------  
Detalhamento do cálculo do lançamento financeiro INSS DCTFWEB da seção centralizadora 01:  
Total Lanc Financ = Empresa + Segurados + Acidente de trabalho + Terceiros - Deduções  
Total Lanc Financ = 400,00 + 150,00 + 60,00 + 116,00 - 0,00 = 726,00

Lancto. Fin. ID: 1 ---> Tipo: [INSSPagar] Valor: 726,00

Detalhamento do cálculo do lançamento financeiro INSS DCTFWEB da seção centralizadora 03:  
Total Lanc Financ = Empresa + Segurados + Acidente de trabalho + Terceiros - Deduções  
Total Lanc Financ = 67,93 + 25,47 + 10,19 + 19,70 - 0,00 = 123,29

Lancto. Fin. ID: 2 ---> Tipo: [INSSPagar] Valor: 123,29

-----------------------------------------------------------------------------------------------------------------------------  
Total de Lançamentos Financeiros efetuados: 2  
### Fim memória de Cálculo

Geração será conforme o parâmetro financeiro estiver no exemplo acima o parâmetro está for filial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34674841800215)

O valor também confere com o relatório de conferencia do INSS PATRONAL:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34674832192279)![](https://centraldeatendimento.totvs.com/hc/article_attachments/34674841808663)

Saiba mais:

[RH - RM - FOP - Lançamento financeiro tipo 25 - Total Guia INSS com o mesmo valor apresentado na DCTFWeb](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13423681275159-RH-RM-FOP-Lan%C3%A7amento-financeiro-tipo-25-Total-Guia-INSS-com-o-mesmo-valor-apresentado-na-DCTFWeb)

[DT - Lançamento Financeiro - Tipo "25 -Total Guia INSS DCTFWeb" e "26 -Total Guia INSS DCTFWeb 13° Salário" - Evolução no Log](https://tdn.totvs.com/pages/releaseview.action?pageId=967107264#1-3)
