---
content_hash: 1b49c5adf320c7476514a741454abdc773e0730b63d1c68e14a309b887a2843a
fetched_at: '2026-06-29T00:09:22.801702+00:00'
page_id: '422546034'
product: rm
source: tdn-rm
title: Regras aplicadas à geração dos registros M312 e M362
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546034
version: 2
---

Conforme a regra "**REGRA\_REGISTRO\_M312\_OBRIGATORIO**" e "**REGRA\_REGISTRO\_M362\_OBRIGATORIO**" especificada no manual da ECF no registro M310/M360, o registro M312 e M362 deve ser gerado somente quando os valores apurados forem diferentes dos valores do bloco K.  Entendemos que isso irá ocorrer quando o usuário utilizar filtros para identificar o valor a ser processado pela apuração no TOTVS Gestão Fiscal, exemplo, utilizar um filtro por departamento ou conta gerencial, neste caso o valor processado será diferente do valor apresentado no K155/K355. Quando isto ocorrer então iremos gerar o registro M312/M362 com o identificadores dos lançamentos que compõem as informações parametrizadas no Evento Tributário, exemplo:

Evento Tributário:   
Conta : A,   
Gerencial: 5.01,  
Origem: Total de Débitos. Identificamos todos lançamentos a débito para a conta A e que tenha o gerencial a débito igual a 5.01.
