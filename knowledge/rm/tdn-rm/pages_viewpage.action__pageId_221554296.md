---
content_hash: ad817c519101c98e4248d4238c71311424031f319c3d7693ee4a8adc14256a37
fetched_at: '2026-06-29T00:06:20.358970+00:00'
page_id: '221554296'
product: rm
source: tdn-rm
title: Guia de INSS Desoneração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221554296
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Versões:** | RMLabore.exe: 11.82.41(5); 12.1.7(1); 12.1.8(1) |
| **Ocorrência:** | Geração da Guia de INSS Folha Normal e 13º Salário com desoneração |
| **Ambiente:** | Guia de INSS |
| **Observações:** | O parâmetro "Aplicar Percentual Redutor no 13º Salário Até:" só estará disponível na Guia de INSS em Delphi, para ter acesso a versão em Delphi instale o executável do RM Labore nas versões mencionadas acima. |
| **Passo a passo:** | **Guia de INSS Desoneração**    Foi criado a tela de cadastro '**Parâmetros da Guia de INSS Desoneração'** disponível no menu Relatórios\Guia de INSS que deve ser abastecida antes da geração da guia de INSS para empresas que possuem o percentual redutor para aplicar no campo parte empresa da guia.        Na tela acima devem ser informados os valores da receita bruta com desoneração e receita bruta de demais atividades. O percentual redutor será calculado automaticamente com base nestes valores. O cálculo será realizado conforme abaixo:    **PercentualRedutor  = (ReceitaBrutaDemaisAtividades /( ReceitaBrutaDemaisAtividades + ReceitaBrutaDesoneracao)) \* 100**    **OBS**: Caso o valor do camporeceita bruta de demais atividades esteja zerado e o campo receita bruta com desoneração for informado, o campo parte Empresa da Guia de INSS será zerado.    Uma vez informados os valores acima, o recolhimento da parte empresa será feito da seguinte forma:  a)      O recolhimento referente à receita bruta com desoneração deverá ser feito através de relatório DARF com código 2985.  b)      O recolhimento referente à receita bruta das demais atividades será feito na própria GPS, utilizando para isto o percentual redutor calculado acima.          Na guia de INSS foi criado o parâmetro **‘Utilizar percentual redutor (Lei 12.546/2011)’** para correto cálculo da parte empresa. O parâmetro **‘Por filial’** busca os valores do novo cadastro de acordo com a quebra de CNPJ.         O parâmetro **‘Por Empresa’** busca o valor do novo cadastro de acordo com a seção informada na guia. O percentual definido na Empresa informada será utilizado para as demais Empresas.      O parâmetro **‘Aplicar percentual redutor no 13º salário Até’** aplica o percentual redutor até o mês e ano (inclusive) informados na tela. O valor default do campo é 12/2011 quando a lei 12546/2011 entrou em vigor. Com este parâmetro menor ou igual a 11/2015 o campo BASE INSS conterá a base de INSS onde o percentual redutor irá incidir. Foi criado o campo LEI 12.546/2011 (Base INSS 13º sem Redutor) que conterá a base de INSS 13º onde o percentual redutor não irá incidir, conforme abaixo:        O campo LEI 12.546/2011 (Base INSS 13º sem Redutor) é calculado conforme número de avos de 13º de direito de cada funcionário que pode ser verificado no log detalhado por funcionário: |

divs
