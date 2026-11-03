---
content_hash: c960962597a581aeb9cc6f8c38b8e689163104ebcc34125c4e806d73f333db47
fetched_at: '2026-06-29T00:11:16.198341+00:00'
page_id: '664192404'
product: rm
source: tdn-rm
title: Capacidade do Bem
type: documentation
url: https://tdn.totvs.com/display/LRM/Capacidade+do+Bem
version: 1
---

Para que seja considerada a capacidade do Bem no cálculo da apropriação, é necessário realizar o cadastro dos campos complementares no módulo de Backoffice - Gestão Patrimonial; conforme detalhado abaixo:

No módulo de Gestão Patrimonial, acesse o menu Cadastros/Campos Complementares/Patrimônio:

E realize o cadastro dos dois campos conforme as imagens:

**Importante:**

* **É imprescindível que as colunas sejam criadas com a nomenclatura exata - CAPACIDADEPROD e CAPACIDADECODUND - caso considere a capacidade do bem na apropriação.**
* **Isso também é válido para o correto funcionamento da integração com o SIGAMNT, pois esses campos deverão ter seus valores preenchidos através do sincronismo entre os sistemas.**

Com base nos valores desses campos complementares, contidos no cadastro do patrimônio associado ao insumo informado no ciclo de transporte, que é calculada a apropriação:

Caso os campos não sejam informados, o cálculo da apropriação será realizado como se o checkbox "Considera Capacidade do Bem" não estivesse marcado.

Para saber mais sobre a apropriação do Ciclo de Transporte, navege até a aba "Apropriar Custos de Apontamento"
