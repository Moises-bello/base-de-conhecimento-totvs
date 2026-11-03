---
article_id: 32996444408471
category: Gestão organizacional
content_hash: 0f463e7085455a3c213b36a8c0d7efe522f4029b27adea49047fc732a5cd7700
fetched_at: '2026-06-28T22:47:22.227292+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processo Trabalhista - S-2500: Situações que exigem cadastro
  prévio ou retificação de eventos no eSocial'
type: support-article
updated_at: '2025-06-23T19:45:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32996444408471-RH-RM-RHU-Processo-Trabalhista-S-2500-Situa%C3%A7%C3%B5es-que-exigem-cadastro-pr%C3%A9vio-ou-retifica%C3%A7%C3%A3o-de-eventos-no-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32996428657559) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como seria o envio dos Processos Trabalhistas para situações que exigem cadastro prévio ou retificação de eventos no eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas **- 12.1.34** e **superiores.**  
  
**Solução**  
Segue abaixo as possíveis situações que exigem cadastro prévio ou retificação de eventos relacionados a decisões trabalhistas e os procedimentos adequados para cada caso, conforme o [Manual de Orientação ao eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)**.**

1. **Continuidade da Prestação de Serviço Após a Decisão Judicial**

**Condição:** O trabalhador permanece em atividade no declarante após o último mês abrangido pela decisão judicial.

**Procedimentos:**

* **Se o vínculo ainda não estiver formalizado no eSocial:**
  + Enviar o evento de admissão **S-2200** ou **S-2300**, com o campo ***{nrProcTrab}*** preenchido.
  + No caso do **evento S-2200**, também é obrigatório preencher o campo ***{indAdmissao}*** com o valor ***[3]***.

---

2. **Vínculo Encerrado e Tipo de Contrato Informado como [2], [3] ou [4]**

**Condição:**Para {tpContr} = [2] ou [4].

**Procedimentos:**

* Retificar o **evento S-2200**:
  + ***{indAdmissao}*** = **[3]**
  + ***{nrProcTrab}*** = número do processo judicial (igual ao informado no S-2500)
  + ***{dtAdmOrig}*** = data original de admissão
  + ***{dtAdm}*** = data de admissão reconhecida pela decisão judicial

**Condição:**Para {tpContr} = [3] ou [4].

**Procedimentos:**

**Quando a modificação da data de desligamento NÃO altera o período de apuração:**

* Retificar o **evento S-2299**:
  + Atualizar a **data e o motivo de desligamento**
  + Preencher o campo ***{nrProcTrab}*** com o número do processo judicial informado no S-2500

**Quando a modificação da data de desligamento ALTERA o período de apuração:**

* Excluir e reenviar o evento **S-2299**, com o campo ***{nrProcTrab}*** preenchido.

**⚠️Atenção**

* Para excluir o evento **S-2299**, é obrigatória a **exclusão prévia do evento S-1210** correspondente.
* As verbas do evento S-2299 excluído devem ser informadas em um **evento S-1200** do mês correspondente, além do **reenvio de um novo evento S-1210**.
* Se a nova data de desligamento for em mês anterior, no evento **S-2299**:  
  + ***{dtFimRemun}*** = último dia do mês referente ao último S-1200 existente
  + ***{indRemun}*** = **[2]**

---

3. **Declaração de Exposição a Agentes Nocivos – PPP Eletrônico**

**Condições:**

* Existência de decisão judicial determinando a exposição a agentes nocivos;
* Tipo de contrato ***{tpContr}*** = [5]

**Procedimentos:**

* Enviar previamente o evento **S-2200**:
  + ***{indAdmissao}*** = **[3]**
  + ***{nrProcTrab}*** = número do processo informado no **evento S-2500**

**⚠️Atenção**

* Esse envio é **pré-requisito para envio do evento S-2240** (PPP eletrônico).
* O mesmo procedimento se aplica para a **CAT** de acidente após a substituição da CATWeb pelo evento **S-2210**.

**Adicional de Financiamento da Aposentadoria Especial:**

* Se a decisão judicial trata do recolhimento desse adicional sobre verbas já declaradas:
  + Não declarar bases de cálculo no **evento S-2500**.
  + Informar **apenas o valor do adicional** no evento **S-2501**.
  + Para isso, é necessário o envio prévio do **evento S-2500**, mencionando cada competência devida.
  + Se não houver outras parcelas reconhecidas na competência, informar valor **"0,00".**

---

4. **Mudança no Motivo de Desligamento**  
  
**Procedimentos:**

* Retificar o evento **S-2299** com o campo***{nrProcTrab}*** preenchido.
* **Excluir previamente o evento S-1210**, se existente.
* Após a retificação, **enviar novo evento S-1210**.

---

5. **Recolhimento da Multa de 40% do FGTS via FGTS Digital (a partir de 01/03/2024)**

**Condições:**

* Reconhecimento judicial de vínculo e desligamento de trabalhador **sem registro prévio no eSocial**.
* Determinação judicial de recolhimento da **multa de 40% do FGTS**.

**Procedimentos:**

1. Enviar o evento de **admissão (S-2200)** com:
   * ***{indAdmissao}*** = **[3]**
   * ***{nrProcTrab}*** = número do processo
2. Enviar o evento de **desligamento (S-2299)** com a mesma referência processual.
3. Enviar o **evento S-2500**, com:
   * ***{indContr}*** = **[S]**
   * Indicação do vínculo informado no S-2200
   * Informações das verbas reconhecidas

**⚠️Atenção**

O empregador pode informar diretamente no **FGTS Digital**:

* O histórico de remunerações.
* O valor da base de cálculo para a multa rescisória.

---

6. **Alteração de Dados do RET do Trabalhador**

**Exemplo:** Alteração do cargo exercido.

**Procedimentos:**

* Realizar a **retificação do evento S-2200**
* Ou, se aplicável, realizar **inclusão ou retificação do evento S-2206.**

**Saiba Mais**  
Para maiores informações, acesse:

- [RH - RM - RHU - eSocial: S-2500 - Mapeamento dos campos para geração do evento S-2500](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256276341783)

- [Manual de Orientação eSocial - Leiaute S-1.3 NT 03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf)

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
