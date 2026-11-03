---
content_hash: a22131888bb1421543581b9c52a955c9e750eabcf20a316ad36ff04bdc744581
fetched_at: '2026-06-29T00:09:10.004620+00:00'
page_id: '394222751'
product: rm
source: tdn-rm
title: S-2230 - Como funcionam os motivos(codMotAfast) para afastamentos de Licença
  Maternidade?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394222751
version: 14
---

---

No parametrizador da Folha de Pagamento, existem quatro parâmetros que definirão quais serão os motivos de afastamento relacionados à licença maternidade que serão levados ao eSocial.

Para visualizar esses parâmetros, acesse o menu Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Salário Maternidade 2/2:

Ao incluir qualquer afastamento do tipo E - Licença Maternidade, no momento que gerar o XML dos eventos de afastamento, o sistema verifica qual o código do motivo do afastamento informado nesses parâmetros para definir qual será o motivo do eSocial a ser considerado.

---

# Veja abaixo alguns exemplos de afastamentos e como serão levados ao eSocial:

## 

## TIPO E LICENÇA MATERNIDADE 120 DIAS

17 - Licença Maternidade - 120 dias, inclusive para o cônjuge sobrevivente

## **TIPO E LICENÇA MATERNIDADE 120 DIAS COM ANTECIPAÇÃO MEDIANTE ATESTADO**

35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico

17 - Licença Maternidade - 120 dias, inclusive para o cônjuge sobrevivente

Observe que o código do motivo do afastamento dos primeiros 15  dias é o mesmo definido no parametrizador como “Antecipação”.

**TIPO E LICENÇA MATERNIDADE 120 DIAS COM PRORROGAÇÃO MEDIANTE ATESTADO**

17 - Licença Maternidade - 120 dias, inclusive para o cônjuge sobrevivente

35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico

## TIPO W LICENÇA MATERNIDADE COMPLEMENTAR 180 DIAS

17 - Licença Maternidade - 120 dias, inclusive para o cônjuge sobrevivente

18 - Licença Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidadã), inclusive para o cônjuge sobrevivente

## TIPO E LICENÇA MATERNIDADE 120 DIAS + TIPO W LICENÇA MATERNIDADE COMPLEMENTAR DE 60 DIAS + PRORROGAÇÃO MEDIANTE ATESTADO

17 - Licença Maternidade - 120 dias, inclusive para o cônjuge sobrevivente

18 - Licença Maternidade - 121 dias a 180 dias, Lei 11.770/2008 (Empresa Cidadã), inclusive para o cônjuge sobrevivente

35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico

## TIPO E LICENÇA MATERNIDADE – “Motivo de afastamento ref. a licença maternidade por aborto não criminoso”

19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso

## TIPO E LICENÇA MATERNIDADE – “Motivo de afastamento ref. a licença maternidade por adoção”

20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança, inclusive para o cônjuge sobrevivente

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
