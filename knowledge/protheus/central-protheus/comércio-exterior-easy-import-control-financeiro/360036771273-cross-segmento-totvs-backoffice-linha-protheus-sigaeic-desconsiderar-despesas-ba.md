---
article_id: 360036771273
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: efbd951ca5ef6a237c44caaddd10b3dc2462b94c21f4615509c06b9c323bced7
fetched_at: '2026-06-28T22:39:44.354150+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Desconsiderar
  despesas base de imposto sim e base de custo não do valor da mercadoria
type: support-article
updated_at: '2022-04-08T20:08:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036771273-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Desconsiderar-despesas-base-de-imposto-sim-e-base-de-custo-n%C3%A3o-do-valor-da-mercadoria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como configurar o SIGAEIC para que o custo da despesa base de imposto entre na Base do Imposto, mas não no custo da mercadoria?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 11.80  
  
**Solução****Pré-requisito****:**

* Possuir um processo de importação em fase de desembaraço.
* Possuir uma despesa que seja (base imposto = SIM, base custo = NAO) associada ao desembaraço.
* Possuir Adições geradas no desembaraço.
* Parâmetro MV\_EIC0016 (rateio de despesas como acréscimo) desabilitado.
* Parâmetro MV\_TEM\_DI habilitado ou falso

**Sequencia 001**1. Acesse Atualizações > Desembaraço > Receb. Importação;  
2. Selecionar o processo e emitir a NF Primeira;  
3. Com o parâmetro habilitado (MV\_EIC0070 = .T.), verifique que a despesa que é base imposto = SIM e base custo = NÃO, não deve estar sendo contabilizada no valor da mercadoria e, por consequência, no Total Geral;  
4. Gerar também o Custo Realizado;  
5. Com o parâmetro habilitado (MV\_EIC0070 = .T.), verifique que a despesa não consta e portanto não compõe os valores do relatório;  
6. Com o parâmetro desabilitado (MV\_EIC0070 = .F.), verifique que a despesa no relatório da NF Primeira, é contabilizada no valor da mercadoria e, por consequência, no Total Geral. Já no relatório do Custo Realizado, a despesa constará como '105-DESPESAS BASE II (SEM CUSTO)' e irá compor os valores do relatório.  
  
**Saiba mais**  
[Criação do Parâmetro MV\_EIC0070](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=419538879)
