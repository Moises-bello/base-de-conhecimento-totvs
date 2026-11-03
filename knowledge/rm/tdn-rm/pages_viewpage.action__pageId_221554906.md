---
content_hash: 7a7b9ba22d9b8e757acf979fcaa7c9085fd5793052ab05b1b563f9a0af623804
fetched_at: '2026-06-29T00:06:20.380920+00:00'
page_id: '221554906'
product: rm
source: tdn-rm
title: FOP_0001_GUIA_DE_INSS_DES0NERAÇÃO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221554906
version: 2
---

\_GoBack

**Guia de INSS Desoneração**   
 Foi criado a tela de cadastro '**Parâmetros da Guia de INSS Desoneração'** disponível no menu Relatórios\Guia de INSS que deve ser abastecida antes da geração da guia de INSS para empresas que possuem o percentual redutor para aplicar no campo parte empresa da guia.   
   
   
 Na tela acima devem ser informados os valores da receita bruta com desoneração e receita bruta de demais atividades. O percentual redutor será calculado automaticamente com base nestes valores. O cálculo será realizado conforme abaixo:

 **PercentualRedutor** **= (ReceitaBrutaDemaisAtividades /(** **ReceitaBrutaDemaisAtividades + ReceitaBrutaDesoneracao)) \* 100**

 **OBS**: Caso o valor do campo receita bruta de demais atividades esteja zerado e o campo receita bruta com desoneração for informado, o campo parte Empresa da Guia de INSS será zerado.   
 Uma vez informados os valores acima, o recolhimento da parte empresa será feito da seguinte forma:

1. O recolhimento referente à receita bruta com desoneração deverá ser feito através de relatório DARF com código 2985.
2. O recolhimento referente à receita bruta das demais atividades será feito na própria GPS, utilizando para isto o percentual redutor calculado acima.

   
 Na guia de INSS foi criado o parâmetro **'Utilizar percentual redutor (Lei 12.546/2011)'** para correto cálculo da parte empresa. O parâmetro **'Por filial'** busca os valores do novo cadastro de acordo com a quebra de CNPJ.

   
   
 O parâmetro **'Por Empresa'** busca o valor do novo cadastro de acordo com a seção informada na guia. O percentual definido na Empresa informada será utilizado para as demais Empresas.

 

 O parâmetro **'Aplicar percentual redutor no 13º salário Até'** aplica o percentual redutor até o mês e ano (inclusive) informados na tela. O valor default do campo é 12/2011 quando a lei 12546/2011 entrou em vigor. Com este parâmetro menor ou igual a 11/2015 o campo BASE INSS conterá a base de INSS onde o percentual redutor irá incidir. Foi criado o campo LEI 12.546/2011 (Base INSS 13º sem Redutor) que conterá a base de INSS 13º onde o percentual redutor não irá incidir, conforme abaixo:

   
   
 O campo LEI 12.546/2011 (Base INSS 13º sem Redutor) é calculado conforme número de avos de 13º de direito de cada funcionário que pode ser verificado no log detalhado por funcionário:
