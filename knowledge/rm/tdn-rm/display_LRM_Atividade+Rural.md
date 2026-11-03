---
content_hash: f8321b39a7864160e4c40e50b05d704119e9c54a17cf89e9263bd84b9ad75c2a
fetched_at: '2026-06-29T00:09:20.123404+00:00'
page_id: '422545671'
product: rm
source: tdn-rm
title: Atividade Rural
type: documentation
url: https://tdn.totvs.com/display/LRM/Atividade+Rural
version: 6
---

#f5f5f5#363636noneAtividades Rurais

## **Conteúdo**



**01. Sobre****Sobre**

A distinção entre atividade geral e atividade rural é necessária apenas na Parte A do Lalur, ou seja, na demonstração do Lucro Real do período: conhecer o lucro real de cada uma das atividades de forma distinta.

De acordo com a legislação tributária, é possível compensar o prejuízo obtido em uma atividade com o lucro apurado na outra, limitado apenas ao montante do lucro.  
A parte excedente do prejuízo não compensada no período deve ser controlada na Parte B do Lalur e compensada nos períodos subsequentes.

## **02. Evento Tributário****EventoTributario**

No cadastro de [Evento Tributário](http://tdn.totvs.com/pages/viewpage.action?pageId=422545748), foram criados os  seguintes campos:  
Na tela de Identificação, criada flag "Atividade Rural" para indicar que o evento será utilizado para este fim. Nos Eventos Tributários com este campo marcado, devem ser apresentados os seguintes Grupos: 

Grupos Eventos Tributários

* Resultado Contábil
* Adições do Lucro
* Adições por Doação
* Exclusões do Lucro
* Compensação de Prejuízos

Em cada um desses Grupos, devem ser parametrizados os Itens Tributários referentes à atividade rural, com os Códigos da Tabela Dinâmica referentes a esta atividade.

O Evento de Atividade Rural deve ser vinculado ao evento Pai, através do cam**po Cod. Evento Atividade Rural.**Considere:

* Evento "pai" – aquele parametrizado para apuração do IRPJ/CSLL da atividade geral
* Evento "filho" – aquele parametrizado para apuração do IRPJ/CSLL da atividade rural.

Os itens tributários dos dois eventos devem ser gravados no Anexo "Detalhamento da Apuração" do Período de Apuração. Na pasta "Detalhamento" do Período de Apuração  
O PVA da ECF não importa a linha de "Compensação de Prejuízo do Próprio Período" no **Registro M300/M350**, uma vez que o campo é do tipo CNA (cálculo não alterável). Mesmo assim, para maior transparência ao usuário, a "**Compensação de Prejuízo do Próprio Período**" também deve ser gravado no Anexo "**Detalhamento da Apuração**", tendo como Origem "**Apuração**". Porém sem vínculo com a Tabela Dinâmica: 

## **03. Tributo IRPJ****TributoIRPJ**

Prejuízo da atividade rural compensado com lucro da atividade geral:

**"170 - Compensação de Prejuízo do Próprio Período - Atividade Rural"**

Prejuízo da atividade geral compensado com lucro da atividade rural:

**"344 -  Compensação do Prejuízo do Próprio Período - Atividades em Geral"**

Tributo Prejuízo da atividade rural compensado com lucro da atividade geral:

**"170 -  Compensação da Base de Cálculo Negativa do Próprio Período - Atividade Rural"**

Prejuízo da atividade geral compensado com lucro da atividade rural:

**"344 -  Compensação da Base de Cálculo Negativa do Próprio Período - Atividades em Geral".**

---
