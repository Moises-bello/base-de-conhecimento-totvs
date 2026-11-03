---
content_hash: 696ca93541eddf352654b7ef1fd83e6a7ff35828083522a99efb02f36602aff0
fetched_at: '2026-06-29T00:11:25.437029+00:00'
page_id: '708882561'
product: rm
source: tdn-rm
title: Tag para complemento de histórico de lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708882561
version: 6
---

---

As tags são recursos que permitem ao usuário adicionar alguma informação acadêmica ou financeira específica do TOTVS Gestão Educacional no complemento histórico do lançamento financeiro vinculado ao contrato do aluno no TOTVS Gestão Financeira.

**Variáveis disponibilizadas**:

* **[SRV.C]**- Código do Serviço
* **[SRV.D]**- Nome do Serviço
* **[ALU.C]**- RA do Aluno
* **[ALU.D]**- Nome do Aluno (Caso o Nome Social esteja preenchido, a tag será preenchida com essa informação. Essa regra foi descontinuada a partir dos patches **12.1.2306.255, 12.1.2310.199, 12.1.2402.139, 12.1.2406**, pois foi criado uma variável específica para o Nome Social do Aluno)
* **[ALU.S]** - Nome Social do Aluno. Variável disponível a partir dos patches **12.1.2306.255, 12.1.2310.199, 12.1.2402.139, 12.1.2406**
* **[CUR.C]**- Código do Curso
* **[CUR.D]**- Nome do Curso
* **[PAR.C]**- Número da Parcela
* **[COT.C]**- Número da Cota
* **[BOL.CX]**- Código da Bolsa
* **[BOL.DX]**- Nome da Bolsa
* **[BOL.VX]**- Valor da Bolsa
* **[LAN.DV]** - Data de Vencimento do Lançamento
* **[PRL.C]** - Período Letivo
* **[CNT.C]** - Código do Contrato do Aluno. Variável disponível a partir dos patches **12.1.32.315, 12.1.33.284, 12.1.34.185, 12.1.2205.124**

O histórico padrão é preenchido nos parâmetros do sistema em Configurações | Parâmetros | Integração | Financeiro | Educacional | Fin - Geral 2/4. Durante a execução da geração de lançamentos em lote, é possível visualizar e definir novos itens para o histórico. Se não houver nenhum item na geração de lançamento, o histórico considerado será o da parametrização.

A letra 'X' das variáveis de Bolsa serve para indicar qual Bolsa será utilizada.

Vamos supor que no contrato do aluno existam 2 bolsas associadas. Para que as duas bolsas sejam referenciadas no complemento do histórico, inclua a variável duas vezes e substitua o 'X' número de ordem da bolsa.

**Exemplo:**   
Bolsas associadas no contrato do aluno: **'FIES'** e **'Aproveitamento'**Para que no lançamento contábil seja impresso o nome das duas Bolsas e seus respectivos valores, inclua no complemento uma variável para cada Bolsa e indique o número correspondente, assim: [BOL.D1] = [BOL.V1] - [BOL.D2] = [BOL.V2]

A ordem da Bolsa irá respeitar o código da Bolsa.   
As duas Bolsas associadas são:  
- Bolsa 'FIES' de código 5 com valor de 20,00  
- Bolsa 'Aproveitamento' de código 10 com valor de 30,00

Desta forma, no complemento do histórico onde o 'X' foi substituído por 1, serão apresentados os dados referentes à Bolsa 'FIES'. E onde o 'X' foi substituído por 2, serão apresentados os dados referentes à Bolsa 'Aproveitamento', assim:  
[BOL.D1] = [BOL.V1] - [BOL.D2] = [BOL.V2]   
FIES = 20,00 - Aproveitamento = 30,00
