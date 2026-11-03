---
article_id: 33157666657559
category: Gestão organizacional
content_hash: 12a04e2950226720efe6612c20b744f76d2a7c06624ef991b9850834bc90c48b
fetched_at: '2026-06-28T22:47:22.198615+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - S-2500: Envio do Evento S-2500 em casos
  de Mudança de categoria ou de Natureza da atividade'
type: support-article
updated_at: '2026-01-08T12:24:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33157666657559-RH-RM-RHU-Processo-Trabalhista-S-2500-Envio-do-Evento-S-2500-em-casos-de-Mudan%C3%A7a-de-categoria-ou-de-Natureza-da-atividade
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33157711372183) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como seria o envio dos Processos Trabalhistas em casos onde há Mudança de Categoria ou de Natureza da Atividade?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas **- 12.1.34**e**superiores.**

**Solução**  
Segue abaixo as orientações para quando há reconhecimento judicial que envolve **mudança de categoria** e/ou de **natureza da atividade** do trabalhador, conforme o [Manual de Orientação ao eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf).

**1. Situações em que se aplica o grupo [mudCategAtiv]**

O grupo **[mudCategAtiv]** no evento S-2500 **somente deve ser preenchido** nos seguintes casos:

a) ***{tpContr}*** = 6:

* Quando há **mudança entre categorias do S-2300** (ex: de estagiário [901] para bolsista [903]);
* E o contrato esteja **encerrado** na data do **trânsito em julgado da decisão**.

b) Demais ***{tpContr}***:

* Quando há **mudança entre categorias do S-2200** (ex: de [103] para [101]);
* E o contrato também esteja **encerrado** na data do trânsito em julgado.

**Não preencher [mudCategAtiv]** se:

* A mudança for de **TSVE para empregado** ou **vice-versa**;
* O vínculo estiver **ativo** — nesse caso, a correção deve ocorrer via:
  + Retificação do S-2200, ou
  + Envio do S-2206 (alteração contratual).

---

**2. Como preencher corretamente os campos no S-2500**

Quando for necessário informar mudança de categoria ou natureza de atividade com base em decisão judicial:

**Campos obrigatórios:**

* ***{indCateg}*** e ***{indNatAtiv}*** = S (sim);
* Preencher o grupo **[mudCategAtiv]** com:
  + ***{codCateg}***: nova categoria;
  + ***{natAtividade}***: nova natureza da atividade;
  + ***{dtMudCategAtiv}***: data a partir da qual se aplica a nova categoria/atividade.

Se a categoria original foi declarada via **GFIP**, utilize o **Anexo II do Manual** para identificar o código correspondente. --> [Manual de Orientação ao eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf).

#### E também:

* Preencher o grupo **[baseMudCateg]** com a base de cálculo da previdência, informando:
  + Código da categoria antiga;
  + Valor da remuneração:
    - Informada em **GFIP** (se período anterior à DCTFWeb), ou
    - No evento **S-1200** (caso tenha sido informado sem prévio S-2300).

---

**3. Casos específicos envolvendo mudança de TSVE para empregado**

**Se o contrato de TSVE já está encerrado:**

* ***{tpContr}*** = 9;
* ***{indCateg}*** = N;
* **Não preencher** o grupo ***[mudCategAtiv]*** nem ***[baseMudCateg]***;
* Preencher o grupo ***[unicContr]*** para unificar com o novo vínculo criado no evento S-2500.

📌 Exemplo:

Trabalhador autônomo (cat. 701) teve vínculo reconhecido judicialmente de 10/2021 a 02/2022. Na época, foi enviado S-2300 + S-2399. No S-2500: preencher***{tpContr}*** = 9, ***{indCateg}***= N, **sem preencher** ***[mudCategAtiv]*** ou ***[baseMudCateg]***, e realizar unificação com o contrato anterior via ***[unicContr]***.

**Se o contrato de TSVE ainda está ativo:**

* ***{tpContr}*** = 9;
* **Enviar antes**:
  + **S-2399** com ***{dtFim}*** = data do trânsito em julgado;
  + **S-2200** com nova admissão reconhecida judicialmente:
    - ***{indAdmissao}*** = 3;
    - ***{nrProcTrab}*** = número do processo.
* No S-2500:
  + ***{indCateg}*** e ***{indNatAtiv}*** = N;
  + Informar **[unicContr]** com a matrícula anterior;
  + **Não preencher [mudCategAtiv] nem [baseMudCateg]**, pois trata-se de mudança TSVE → empregado.

📌 Exemplo:

Prestador autônomo ativo até 10/2023, decisão reconhece vínculo desde 10/2021. Encerrar S-2300 via S-2399; criar novo S-2200; no S-2500, fazer a unificação e preencher os campos conforme acima.

**Saiba Mais**  
Para maiores informações, acesse:

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [Manual de Orientação eSocial - Leiaute S-1.3 NT 03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
