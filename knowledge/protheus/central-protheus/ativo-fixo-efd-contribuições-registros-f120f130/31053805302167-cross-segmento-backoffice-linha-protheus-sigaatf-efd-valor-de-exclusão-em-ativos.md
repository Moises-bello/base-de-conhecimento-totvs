---
article_id: 31053805302167
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: f7c9eafcbc663587973f94d4bef90bc4430df2b5e4e3ec5ca74a4bcebefeff48
fetched_at: '2026-06-28T22:41:36.221424+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - EFD - Valor de Exclusão
  em ativos sem integração com Compras
type: support-article
updated_at: '2025-04-01T12:02:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31053805302167-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-EFD-Valor-de-Exclus%C3%A3o-em-ativos-sem-integra%C3%A7%C3%A3o-com-Compras
---

**Dúvida:**

Ao realizar a apuração utilizando a rotina FISA001, o sistema está preenchendo o campo com valor de exclusão para itens que não possuem integração com o documento de entrada.

**Ambiente:**

Microsiga Protheus - Ativo Fixo - Todas as versões

**Solução:**

Com o ajuste na legislação **14.592/2023**, os valores de exclusão passarão a ser gerados com base no **campo ICMS** da entrada do bem, conforme a parametrização sistêmica.

Isso significa que ativos/componentes que tiveram suas entradas registradas por meio de um **documento de entrada** e posteriormente foram agregados a um **novo bem (bem principal) utilizando rotinas de aglutinação, como a ATFA251.** levarão consigo as informações do **ICMS da nota de cada componente**, garantindo a geração dos valores de exclusão no novo bem vinculado.

É importante ressaltar que, no processo de vínculo do componente ao bem principal, o histórico dos **dados de entrada** será mantido, assegurando que todos os valores de dedução necessários sejam gerados corretamente para a apuração.

Caso os componentes sejam adquiridos **após a entrada em vigor da lei**, tenham **ICMS na entrada** e a **TES esteja configurada com CRED ICM = NÃO**, todos os valores serão contabilizados para apuração e preenchimento do valor de exclusão. 

Além disso, outro exemplo seria a **inclusão de um frete agregado ao ativo.** Caso o frete tenha um valor de ICMS aplicado, o sistema utiliza o campo Vlr.ICMS (D1\_VALICM) para preencher o Vl.Exclu (CL2\_VLEXCL). Assim, **se o frete do ativo incluir ICMS**, esse valor será somado ao total de exclusão, pois o ativo está configurado para incorporar o valor do frete ao seu total.  
   
Para a conferência deste cenário, emita o relatório [COMSV018](%20https://tdn.totvs.com.br/display/public/PROT/Smart+View+-+Listagem+de+Notas+Fiscais+x+Notas+Fiscais+de+Frete)**,** filtrando pelo campo número do documento de entrada original, para identificar **se a nota fiscal possui algum valor de frete (CTE).** Caso exista, o sistema pode estar considerando esse valor na composição dos créditos do ativo.
