---
content_hash: 3a0d63f201112e1233fe8040707ec18e53fe84ef3bc60a9945c05586264dcf3a
fetched_at: '2026-06-29T00:08:20.218929+00:00'
page_id: '268572052'
product: rm
source: tdn-rm
title: RPTMIG00019.1.1 - Executando Fórmulas onde Resultado deve ser Mostrado de Imediato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268572052
version: 10
---

# Executando Fórmulas onde Resultado deve ser Mostrado de Imediato

|  |  |
| --- | --- |
| **Produto:** | TOTVS Reports |
| **Versões:** | 12.1.x |
| **Ocorrência:** |  |
| **Ambiente:** |  |
| **Passo a passo:** | Conteúdo  ---  Conteúdo|Executando Fórmulas onde Resultado deve ser Mostrado de ImediatoIntrodução  ---   Com o advento da migração do **TOTVS Reports** da **versão 11.8x** para as versões **superiores a versão 12.1.4**, muitas alterações foram feitas principalmente **na geração sobre demanda dos dados** vinculados a cada componente presente no relatório.  Em relatórios da versão **11.8x**, por exemplo, **a geração sobre demanda dos dados** era realizada no momento da impressão de cada componente, ao contrário dos das versões mais atuais **(12.1.5 ou superiores)**, onde a geração dos dados é feita através de apenas uma consulta SQL **(Fase de Preparação)**, que é gerada a partir das tabelas e consultas SQL vinculadas ao relatório. 1 - Executando Fórmulas onde Resultado deve ser Mostrado de Imediato  ---   Existem diversos tipos de fórmulas, com diversos propósitos, vamos tratar, porém, de fórmulas, que necessitam do resultado imediato, para que o relatório apresente os valores devidamente atualizados.   1.1 - Executando Fórmulas com Resultado Imediato (1180)  ---   Vamos utilizar o relatório abaixo como exemplo:    **RELATÓRIO PRINCIPAL 1180**      **OBS:** A fórmula **FRM003** atualiza a tabela **"Histórico de Disciplinas Concluídas"**.  Temos os campos necessários para a execução da Fórmula e para a execução da **Consulta SQL** vinculada a banda **"Detalhe2".**  Como na versão **1180** gera as informações **sobre demanda**, ou seja, **prepara e executa os controles em um mesmo momento**, a fórmula será executada, a tabela **Histórico de Disciplinas Concluídas** será atualizada, e consequentemente o relatório será gerado com as informações já atualizadas.       1.2 - Executando Fórmulas com Resultado Imediato (1200)  ---   Com a migração da versão **1180** para a **1200**, teremos que mudar a estrutura do relatório para que tenhamos o mesmo resultado.  Motivo: Com a **Reestruturação do Reports** em **duas fases**, os controles não mais são preparados e executados num mesmo momento, pelo contrário, **as fases são bem distintas**, onde os dados são recuperados na fase de **Preparação** e os controlessão executados na fase de **Geração**.  Por esse motivo, **não poderemos** executar num mesmo relatório a Fórmula e o restante da informação.  Teremos que dividir esse relatório em **dois**, onde a fórmula será executada no relatório principal, e o restante da informação, em um sub-relatório (controle), dentro do relatório principal.    **RELATÓRIO PRINCIPAL 1200**        **OBS:** A fórmula **FRM003** atualiza a tabela **"Histórico de Disciplinas Concluídas"**.  Temos os campos necessários para a execução da Fórmula e para a execução da **Consulta SQL** vinculada a banda **"Detalhe1",** localizada no próprio sub-relatório.        O sub-relatório deverá **conter o restante das informações**. Cada relatório **é executado por completo**; após a execução do relatório principal o sub-relatório também é executado, fazendo com que a Fórmula pertencente ao relatório principal **execute primeiro**, já que o relatório principal é executado antes, fazendo com que os dados do relatório gerem atualizados.       1.3 - Executando Fórmulas com Resultado Imediato (Outras Considerações)  ---   Caso o relatório modelo da versão **1180** seja executado na versão **12** (a partir da versão **12.1.5**), o relatório será gerado normalmente, porém as informações mostradas não estarão atualizadas.  **Motivo:** A **Consulta SQL** recuperará os dados antes da execução da **Fórmula**, fazendo com que os dados mostrados no relatório **não sejam os mais atualizados**.        Será necessário a execução do relatório **uma segunda vez** para que a atualização provocada pela **execução da fórmula** seja percebida. |
| **Observações:** |  |
