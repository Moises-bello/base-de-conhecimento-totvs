---
article_id: 33712546428055
category: Financeiro - Contas a Receber
content_hash: e264e35384c3cc5b1043bce5e635d016936981ed6e198f953cc89d848783b169
fetched_at: '2026-06-28T22:38:12.533109+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - BackOffice Linha Protheus - SIGAFIN - Migrador offline SE5
  para FKs
type: support-article
updated_at: '2026-04-14T17:40:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33712546428055-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-Migrador-offline-SE5-para-FKs
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33712530784663) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Como migrar os movimentos da SE5 para as FKs?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Para realizar a migração off-line dos registros da tabela **SE5 – Baixas e Movimento Bancário** para a nova estrutura de tabelas da família **FKx**, siga os passos abaixo:

1. Adicione a rotina **FINXSE5** para habilitar o assistente de migração (*wizard*).
2. Execute a rotina. O sistema exibirá a tela do assistente.
3. Acesse a opção **Perguntas** e informe o intervalo de datas desejado. Esse intervalo determinará o período dos movimentos da tabela SE5 que serão considerados na migração.
4. Confirme a execução para iniciar o processamento.

**Importante**

Neste caso, o processo envolve a manipulação de tabelas, o que está fora do escopo de atendimento padrão. Para a execução, será necessário acionar um analista de banco de dados. validar as documentações complementares indicadas a seguir.

**Saiba mais**

[**Migrador\_FINXSE5**](https://tdn.totvs.com/display/public/PROT/FIN0034_Migrador_FINXSE5)

[Migrador Off-line (SE5 - FKs)](https://tdn.totvs.com/pages/releaseview.action?pageId=185754496)

[Reestruturação da tabela SE5 na família de tabelas FKx](https://tdn.totvs.com.br/pages/releaseview.action?pageId=203760476)
