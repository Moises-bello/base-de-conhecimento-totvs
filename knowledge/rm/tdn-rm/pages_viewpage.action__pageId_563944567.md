---
content_hash: f71f4d9ed274b4991d3284e7d0252fe9a5020c71e3951e5f322fc99ee89a9307
fetched_at: '2026-06-29T00:10:50.860297+00:00'
page_id: '563944567'
product: rm
source: tdn-rm
title: Como transferir o anexo Vínculo Empregatícios com Outras Empresas (Terceiros)
  ao calcular uma rescisão por transferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563944567
version: 23
---

**A partir das Versões:**

* 12.1.29.115
* 12.1.28.193
* 12.1.27.279

# Objetivo:

---

Permitir que ao calcular uma rescisão por transferência o anexo do funcionário" Vinculo empregatícios com outras empresas (Terceiros )" seja transferido para uma nova chapa.

---

**Exemplo:**

**Rescisão Tipo 5**

 Anexo do funcionário:

Após calcular uma rescisão tipo 5(Transferência sem onus p/ cedente) dia 31/08/2020, onde o funcionário possui 1 vínculo empregatício cadastrado com Competência Inicio=08/2020 e Competência Final =12/2020 e outro vínculo no ano 2018. O sistema irá transferir o anexo para nova chapa conforme abaixo:

**Observação:**

* Ao transferir um vínculo empregatício com o cadastro incorreto, o mesmo não será acertado na transferência.
* No tipo de demissão 6 rescisão com ônus p/ cedente não haverá transferência do anexo, isso acontece porque neste tipo de rescisão a empresa cedente irá realizar a rescisão arcando com todo o passivo trabalhista do funcionário.
* Ao transferir o funcionário com o parâmetro "Considera data de transferência igual a data demissão na transferência sem Ônus " **marcado,** o sistema não irá transferir o anexo.
* O sistema só irá transferir o anexo se a data de transferência for no ultimo dia da competência.
