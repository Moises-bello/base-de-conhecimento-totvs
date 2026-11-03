---
article_id: 360045162434
category: Banco de Horas
content_hash: 83f7d20ad69b9eedf81e7f155e5d450255889fe4afbc97bc9ba1368dfc022528
fetched_at: '2026-06-28T22:46:27.763574+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Compensação e lançamento do banco de horas considerando limite
  de dias
type: support-article
updated_at: '2025-12-22T21:33:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045162434-RH-RM-PTO-Compensa%C3%A7%C3%A3o-e-lan%C3%A7amento-do-banco-de-horas-considerando-limite-de-dias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981607529367) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**Como efetuar a compensação e lançamento considerando o limite de dias?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**

A parametrização do limite de compensação do banco de horas permite que você defina quantos dias são permitidos para a compensação. Esse limite pode ser configurado nos **parâmetros iniciais** e no **parametrizador do sindicato**. Essa configuração determina as datas em que a compensação do banco de horas será calculada.

1. Nos **parâmetros Iniciais**: Acesse no módulo de Automação de Ponto o menu **Configurações | Parametrizador**. Ao abrir o assistente, clique em avançar e selecione o processo **Iniciais** e avance, novamente.   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21258847892119)
2. Avance até a etapa **Compensação,** e no campo "**Limite de dias para compensação**" informe a quantidade desejada:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21258847900695)  
   Vamos supor que o limite para compensação de horas seja de 30 dias. Durante o processo de compensação e/ou lançamento do banco de horas, será verificado o último dia do período ativo e somado o número de dias informado no parâmetro para atras.
3. No **parametrizador do Sindicato**: Acesse no módulo de **Automação de Ponto** o menu **Configurações | Parametrizador**. Ao abrir o assistente, clique em avançar e selecione o processo **Sindicato**. Em seguida, edite o sindicato desejado:  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21251785303063)![](https://centraldeatendimento.totvs.com/hc/article_attachments/21251764489239)
4. Ao abrir o assistente avance até a etapa "**Limite de dias de compensação**", e informe a **data de início** da utilização/compensação do banco de horas e a **quantidade** do **limite de dias compensação.** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21251785326231)  
     
   No exemplo abaixo, considerei que começou a usar o banco de horas em 22/03/2020 e estabeleci um exemplo de limite de dias de 18 meses (conforme a MP927 - Banco de Horas Covid) multiplicado por 30 dias, mais 15 dias considerados como período de calamidade pública, totalizando 555 dias.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21371277046423)  
     
   **Observações**:  
   - O campo "Data de Início" no parametrizador do sindicato tem a função de verificar se o limite deve ser considerado na rotina de compensação e/ou lançamento do banco de horas.  
   - Para configurar o limite de compensação do banco de horas através dos parâmetros do sindicato no Automação de Ponto, é necessário fazer essa configuração em cada um dos sindicatos que abrangem os funcionários que desejam utilizar o banco de horas.
5. Para utilizar o limite, no processo de **Compensação e/ou Lançamento do Banco de Horas**, marque a opção "**Considera Limite Dias Compensação conforme parametrização**". ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21258787145111)  
     
   Caso haja um limite de dias cadastrados no parametrizador inicial e no sindicato, ao marcar a opção **"Considerar Limite Dias Compensação conforme parametrização"** no processo de compensação e/ou lançamento do banco de horas, o **sistema deixará de verificar o limite de dias** dos **parâmetros iniciais** e passará a **verificar o número limite de dias do sindicato**.  
     
   **Exemplo 1: Considerando o limite de parametrizador Inicial**  
   Período atual e ativo: 01/03/2023 a 31/03/2023  
   Limite Parametrizador Inicial: 60 dias  
   Limite Parametrizador do Sindicato: Não há cadastrado  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21358120699287)  
     
   No parametrizador iniciais foi informando a quantidade de 60 dias.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21360987896087)  
     
   Ao realizar o processo, de compensação e/ou lançamento do banco de horas, ao marcar o parâmetro **"Considera limite de dias conforme parametrização"**, a data de início do Período é alterada para 30/01/2023, respeitando assim o limite.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21358137328791)  
      
   Sem o parâmetro marcado, será informado a data de início do período ativo no momento.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21358419408279)  
     
   **Exemplo 2:  Considerando o limite de parametrizador do sindicato**Período atual e ativo: 01/03/2023 a 31/03/2023  
   Limite Parametrizador Inicial: 30 dias  
   Limite Parametrizador do Sindicato: 60 dias, a partir do dia 01/01/2023.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21361205855127)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21360966934935)  
     
   Quando o limite cadastrado do sindicato é definido e o parâmetro para considerar esse limite é marcado, a data de início da compensação não será alterada. Ela permanecerá como a data do período atual e ativo. Durante a execução do processo interno, esse limite será validado.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21361370395159)  
     
   Podemos confirmar que, neste caso, que o limite foi levado em consideração com base no registro de memória de compensação e/ou lançamento do banco de horas.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21371277057047)  
     
   **Importante**:  
   - Os exemplos são fictícios e devem ser considerados de acordo com a legislação trabalhista ou acordos coletivos ou convenções coletivas de trabalho.  
   - O limite de dias para a compensação se aplica apenas ao **banco de horas diário** e ao **banco de horas diário por ocorrência**.

**Saiba Mais**  
[Limite de dias para compensação](https://tdn.totvs.com/pages/viewpage.action?pageId=452719097)[MP927 - Banco de Horas](https://tdn.totvs.com/display/LRM/MP927+-+Banco+de+Horas)  
[Compensação e Lançamento do Banco de Horas](https://tdn.totvs.com/pages/viewpage.action?pageId=452719612)  
[RH - RM - PTO - Acessar a memória do processo compensação/lançamento do banco de horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014004312)
