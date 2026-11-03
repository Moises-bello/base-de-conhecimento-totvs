---
article_id: 35831901591703
category: Financeiro - Conciliador Backoffice
content_hash: 2ede686e2389aef89a3d8ef8e8f7a1ba004c7931d3407e81ecd6bc91a8ab9681
fetched_at: '2026-06-28T22:37:47.133958+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Amarrações CTBA940
type: support-article
updated_at: '2026-02-02T19:39:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35831901591703-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Amarra%C3%A7%C3%B5es-CTBA940
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35831901576087) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Quando é realizado a conciliação usando o CTBA940, quais os campos devem ser amarrados durante o processo de conciliação?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2310  
  
**Solução**

O ciclo de vida do título, até a conciliação, pode ser dividido em três fases principais: **Criação**, **Baixa/Movimentação Bancária** e **Conciliação Efetiva**.

#### **Fase 1: Criação do Título (Previsão)**

O título pode nascer como uma **previsão** de pagamento ou recebimento:

* **SE1 (Contas a Receber)** e/ou **SE2 (Contas a Pagar)**: O título é registrado aqui com seus dados básicos (vencimento, valor, fornecedor/cliente). **Neste momento, não há vínculo direto com conta bancária (movimentação bancaria) ou conciliação.**

#### **Fase 2: Baixa e Movimentação Bancária (Efetivação)**

A baixa pode ser um evento que gera o movimento de caixa/banco, tornando-o conciliável, para isso é importante validar o tipo a ser gerado no campo [**E5\_TIPODOC.**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=207357394) Caso haja movimentação bancária, segue-se o fluxo abaixo:

* **Tabela FK1: armazena** as informações detalhadas da baixa (banco, agência, conta, tipo de baixa, etc.).
* **Geração SE5 e FK5:** na baixa do título, ocorre a geração da movimentação bancária:
  + **SE5 (Movimento Bancário):** Armazena o registro do movimento.
  + **FK5 (Movimento de Extrato):** **Deve ser um espelho da SE5.** Ao ser preenchida, a SE5 gera automaticamente o registro correspondente na FK5.
* **Vínculo entre as tabelas:** A **SE5** cruza os dados com a baixa (FK1) pelo campo **E5\_IDORIG**, relacionando-se com o **FK1\_IDFK1** da **FK1**.
* **Tabela FK7: mantém** o vínculo entre a **movimentação bancária (SE5/FK5)** e a **origem do título (FK1/FK2)**.
* **Tabela FK7: também mantem-se vinculada ao movimento bancário através do campo FK5\_IDFK7 (FK5) e FK7\_IDDOC (FK7)**

#### **Fase 3: Conciliação Efetiva (CTBA940)**

O **CTBA940** atua na conferência e no cruzamento dos movimentos (Fase 2) com os extratos.

1. **Marcar** ***Flags*** **de Conciliação:**
   * O sistema marca *flags* de conciliação nas tabelas **FK5** e **SE5** de formas equivalentes, preservando os dados do legado.
2. **Popular Campos de Identificação:**
   * A ação de conciliação (o *match*) no **CTBA940** preenche automaticamente os campos **FK5\_DTCONC** e **E5\_RECONC** para registrar a data e o status da conciliação, preservando a integridade dos dados.
3. **Registro da Conciliação (QLC/QLD):**
   * As tabelas **QLC** (cabeçalho) e **QLD** (itens) são geradas **apenas no momento em que a conciliação é realizada**.
   * A **QLD** mantém o relacionamento entre o **ID de origem** e o **ID de destino** (o *match*), sendo o registro definitivo.

     ![unnamed.webp](https://centraldeatendimento.totvs.com/hc/article_attachments/35831917490071)

Segue mais um exemplo de amarrações

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/38110933169431)](https://centraldeatendimento.totvs.com/hc/article_attachments/38110933169431)

**Atenção**

**Este vínculo não é replicado em nenhuma outra tabela**, ou seja, a QLD é a única amarração física do Conciliador com as tabelas de referência do Financeiro.
