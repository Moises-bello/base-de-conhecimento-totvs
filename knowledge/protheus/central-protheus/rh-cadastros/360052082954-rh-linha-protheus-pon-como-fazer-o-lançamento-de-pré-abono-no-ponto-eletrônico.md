---
article_id: 360052082954
category: RH - Cadastros
content_hash: 847eca3534505adf63fa4451e6b16ae576073c3d1bd14fc358eb720b9e04e105
fetched_at: '2026-06-28T22:44:52.681057+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON -  Como fazer o lançamento de  Pré Abono no Ponto
  Eletrônico
type: support-article
updated_at: '2026-02-24T20:33:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052082954-RH-Linha-Protheus-PON-Como-fazer-o-lan%C3%A7amento-de-Pr%C3%A9-Abono-no-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31781991627287)** **Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como realizar o cadastro de um Pré Abono no Ponto Eletrônico?  
  
**Ambiente**  
O cadastro do Pré Abono é utilizado para que exista um pré cadastro de um Motivo de Abono para um dia que ocorrerá um absenteísmo (falta, atraso, etc). Este cadastro pode ser feito para datas dentro do período de apontamento ou datas futuras.

Quando for processado um Apontamento desse dia, o sistema automaticamente vai abonar a quantidade de horas com o Motivo de Abono informado no cadastro do Pré Abono.

Somente os motivos de abonos que possuem o **campo Pré-Abono = SIM**, são visualizados.  
[*Veja mais detalhes sobre cadastros de motivos clique aqui*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000047328-RH-Linha-Protheus-PON-Como-cadastrar-Motivos-de-Abono-Justificativa)

---

Para cadastrar o Pré-abono, é necessário acessar no Ponto Eletrônico a rotina em **Atualizações > Cadastro de Funcionários > Pré-Abonos**, clicar em Incluir e preencher os campos conforme necessidade.

---

Abaixo estão alguns pontos de atenção para cadastros dos pré-abonos:

* Não são permitidas inclusões de períodos anteriores à data inicial do período de apontamento aberto;
* Para que o Sistema assuma os horários do funcionário, conforme a Tabela de Horário Padrão, não informe as horas inicial e final, o **campo Conf.** Tabela deve estar como **Sim**;
* Sempre que um período for utilizado para gerar um abono, o campo **Utilizado** terá o conteúdo **Sim** e a modificação ou eliminação desse período será antecedido por uma mensagem de advertência. Isto porque os abonos deixam de ter um histórico de geração e um novo apontamento elimina os abonos gerados. Assim como o redimensionamento do período pode alterar a quantidade de horas pré-abonadas, se o limite de horas for modificado;
* Na manutenção de Integrados ou em Leitura/Apontamento, ao executar o processo de apontamento, os eventos (faltas, atrasos e saídas) terão os seus horários de ocorrência confrontados com os períodos de pré-abono. As ocorrências compreendidas pelos limites impostos irão gerar os abonos correspondentes.

Vale lembrar que os abonos gerados anteriormente serão eliminados. A existência de abonos informados ou modificados inibe a geração de novos abonos para o mesmo evento, num mesmo centro de custo e tipo de marcações ocorridas em determinada data.

* Os abonos podem ser consultados por meio da manutenção de Apontamentos ou Integrados.  
    
  Segue exemplo de lançamento do pré-abono:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29571398376727)  
    
  Acessando em **Atualizações > Lançamentos > Integrados**, filtre a matricula e acesse em O**utras Ações > Alterar,** clique na data do lançamento e Força o Reapontamento das Marcações **<F12>**  
  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/29571405419799)**  
    
  Visualize o abono/justificativa **<F7>**, veja que o abono foi acatado após apontamento ou reapontamento:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29571405420823)  
    
  Com isso, no pré-abono ficará com o **campo Utilizado** igual à **Sim**, não podendo ser alterado com este preenchimento, veja:  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29571398385047)  
    
  Em caso de necessidade de alteração do pré-abono utilizado igual à SIM, [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059450793-RH-Linha-Protheus-PON-Altera%C3%A7%C3%A3o-ou-Exclus%C3%A3o-de-Pr%C3%A9-Abonos-j%C3%A1-utilizados) e siga a documentação.  
    
    
  **Saiba mais:**  
  [Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
  [Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
  [RH - Linha Protheus - PON - Pontos de Entrada da rotina PONA350 - Pré-Abono](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19195423064727-RH-Linha-Protheus-PON-Pontos-de-Entrada-da-rotina-PONA350-Pr%C3%A9-Abono)  
  [RH - Linha Protheus - PON - Pré Abono não é salvo após o Apontamento quando o horário é Móvel Livre](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403845669271-RH-Linha-Protheus-PON-Pr%C3%A9-Abono-n%C3%A3o-%C3%A9-salvo-ap%C3%B3s-o-Apontamento-quando-o-hor%C3%A1rio-%C3%A9-M%C3%B3vel-Livre)
