---
article_id: 6067104184087
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a778d5fedbf0628db02a10c8c24493886164727711a36a381dac0729e6289d74
fetched_at: '2026-06-28T22:37:21.513527+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como gerar Titulo Financeiro
  pela rotina de Medição Automática CNTA260?
type: support-article
updated_at: '2022-12-02T11:19:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6067104184087-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-gerar-Titulo-Financeiro-pela-rotina-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-CNTA260
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00** **Dúvida**Como gerar Titulo pela rotina de Medição Automática CNTA260?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução** **Para gerar um Titulo Financeiro pelo processo de medição automática se faz necessário a configuração:**

- Acessando o configurador, deve preencher o parâmetro MV\_CNNATMD com a natureza do titulo.

- Após a configuração padrão do contrato, na linha do item, o sistema possui um campo chamado "Nota/Titulo" o mesmo deve estar configurado para Titulo, ou o processo não irá gerar corretamente Título para a Medição.

- Após confirmar o contrato, gere a medição automática "CNTA260" conforme a data prevista da parcela do Cronograma Financeiro.

- Após o processo finalizado, pode verificar na rotina FINA050 (Contas a Pagar) que os títulos referentes a medição foram gerados corretamente. Caso queira conferir no título gerado, clique em visualizar e na aba outros terá a informação do contrato que originou o titulo.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Medição Automática no Gestão de Contratos via Schedule e via Execução por Menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015929231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Medi%C3%A7%C3%A3o-Autom%C3%A1tica-no-Gest%C3%A3o-de-Contratos-via-Schedule-e-via-Execu%C3%A7%C3%A3o-por-Menu?source=search)
