---
content_hash: 8e5427017311026b78eff804f06f81d15fcfbf2669885cb8a56f7c625b2b407a
fetched_at: '2026-06-29T00:05:54.933414+00:00'
page_id: '118883664'
product: rm
source: tdn-rm
title: COMO FAZER - Desoneração Guia de INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=118883664
version: 1
---

**Produto: RM Labore**

Processo: Desoneração da Guia de INSS

Versão: 11.5X ou superior

Foi criado a tela de cadastro '**Parâmetros da Guia de INSS Desoneração'**  disponível na geração da Guia de INSS, que deve ser abastecida antes da sua geração para empresas que possuem o percentual redutor para aplicar no campo parte empresa da guia.

 

Na tela acima devem ser informados os valores da receita bruta com desoneração e receita bruta de demais atividades. O percentual redutor será calculado automaticamente com base nestes valores. O cálculo será realizado conforme abaixo:

**PercentualRedutor = (ReceitaBrutaDemaisAtividades /( ReceitaBrutaDemaisAtividades + ReceitaBrutaDesoneracao)) \* 100**

**OBS:** Caso o valor do campo receita bruta de demais atividades esteja zerado e o campo receita bruta com desoneração for informado, o campo parte Empresa da Guia de INSS será zerado.

Uma vez informados os valores acima, o recolhimento da parte empresa será feito da seguinte forma:

a) O recolhimento referente à receita bruta com desoneração deverá ser feito através de relatório DARF com código 2985.

b) O recolhimento referente à receita bruta das demais atividades será feito na própria GPS, utilizando para isto o percentual redutor calculado acima.

Na guia de INSS foi criado o parâmetro

**‘Utilizar percentual redutor (Lei 12.546/2011)’**  para correto cálculo da parte empresa. O parâmetro **‘Por filial’**  busca os valores do novo cadastro de acordo com a quebra de CNPJ.

O parâmetro **‘Por Empresa’**  busca o valor do novo cadastro de acordo com a seção informada na guia. O percentual definido na Empresa informada será utilizado para as demais Empresas.

 

 

É possível verificar o cálculo na memória da guia:
