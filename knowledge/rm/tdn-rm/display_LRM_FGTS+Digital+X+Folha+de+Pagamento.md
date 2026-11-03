---
content_hash: a6ef6a386fbc59dcb6241a5324094c16f269b117c6c75bdb7c09dd23da94b388
fetched_at: '2026-06-29T00:11:50.288241+00:00'
page_id: '839969063'
product: rm
source: tdn-rm
title: FGTS Digital X Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/FGTS+Digital+X+Folha+de+Pagamento
version: 18
---

**OBJETIVO**

        Este documento tem como objetivo detalhar as principais dúvidas e ocorrências do **FGTS Digital**:

**Índice:**

---

* ## **Como realizar a conferencia das bases de FGTS na rescisão?**

No relatório da Folha Analítica, foram criadas as seguintes bases para auxiliar na conferência:

* + **Base FGTS eSocial:** É a soma dos eventos que incidem FGTS, subtraindo os eventos que estornam o FGTS. Nesse cálculo, são desconsiderados os códigos de cálculos 62, 99, 219 e 140.
  + **Base FGTS 13o. Sal.** **eSocial:** É a soma dos eventos que incidem FGTS 13º salário, subtraindo os eventos que estornam o FGTS 13º salário. Nesse cálculo, são desconsiderados os códigos de cálculos 71, 98 e 220.
  + **Base FGTS Indeniz.** **eSocial:** É calculada considerando apenas os eventos que estão associados aos códigos de cálculos 62, 99, 219, 140, 71, 98 e 220.
  + **FGTS eSocial:** É calculado como 8% ou 2% da **Base FGTS eSocial**, dependendo da alíquota aplicável.
  + **FGTS 13o. Sal. eSocial:** É calculado como 8% ou 2% da **Base FGTS 13o. Sal.** **eSocial**, dependendo da alíquota aplicável.
  + **FGTS Indeniz.** **eSocial:** É calculado como 8% ou 2% da **Base FGTS Indeniz.** **eSocial**, dependendo da alíquota aplicável.

No Relatório de Conferência de FGTS, é possível comparar os valores enviados com os valores do envelope, exceto no caso da multa rescisória.

**Documentação de apoio:**

---

* ## **Como realizar o lançamento financeiro do FGTS Digital?**

Foi realizada a criação e de um novo tipo de lançamento financeiro: "**24 - Total Guia FGTS Digital**". Este deverá ser parametrizado e utilizado através do menu Encargos | Geração dos Lançamentos, conforme documentação completa abaixo:

**Documentação de apoio:**

---

* ## **Como o sistema trata as bases negativas de FGTS e/ou FGTS 13º Salário?**

O produto TOTVS Folha de Pagamento foi ajustado para ser compatível com as normas do FGTS Digital, especialmente para situações de **rescisão** que envolvem **descontos de adiantamento do 13º salário superiores ao valor pago** e **estorno de FGTS maior do que os proventos**.

Com a implementação do FGTS Digital, foram realizadas alterações na demonstração das bases de FGTS para os seguintes cenários:

- Quando o funcionário demitido possui desconto de adiantamento de 13º salário superior ao valor pago.  
- Quando o funcionário demitido possui um estorno de FGTS maior que os proventos

Veja a documentação completa abaixo:

**Documentação de apoio:**   
[FGTS Digital - Tratativa quando há base negativa de FGTS e/ou FGTS 13o. Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=832650111)

---

* ## **Por que alguns funcionários aparecem sem tomador de serviços no eSocial, embora haja o vínculo do tomador na folha de pagamento?**

A identificação do tomador é enviada através da lotação tributária, evento S-1020.  
É necessário enviar o S-1020 com o CNPJ ou CPF do tomador de serviços, para que haja a identificação do mesmo no portal do governo e consequentemente no FGTS Digital. 

Verifique mais informações através da documentação abaixo:

**Documentação de apoio**:   
[Como informar ao governo que o estabelecimento possui tomador de serviços, para identificação no FGTS Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22853725160343)

---

* ## **Como proceder para lançar a diferença do Dissídio, agora que o sindicato enviou o percentual correto? Como isso afeta o processo para os Códigos 115 e 650 no contexto do FGTS Digital?**

No caso de recolhimento de **FGTS** mensal devido a partir da competência março/2024, o empregador deve **recolher** por meio do **FGTS Digital todos os valores já declarados ao eSocial** no evento S-1200/S-2299/S-2299/S-2399. Apenas os **valores ainda não declarados ao eSocial** e **reconhecidos em processo trabalhista**, devidos a qualquer tempo, devem ser **recolhidos via guias SEFIP 650/660**, pois serão informados apenas no evento S-2500, que ainda não foi internalizado no FGTS Digital.

Veja a orientação completa na documentação abaixo:

**Documentação de apoio**:   
[Emissão da guia SEFIP 650/660 no FGTS Digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22874966911127)

---

* ## **Como posso acessar os vídeos e as perguntas frequentes disponíveis pelo governo para o FGTS Digital?**

* + Pagina centralizadora FGTS Digital - Principais notícias, alertas, agendas com as lives tira dúvidas a serem realizadas pelo governo:  
    <https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital>
  + Manual e documentação técnica:  
    <https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica>
  + Vídeos e tutoriais FGTS Digital:  
    <https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/videos-e-tutoriais>
  + Fale Conosco FGTS Digital:  
    <https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/fale-conosco>

---
