---
content_hash: 176883645981835e5d320a2b311074986be31a6ef511ef0732d144e2437ee6aa
fetched_at: '2026-06-29T00:10:07.007432+00:00'
page_id: '452719357'
product: rm
source: tdn-rm
title: Férias Coletivas / Globais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719357
version: 2
---

Através deste processo é efetuado o cadastramento das Férias Coletivas ou Férias Globais, sendo que:  
    
 Globais  
 É o cadastramento do mesmo período de gozo para um grupo de funcionários, seguindo as regras da CLT para Férias Normais.  
    
 Coletivas  
 É o cadastramento do mesmo período de gozo para um grupo de funcionários, seguindo as regras da CLT para Férias Coletivas, e verificando os parâmetros do Labore para atender a Convenção Coletiva da empresa.  
    
 É necessário que antes da execução deste processo, sejam verificados os parâmetros de férias nos Sindicatos e nos parâmetros do Labore.  
    
 Com o parâmetro 'Férias Coletivas' desmarcado é considerado Férias Normais.  
    
 Somente é possível cadastrar férias para funcionário com Situação igual 'A-Ativo'.  
    
 Quando nos parâmetros de férias do Sindicato o parâmetro 'Permite antecipação de dias de férias do próximo período aquisitivo' estiver marcado são antecipados dias de férias do próximo período aquisitivo caso o funcionário não tenha saldo suficiente para total de dias de férias.  
 Veja mais detalhes no help do Sindicato.  
    
 Quando o funcionário tem menos de 1 ano de casa e a parametrização do sindicato permitir o pagamento da licença remunerada, é verificada a necessidade do cálculo dos campos 'Lic. Rem. Mês' e 'Lic. Próx. Mês' no cadastro de férias.  
    
 **Exemplo:**  
 Funcionário admitido: 01/05/2013  
 Período aquisitivo: 01/05/2013 a 30/04/2014  
 Dias de direito de Férias: 22,5 dias  
 Competência: 02/2014  
 Período de férias coletivas: 01/02/2014 a 03/03/2014 = 30 dias de férias  
 Serão lançados:  
 Dias de Férias = 22,5  
 Lic. Rem. Mês = 5,5  
 Lic. Próx. Mês = 2  
    
    
 Considerações quando no cadastro do Sindicato, o parâmetro 'Ignora feriados na contagem das férias' está marcado  
    
 É verificado no calendário da seção do funcionário os feriados que tem o parâmetro 'Ignorar o dia na contagem das férias' marcado, para desconsiderar este feriado na contagem dos dias de férias.  
    
 Ao preencher os campos 'Data Inicial' e 'Data Final' é verificado quantos dias têm entre as datas informadas e subtraído o total de dias de feriados para calcular o campo 'Dias de Férias' de cada funcionário.   
    
 **Exemplo:**   
 No calendário da seção 01.01 a data 07/09/2012 esta com o parâmetro marcado.  
 No processo de cadastramento de férias foram preenchidos os seguintes campos:  
 Data Inicial       = 01/09/2012  
 Data Final         = 30/09/2012  
 Após a execução do processo, para os funcionários que estão na seção 01.01, serão considerados 29 dias de férias, e para os funcionários das demais seções serão considerados 30 dias de férias.  
    
 **Atenção:**  
 Sendo assim sempre que o campo 'Data Final' é preenchido, o campo 'Dias de Férias' fica em branco.  
    
    
 Ao preencher os campos 'Data Inicial' e 'Dias de Férias', o campo 'Data Final' é calculado de tal forma que o número de dias de férias ignorando os dias de feriados (conforme calendário da seção do funcionário) seja igual à quantidade de 'Dias de Férias' informado.  
    
 **Exemplo:**   
 No calendário da seção 01.01 a data 07/09/2009 esta com o parâmetro marcado.  
 No processo de cadastramento de férias foram preenchidos os seguintes campos:  
 Data Inicial       = 01/09/2012  
 Dias de Férias   = 30  
 Após a execução do processo, para os funcionários que estão na seção 01.01, a Data Final é preenchida com 01/10/2012, e para os funcionários das demais seções a Data Final é preenchida com 30/09/2012.  
    
 **Atenção:**  
 Sendo assim sempre que o campo 'Dias de Férias' é preenchido, o campo 'Data Final' fica em branco.  
    
 **Observação:**  
 Os dias de feriados a desconsiderar serão somados nos códigos de cálculos: 1-Horas Normais ou 2-Dias Trabalhados.  
 Veja mais detalhes sobre feriados nas férias em Feriados nas Férias   
    
 Pagar Abono  
 Ao marcar este parâmetro é acrescentado o abono pecuniário no cadastro de férias do funcionário, sendo que o cálculo dos dias de abono é a metade do número dias de férias.  
 Lembrando que, são verificados os parâmetros do sindicato.  
    
 **Atenção:**  
 Somente é habilitado quando os dias de férias é menor ou igual a 20 dias.  
    
    
 1ª Parc. 13º Salário  
 Com este parâmetro marcado, na execução do processo, o parâmetro 'Pagar 1ª Parcela 13º' é marcado para os funcionários executados.  
    
 **Atenção:**  
 Mesmo quando o funcionário já recebeu a 1ª Parcela no ano corrente ao gozo das férias, o parâmetro é marcado.  
    
    
 Verifica faltas funcionário >1 ano  
 Quando o parâmetro está marcado e o funcionário possui faltas, é verificado o parâmetro sindical 'Ignora faltas em férias' para considerar ou não as faltas. Caso contrário, as faltas não serão consideradas.  
    
 **Exemplo:**  
 O funcionário tem 30 dias de direito de férias, porém teve 10 dias de faltas neste período aquisitivo e no sindicato esta parametrizado para considerar as faltas.  
    
 Ao cadastrar as ferias com o parâmetro marcado serão lançados 24 dias de férias. Caso contrário, as faltas serão ignoradas e serão lançados 30 dias de férias.  
    
 **Observação I:**  
 O objetivo deste parâmetro nas Férias Coletivas é para atender aos clientes que consideram as faltas no gozo das férias normais e não consideram as faltas no gozo das férias coletivas.  
    
 **Observação II:**  
 O objetivo deste parâmetro nas Férias Globais, é devida a impossibilidade de interromper o processo para alertar o usuário que o funcionário tem menos dias de direito de férias do que o cadastrado devido às faltas, como ocorre atualmente no cadastro individual de férias.  
    
    
 Férias Coletivas  
 Para empregados contratados há menos de 12 meses gozarão, na oportunidade, férias proporcionais, iniciando-se novo período aquisitivo a partir do primeiro dia de gozo.   
 Se, eventualmente, as Férias Coletivas / Globais forem superiores ao direito do empregado, a empresa deve lhe pagar os dias excedentes, a título de licença remunerada, evitando-se, assim, o prejuízo salarial. Serão verificados os parâmetros de férias coletivas do Sindicato e no Parametrizador.  
    
 **Exemplo I:**  
 Empregado admitido em 07/08/2012. Férias Coletivas de 20 dias a partir de 05/02/2013:   
 Teremos 06 meses (que correspondem há 15 dias) de direito de férias na seguinte proporção:  
 15 dias de férias proporcionais  
 05 dias de licença remunerada  
    
 Onde o período aquisitivo do funcionário fica da seguinte forma:   
 Período Aquisitivo:         07/08/2012 a 06/08/2013  
 Período de Gozo:           05/02/2013 a 24/02/2013   
 Após a finalização das férias, o mesmo terá o fim do período aquisitivo alterado para 04/02/2013 e é criado o novo período aquisitivo com o período de 05/02/2013 a 04/02/2014.  
 Lembrando que, isso conforme parametrização do Sindicato e no Parametrizador.  
    
 **Atenção:**  
 É imprescindível o cadastramento do 'Evento para Pagamento de Licença Remunerada' e do ' Motivo de Afastamento por Licença Remunerada' existente em Configurações | Parametrizador | Férias | Férias Coletivas, para que o processo de lançamento das férias fique correto.  
    
 Limita os dias de direito  
 Caso o total de dias de direito do funcionário seja inferior ao total de dias de férias a lançar, será considerado o total dias de direito que o funcionário possui ao cadastrar as férias.  
    
 **Exemplo I:**  
 Dias de férias a lançar: 30;  
 Dias de direito do funcionário: 10;  
 Número de dias do período de gozo do funcionário será de 10 dias.   
    
 Substituir Férias   
 Serão substituídas as férias cujo período de gozo cadastrado contemple o período informado na tela no campo 'Período considerado para substituir as férias'.  
    
 **Atenção I:**

* Serão consideradas apenas as férias 'M-Marcadas' e não calculadas.
* Esse parâmetro, será utilizado no Evento de Exclusão (S-3000) do eSocial.

**Atenção II:**  
 Serão consideradas também as férias que tem somente abono cadastrado e a data de pagamento contemple o período informado na tela no campo 'Período considerado para substituir as férias'.  
    
 **Exemplo:**  
 Ao processar as férias informando o período de gozo de 01/04/2014 a 20/04/2014 e no parâmetro 'Período considerado para substituir as férias' informando de 01/03/2014 a 30/04/2014, todas as férias ou apenas abono cadastrados e não calculadas neste período serão substituídas.  
    
    
    
 Gerar Log Consolidado  
    
 Marcando este parâmetro, será gerado um log mais detalhado no processo de Férias Coletiva Globais em um arquivo txt onde constará:

1. Motivo pelo qual não foi possível marcar férias a um funcionário.
2. A quantidade de dias foi concedido para cada funcionário e o motivo para isso conforme parâmetro Limita dias de Direito estiver marcado.
3. Os dias que o funcionário pode ter de férias e a quantidade que foi paga em licença remunerada.
4. Totalizadores por seção e de todo o processo.

Caso não seja definido um caminho para salvar o arquivo, será salvo no caminho parametrizado no Parametrizador/Folha Normal/Geral/Diretório Utilizado para Processos que geram arquivos em .net (Jobserver).  
 Se não for definido caminho em nenhum dos campos citados acima, será gerado na pasta RM.Net.  
    
    
 Local de Chamada

Processo Férias | Férias Coletivas / Globais  
    
 **Importante:** Informações das Férias para o eSocial
