---
content_hash: 3da5acb48641707e6a8d84d42da76bde456ea513824affedafcb18f088e63d74
fetched_at: '2026-06-29T00:10:27.917547+00:00'
page_id: '517122779'
product: rm
source: tdn-rm
title: NF-e - Valor do Crédito no ICMS - Empresa Optante pelo Simples Nacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=517122779
version: 19
---

As pessoas jurídicas e aquelas a elas equiparadas pela legislação tributária não optantes pelo Simples Nacional terão direito a crédito correspondente ao ICMS incidente sobre as suas aquisições de mercadorias de microempresa ou empresa de pequeno porte optante pelo Simples Nacional, desde que destinadas à comercialização ou industrialização e observado, como limite, o ICMS efetivamente devido pelas optantes pelo Simples Nacional em relação a essas aquisições.

# Cadastros

Será necessário cadastrar o "ICMS  Crédito SN" no cadastro de tributos. Vide documentação especifica .

A filial deverá ser cadastrada como *"Optante pelo Simples Nacional"*. Para alterar o cadastro da Filial, acesse o Anexos | Dados Fiscais na guia Tipo de Estabelecimento e marque a opção "*Optante Regime Simplificado*".

# Movimento

Ao criar um Movimento no Nucleus que esteja parametrizado com "ICMS Crédito SN",  na linha do tributo, os campos serão preenchidos com as seguintes regras:

* **Base de Cálculo:** Será preenchida com o resultado da Fórmula de Base de Cálculo defina nos Parâmetros do Tipo de Movimento;
* **Alíquota:** No caso do "ICMS Crédito SN"  o campo de alíquota será preenchido conforme documentação "[O Processo do Simples Nacional](https://tdn.totvs.com/display/LRM/O+Processo+do+Simples+Nacional)" etapa "**Calculo da Alíquota na inclusão do Movimento".**
* **Valor:** Será preenchido com o resultado da Multiplicação dos campos **Base de Cálculo** **X** **Alíquota**, se a alíquota tiver sido preenchida.

# NF-e

No XML da NF-e (Nota Fiscal Eletrônica) os campos abaixo referente ao crédito do simples serão preenchidos.

Na tributação do item:

* **pCredSN;**
* **vCredICMSSN;**

Atenção

Na geração das tags indicadas acima, o  sistema irá considerar o tributo "ICMS Crédito SN"  para os CSOSN 101, 201 e 900.

Atenção

Na geração das tags indicadas acima, o sistema irá priorizar o tributo "ICMS Crédito SN", na ausência do mesmo será considerado o tributo "ICMS".

Documentação especifica  | Grupo CRT=1 (Tributação ICMS pelo Simples Nacional).

# Escrituração

No processo de Escrituração Fiscal, o tributo "ICMS  Crédito SN" não será escriturado para o Lançamento Fiscal, ou seja, independente do status do Período de Apuração (Aberto/Encerrado)

## Base Legal

Resolução CGSN 140/2018 - Art. 60...

Resolução CGSN 140/2018) - Art. 25 § 8º...

Lei Complementar 123/2006.

Importante

Implementação a partir do release 12.1.24.
