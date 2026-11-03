---
content_hash: f9a060ea3f10d0000b7dfa92aa9d6caff20969bf4485ab6aaf5abae35cdfa5a4
fetched_at: '2026-06-29T00:05:47.418096+00:00'
page_id: '1013635882'
product: rm
source: tdn-rm
title: SPED Fiscal Alterações do Layout 2026 - Versão 3.2.1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1013635882
version: 20
---

# Conteúdo

2Conteúdononenone

# 1. Sobre

Neste documento iremos destacar as mudanças do Layout da EDF ICMS e IPI considerando as versões do Guia Prático 3.1.19, 3.2.0 e 3.2.1. Também apresentaremos as alterações no sistema para atender as mudanças introduzidas por estas versões.

# 2. Versões para atualização

A solução para atender estas alterações está disponível a partir dos patches:

Data: **18/12/2025**

Biblioteca RM

* 12.1.2502.251
* 12.1.2506.210
* 12.1.2510.137

# 3. Alterações do Layout

## 3.1 Alterações implementadas

1lefttrue1Bloco 0

* Registro 0000:

Na tela de geração da rotina, alterado a versão para “020”. Essa versão só é válida a partir de 01/01/2026.

3Registro 1310

Foi criado o campo campo 11 no registro 1310 para que seja informada a capacidade de armazenamento do tanque.

**Campo 11**- CAP\_TANQUE; Capacidade de armazenagem, em litros.

Consulte os detalhe da geração dos campos desse registro no link:

2Bloco D

A alteração do Registro D700 é referente a geração do Código do Participante.

* Registro D700:

Alteração de preenchimento do campo :  
**Campo 04** - COD\_PART, Código do participante (Campo 02 do Registro 0150) do prestador, deve ser preenchido somente referente a lançamentos Fiscais de **Entradas**. 

## 3.2 Demais alterações

Abaixo seguem as demais alterações introduzidas por estes manuais nas quais não foram realizadas alterações no sistema

1. Inclusão do valor válido ‘2’ no campo 02 do registro C120
2. Desabilitação da regra aplicada nos campos 12 do registro C100 e campo 05 do registro C190
3. Inclusão da observação do registro C100 acerca da não escrituração dos documentos fiscais que carreguem informações exclusivamente acerca dos novos tributos criados na Reforma Tributária do Consumo e que não versem sobre fatos geradores do ICMS e do IPI.
4. Inclusão de orientação no registro 0150, relativamente ao DIFAL da EC 87/2015, na hipótese do § 30 do art. 19 do Convênio SN/1970.
5. Inclusão de orientação de preenchimento no campo 04 do registro D700
6. Inclusão no Capítulo I da Seção 10 – Informações sobre a Reforma Tributária sobre o Consumo.
7. Inclusão de orientação no registro K230
8. Alteração do tipo do campo 07 (SER) registro D700, de N para C.
9. Alteração na orientação de preenchimento do registro 0150.
10. Alteração da orientação disposta no Capítulo I da Seção 10 – Informações sobre a Reforma Tributária sobre o Consumo
11. Alteração na orientação de preenchimento do campo 12 (VL\_DOC) do registro C100.
12. Alteração na orientação de preenchimento do campo 25 (COD\_MUN\_DEST) do registro D100.

# 4. Legislação

Este documento foi elaborado com base nas alterações abaixo disponíveis no portal do SPED

* [Guia Prático EFD ICMS IPI versão 3.1.9](http://sped.rfb.gov.br/item/show/7818)
* [Guia Prático EFD ICMS IPI versão 3.2.0](http://sped.rfb.gov.br/item/show/7867)
* [Guia Prático EFD ICMS IPI versão 3.2.1](http://sped.rfb.gov.br/item/show/7900)
