---
content_hash: 48d66ee6c78b71a0679caddd9fd02f1028c843578f2b3da9f0cfe2e41158bc60
fetched_at: '2026-06-29T00:12:03.569232+00:00'
page_id: '911855764'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Processo - Cancelar Lançamentos
  Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911855764
version: 2
---

### **Cancelar Lançamentos**

---

Para o condomínio gerado de forma individual, ou seja, cujas cobranças em determinada competência incidem somente sobre aquela subunidade cujo cálculo de apuração já foi realizado, também é possível excluir os lançamentos gerados após a geração de lançamentos.  
Como o processo só poderá ser utilizado por subunidade, **não será possível excluir lançamentos de vários fechamentos ao mesmo tempo.**

Ao selecionar o processo "*Cancelar lançamentos financeiros"*, serão apresentados todos os lançamentos gerados na apuração individual, bem como suas respectivas cobranças se são responsáveis por vacâncias dentre outras informações pertinentes:

* Código do empreendimento: Empreendimento cujo fechamento pertence;
* Unidade: ID da unidade que possui subunidade com lançamento gerado;
* Subunidade: A subunidade que já possui lançamento gerado;
* Processo: O processo apurado que gerou o lançamento financeiro, por exemplo: Cobrança Direta;
* Vacância: Se este registro é um lançamento de vacância;
* Taxa: Se este registro é um lançamento de taxas.

Este processo então só poderá ser realizado quando a subunidade possui status como "**Integrado**" e se possui registros gerados, ou seja,  o campo "**Apurado?**" está como "**Com registros**" na visão de *Anexos / Apuração de Condomínio* do registro de fechamento em questão.

**Como utilizar**

1. Entre no Cadastro de Fechamento Individual, através do caminho *Condomínio / Fechamento / Fechamento do Condomínio Individual;*
2. Selecione um fechamento desejado que possua subunidades com status = "Integrado" e o campo "Apurado?" é igual a "Com registros";
3. Em Processos, selecione a opção "Cancelar Lançamentos Financeiros";
4. Na interface do processo, selecione as subunidades que deverão ter seus lançamentos cancelados;
5. Ao finalizar o processo, as subunidades relacionadas, terão suas situações atualizadas de "Integrado" para "Calculado".
6. Os lançamentos financeiros terão seu status igual a "Cancelado".

**Observações**

* Só poderão ser cancelados os lançamentos que tiverem status igual a "Aberto".
