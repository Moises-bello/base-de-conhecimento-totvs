---
article_id: 360035471514
category: Escrita Fiscal - Impostos - ICMS
content_hash: a9d468f44c9fed82a38ad4780934d83119bc9e89838c10da77157fb622524a37
fetched_at: '2026-06-28T22:39:24.413874+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como emitir nota de
  transferência de crédito/débito de ICMS?
type: support-article
updated_at: '2023-09-06T17:18:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035471514-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-emitir-nota-de-transfer%C3%AAncia-de-cr%C3%A9dito-d%C3%A9bito-de-ICMS
---

**Dúvida**Como emitir nota de transferência de crédito/débito de ICMS?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

**Tipo de Nota fiscal :**Complemento de ICMS

* **Configuração de TES**

Credita ICMS (F4\_CREDICM) = Não

Calcula ICMS (F4\_ICM) = Sim

Cod. Fiscal (F4\_CF) = Informar CFOP de transferência

L.Fisc. ICMS (F4\_LFICM) = ICMS Zerado/Outros/Isento - A escrituração da nota fiscal deve ser analisada pelo departamento fiscal de sua empresa.

Agrega Valor (F4\_AGREG) = Não

Ajuste CIAP (F4\_AJUSTE)= S

Txt Padrão (F4\_TEXTO) = Transferência

TRF. Deb/Crd (F4\_TRFICM) = SIM - Esse campo levará o valor do ICMS transferido para linha 21 (transf. Cred) ou 22 (transf. Deb) na parte de Informações Complementares da Apuração de ICMS.

Fórmula (F4\_FORMULA) = Criar uma fórmula para ser amarrada a TES

Menu Atualizações > Cadastros > Fórmulas:

Informar código, descrição e no campo fórmula informar o conteúdo: “Transferência de saldo (credor/devedor) conforme art. 98 do RICMS” (utilizar aspas duplas)

**Lançamento da Nota**

Produto = Criar um produto “Transferência de Saldo de ICMS”

Quantidade = 1

Valor unitário e valor total = Valor do ICMS

TES = Informar o TES de transferência

Para destacar o valor da **transferência de crédito de ICMS** no **XML** e no **Danfe** incluir o CFOP da nota conforme o exemplo abaixo:

**MV\_CFOPTRA =** 5601/5602/

* **Exemplo do parâmetro no configurador:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17323112300439)

**Saiba mais:**

Transferência de **crédito GO:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=341223557>

Transferência de **crédito SP:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=201741587>
