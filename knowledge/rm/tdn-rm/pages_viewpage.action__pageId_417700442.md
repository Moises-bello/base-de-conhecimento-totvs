---
content_hash: 7f5d2c958498408cedbeaf7710f58729abca62b0ae6eaccea60fd4bb05b8b74e
fetched_at: '2026-06-29T00:09:12.406498+00:00'
page_id: '417700442'
product: rm
source: tdn-rm
title: Taxa Componente Crítico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700442
version: 1
---

**Taxa Componente Crítico**   
O cubo taxa componente crítico faz parte das estatísticas do menu Relatórios. Expressa as taxas das áreas críticas do hospital (CTI Adulto, CTI Neonatal, etc.) em que esta internação pode ser dentro de uma internação hospitalar do paciente ou que o mesmo interna diretamente nestas áreas.   
O resultado deste cubo encontra-se vinculado diretamente ao cadastro de área crítica.   
Dimensões: Unidade Clínica (categoria B), Peso.  
Fatos de análise: Infecções rel. proc. Invasivos, Novos procedimentos, Proc/dia, Permanência Média, Tx. Infec./Procedimento Dia x 1000. Ordenam entre si, para direita ou esquerda.  
Observações  
Unidade Clínica: dimensão referente às unidades de categoria B, classificação das categorias das unidades de área crítica.   
Peso: dimensão que é trazida somente quando é alimentada pelo usuário no cadastro do paciente. Expressa a taxa da unidade clínica CTI Neonatal em que a metodologia publica referencial por faixas de peso (<=1000; <=1500; <=2500 e >2500).  
As taxas que dispõe este cubo estão relacionadas aos procedimentos invasivos usados pelos pacientes que internaram nestas áreas.   
Contagem de procedimento/dia   
Conta-se o procedimento que tenha iniciado depois do início do relatório e os que tenham iniciado antes da data de fim do relatório. Também, contam-se os procedimentos iniciados antes do início do relatório e que ainda estejam em aberto no período do relatório.   
Exemplo  
Considerando-se que o período do relatório seja 01/01/2009 a 31/03/2009, entrarão no relatório:  
- todos os procedimentos que iniciaram antes de 01/01/2009 e não terminaram

* todos os procedimentos que iniciaram antes de 01/01/2009 e terminaram dentro do período
* todos os procedimentos que iniciaram e terminaram entre 01/01/2009 e 31/03/2009
* todos os procedimentos que iniciaram entre 01/01/2009 e 31/03/2009e terminaram  
     
  Observação  
  Serão considerados apenas os dias dentro do período do relatório  
  As infecções relacionadas a procedimento invasivo neste relatório são:  
  ITU (Infecção do Trato Urinário) relacionada a SVD/dia  
  PNEU (Pneumonia) relacionada a VAP/dia  
  CVC (Cateter Venoso Central) relacionada a CVC/dia  
  Caso associem outros sítios de infecção a estes procedimentos invasivos esses não serão apresentados neste relatório.  
     
  Atenção  
  O relatório em cubo difere do relatório em Excel. As informações não constam num conjunto de um mesmo relatório, estão divididas entre os relatórios estatísticos Taxa Global e Taxa de Componente Crítico.  
  Taxa Global por unidade clínica você obterá informações da área crítica nas unidades clinicas em que a taxa geral esta classificada como categoria B. Você obterá as informações: total de infecções, total de pacientes infectados, total de admissões, total de paciente/dia, taxa global de infecções, taxa de infecção por paciente/dia x 1000.   
  Taxa de Componente Crítico você obterá as informações: total de infecções por procedimentos, novos procedimentos, procedimentos/dia, permanência média por procedimento, taxa de infecção por procedimento.
