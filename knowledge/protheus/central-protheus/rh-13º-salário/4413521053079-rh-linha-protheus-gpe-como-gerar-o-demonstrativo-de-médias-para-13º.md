---
article_id: 4413521053079
category: RH - 13º salário
content_hash: 23ec06be0a3fdc18c6ef498af07812b9a68dbc1118b09ae3a9ba1e467c7427a4
fetched_at: '2026-06-28T22:44:00.647780+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para 13º
type: support-article
updated_at: '2025-08-11T19:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413521053079-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-m%C3%A9dias-para-13%C2%BA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18958568213143) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como gerar o **demonstrativo de médias** para conferencia dos valores de médias de 13º?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O demonstrativo de médias pode ser gerado diretamente no cálculo **(DEM\_MED)** ou na rotina de Demonstrativo de Médias **(GPER080)**Indicamos gerar o relatório diretamente no cálculo, pois as parametrizações serão geradas automaticamente e estarão condizentes com o cálculo**,** sem risco de informar algum parâmetro errado. 

**-Demonstrativo de Médias (DEM\_MED)**Acesse: Atualizações > Lançamentos > Por funcionário (GPEA580)   
Selecione o funcionário e clique em Visualizar![](https://centraldeatendimento.totvs.com/hc/article_attachments/18958606829207)

Altere o roteiro de FOL para o roteiro **131** ou **132** dependendo de qual tenha calculado  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18958606839831)

Clique em **Outras Ações > Médias  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18958606842903)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18958568240663)**

**-Demonstrativo de médias via rotina (GPER080)**Acesse: Relatórios > Lançamentos > Demonstrativo de Médias   
Clique em parâmetros para preencher o grupo de perguntas.  
  
**Data Base:** Informe a Data Base que será utilizada como Período para impressão.  
**Filial De/Até:** Informe ou Selecione o Código da Filial Inicial/final para Filtrar os dados do Relatório.  
**Centro de Custo De/Até:** Informe ou Selecione o Código do Centro de Custo Inicial/Final para Filtrar os dados do Relatório.  
**Matricula De/Até:** Informe ou Selecione o Código de Matrícula Inicial/Final para Filtrar os dados do Relatório.  
**Nome De/Até:** Informe o Nome do Funcionário Inicial/Final para Filtrar os dados do Relatório.  
**Médias De:** Informe sobre qual Rotina deseja imprimir o Relatório de Médias.  
**Situações a Imp:** Informe ou Selecione as Situações para Filtrar os Funcionários que serão impressos no Relatório.  
**Categorias a Imp:** Informe ou Selecione as Categorias para Filtrar os Funcionários que serão impressos no Relatório.  
**Considera Mês Atual:** Informe se considera para Média o Mês Atual, o Acumulado ou não considera o Mês Atual, somente o Acumulado.  
**Imprime "Média Pgto":** Informe se deseja imprimir a linha "Medias de Pagamento".

**Exemplo:**![Demontrativo_de_medias_decimo_terceiro.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413534804503)

**Observações:**

O relatório GPER080 apresenta a remuneração mensal do funcionário em um único campo, sem detalhar os adicionais. Já o relatório DEM\_MED exibe o detalhamento de cada valor que compõe a remuneração do funcionário.

A principal diferença entre os relatórios é que o GPER080 valida as verbas da remuneração do funcionário na Folha de Pagamento, enquanto o DEM\_MED (emitido neste caso pelo cálculo do 13º salário) valida as verbas referentes ao roteiro 131 e/ou 132.

Dessa forma, caso existam verbas que integrem o salário do funcionário na Folha, mas que não estejam incluídas no cálculo do 13º, essas verbas aparecerão apenas no GPER080 e não no DEM\_MED — e o contrário também é válido.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Médias no cálculo do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016223611-RH-Linha-Protheus-GPE-M%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Sistema não calcula verbas de médias no 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016249711-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-verbas-de-m%C3%A9dias-no-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Relatório de Memória de Cálculo no 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058080854-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Mem%C3%B3ria-de-C%C3%A1lculo-no-13%C2%BA)  
[RH - Linha Protheus - GPE - Médias de 13º Salário não consideram adicionais para compor o salário incorporado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019896372-RH-Linha-Protheus-GPE-M%C3%A9dias-de-13%C2%BA-Sal%C3%A1rio-n%C3%A3o-consideram-adicionais-para-compor-o-sal%C3%A1rio-incorporado)
