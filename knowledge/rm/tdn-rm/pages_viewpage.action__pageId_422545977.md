---
content_hash: 98a62f49717ddd2a40a49a133292c29a34472a4c14a7683910aac569e73c6f4c
fetched_at: '2026-06-29T00:09:22.124418+00:00'
page_id: '422545977'
product: rm
source: tdn-rm
title: Bloco P (EFD Contribuições)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545977
version: 7
---

## Apuração da Contribuição Previdenciária Sobre a Receita Bruta (CPRB)

**Adequação a Nota técnica nº 007/2018:** Bloco P não será mais gerado pela rotina da EFD-Contribuições, assim como o Registro 0145, a partir da vigência de julho/2018. Por meio da [Nota Técnica EFD-Contribuições nº 007, de 23 de maio de 2018](http://sped.rfb.gov.br/pagina/show/2678), o Bloco P não deverá mais ser gerado no arquivo do EFD PIS\COFINS a partir da Competência de julho/2018, entregue até o 10º (décimo) dia útil do 2º (segundo) mês subsequente.

Conforme disposto nos art. 7º e 8º da Medida Provisória nº 540/2011, convertida na [Lei nº 12.546/2011](http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12546.htm), as empresas que prestam serviços de tecnologia da informação (TI), de tecnologia da informação e comunicação (TIC), serviços de call center, bem como as empresas fabricantes de vestuário e seus acessórios, calçados, bolsas e outros produtos de couro curtido ou natural, etc., se sujeitam à apuração da Contribuição Previdenciária incidente sobre o valor da receita bruta mensal, cuja escrituração será efetuada no Bloco "P – Apuração da Contribuição Previdenciária sobre a Receita Bruta", da EFD — Contribuições, conforme art. 4º da [Instrução Normativa RFB nº 1.252/2012](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=37466).

A escrituração do Bloco "P" será específica para a  apuração da Contribuição Previdenciária sobre Receita, efetuada pela pessoa jurídica de forma autônoma e independente da escrituração de apuração do PIS/Pasep e da Cofins, constante nos Blocos  "A", "C", "D", "F" e "M".

Trata-se de nova contribuição, exigível em relação aos fatos geradores a ocorrer a partir de março de 2012, não guardando a escrituração do Bloco "P" qualquer correlação ou vinculação com os registros informados nos referidos blocos.

Será acrescido no Bloco "0" o registro "0145 — Regime de Apuração da Contribuição Previdenciária Sobre a Receita Bruta" filho do registro "0140 — Tabela de Cadastro de Estabelecimento" que servirá como registro identificador de obrigatoriedade de escrituração do Bloco "P", pelo correspondente estabelecimento da pessoa jurídica.

O bloco "P" só deve ser exigido na EFD-PIS/Cofins da pessoa jurídica caso tenha sido gerado no mínimo 01 (um) registro "0145", indicando a sujeição da pessoa jurídica à nova contribuição, no período da escrituração.

A inexistência de registro "0145" no Bloco "0", deve dispensar a necessidade de gerar o Bloco "P", inclusive em relação a registros de abertura e de encerramento deste.

Para a correta geração do bloco P deve-se:

* Criar o Tributo Contribuições Previdenciárias cujo tipo será CONTR PREVIDENCIARIA.
* Gravar nos itens dos Lançamentos Fiscais o novo tributo.
* Os [Produtos](http://tdn.totvs.com.br/display/LRM/Produto) utilizados nos lançamentos Fiscais deverão ter a informação do NCM gravada em seus detalhes conforme a tabela 5.1.1 de conversão disponibilizada no guia prático da EFD Contribuições.
* Na tela de geração da rotina, no parâmetro *"Contribuição Previdenciária Indicador da Incidência"* deverá ser gravado o valor "*Contribuição Previdenciária apurada com base na Receita Bruta e com base nas Remunerações pagas"* .
* No [Período de Apuração](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422545656) deverá ser informado o total da receita bruta, manualmente, para a geração do registro 0145 e registro P100.

1leftp001Registro P001**Registro P001 — Abertura do bloco**  
Este é um registro de controle gerado automaticamente pelo processo da rotina.p010Registro P010**Registro P010 — Identificação do Estabelecimento**  
Será gerado um registro para cada Filial que possuir informações de apuração sobre a receita bruta. Serão considerados para que este registro seja gerado os Lançamentos Fiscais de entrada ou saída que possuam em seus itens o tributo do tipo Cont Previdenciária.p100Registro P100**Registro P100 — Contribuição Previdenciária sobre a Receita Bruta**  
Este registro será gerado somente se o campo 4 do Registro 0145 for maior que zero.  
Aqui a Contribuição Previdenciária será detalhada por código de atividade e por alíquota.  Para a correta geração e totalização das informações neste registro, o campo NCM nos detalhes do cadastro do Produto deverá estar preenchido de acordo com a tabela 5.1.1 do guia da EFD Contribuições.p110Registro P110**Registro P110 — Complemento da Escrituração - Detalhamento da Apuração da Contribuição**  
Este registro não será gerado e conforme o guia da EFD ele é opcional. Já está sendo estudado para ser implementado futuramente.p199Registro P199**Registro P199 — Processo Referenciado**  
Este registro não será gerado, pois hoje não é possível associar Processo Judicial/Administrativo ao Período de Apuração.p200Registro P200**Registro P200 — Consolidação da Contribuição Previdenciária sobre a Receita Bruta**  
Este registro consolida a Contribuição Previdenciária de todos os estabelecimentos.  
Os campos 04 — Valor Total do Ajuste de Redução e 05 - Valor Total do Ajuste de Acréscimo são gerados com base no registro P210.p210Registro P210**Registro P210 — Ajuste da Contribuição Previdenciária Apurada sobre a Receita Bruta**  
A informação deste registro tem origem nos lançamentos de Outros Débitos/Créditos do Tributo do tipo Contr Previdenciaria.  
O campo 02 — Indicador do Tipo de Ajuste será gerado com o valor 0 (zero) quando o lançamento for de crédito. Quando o lançamento for de débito este campo será gerado com o valor 1 (um).  
O campo 04 — Código do Ajuste será gerado com a informação gravada no campo Código Ajuste SPED. Os valores possíveis para este campo são encontrados na tabela 4.3.8 do guia da EFD Contribuições.  
O campo sub-tipo do lançamento de Outros Débitos/Créditos deve ser preenchido com "Não se aplica".p990Registro P990**Registro P990 — Encerramento do Bloco P**  
Este registro destina-se a identificar o encerramento do bloco P sendo gerado automaticamente pelo processo da rotina.
