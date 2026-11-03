---
article_id: 4407779446679
category: RH - Cadastros
content_hash: b6e019df26378cf8270c8f41f127c8eadd98ac5bb72698cb6deea0aac93e2b77
fetched_at: '2026-06-28T22:44:53.080741+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Pré abono ponto eletrônico
type: support-article
updated_at: '2025-12-16T13:22:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407779446679-RH-Linha-Protheus-PON-Pr%C3%A9-abono-ponto-eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34259530742295) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como funciona a rotina de pré-abono no SIGAPON?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Esta rotina **possibilita a geração automática de abonos**, a partir de **períodos** (datas e horas) **previamente cadastrados**. Serão abonados somente os eventos de faltas, faltas meio período, atrasos e saídas antecipadas ou durante o expediente.  
  
Localização no menu do ambiente: Atualizações -> Cadastro de Funcionários -> **Pré-abonos**  
  
Pode ser utilizada, por exemplo, pelo Departamento Médico da empresa, de forma que o médico possa informar o período em que o funcionário permanecerá ausente do trabalho, especificando o motivo de abono/justificativa correspondente. No momento do apontamento das marcações do funcionário, as ocorrências dos eventos citados serão abonadas conforme as informações do pré-abono.   
Somente os motivos de abonos que pré-abonam serão visualizados.  
Não serão permitidas inclusões de períodos anteriores à data inicial do período aberto.  
  
Existem integrações entre módulos e produto que integra com esta rotina. No caso dos abonos lançados no MEU RH, após passados pelo processo de aprovação subirá nesta rotina de pré-abono.  
Veja mais detalhes: [RH - Linha Protheus - MEU RH - Como registrar a solicitação de Pré-Abono através do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056545994-RH-Linha-Protheus-MEU-RH-Como-registrar-a-solicita%C3%A7%C3%A3o-de-Pr%C3%A9-Abono-atrav%C3%A9s-do-MEU-RH)  
  
Temos, também , o lançamento de atestado médico pelo SIGAMDT que integra com o pré-abono, segue documentação: [RH - Linha Protheus - MDT - Integração do Atestado Médico com o Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025162074-RH-Linha-Protheus-MDT-Integra%C3%A7%C3%A3o-do-Atestado-M%C3%A9dico-com-o-Ponto-Eletr%C3%B4nico)  
  
É possível ao invés de colocar hora inicial e final, utilizar com base na tabela de horário padrão.  
Para que o sistema assuma os horários do funcionário, conforme a Tabela de Horário Padrão, ambas as horas (inicial e final) não devem ser informadas.  
Sempre que um período informado no cadastro de pré-abono for utilizado no apontamento, o **campo** "**Utilizado**" terá o conteúdo "**Sim**" e a modificação ou eliminação desse período será antecedido por uma mensagem de advertência.  
  
Na manutenção de Marcações ou na rotina de Leitura/Apontamento, ao executar o processo de apontamento, os eventos (faltas, atrasos e saídas) terão os seus horários de ocorrência confrontados com os períodos de pré-abono. As ocorrências compreendidas pelos limites impostos irão gerar os abonos correspondentes.  
Tela de exemplo com pré-abono:  
**Principais Campos**  
**Data Inicial e Data Final:**  
Neste campos devem ser informadas as datas, inicial e final do abono cadastrado para o funcionário.  
**Hora Inicial e Hora Final:**  
Estes campos devem ser preenchidos com hora inicial e final do abono caso ele tenha sido cadastrado para fazer um abono parcial do apontamento.  
**Conforme Tabela:**  
Deve ser preenchido quando o abono for Integral, e a hora inicial e final tiver que ser igual a hora cadastrada na tabela de horário padrão.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31913926339607)  
  
Vale lembrar que os abonos gerados anteriormente serão eliminados. A existência de abonos informados ou modificados inibirá a geração de novos abonos para o mesmo evento, no mesmo centro de custo e tipo de marcação, ocorridos em determinada data. Os abonos poderão ser consultados também através da manutenção de Apontamentos (Atualizações > Lançamentos > Apontamentos).  
  
Após apontamento veja como ficou o abono:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31913896931223)  
  
Após isto, basta efetuar o Cálculo Mensal em Miscelânea > Cálculos > Cálculo Mensal. Assim, o sistema atualizará o abono do funcionário, seja no Banco de Horas ou na Folha de Pagamento.  
  
**Saiba Mais**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como fazer o lançamento de Pré Abono no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052082954-RH-Linha-Protheus-PON-Como-fazer-o-lan%C3%A7amento-de-Pr%C3%A9-Abono-no-Ponto-Eletr%C3%B4nico)  
[RH - Linha Protheus - PON - Pré Abono não é salvo após o Apontamento quando o horário é Móvel Livre](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403845669271-RH-Linha-Protheus-PON-Pr%C3%A9-Abono-n%C3%A3o-%C3%A9-salvo-ap%C3%B3s-o-Apontamento-quando-o-hor%C3%A1rio-%C3%A9-M%C3%B3vel-Livre)  
[RH - Linha Protheus - PON - Registo já gravado na rotina Pré-Abono, não é possível alterar ou excluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059450793)
