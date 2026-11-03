---
content_hash: 7031cf45457fa6280b82e61ef154bdd4f6c14ad88f152f3c4b33cedd4cbf5d33
fetched_at: '2026-06-29T00:10:06.665129+00:00'
page_id: '452719326'
product: rm
source: tdn-rm
title: Passo a passo para o cálculo da Remuneração Variável utilizando Metas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719326
version: 1
---

**Passo a passo para o cálculo da Remuneração Variável utilizando Metas**

---

**1 - Cadastro das metas do tipo "Valor" (Acompanhamento| Gestão de Metas)**  
Campos importantes para o cálculo da remuneração variável:

* Tipo de valor = Faixa de valores - Valor de referência (% para cumprimento da meta) - Forma de avaliação = somatório dos lançamentos ou último lançamento - Atribuições da meta
* Faixa de valores para avaliar o cumprimento da meta, sendo que uma faixa deve identificar a meta cumprida - Faixa de valores com o fator multiplicador informado  
     
  **2 - Cadastro das metas do tipo "Agrupadora" (Acompanhamento| Gestão de Metas)**  
  Campos importantes para o cálculo da remuneração variável:
* Forma de avaliação = somatório dos lançamentos ou último lançamento - Composição das metas = metas valor criadas anteriormente, cada uma com o seu percentual (peso) de composição - Atribuições da meta  
     
  **3 - Cadastro do Target da meta "Agrupadora" (Acompanhamento| Gestão de Metas| Anexos| Cadastro de Targets)**  
  Campos importantes para o cálculo da remuneração variável:
* Descrição do Target - Bonificação - Funções que aplicam este Target  
     
  **4 - Lançamento de resultado das metas do tipo "Valor" (Acompanhamento| Gestão de Metas - Lançamentos)**  
  Editar cada meta valor criada anteriormente e na aba Lançamentos inserir o resultado da meta informando: Valor, Comentário e Situação do lançamento.  
     
  OBS.: O lançamento da meta pode ser realizado também no Totvs Portal.  
     
  **5 - Cadastro das fórmulas para o cálculo da remuneração variável (Serviços Globais| Administração| Fórmulas - Gestão de Pessoas)**  
  Funções de fórmula:  
     
  CALCULAMETAAGRUPADORA (Meta agrupadora)  
  METAATINGIDA (Meta valor)  
  BUSCARTARGETMEDIAMETA (Meta agrupadora) BUSCARTARGETFINALMETA (Meta agrupadora) BUSCARFATORMULTIPLICADORMETAVALOR (Meta valor) BUSCARFATORMULTIPLICADORMETAAGRUPADORA (Meta agrupadora) SALFUNC BUSCARPROPORCIONALIDADE RESULTADOMETAPERIODO (MetaAgrupadora, Mês, Ano, ConsideraFator)  
     
  **6 - Cadastro do benefício a ser lançado como remuneração variável (Valorização| Benefícios e Remuneração Variável)**  
  Campos importantes para o cálculo da remuneração variável:
* Período de vigência - Marcar o campo "natureza monetária" - Origem do valor = por fórmula, indicando a fórmula criada para cálculo da remuneração variável - Marcar "Gerar ficha financeira", informando o tipo de lançamento (Lançamento do benefício mensal) e evento funcionário/empresa necessários para o pagamento da remuneração variável  
     
  **7 - Vinculação de Benefícios (Valorização| Vinculação de Benefícios)**  
  Vincular o benefício criado às atribuições da meta Agrupadora.  
     
  **8 - Lançamento de Benefícios (Valorização| Lançamento de Benefícios)**  
  Lançar o benefício criado anteriormente para todas as atribuições da meta Agrupadora.  
     
  **9 - Lançamento do Benefício na Folha de Pagamento (Folha de Pagamento| Folha mensal| Lançamentos| Grupo de Eventos)**  
  No grupo de eventos marcar a opção "Lançar eventos da integração com outros aplicativos". Na aba Integração com outros aplicativos marcar "Lançamento do benefício mensal". Clicar em Lançar.  
     
  **10 - Cálculo de Benefícios de Funcionários (Folha de Pagamento| Folha Mensal| Lançamentos| Cálculo de Benefícios de Funcionários)**  
  Selecione o benefício a calcular (benefício criado anteriormente) e clicar em Executar.  
     
  **11 - Conferência do valor do Benefício lançado**  
  No Totvs Folha de Pagamento, acessar Administração de Pessoal| Funcionários| Anexos| Movimento| Envelope de Pagamento.  
  Ou então, acessar Folha mensal| Consulta| Consulta movimento de integração.   
     

  |  |  |
  | --- | --- |
  |  | Informações Complementares |

    


  ---

  O que cada função de fórmula retorna?  
     
  CALCULAMETAAGRUPADORA   
  Encontra as metas filhas (meta valor) da meta agrupadora informada. Para cada meta valor, verifica o resultado, localiza a faixa que o resultado se encontra e seu fator multiplicador. Encontra o target da meta agrupadora que se relacione com a função do funcionário informado. Multiplica o target pela soma dos fatores multiplicadores. Aplica o salário do funcionário pelo valor encontrado.  
     
  METAATINGIDA  
  Busca a forma de avaliação da meta (somatório dos lançamentos ou último lançamento). Verifica se a meta foi atingida ou se está numa faixa de valor que a define como cumprida. Retorna um valor sim/não (true/false).  
     
  BUSCARTARGETMEDIAMETA   
  Identifica as funções desempenhadas pelo funcionário informado no período de vigência da meta. Calcula a média ponderada de targets de acordo com os targets das funções desempenhadas. Retorna a média calculada.  
  BUSCARTARGETFINALMETA  
  Identifica a função do funcionário informado na data final de vigência da meta. Busca o target para a função encontrada.  
     
  BUSCARFATORMULTIPLICADORMETAVALOR   
  Identifica a faixa de valor de atingimento da meta informada. Retorna o fator multiplicador da meta para a faixa.  
  BUSCARFATORMULTIPLICADORMETAAGRUPADORA  
  Identifica dentro de uma meta agrupadora, a meta valor que esteja atribuída ao funcionário informado. Identifica a faixa de valor de atingimento da meta valor. Retorna o fator multiplicador da meta para a faixa.  
  SALFUNC  
  Retorna o valor do salário do funcionário.  
  BUSCARPROPORCIONALIDADE  
  Verifica quantos meses do ano o funcionário trabalhou (mesma regra do 13º). Retorna o resultado de (meses / 12).  
  RESULTADOMETAPERIODO  
  Verifica todos os lançamentos aprovados no período informado (mês, ano). Considera do primeiro dia do mês até o último. Realiza a soma dos lançamentos ou considera o último lançamento, de acordo com a forma de avaliação da meta (somatório dos lançamentos ou último lançamento). O parâmetro "considerafator" indica se vai ser realizado somente a soma dos lançamentos ou a soma dos lançamentos multiplicado pelos fatores.  
     
  **Exemplo prático:**  
     
  **Cadastro das metas do tipo valor**   
  1 - Meta valor 1        2 - Meta valor 2         
  Meta valor 1 – Valor de referência 100% - Forma de avaliação: somatório dos lançamentos – Atribuições: 02.01 e 02.02 Meta valor 2 - Valor de referência 100% - Forma de avaliação: somatório dos lançamentos - Atribuições: 02.01   
  Faixa de valores com fator multiplicador  

  |  |  |
  | --- | --- |
  | <90 | Fator 0,80 |
  | >=90 e <100 | Fator 1 |
  | >=100 | Fator 2 (meta cumprida) |

    
  **Cadastro da meta do tipo agrupadora**  
  3 - Meta agrupadora  
  Forma de avaliação: somatório de lançamentos Atribuições: 02.01, 02.02 Composição de metas  

  |  |  |
  | --- | --- |
  | Meta valor 1 | 50% |
  | Meta valor 2 | 50% |

    
  **Cadastro do Target da meta agrupadora**   

  |  |  |  |
  | --- | --- | --- |
  | Gerente | Bonificação 3 | Funções 00003, 00004, 00005 |
  | Comercial | Bonificação 2 | Funções 00012, 00021 |
  | Demais funções | Bonificação 1 | Função 00013 |

    
  **Lançamento do resultado das metas do tipo valor**  

  |  |  |  |
  | --- | --- | --- |
  | Meta valor 1 | 92% | Fator 1 |
  | Meta valor 2 | 105% | Fator 2 (meta cumprida) |

    
     
  **Cadastro das fórmulas**  

  |  |  |  |  |
  | --- | --- | --- | --- |
  | Fórmulas | Chapa 25914 | Chapa 00077 | Chapa 25090 |
  | CALCULAMETAAGRUPADORA(3) | 1485,00 | 4829,13 | 8000,00 |
  | METAATINGIDA(1) | False | False | False |
  | METAATINGIDA(2) | True | - | - |
  | BUSCARTARGETMEDIAMETA(3) | 2 | 3 | 2 |
  | BUSCARTARGETFINALMETA(3) | 2 | 3 | 2 |
  | BUSCARFATORMULTIPLICADORMETAVALOR(1) | 1 | 1 | 1 |
  | BUSCARFATORMULTIPLICADORMETAVALOR(2) | 2 | - | - |
  | BUSCARFATORMULTIPLICADORMETAAGRUPADORA(3) | 1,5 | 0,5 | 0,5 |
  | SALFUNC | 495,00 | 3219,42 | 8000,00 |
  | BUSCARPROPORCIONALIDADE | 3 | 3 | 3 |
  | RESULTADOMETAPERIODO(3,MESDT(HOJE),ANODT(HOJE),'S') | 292 | 92 | 92 |
  | RESULTADOMETAPERIODO(3,MESDT(HOJE),ANODT(HOJE),'N') | 192 | 92 | 92 |

    
  **Cadastro do benefício**  
  00001 - PLR Fórmula de cálculo: BUSCARTARGETFINALMETA(3)\*(BUSCARFATORMULTIPLICADORMETAAGRUPADORA(3)\*SALFUNC)  
     
  Tipo de lançamento: Lançamento do Benefício Mensal Evento Funcionário: 0001  
     
  **Vinculação de benefícios**  
  Seções 02.01, 02.02  
     
  **Lançamento de benefícios**  
  Lançamento do benefício para os funcionários chapa: 25914, 00077, 25090  
     
  **Cálculo de benefícios de funcionários**  
  Cálculo do benefício 00001 - PLR  
     
  **Valor da PLR para os funcionários**  

  |  |  |
  | --- | --- |
  | Chapa 25914 | R$1.485,00 |
  | Chapa 00077 | R$4.829,13 |
  | Chapa 25090 | R$8.000,00 |
