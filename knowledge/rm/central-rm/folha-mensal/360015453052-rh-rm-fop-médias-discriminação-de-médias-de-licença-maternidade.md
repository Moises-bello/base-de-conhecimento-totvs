---
article_id: 360015453052
category: Folha Mensal
content_hash: 9766f489ec09ed6bb040e6c2898448b9f718cb47fcd601cec1eda84a6d77840b
fetched_at: '2026-06-28T22:47:00.243706+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Médias: Discriminação de  médias de licença maternidade'
type: support-article
updated_at: '2025-07-19T12:39:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015453052-RH-RM-FOP-M%C3%A9dias-Discrimina%C3%A7%C3%A3o-de-m%C3%A9dias-de-licen%C3%A7a-maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33579695088151)**Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida**Como parametrizar um evento específico para o pagamento de médias de salário maternidade?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para parametrizar as médias discriminadas, siga os passos abaixo:  
  
1. Acesse a aba **Administração de pessoal | Eventos** e cadastre um novo evento como Média de Licença Maternidade, com o [Código de Cálculo 17 - Licença Maternidade.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719064)  
2. Acesse **Administração de Pessoal | Sindicatos** e depois acesse a aba **Licença maternidade**.Na aba inferior **Eventos p/ pagamento de Média de lic. maternidade**, é necessário parametrizar os grupos de médias e informar os eventos para pagamento das médias específicas.  
  
Para que o pagamento das médias ocorra separadamente informe um evento específico, no grupo 1. Isso é necessário pois, ao informar o grupo 0, as médias serão somadas ao evento de pagamento de salário maternidade com código de cálculo 17.

**Neste cadastro é permitido utilizar apenas o grupo 0-Zero e o grupo 1-Um (para os casos de média discriminada). Os demais grupos não deverão ser preenchidos, porque provocariam a redução do valor da média calculada.**

![Sem_t_tulo2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010603632)

3. Após parametrizar os grupos de médias nos **Eventos p/ pagamento de Média de Lic. maternidade**, é necessário informar a incidência de média no cadastro dos eventos pagos ao funcionário. Acesse **Administração de Pessoal | Eventos | Eventos** edite o evento que deseja informar a incidência das médias e vá em **Anexos | Eventos de Média**. O evento de pagamento de média, não poderá incidir em média.  
  
Cadastre a incidência em licença maternidade e o grupo de média utilizado, conforme explicado nos passos anteriores. Lembrando que este evento deverá estar lançado e com valores no período estabelecido nas parametrizações da média de licença maternidade para que as médias sejam corretamente lançadas. Desta forma, ao calcular o salário maternidade para o funcionário, o evento informado para pagamento de médias do grupo 1 será lançado na movimentação do funcionário.

![Sem_t_tulo2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010603792)

**Saiba mais:**

[Eventos para Pagamento de Média Licença Maternidade](Eventos%20para%20Pagamento%20de%20M%C3%A9dia%20Licen%C3%A7a%20Maternidade)
