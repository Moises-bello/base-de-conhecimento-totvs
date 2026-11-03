---
article_id: 360022404872
category: TAF - eSocial - Eventos Periódicos
content_hash: 3fb94226eb35337e42d46b93caad228af8cc6f8deb135203f045a1c244b249c6
fetched_at: '2026-06-28T22:45:19.160093+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Não Periódicos - S-2299 - Descrição:
  Não pode existir qualquer evento para o vínculo trabalhista com data posterior a
  data do desligamento'
type: support-article
updated_at: '2026-06-24T12:12:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022404872-RH-Linha-Protheus-TAF-eSocial-Eventos-N%C3%A3o-Peri%C3%B3dicos-S-2299-Descri%C3%A7%C3%A3o-N%C3%A3o-pode-existir-qualquer-evento-para-o-v%C3%ADnculo-trabalhista-com-data-posterior-a-data-do-desligamento
---

**Ocorrência:**

Ao transmitir o evento de desligamento para o e-Social ocorre o retorno RET 677: *Não pode existir qualquer evento para o vínculo trabalhista com data posterior*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019750292)

**Ambiente**:

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos Não Periódicos - S-2299 - Todas as versões  
  
  
**Causa**O erro ocorre pois o colaborador demitido não pode ter a folha de pagamento no mesmo mês (S-1200), ou existem eventos de alteração com data posterior a data do desligamento (S-2205 e S-2206).

**Exemplo:**

Colaborador foi demitido em Junho de 2023 e a empresa já tinha encaminhado o S-1200 desse colaborador do mês de junho, entretanto nesse mês não pode ter o S-1200, e sim apenas o S-1210 (referente aos periódicos) e o S-2299 (referente ao desligamento).

**Solução**

No caso em que existe folha de pagamento para o mesmo período, deverá excluir o S-1200 e encaminhar novamente apenas o  S-2299 e S-1210.

Se existir alteração de contrato ou alteração cadastral com data posterior, deverá excluir o evento e retransmitir com data igual ou anterior ao evento S-2299, ou somente excluir o S-2206 e S-2205 e retransmitir o S-2299.
