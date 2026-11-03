---
content_hash: b6de6f3fce9f85682a6a3f0aa99566fa52f360e43b09523bd9ab19de9a555f8e
fetched_at: '2026-06-29T00:10:11.848398+00:00'
page_id: '453290835'
product: rm
source: tdn-rm
title: Eventos Societários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453290835
version: 3
---

Versão 12.1.2302

A partir da versão 12.1.2302, os cadastros de "Controladas" e "Eventos Societários" serão descontinuados do sistema e substituídos por Grupos Empresariais.  
Para mais informações consulte a documentação a seguir :

O cadastro  tem como objetivo incluir os eventos societários e as empresas participantes que irão compor os registros k110 e K115, que serão gerados pelo SPED Contábil.

A tela possui os seguintes campos:

1 - Descrição: Lista com os eventos societários ocorridos no período.

2 - Data: Data do evento.

3 - Empresa: Código da Coligada/Empresa que sofreu o evento societário. Deverá retornar a controladora e suas controladas.

4 - Empresa Envolvida: Código da Coligada/Empresa envolvida na operação. Deverá retornar a controladora e suas controladas.

5 - Condição da Empresa: Condição da empresa relacionada a operação. Ela possui as seguintes regras:

* Será igual a "Adquirente", se o evento societário ocorrido no período for preenchido como "Aquisição";
* Será igual a "Alienante", se o evento societário ocorrido no período for preenchido como "Alienação";
* Será igual a "Sucessora", se o evento societário ocorrido no período for preenchido como "Fusão", "Cisão Parcial", "Cisão Total" ou "Incorporação".

6 - % Empresa Participante: Percentual da empresa participante envolvida na operação

Todos os campos acima são obrigatórios, porém se a descrição selecionada for “Extinção” ou “Constituição” os campos Empresa Envolvida, Condição da Empresa e % da Empresa Participante ficarão desabilitados e deixarão de ser obrigatórios.

Observações:

1 - Os campos Empresa e Empresa Envolvida deverão ser diferentes;

2 - Para uma mesma data não poderão haver eventos societários com as mesmas empresas, descrição e condição;

3 - O percentual de participação dever ser maior ou igual a zero e menor ou igual a cem.
