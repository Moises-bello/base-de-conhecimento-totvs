---
article_id: 33146432880407
category: Gestão organizacional
content_hash: b3e1a32f3c93fb4639842ac07021b77213758cbd6c1f6fcc12b0370dca4f7917
fetched_at: '2026-06-28T22:47:22.212955+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - S-2500: Envio do Evento S-2500 em casos
  de Unificação de Vínculos'
type: support-article
updated_at: '2026-01-08T12:21:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33146432880407-RH-RM-RHU-Processo-Trabalhista-S-2500-Envio-do-Evento-S-2500-em-casos-de-Unifica%C3%A7%C3%A3o-de-V%C3%ADnculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33146479589655) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como seria o envio dos Processos Trabalhistas em casos de Unificação de Vínculos?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas **- 12.1.34**e**superiores.**  
  
**Solução**  
A unificação de vínculos ocorre quando há uma **decisão judicial que reconhece a unicidade contratual** entre vínculos anteriormente registrados de forma separada no eSocial. O evento **S-2500** deve refletir corretamente esta decisão, abrangendo todos os períodos reconhecidos como parte de um único vínculo empregatício.

Segue abaixo as orientações para Unificação de Vínculos relacionados a decisões trabalhistas e os procedimentos adequados para cada caso, conforme o [Manual de Orientação ao eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf).

**Regras de Preenchimento do Evento S-2500**

**1. Contrato deve abranger todos os períodos unificados**

Se houver decisão judicial reconhecendo a **unicidade contratual**, o período do contrato no evento S-2500 **deve abranger todos os períodos vinculados à(s) matrícula(s) incorporadas**.

📌 **Atenção**: O vínculo informado no evento S-2500 precisa cobrir desde a **data mais antiga** entre os vínculos até a data final reconhecida pela Justiça.

---

**2.** **Situação do contrato: encerrado ou ativo**

**a) Se o contrato reconhecido já estiver encerrado:**

* Criar uma **nova matrícula** no evento S-2500.
* Preencher:
  + ***{indContr}*** = N (novo vínculo);
  + ***{tpContr}*** = 9 (tipo de contrato decorrente de decisão judicial).

**b) Se o contrato reconhecido ainda estiver ativo:**

* **Retificar o evento S-2200** mais recente:
  + Atualizar a **data de admissão** para refletir o início do período reconhecido;
  + Preencher:
    - ***{indAdmissao}*** = 3 (decisão judicial);
    - ***{nrProcTrab}*** = número do processo judicial.

---

**3. Vínculos encerrados antes da substituição da GFIP**

Se houver vínculo(s) encerrado(s) **anteriormente à entrada do eSocial para fins previdenciários**:

* Enviar previamente o(s) **evento(s) S-2200** com o **grupo [desligamento] preenchido**;
* No evento S-2500:
  + Preencher o campo ***{matUnic}*** com a(s) **matrícula(s) antiga(s)** dos vínculos incorporados.

---

**4. Encerramento de vínculos que ainda não foram finalizados**

Caso algum dos vínculos a serem unificados **ainda esteja aberto**, ou seja, **sem desligamento informado**, é necessário:

* **Encerrar previamente** por meio de:
  + Evento **S-2299**, informando:
    - Motivo de desligamento = 44 (Agrupamento contratual);
  + ou Evento **S-2399**, conforme o caso (trabalhador sem vínculo de emprego);
  + Em ambos, **incluir o número do processo judicial** no campo ***{nrProcTrab}***;
  + A data do desligamento deve ser a **determinada na decisão judicial.**

---

**5. Proibição de alterações nos contratos incorporados**

Após a unificação (envio do S-2500):

* **Não é permitido retificar ou excluir os contratos incorporados** diretamente.
* Para realizar qualquer correção:
  + Excluir **primeiramente o evento S-2500**;
  + E, se existir, também o evento **S-2501** correspondente.

---

**6. Categoria do vínculo incorporador**

O vínculo incorporador no S-2500 deve conter a **categoria inicial do vínculo original**.

Se houver alteração de categoria ao longo do período reconhecido judicialmente:

* Devem ser observadas as orientações específicas **do evento S-2500**, que trata sobre **mudanças de categoria no tempo** (como aprendiz que vira empregado efetivo, por exemplo).  
  [RH - RM - RHU - Processo Trabalhista - S-2500: Envio do Evento S-2500 em casos de Mudança de categoria ou de Natureza da atividade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33157666657559)

**Saiba Mais**  
Para maiores informações, acesse:

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [Manual de Orientação eSocial - Leiaute S-1.3 NT 03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
