---
content_hash: bb3e8aaeb6d9a7917371ae06b8717c507c42e38d977a51bec94b6baaa797e72c
fetched_at: '2026-06-29T00:10:02.076440+00:00'
page_id: '452718882'
product: rm
source: tdn-rm
title: Alteração do Status no Controle de Extintores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718882
version: 3
---

Sobre o Status do Extintor (Funcional, Requer Atenção, Requer Intervenção):

**Funcional:**

Para que um extintor receba o status de funcional é necessário que:

* Exista um registro de controle do tipo Inspeção com "Data de Próximo Controle" maior que a data atual acrescida da quantidade de dias definida no Parametrizador (Opções > Parametrizador > EPC > Periodicidade de alteração do status do EPC para "Requer Atenção" (em dias)) e esteja "Aprovado";

**DPCI > (DA + DIAS)**

**Obs.:** Só o registro de inspeção é que garante o status de Funcional ao Extintor.

**Requer Atenção:**

O status de Requer Atenção será aplicado sempre que:

* A data atual for menor que a "Data de Próximo Controle" da Inspeção e maior que a "Data Limite para Atenção" (esta é obtida através do cálculo da Data de Próximo Controle da Inspeção menos a quantidade de dias do parametrizador).

**(DA < DPCI) && (DA > (DPCI - DIAS))**

* Atenda ao requisito de estar Funcional, porém, dentro do período do registro de inspeção exista algum "Teste" ou "Manutenção" não "Aprovado".

**DA > (DPC - DIAS) && ((DCM > DCI && DCM < DPCI && CNA) || (DCT > DCI && DCT < DPCI && CNA))**

**Requer Intervenção:**

O status de ‘Requer Intervenção’ será aplicado sempre que:

* Não existir registro de controle no Extintor
* Não existir controle do tipo Inspeção
* Controle do tipo Inspeção estiver com "Data de Próximo Controle" vencida.

**DA > DPCI**

* O maior registro de Controle do tipo Inspeção não estiver "Aprovado"

Legenda:

- DA.............. Data Atual 

- DCI............. Data do Controle de Inspeção

- DCM........... Data do Controle de Manutenção

- DCT…….... Data do Controle de Teste

- DPCI……... Data do Próximo Controle de Inspeção

- DIAS……... Dias de Periodicidade definida no Parametrizador

- CNA ……... Controle Não Aprovado

<https://docs.google.com/document/d/1kIniq1R-1vfCfSbxnRmsF9WzAr6EeTOBhz3g1rxKSFM/edit?usp=sharing>
