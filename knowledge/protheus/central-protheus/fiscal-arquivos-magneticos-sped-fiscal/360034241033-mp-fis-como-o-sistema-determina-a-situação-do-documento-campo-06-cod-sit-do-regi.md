---
article_id: 360034241033
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: e7076347d1553a5d6803e7cae511a86c54954eefd720869da4a9be0dd16936bd
fetched_at: '2026-06-28T22:42:03.758640+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS -  Como o Sistema Determina a Situação do Documento? Campo 06 (COD_SIT)
  do Registro C100
type: support-article
updated_at: '2021-04-30T13:14:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034241033-MP-FIS-Como-o-Sistema-Determina-a-Situa%C3%A7%C3%A3o-do-Documento-Campo-06-COD-SIT-do-Registro-C100
---

**Dúvida**  
 Como o sistema determina a situação do documento? Campo 06 (COD\_SIT) do Registro C100  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**O campo COD\_SIT determina qual o tipo de documento é gerado no Sistema.

Seu preenchimento é feito de acordo com o conteúdo do campo **FT\_TIPO,** com os devidos códigos da tabela **4.1.2.**

**Tabela Situação do Documento para:**

* 00 Documento regular
* 01 Documento regular extemporâneo
* 02 Documento cancelado
* 03 Documento cancelado extemporâneo
* 04 NF-e ou CT-e - Denegado
* 05 NF-e ou CT-e - Numeração inutilizada
* 06 Documento Fiscal Complementar
* 07 Documento Fiscal Complementar extemporâneo.
* 08 Documento Fiscal emitido com base em Regime Especial ou Norma Específica

**Observação:** Não são todos os tipos de nota fiscal tratados pelo Sistema e por este motivo não são gerados no meio magnético.**Exemplo:** Documentos Extemporâneos.

00 - Normal - Caso campo **FT\_DTCANC** estiver em branco.

01 - Escrituração extemporânea de documento regular.

       Tabela CDT preenchida e os campos **CDT\_SITEXT = R** e **FT\_TIPOMOV = E**

02 - Cancelado - Caso campo **FT\_DTCANC** esteja preenchido.

04 - Uso Denegado - É necessário que exista o campo **F3\_CODRSEF**, e o campo esteja preenchido com valor de 110/204/205/301/302/303/304/305/306.

05 - Inutilizada - Uso Denegado - É necessário que exista o campo **F3\_CODRSEF**, e o mesmo esteja preenchido com valor de 102.

06 - Complemento - Campo **FT\_TIPO** conter as letras **I**, **C** ou **P** e campo **D1\_ORIGLAN** for diferente das expressões **FR** ou **F** ou **FD**.

       Complemento de IPI, Complemento de ICMS, Complemento de Preço e Beneficiamento.

07 - Escrituração extemporânea de documento complementar

Tabela CDT preenchida, e os campos **CDT\_SITEXT= P** e **FT\_TIPOMOV = E** e **FT\_TIPOMOV =** Contem a expressão **ICP** e campo  **D1\_ORIGLAN** for diferente das expressões **FR** ou **F** ou **FD**.

08 - Regime especial ou norma especifica.

Para que campo 6 do registro C100 COD\_SIT seja gerado como 8 é necessário que um dos campos **FT\_RGESPST** e **F4\_RGESPCI** estejam preenchidos como 1.

Os campos **FT\_RGESPST** e **F4\_RGESPCI** são preenchidos na TES nos campos:

* **F4\_RGESPCI**: Campo para Indicar se a operação deve ser tratada como Regime Especial de CIAP.
* **F4\_RGESPST**: Campo para Indicar se a operação deve ser tratada como  Regime Especial ST.

Ou

Quando parâmetro **MV\_UFRESPD** estiver preenchido com mesmo conteúdo do parâmetro **MV\_ESTADO** e cliente/fornecedor for optante pelo **Simples Nacional** (campo **A1/A2\_SIMPNAC**).

**MV\_UFRESPD**

Tipo: Caractere

Define as UF que devem considerar como regime especial os Clientes/Fornecedores optantes pelo Simples Nacional no SPED FISCAL

Ou

Quando campo **FT\_NORESP** estiver preenchido como **1** para nota fiscal de Norma Específica.

Este campo é preenchido pelo campo **F4\_NORESP** – **Norma Esp** no cadastro da TES na aba IMPOSTOS.
