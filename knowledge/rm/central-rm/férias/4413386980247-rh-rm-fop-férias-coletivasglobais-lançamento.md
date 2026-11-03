---
article_id: 4413386980247
category: Férias
content_hash: cfd0763a8b3785087cf1312530d1103920ef5e2a8aea47f6cbfb8ab731366581
fetched_at: '2026-06-28T22:46:56.353728+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias Coletivas/Globais: Lançamento'
type: support-article
updated_at: '2024-09-16T19:37:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413386980247-RH-RM-FOP-F%C3%A9rias-Coletivas-Globais-Lan%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:08:19 min****Dúvida**Como lançar férias coletivas/globais marcadas para os funcionários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Através deste processo é efetuado o cadastramento das Férias Coletivas ou Férias Globais, sendo que:

* **Globais:** É o cadastramento do mesmo período de gozo para um grupo de funcionários, seguindo as regras da CLT para Férias Normais.
* **Coletivas:** É o cadastramento do mesmo período de gozo para um grupo de funcionários, seguindo as regras da CLT para Férias Coletivas, e verificando os parâmetros do Labore para atender a Convenção Coletiva da empresa.

Para realizar o lançamento de Férias coletivas/Globais marcadas, siga os passos:  
  
1**.** Acesse: **Férias | Coletivas Globais.**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8906689626007/mceclip0.png)  
  
2. Preencha a data do período que as férias foram marcadas. O sistema irá lançar as férias para todos os funcionários que estão com férias marcadas dentro do período informado.  
  
3**.** O campo **Seleção de funcionários** permite criar filtros para determinados funcionários, caso queira especificar os funcionários que terão suas férias lançadas.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8906691441559/mceclip1.png)  
  
Segue funcionalidade dos parâmetros das Férias Coletivas/ Globais:  
  
**--> 1ª Parc. 13º Salário:**Com este parâmetro marcado, na execução do processo, o parâmetro **Pagar 1ª Parcela 13º** é marcado para os funcionários executados. Mesmo quando o funcionário já recebeu a 1ª Parcela no ano corrente ao gozo das férias, o parâmetro é marcado.  
  
**--> Verifica faltas funcionário >1 ano:**Quando o parâmetro está marcado e o funcionário possui faltas, é verificado o parâmetro sindical **Ignora faltas em férias** para considerar ou não as faltas. Caso contrário, as faltas não serão consideradas.  
  
**Exemplo:**  
O funcionário tem 30 dias de direito de férias, porém teve 10 dias de faltas neste período aquisitivo e no sindicato esta parametrizado para considerar as faltas.  
  
Ao cadastrar as férias com o parâmetro marcado serão lançados 24 dias de férias. Caso contrário, as faltas serão ignoradas e serão lançados 30 dias de férias.  
   
**Importante**  
O objetivo deste parâmetro nas Férias Coletivas é para atender aos clientes que consideram as faltas no gozo das férias normais e não consideram as faltas no gozo das férias coletivas.  
  
O objetivo deste parâmetro nas Férias Globais, é devida a impossibilidade de interromper o processo para alertar o usuário que o funcionário tem menos dias de direito de férias do que o cadastrado devido às faltas, como ocorre atualmente no cadastro individual de férias.  
  
**--> Férias Coletivas:**Para empregados contratados há menos de 12 meses gozarão, na oportunidade, férias proporcionais, iniciando-se novo período aquisitivo a partir do primeiro dia de gozo.  
Se, eventualmente, as Férias Coletivas / Globais forem superiores ao direito do empregado, a empresa deve lhe pagar os dias excedentes, a título de licença remunerada, evitando-se, assim, o prejuízo salarial. Serão verificados os parâmetros de férias coletivas do Sindicato e no Parametrizador.  
  
**Exemplo:**  
Empregado admitido em 07/08/2012. Férias Coletivas de 20 dias a partir de 05/02/2013:  
Teremos 06 meses (que correspondem há 15 dias) de direito de férias na seguinte proporção:  
15 dias de férias proporcionais  
05 dias de licença remunerada  
  
Onde o período aquisitivo do funcionário fica da seguinte forma:  
Período Aquisitivo:         07/08/2012 a 06/08/2013  
Período de Gozo:           05/02/2013 a 24/02/2013  
  
Após a finalização das férias, o mesmo terá o fim do período aquisitivo alterado para 04/02/2013 e é criado o novo período aquisitivo com o período de 05/02/2013 a 04/02/2014. Lembrando que, isso conforme parametrização do Sindicato e no Parametrizador.  
  
**Importante**É imprescindível o cadastramento do **Evento para Pagamento de Licença Remunerada** e do **Motivo de Afastamento por Licença Remunerada** existente em **Configurações | Parametrizador | Férias | Férias** Coletivas, para que o processo de lançamento das férias fique correto.  
   
**--> Limita os dias de direito:**Caso o total de dias de direito do funcionário seja inferior ao total de dias de férias a lançar, será considerado o total dias de direito que o funcionário possui ao cadastrar as férias.   
  
**Exemplo:**  
Dias de férias a lançar: 30;  
Dias de direito do funcionário: 10;  
Número de dias do período de gozo do funcionário será de 10 dias.  
   
**--> Substituir Férias:**Serão substituídas as férias cujo período de gozo cadastrado contemple o período informado na tela no campo **Período considerado para substituir as férias**.  
  
**Importante**Serão consideradas apenas as férias M-Marcadas e não calculadas;  
  
Esse parâmetro, será utilizado no [Evento de Exclusão- S-3000](https://tdn.totvs.com/pages/viewpage.action?pageId=452718305) do eSocial;  
  
Serão consideradas também as férias que tem somente abono cadastrado e a data de pagamento contemple o período informado na tela no campo **Período considerado para substituir as férias**.  
  
**Exemplo:**  
Ao processar as férias informando o período de gozo de 01/04/2014 a 20/04/2014 e no parâmetro **Período considerado para substituir as férias** informando de 01/03/2014 a 30/04/2014, todas as férias ou apenas abono cadastrados e não calculadas neste período serão substituídas.  
  
**--> Gerar Log Consolidado:**Marcando este parâmetro, será gerado um log mais detalhado no processo de Férias Coletiva Globais em um arquivo txt onde constará:

1. Motivo pelo qual não foi possível marcar férias a um funcionário.
2. A quantidade de dias foi concedido para cada funcionário e o motivo para isso conforme parâmetro Limita dias de Direito estiver marcado.
3. Os dias que o funcionário pode ter de férias e a quantidade que foi paga em licença remunerada.
4. Totalizadores por seção e de todo o processo.

Caso não seja definido um caminho para salvar o arquivo, será salvo no caminho parametrizado no **Parametrizador/Folha Normal/Geral/Diretório.** Utilizado para Processos que geram arquivos em .net - Jobserver. Se não for definido caminho em nenhum dos campos citados acima, será gerado na pasta RM.Net.  
  
**Importante**  
É necessário que antes da execução deste processo, sejam verificados os parâmetros de férias nos Sindicatos e nos parâmetros do Labore.  
  
**Saiba Mais**[Férias Coletivas / Globais](https://tdn.totvs.com/pages/releaseview.action?pageId=452719357)
