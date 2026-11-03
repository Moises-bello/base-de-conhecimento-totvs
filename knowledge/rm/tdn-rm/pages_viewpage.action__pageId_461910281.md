---
content_hash: f8d4307c8aeff35f53f01738cb389add1a7d7d64b09cf5c62765bfe62b33c04a
fetched_at: '2026-06-29T00:10:14.602618+00:00'
page_id: '461910281'
product: rm
source: tdn-rm
title: Como realizar a geração do evento S-1200 com a tag remunSuc com valor "S"?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461910281
version: 12
---

false

**A partir das Versões:**

* + 12.1.23.129
  + 12.1.22.195
  + 12.1.21.218

# Objetivo:

---

Realizar um pagamento de  uma remuneração relativa a verbas de natureza salarial ou não salarial devidas pela empresa sucessora a empregados desligados ainda na sucedida.

Siga o passo a passo abaixo:

Execute o script especifico no sistema RM.Script.Executor.exe.

Acesse RH / Folha de Pagamento / eSocial / Acordo Coletivo / Reajuste por Lei

Cadastre o acordo coletivo/reajuste por lei, marque o parâmetro "Pagamento de verbas devidas pela empresa sucessora a empregador desligados ainda na sucedida" .

Acesse RH / Folha de Pagamento / Administração de Pessoal / Funcionários

O cadastro do funcionário demitido deve estar com o tipo de admissão "T-Ent Transf sem ônus p/ Cedente" e os dados da sucessão de vínculo cadastrado.

Acesse RH / Folha de Pagamento / Rescisão / Rescisão Complementar

Selecione a rescisão complementar com o parâmetro "Dissidio/Convenção/Acordo Coletivo" tipo sim, vincule os dados do Dissidio/Convenção/Acordo Coletivo cadastro acima e realize o calculo.

Acesse RH / Folha de Pagamento / eSocial / Gerar XML

Acesse RH / Folha de Pagamento / eSocial / Eventos Periódicos

Abaixo segue um exemplo do XML gerado corretamente através do sistema, sistema gerou corretamente, informando a tag remunSuc = S.
