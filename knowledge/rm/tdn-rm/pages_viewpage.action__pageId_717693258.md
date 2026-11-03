---
content_hash: d784d922b958955fcc4ebb39a66fefc63cbb84d4b64778766d0323a7063d807c
fetched_at: '2026-06-29T00:11:26.448909+00:00'
page_id: '717693258'
product: rm
source: tdn-rm
title: Código de Cálculo 465 - DIFERENÇA ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=717693258
version: 7
---

Provento do tipo valor.

Este evento será utilizado para cálculo da diferença do evento com código de cálculo 445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO e será lançado no envelope do funcionário após a realização do processo de cálculo da diferença salarial.

De acordo com Jurisprudência consolidada do STJ, [Parecer SEI Nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-), veja maiores informações em [Folha de Pagamento - Atestado médico com incidência somente segurado (CC445)](https://tdn.totvs.com/pages/viewpage.action?pageId=590618716).

**Atenção:**

Devido a alteração posterior no Parecer SEI Nº 16120/2020/ME, os  eventos com o Código de Cálculo 465 - DIFERENÇA ATESTADO MÉDICO SEM INCIDÊNCIA INSS, na aba Inc. Proventos, não deverão ter marcadas as flags INSS e Incidência exclusiva do segurado.

**Observação:**

O evento com CC465 - DIFERENÇA ATESTADO MÉDICO SEM INCIDÊNCIA EM INSS, será lançando no envelope de diferença salarial, após ser calculada pelo módulo Diferença Salarial,  onde o funcionário tenha no envelope original para recálculo, o evento com código de cálculo 445 - ATESTADO MÉDICO COM INCIDÊNCIA SOMENTE SEGURADO. O evento de forma manual no cadastro de eventos.
