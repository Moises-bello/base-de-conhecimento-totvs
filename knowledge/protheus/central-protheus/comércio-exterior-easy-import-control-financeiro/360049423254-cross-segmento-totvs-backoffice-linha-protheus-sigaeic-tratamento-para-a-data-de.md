---
article_id: 360049423254
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: e5d53f1df8c048bcdaaf78a3053d3a2523344895be4b19bd7a612d2cf2b1ab81
fetched_at: '2026-06-28T22:39:44.433889+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Tratamento para
  a Data de Vencimento dos títulos PRE
type: support-article
updated_at: '2021-08-27T13:34:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049423254-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Tratamento-para-a-Data-de-Vencimento-dos-t%C3%ADtulos-PRE
---

**Dúvida**Qual é o cálculo para a Geração da Data de Vencimento dos Títulos PRE?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**

Tratamento para a Data de Vencimento dos títulos PRE conforme a ordem de preenchimento das datas.

Primeiramente vamos listar as Variáveis dos Cálculos:

*Lead* Desembaraço - Caso este campo não esteja Preenchido no Cadastro de Portos e Aeroportos - campo Y9\_LT\_DES - é preenchido pelo Parâmetro MV\_LT\_DESE

*Lead Time* Trânsito - Caso este campo não esteja Preenchido no Cadastro de Portos e Aeroportos - campo Y9\_LT\_TRA

Verificar o Parâmetro MV\_DTLEADT - Quando este Parâmetro retorna .F., o sistema calcula a data de vencimento dos titulos PRE da forma padrão antiga(somando os *lead times* desembaraço e Trânsito do cadastro de via de transporte).

Agora vamos aos Cálculos para a Data de Vencimento dos Títulos PRE de Acordo com campos Preenchidos:

- Caso o campo Campo Data de Entrega - W6\_DT\_ENTR - estiver preenchido - é gerado o Vencimento apenas do Campo W6\_DT\_ENTR;

- Caso o campo Campo Data de Previsão de Entrega - W6\_PRVENTR - estiver preenchido - é gerado o Vencimento apenas do Campo W6\_PRVENTR;

- Caso o campo Campo Data de Desembaraço - W6\_DT\_DESE - estiver preenchido - é gerado o Vencimento pelo Cálculo W6\_DT\_DESE + *Lead Time* Trânsito (Y9\_LT\_TRA)

- Caso o campo Campo Data de Previsão do Desembaraço - W6\_PRVDESE - estiver preenchido - é gerado o Vencimento pelo Cálculo W6\_PRVDESE + *Lead Time* Trânsito (Y9\_LT\_TRA)

- Caso o campo Campo Data de Atracação - W6\_CHEG - estiver preenchido - é gerado o Vencimento pelo Cálculo W6\_CHEG + Lead Time Transito (Y9\_LT\_TRA) + *Lead* Desembaraço (Y9\_LT\_DES)

- Caso o campo Campo Data de Atracação - W6\_DT\_ETA - estiver preenchido - é gerado o Vencimento pelo Cálculo W6\_DT\_ETA + *Lead Time Transito* (Y9\_LT\_TRA) + *Lead* Desembaraço (Y9\_LT\_DES)

- Caso o campo Campo Data de Embarque - W6\_DT\_EMB - estiver preenchido - é gerado o Vencimento pelo Cálculo W6\_DT\_EMB + *Lead Time Transito* (Y9\_LT\_TRA) + *Lead* Desembaraço (Y9\_LT\_DES) + Transit Time (YR\_TRANS\_T)

- Caso o campo Campo Data Prevista de Embarque - W6\_DT\_ETD - estiver preenchido - é gerado o Vencimento pelo Cálculo W6\_DT\_ETD + *Lead Time* Trânsito (Y9\_LT\_TRA) + *Lead* Desembaraço (Y9\_LT\_DES) + *Transit Time* (YR\_TRANS\_T)

Importante - Verificar quais campos foram Preenchidos já no Embarque, os Campos no Cadastro de Via de Transporte (Tabela SYR), e os Campos no Cadastro de Portos e Aeroportos SY9.
