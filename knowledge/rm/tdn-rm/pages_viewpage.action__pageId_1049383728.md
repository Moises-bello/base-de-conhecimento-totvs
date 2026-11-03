---
content_hash: e0233c522525dad5f95b3cfeb283f6733ddb11a694527a663e91c45186c7d98d
fetched_at: '2026-06-29T00:05:51.211763+00:00'
page_id: '1049383728'
product: rm
source: tdn-rm
title: 9 - Bancos Habilitados para Registro de Boleto Híbrido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1049383728
version: 3
---

O **registro de Boletos Híbridos** está disponível para os seguintes bancos:

* Itaú
* Banco do Brasil
* Santander
* Sicoob
* Caixa (CEF)​\*
* Bradesco\*
* Sicredi

\*O banco Bradesco e a Caixa (CEF) não disponibilizam no retorno as informações de Juros, Multa, Descontos e Abatimentos em campos separados. Caso o boleto seja pago e de acordo com a data do pagamento ocorrer Juros, Multa, Descontos ou Abatimentos, este valores não são discriminados na API de retorno dos bancos citados. No retorno é informado o valor total pago pelo pagador (sacado).

Esta e demais orientações a respeito das particularidades por banco para configuração de boleto no ERP estão descritas do TDN:

---

Cada instituição financeira possui **regras e particularidades próprias** para os seguintes parâmetros do boleto:

* **Multa**
* **Juros**
* **Desconto**
* **Protesto**

⚠️ **Importante**

As regras apresentadas nesta documentação **não são definidas pelo sistema**, mas sim pelos **padrões estabelecidos pelos próprios bancos**.

Por esse motivo, é fundamental respeitar essas exigências para garantir que o **registro do boleto híbrido seja realizado com sucesso**.

---

# Regras de Multa

A modalidade de **multa por percentual** é suportada por todos os bancos habilitados.

| Modalidade | Itaú | Banco do Brasil | Santander | Sicoob | Bradesco | Sicredi |
| --- | --- | --- | --- | --- | --- | --- |
| Percentual | Sim | Sim | Sim | Sim | Sim | Sim |

---

# Regras de Juros

Cada banco possui regras específicas para cálculo de juros. Consulte a tabela abaixo para verificar quais modalidades são aceitas.

| Modalidade | Itaú | Banco do Brasil | Santander | Sicoob | Bradesco | Sicredi |
| --- | --- | --- | --- | --- | --- | --- |
| Percentual por Dia Corrido | Sim | Sim | Não | Não | Sim | Sim |
| Percentual por Mês Corrido | Sim | Sim | Sim | Sim | Não | Não |
| Percentual por Ano Corrido | Não | Não | Não | Não | Não | Não |
| Valor por Dia Útil | Sim | Não | Não | Não | Não | Não |
| Percentual por Dia Útil | Sim | Não | Não | Não | Não | Não |

---

# Regras de Desconto

As opções de desconto aceitas variam conforme o banco. Atualmente, a principal modalidade suportada é **percentual até a data de vencimento**.

| Modalidade | Itaú | Banco do Brasil | Santander | Sicoob | Bradesco | Sicredi |
| --- | --- | --- | --- | --- | --- | --- |
| Percentual até o Vencimento | Sim | Sim | Não | Sim | Sim | Sim |
| Valor por Dia Corrido Antecipado | Não | Não | Não | Não | Não | Não |
| Valor por Dia Útil Antecipado | Não | Não | Não | Não | Não | Não |
| Percentual por Dia Corrido Antecipado | Não | Não | Não | Não | Não | Não |
| Percentual por Dia Útil Antecipado | Não | Não | Não | Não | Não | Não |

---

# Regras de Protesto

As regras de **protesto de boletos** podem variar de acordo com:

* Convênio bancário
* Tipo de carteira
* Configuração acordada com o banco

⚠️ **Recomendação**

Antes de configurar o protesto no boleto híbrido, valide com o seu banco:

* Se o convênio permite protesto
* O prazo mínimo de dias para protesto
* O tipo de instrução suportada

Essas informações devem estar **alinhadas com o convênio registrado junto à instituição financeira**.
