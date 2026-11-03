---
content_hash: fbac65214fe03f4cc87b6d0a9f82a5ba0fcce951c5416ad0c3c40b087fb33e6a
fetched_at: '2026-07-02T19:24:27.015513+00:00'
page_id: '655442763'
product: protheus
source: tdn-tec
title: e-4 - Pulando Testes
type: documentation
url: https://tdn.totvs.com/display/tec/e-4+-+Pulando+Testes
version: 13
---

Durante a execução dos testes através do PROBAT é possível "pular" alguns testes, esse recurso embora deva ser evitado ao máximo pois um teste deve ser executado sempre e sua finalidade é forçar as correções.

Porém, algumas correções ou pendências podem demorar muito para ocorrer por muitas causas e nesse caso não faz sentido termos o plano de testes quebrando por uma pendência na qual não tenhamos gerência para mudar, por exemplo.

Outro exemplo é realizar o "pulo" para determinadas versões do AppServer, tlppCore, SO específico, Banco de Dados ou até por uma função customizada.

O **PROBAT** embora "pule" a execução do testes, o salto será registrado, e mesmo não quebrando os resultados irá exportar a informação do teste como "skipped".

Pela documentação abaixo é possível aprender todas as técnicas de como marcar Testes para serem pulados:

Para exemplos completos, veja em (Exemplo no GitHub) em: [github.com/totvs/tlpp-probat-samples](https://github.com/totvs/tlpp-probat-samples "https://github.com/totvs/tlpp-probat-samples")
