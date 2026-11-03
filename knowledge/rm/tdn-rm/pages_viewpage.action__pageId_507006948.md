---
content_hash: e123b0d2ef6bb74973b14079e0d1228f8b69a9f6ec90d8e0af58a5a6fd95369e
fetched_at: '2026-06-29T00:10:25.960220+00:00'
page_id: '507006948'
product: rm
source: tdn-rm
title: Licença Maternidade interrompendo férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507006948
version: 3
---

# Objetivo:

---

       O objetivo deste documento é orientar como proceder quando a funcionária entra de licença maternidade durante o período de gozo de férias.

false

**A partir das Versões:**

* 12.1.23
* 12.1.24
* 12.1.25

Ocorrendo o nascimento da criança durante o gozo de férias da funcionária, o início do afastamento para recebimento do salário-maternidade ocorrerá no próprio dia do parto, suspendendo-se, consequentemente, o gozo das férias, o qual será retomado tão logo termine a licença-gestante (120 dias). Considerando que somente o efetivo gozo de férias é suspenso e posteriormente retomado, como o pagamento das férias já foi efetuado, só haverá complementação desse valor se houver reajuste salarial no decorrer do afastamento.  
  
Para tratativa no TOTVS Folha de Pagamento, siga os passos abaixo:

Passo a PassoInício e fim de férias no mesmo mêsIFMesmoPeriodoExemplo

Vamos considerar abaixo um exemplo de férias já calculadas, lançadas e finalizadas para a funcionária, em que o início e fim do período de gozo ocorreram no mesmo mês.

**Período de Gozo**: 01/01/2019 a 30/01/2019  
**Início licença maternidade**: 20/01/2019  
  
  
  
  
**S-2230 de afastamento de férias** já enviado e aceito pelo Governo:

1º Passo - Cadastro Férias

Com as férias já finalizadas:

1. Acesse o cadastro de período aquisitivo e edite o registro relacionado ao período da funcionária;  
2. Na aba **Período de Gozo**, edite o período referente às férias gozadas;  
3. Altere a situação das férias de **Finalizadas** para **Marcada** e salve o cadastro;  
4. Somente após salvar a alteração anterior, altere o **Período de Gozo** informando como término **o dia imediatamente anterior ao início da licença maternidade** e salve novamente o cadastro;  
5. Volte a situação das férias para **Finalizadas** e salve o registro.

**Importante**  
Durante as alterações será apresentada a mensagem abaixo. Selecione a opção "Sim" para que o sistema gere o gatilho de retificação do S-2230.

2º Passo - Retificação do S-2230

Gere o XML do gatilho de **retificação do S-2230** para ajustar o término do afastamento e transmita o evento para o governo.

3º Passo - Ajuste do histórico de situação

Após ajustar o término das férias, para que seja possível cadastrar corretamente a licença maternidade, é importante ajustar o histórico de situação da funcionária.  
Para isso, no cadastro da funcionária:

1. Acesse Anexos | Históricos | Histórico de Situação;  
2. Selecione o registro referente ao retorno das férias (Situação Ativo com data posterior ao término das férias);  
3. Exclua o registro mantendo como último item a situação das férias.

4º Passo - Cadastro da Licença Maternidade

Cadastre a licença maternidade normalmente para a funcionária.

Transmita o **S-2230** relacionado ao afastamento da licença maternidade para o governo.

5º Passo - Término da Licença e conclusão das férias

Quando o período da licença maternidade for concluído, o período restante de gozo das férias deverá ser informado ao eSocial.

Para isso, siga os passos abaixo:

1. Acesse o cadastro de período aquisitivo e edite o registro relacionado ao período da funcionária;  
2. Na aba **Período de Gozo**, inclua um novo registro com data de início imediatamente após o retorno do afastamento da licença maternidade e status **Marcadas**;  
3. Altere a situação das férias para **Finalizadas** e salve o registro;

Ao salvar, será apresentada novamente a mensagem abaixo. Selecione a opção "Sim" para que o sistema gere o gatilho do S-2230.

Transmita o evento para o governo.

Início e fim de férias em meses distintos (Férias Partidas)

O processo em casos de férias partidas será igual ao de férias no mesmo mês, diferenciando somente que para finalizar as férias será necessário:  
  
1. Acessar o menu **Férias | Finaliza** e selecionar o parâmetro **Lança Movimento Próximo Mês** para que o sistema finalize as férias da funcionária.

Posicionamento do Suporte do eSocial (Governo)

Devido à questionamento de clientes em relação ao processo, questionamos o governo qual seria o procedimento adequado à ser feito.

Segue abaixo o retorno dado pela equipe de atendimento do governo:

"[...] Em atenção ao questionamento, a informação de um novo motivo de afastamento só é possível mediante o envio do término do afastamento anterior. Por exemplo, se uma empregada gestante **se afasta para gozo de férias e durante esse período ocorre o parto**, deve ser informado o **retorno do afastamento relativo às férias na data anterior ao parto** (ou feita sua retificação caso a data do retorno já tenha sido informada) e encaminhado um **novo evento de afastamento informando o início da licença maternidade**, após o termino da licença maternidade, o empregador **informará o restante das ferias no evento S-2230**.  
  
A empresa deve definir se vai descontar os valores pagos antecipadamente ou manter os pagamentos realizados. O procedimento mais adequado é **não alterar valores já pagos e logo após o término da licença maternidade, a empregada goza os dias faltantes das férias**. Com esse procedimento, os ajustes serão mais simples.  
  
Atenciosamente,  
Equipe eSocial"
