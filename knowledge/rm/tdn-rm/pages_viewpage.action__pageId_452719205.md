---
content_hash: b300c5f958dea39925652e5b0c3738eda631a5693407a95ebd2badf4b5fd453c
fetched_at: '2026-06-29T00:10:04.154903+00:00'
page_id: '452719205'
product: rm
source: tdn-rm
title: GPS - Desoneração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719205
version: 6
---

falseATENÇÃO!

A partir da versão 12.1.2406, esse processo foi descontinuado. A GPS foi substituída pela DCTFWeb.

* Para a geração do lançamento financeiro da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=727915586)
* Para conferência dos valores da DCTFWeb, consulte a documentação: [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=717708785)

**Desoneração**  
   
O governo está eliminando a atual contribuição previdenciária sobre a folha e adotando uma nova contribuição previdenciária sobre a receita bruta das empresas (descontando as receitas de exportação), em consonância com o disposto nas diretrizes da Constituição Federal.   
   
A substituição da base folha pela base faturamento se aplica apenas à contribuição patronal paga pelas empresas, equivalente a 20% de suas folhas salariais.   
   
Todas as demais contribuições incidentes sobre a folha de pagamento permanecerão inalteradas, inclusive o FGTS e a contribuição dos próprios empregados para o Regime Geral da Previdência Social.  
Ou seja, se a empresa for abrangida pela mudança, ela continuará recolhendo a contribuição dos seus empregados e as outras contribuições sociais incidentes sobre a folha de pagamento (como seguro de acidente de trabalho, salário-educação, FGTS e sistema S).  
   
O governo decidiu adotar duas alíquotas diferentes:   
·          1% para as empresas que produzem determinados produtos industriais (identificados pelo código da Tabela de Incidência do Imposto sobre Produtos Industrializados – TIPI); e  
   
·          2,0% para as empresas do setor de serviços, como aquelas do ramo hoteleiro, de call center e design houses, e que prestam os serviços de tecnologia de informação e tecnologia de informação e comunicação.  
   
Uma empresa tem 70% de sua receita derivada de produtos enquadrados na Medida Provisória e 30% de fora, então ela deve recolher a alíquota de 1% sobre 70% de sua receita e aplicar a alíquota previdenciária normal, de 20%, sobre 30% de sua folha salarial.   
   
**Exemplo:**  
Receita da empresa: R$10.000,00  
Folha de salários de R$2.000,00.   
Atualmente, essa empresa recolhe 20% de R$2.000,00, pagando R$400,00 de contribuição previdenciária.   
Pela nova sistemática, a empresa paga R$190,00, sendo:  
(10.000,00 \* 70%) \* 1% = 70,00 (Valor calculado em DARF)  
(2.000,00 \* 30%) \* 20% = 120,00 (Valor calculado pela guia de INSS)  
   
   
   
**O que muda no recolhimento da nova contribuição?**  
A contribuição previdenciária das empresas sobre a folha é recolhida, em geral, via Guia da Previdência Social (GPS), juntamente com a contribuição do empregado, no código 2100.   
A contribuição sobre a receita bruta das empresas, que agora está sendo estendida para outros setores, é recolhida por meio de Documento de Arrecadação de Receitas Federais (DARF), com os seguintes códigos\*:  
I – 2985: Contribuição Previdenciária Sobre Receita Bruta – Empresas Prestadoras de Serviços de Tecnologia da Informação (TI) e Tecnologia da Informação e Comunicação (TIC);  
   
II – 2991: Contribuição Previdenciária Sobre Receita Bruta – Demais.

* Fonte: Ato Declaratório Executivo da Receita Federal do Brasil nº 86, de 1º de dezembro de 2011.  
     
  **Legislação**  
  • Constituição Federal – Art. 195, §§ 12 e 13  
  • Lei nº 8.212, de 24 de julho de 1991 – Art. 22, inciso I e III  
  • Lei nº 12.546, de 14 de dezembro de 201  
     
  [{+}](http://www.fazenda.gov.br/portugues/documentos/2012/cartilhadesoneracao.pdf)<http://www.fazenda.gov.br/portugues/documentos/2012/cartilhadesoneracao.pdf+>  
    
  **Trazendo esta alteração para o RM Labore.**  
  Em **Encargos | Guia de INSS | Parâmetros da Guia de INSS Desoneração**  
  Preencher as informações necessárias para cada seção centralizadora, antes do cálculo da guia de INSS (GPS).  
  Ao preencher o campo 'Receita Bruta com Desoneração' e 'Receita Bruta Demais Atividade', é calculado automaticamente o campo 'Percentual Redutor'.  
  O 'Percentual Redutor' é calculado da seguinte maneira:  
  (Receita Bruta Demais Atividade / (Receita Bruta Demais Atividade + Receita Bruta com Desoneração)) \* 100.  
     
  **Exemplo:**  
  Receita Bruta total da empresa: R$10.000,00  
  Campo Receita Bruta com Desoneração: R$7.000,00  
  Campo Receita Bruta Demais Atividade: R$3.000,00  
  Percentual Redutor: (3.000,00 / (3.000,00 + 7.000,00)) \* 100 = 30%  
     
  **Observação I:**  
  Quando o campo 'Receita Bruta Demais Atividade' está zerado e o campo 'Receita Bruta com Desoneração' tem valor, no cálculo da guia de INSS o campo 'Empresa' fica zerado. Isso porque entende-se que toda a receita da empresa é com desoneração.  
     
  **Observação II:**  
  Quando o campo 'Receita Bruta com Desoneração' é superior a 95% da Receita Total, o recolhimento do INSS sobre a folha parte empresa é totalmente desonerado.  
  Quando o campo 'Receita Bruta Demais Atividades' é superior a 95% da Receita Total, o recolhimento do INSS sobre a folha parte empresa não é desonerado, ou seja, é integral.  
  Conforme Parecer Normativo nº 3, de 21 de novembro de 2012, Lei nº 12.546, de 2011.  
  [{+}](http://www.receita.fazenda.gov.br/Legislacao/PareceresNormativos/2012/parecer032012.htm)<http://www.receita.fazenda.gov.br/Legislacao/PareceresNormativos/2012/parecer032012.htm+>  
     
  **Atenção:**  
  Para o exemplo acima, o recolhimento referente à 'Receita Bruta com Desoneração' deve ser através do relatório DARF com código 2985.  
  E o recolhimento referente à 'Receita Bruta Demais Atividade' é realizado através da guia de INSS (GPS) utilizando o percentual redutor calculado.  
     
     
  Em **Encargos | Guia de INSS | Guia de INSS**  
  Para que seja considerada a desoneração, o parâmetro 'Utilizar percentual redutor (Lei 12.546/2011)', deve está marcado.  
     
  Quando selecionado o parâmetro 'Por Filial', são utilizados os valores informados em Encargos | Guia de INSS | Parâmetros da Guia de INSS Desoneração de acordo com a quebra de CNPJ (filial).  
  Quando selecionado o parâmetro 'Por Empresa' são utilizados os valores informados em Encargos | Guia de INSS | Parâmetros da Guia de INSS Desoneração na filial informada. Sendo que o percentual definido nesta filial é utilizado para as demais.  
     
  **Atenção:**  
  Quando definir uma filial para utilizar o percentual redutor, mesmo que esta filial não seja selecionada no cálculo da guia de INSS, são considerados os valores desta filial para o cálculo das demais.  
     
  **Exemplo:**  
  Receita Bruta total da empresa: R$10.000,00  
  Receita Bruta com Desoneração: R$7.000,00  
  Receita Bruta Demais Atividade: R$3.000,00  
  Percentual Redutor: (3.000,00 / (3.000,00 + 7.000,00)) \* 100 = 30%  
  Funcionário com remuneração de R$2.000,00  
     
  Na geração da guia de INSS o cálculo do campo 'Empresa' é: (2.000,00 \* 20%(empresa)) \* 30%(redutor) = R$120,00  
  Na geração da DARF o cálculo é: 7.000,00 \* 1% = R$70,00.  
  Total recolhimento: R$190,00

  **Atenção:**  
   A geração da DARF não é realizada no TOTVS Folha de pagamento.  
   

  |  |  |
  | --- | --- |
  |  | Informações Complementares |

  ---

  Guia de INSS
