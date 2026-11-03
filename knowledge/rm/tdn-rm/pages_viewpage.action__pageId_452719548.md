---
content_hash: b5dc22afb9f92fde3b24f78b8b3e61771c9e24cec5a64170c018076ea0deb5cd
fetched_at: '2026-06-29T00:10:08.619746+00:00'
page_id: '452719548'
product: rm
source: tdn-rm
title: Geração Histórico de Provisões (.Net)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719548
version: 4
---

Uma rotina de geração de histórico de provisões acumulada de Férias e 13º Salário dos funcionários servirá para provisionar valores que  o sistema gerará na contabilização da provisão de Férias e 13º Salário, conforme parametrizações.

**Atenção:** O histórico de provisões deverá ser gerado mensalmente.  
É indicado que o sistema esteja parametrizado para a geração obrigatória de Histórico de Provisões, quando a empresa contabiliza ou gera relatórios relativos às provisões. Para verificar a parametrização, deverá acessar os Parâmetros do sistema e em Outros Parâmetros | Parâmetros III, e checar o parâmetro "Provisão Férias /13º obrigatório".  
Quando o parâmetro "Provisão Férias /13º obrigatório" estiver marcado e a provisão ainda não gerada, na liberação de competência será apresentada uma mensagem obrigando o usuário a gerar os históricos antes da liberação da competência.

**Atenção:** O sistema não gera provisão para funcionários admitidos no próximo mês.

**Atenção:** Os valores dos históricos de provisões serão sempre acumulados. Caso o usuário queira gerar as provisões mensais, deverá ser feita através da "Contabilização por Encargos".

**Atenção:** Para gerar o histórico de provisões referente meses anteriores, deverá restaurar backup relativo ao mês e ano desejado, gerar os históricos de provisões, exportar via gerador de relatórios e importar na base atual (competência atual) através do menu Utilitários | Importação de Dados do RM Labore | Pasta Funcionários | Subpasta Históricos.

**Provisão de 13º Salário**  
Selecione esta opção caso deseje gerar o histórico de provisão de 13º Salário e gravar no anexo "Histórico de Provisões existente no cadastro do funcionário.  
 No processo do cálculo da provisão de 13º Salário o sistema irá considerar:  
·   Avos de direito até o último dia da competência atual ou até a data de demissão (incluindo aviso prévio indenizado);  
·   Médias conforme demonstrado no arquivo gerado em "Debug da Média";  
·   Faltas e afastamentos ocorridos no ano atual;  
·   Parâmetros de 13º Salário existentes em Opções | Parâmetros | RM Labore | Pasta Parâm. 13º Salário;  
·   Parâmetros de 13º Salário existentes em Cadastros | Sindicatos | Pasta 13º Salário | Subpasta Parâmetros de Média conforme sindicato do funcionário;  
·   Eventos que incidem salário.

**Provisão de Férias**  
Selecione esta opção caso deseje gerar o histórico de provisão de Férias e gravar na pasta Hist. Provisões existente no cadastro do funcionário.  
No processo do cálculo da provisão de Férias o sistema irá considerar:  
·   Avos de direito até o último dia da competência atual ou até a data de demissão (incluindo aviso prévio indenizado) para férias as férias vencidas e proporcionais e cadastro de férias;  
·   Médias conforme demonstrado no arquivo gerado em "Debug da Média";  
·   Faltas e afastamentos ocorridos no ano atual;  
·   Parâmetros de Férias existentes em Opções | Parâmetros | RM Labore | Pasta Parâm. Férias;  
·   Parâmetros de Férias existentes em Cadastros | Sindicatos | Pasta Férias | Subpasta Média de Férias conforme sindicato do funcionário;  
·   Eventos que incidem salário.

**Atenção:** Se o funcionário for demitido no mês com o tipo de rescisão =1 (iniciativa do empregador por justa causa) será provisionado apenas as férias Vencidas deste funcionário.

**Gerar provisão com valor zero para demitidos no mês**  
Marcando este parâmetro no mês da demissão do funcionário o sistema irá gerar a provisão zerada.

**Provisão abate o valor das férias do mês**  
Com este parâmetro marcado no momento do cálculo da provisão de férias o sistema irá abater o valor das férias gozadas no mês atual.

**Exemplo:** O funcionário possui férias vencidas mais 3/12 avos de férias proporcionais e está em gozo de férias no mês de competência.  
Com o parâmetro marcado o valor integral das férias gozadas no mês será abatido na provisão, ou seja, será calculado apenas 3/12 avos de férias proporcionais.

**Abate o valor da diferença de férias do mês**  
Com este parâmetro marcado no momento do cálculo da provisão de férias o sistema irá abater o valor da diferença  de férias das férias gozadas no mês atual.

**Permite valores negativos**  
Com este parâmetro desmarcado o sistema irá calcular zero para o funcionário que antecipar o gozo das férias, ou seja, tiver avos negativos. Caso contrário será calculado o valor negativo.

**Exemplo:**

O funcionário tem o período aquisitivo em aberto de: 01/2009 a 12/2009 e gozou 20 dias de férias no mês 06/2009.  
Com o parâmetro **desmarcado** o sistema fazer o seguinte cálculo:  
Funcionário: NOME DO FUNCIONÁRIO  
Salário: 440,00   
Período aquisitivo aberto: 01/01/2009 a 31/12/2009  
Gozo de férias: 01/06/2009 a 20/06/2009 => 20  dias = 8 avos  
Avos proporcionais até o mês 06/2009 = 15 dias = 6 avos   
 Desta forma existe um saldo negativo de (-2 avos) a ser provisionado => -5 dias.  
Com o parâmetro **desmarcado** o sistema fazer o seguinte cálculo:  
Total Provisão de Férias   : 0,00 + 0,00 + 0,00 = 0,00  
Com o parâmetro **marcado** o sistema fazer o seguinte cálculo:  
Férias Proporcionais: ((440,00) / 12 \* -2) + 0,00 = -73,33  
Dias de direito  : -5,0 => -2 avos  
Adicional sobre férias : (0,00 + -73,33) \* 0,33 = -24,20  (1/3 férias)  
Total Provisão Férias  : 73,33 + -24,20 = -97,53

**Atenção:** Caso os eventos os eventos de férias e 13º salário possuírem fórmulas, as respectivas provisões considerarão os valores das fórmulas.

**Somente férias antecipadas**

Os parâmetros “Somente férias antecipadas” localizados abaixo dos parâmetros “Permite valores Negativos” e “Permite avos negativos” considerarão somente as férias antecipadas para permitir avos e valores negativos, ou seja, para perda do período aquisitivo integral por faltas a provisão será zerada caso esse parâmetro esteja marcado.

Os parâmetros só devem ficar habilitados se os parâmetros “Permite valores Negativos” e “Permite avos negativos” estiverem marcados.

**Exemplo:**

Funcionário com mais de 32 dias de faltas dentro do período aquisitivo 01/08/2020 a 31/07/2021

Houve o processamento do Acerto de período aquisitivo em novembro/2020, então no cadastro de período aquisitivo será relacionado:

01/08/2021 a 31/07/2022             Aberto

01/08/2020 a 31/07/2021             Fechado (por motivo de Perda por faltas)

Ao executar a geração do histórico de provisões com o **parâmetro desmarcado**:

**NOME                                                                 DT VENC            AVOS    FÉRIAS PROP        MÉDIA FÉRIAS PROP**

FÉRIAS MAIS DE 32 DIAS DE FALTAS                   31/07/2022         -8,00      -2.745,32               -395,67

FÉRIAS ANTECIPADAS                                          31/07/2021         -4,00      -3.132,15               -414,08

Ao executar a geração do histórico de provisões com o **parâmetro marcado**:

**NOME                                                                 DT VENC            AVOS    FÉRIAS PROP        MÉDIA FÉRIAS PROP**

FÉRIAS MAIS DE 32 DIAS DE FALTAS                   31/07/2022         0,00       0,00                        0,00

FÉRIAS ANTECIPADAS                                          31/07/2021        -4,00      -3.132,15                -414,08

**Sobrepõe parâmetro do sindicado (exceto para demitidos ou com férias iniciando no mês)**  
   
Marcando esse parâmetro o sistema ignora o parâmetro "Considera mês das férias p/ cálculo da média" existente no cadastro do sindicato, e passa a considerar o parâmetro "Considera mês atual no cálculo de médias de férias" da tela de provisão. Ele não será considerado para funcionários demitidos ou com férias iniciadas no mês da provisão.  
   
   
**Atenção:**   
Esse parâmetro somente fica visível na geração da provisão de férias.  
   
   
**Considera mês atual no cálculo de médias de férias**  
   
Com esse parâmetro marcado o sistema considera o mês atual para o cálculo das médias. Com esse parâmetro desmarcado os eventos que incidem em média de férias existentes no envelope do mês da provisão, não serão considerados para o cálculo das médias.  
   
   
**Observação:** Para funcionários demitidos ou com férias iniciando no mês da provisão, o sistema continua verificando o parâmetro do sindicato, para que não ocorra divergências com os valores do envelope da rescisão, ou com o recibo de férias. Para funcionários com início de férias no mês anterior e retorno de férias no mês, o sistema irá considerar o parâmetro informado na tela de provisão.
