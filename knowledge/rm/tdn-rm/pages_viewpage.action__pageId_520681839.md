---
content_hash: 8220b5131f45baeea37be222583b31e24cfb574ee7d48a4c0f47a1b569a23ec5
fetched_at: '2026-06-29T00:10:31.198663+00:00'
page_id: '520681839'
product: rm
source: tdn-rm
title: Parâmetros TRCT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520681839
version: 7
---

#### **Para aviso Prévio Trabalhado considerar um dia útil antes no início do aviso (Campo 25)**

Este parâmetro foi criado em Folha de Pagamento| Rescisão| Relatórios| TRCT| TRCT portaria 1621/2010,  para que ao gerar TRCT para funcionário com Aviso Prévio Trabalhado, seja levado no campo '25- Data do Aviso Prévio',  data com um dia útil anterior ao cadastrado.

Exemplo:

Para um funcionário com Aviso Prévio Trabalhado, data 12/11/2021.

No arquivo será levada a data 11/11/2021.

**Obs:**

1. Para funcionários com data iniciada em sábado, domingo ou feriados, será considerada a data do ultimo dia útil anterior a data cadastrada.

2. Para funcionários com Aviso Prévio Misto, com o parâmetro marcado, também retornará um dia útil anterior a data inicial do Aviso Trabalhado.

3. Ao marcar os parâmetros 'Para aviso Prévio Trabalhado considerar um dia útil antes no início do aviso (Campo 25)' e 'Data Aviso Prévio Indenizado igual à data de demissão', também retornará um dia útil anterior a data inicial do Aviso Trabalhado.

**Em Paramêtros II**  
  
  
Emissão dos termos de Quitação / Homologação, é permitido escolher 3 tipos de emissão

1) Emitir Termo de Quitação/Homologação - **De acordo com o tempo de casa**;

Marcando este parâmetro, serão gerados os termos de quitação e homologação, considerando o tempo de casa do funcionário.

2) Emitir Termo de Quitação/Homologação - **Somente o Termo de Quitação independente do tempo de casa**;

Marcando este parâmetro, será gerado somente o termo de quitação independente do tempo de casa do funcionário.

3) Emitir Termo de Quitação/Homologação - **Somente o Termo de Homologação independente do tempo de casa**;

Marcando este parâmetro, será gerado somente o termo de homologação independente do tempo de casa do funcionário.
