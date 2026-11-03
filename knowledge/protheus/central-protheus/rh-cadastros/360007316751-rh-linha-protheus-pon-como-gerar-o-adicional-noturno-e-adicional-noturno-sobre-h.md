---
article_id: 360007316751
category: RH - Cadastros
content_hash: e440c6b70b04a330f288d4782ae41034a6871ec46186a6ce35a0f0bd32c6a813
fetched_at: '2026-06-28T22:44:52.898864+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como gerar o Adicional Noturno e Adicional Noturno
  sobre Horas Extras
type: support-article
updated_at: '2026-02-04T14:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007316751-RH-Linha-Protheus-PON-Como-gerar-o-Adicional-Noturno-e-Adicional-Noturno-sobre-Horas-Extras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35190374589591) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como gerar o Adicional Noturno e Adicional Noturno sobre Horas Extras?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
É importante esclarecer que o Protheus utiliza dois eventos distintos para o cálculo do adicional noturno, sendo eles:

* **003N/004A - Adicional Noturno**
* **027N/028A - Adicional Noturno sobre Horas Extras**

**1. Adicional Noturno (003N/004A)**

Este evento refere-se ao adicional noturno que é calculado com base na jornada de trabalho regular do funcionário. Ele será gerado apenas durante o horário de trabalho previsto para o turno noturno, por exemplo: das 22h às 05h, das 00h às 07h, entre outros.  
  
**2. Adicional Noturno sobre Horas Extras (027N/028A)**  
Este evento é aplicado quando um funcionário que não possui turno noturno programado realiza horas extras dentro desse período.  
Por exemplo, se um funcionário com jornada das 08h às 17h trabalha até às 23h, além das horas extras diurnas, será gerado 01h09 de hora extra noturna. Adicionalmente, será calculado 01h09 de adicional noturno sobre essa hora extra.   
É importante destacar que o evento de adicional noturno sobre horas extras funciona de maneira independente do evento de hora extra noturna. Ou seja, mesmo que haja tolerância para a hora extra, o adicional noturno sobre horas extras será calculado.  
Caso não deseje que esse evento seja gerado, será necessário **configurar a tolerância no cadastro de Regra de Apontamento.**  
  
**3. Configurações Necessárias**  
Para garantir que ambos os eventos sejam corretamente gerados, os seguintes cadastros devem estar devidamente configurados no ambiente:

**1 - Tabela de Horário Padrão**  
É fundamental prestar atenção ao configurar o cadastro de horários, certificando-se de definir corretamente o tipo de hora extra que será gerada para cada dia.   
A rotina pode ser localizada no menu **Atualizações - Cadastro do Ponto - Tabela de Horário Padrão.**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099511553)  
Para saber mais sobre a configuração da tabela de horário padrão siga a documentação: [RH - Linha Protheus - PON - Tabela de Horário Padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047920293-RH-Linha-Protheus-PON-Tabela-de-Hor%C3%A1rio-Padr%C3%A3o)  
  
**2 - Regra de Apontamento**  
Na aba **Apontamentos** do cadastro de Regra de Apontamento, existem os campos **Pg. Ad. Not.** e **Pg. Ad. Not. Ex.**, que **não determinam a geração** do Adicional Noturno ou do Adicional Noturno sobre Horas Extras. Esses campos servem exclusivamente para definir **qual ID de evento de ponto será apontado** no sistema:

* Quando configurados como **SIM**, serão utilizados os eventos:
  + **004A** – Adicional Noturno
  + **028A** – Adicional Noturno sobre Horas Extras
* Quando configurados como **NÃO**, os eventos apontados serão:
  + **003N** – Adicional Noturno
  + **027N** – Adicional Noturno sobre Horas Extras

Ou seja, a configuração desses campos **não interfere no cálculo dos adicionais**, apenas determina **qual código de evento será registrado** nos apontamentos.![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097205014)

**3 – Turno de Trabalho**  
No cadastro de **Turno de Trabalho**, são configurados o **início** e o **término** da hora noturna, bem como o **valor do minuto da hora noturna**. De acordo com a CLT, o padrão é definir:

* Início da hora noturna: **22h**
* Término da hora noturna: **05h**
* Duração do minuto da hora noturna: **52,5 segundos**

Contudo, o sistema oferece flexibilidade, permitindo que o cliente defina os valores que atendem melhor às necessidades da empresa.

Adicionalmente, para que o cálculo da conversão da hora noturna seja realizado corretamente, conforme o horário cadastrado na **Tabela de Horário Padrão**, os campos **Con. H. N. Tab.** e **Con. H. N. Tb. I** devem estar configurados como **SIM**.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097205634)  
  
**4 – Tipos de Horas Extras**  
O cadastro de **Tipos de Horas Extras** impacta diretamente no cálculo do **Adicional Noturno sobre Horas Extras**, além de afetar todos os tipos de horas extras registradas no ponto. Para garantir o correto processamento, é fundamental que os oito primeiros tipos de horas extras estejam configurados corretamente. Estes tipos são:

* **Normal**
* **DSR**
* **Compensado**
* **Feriado**
* **Noturna Normal**
* **Noturna DSR**
* **Noturna Compensado**
* **Noturna Feriado**

Além disso, é **essencial** que não haja **repetição de códigos de eventos** entre os diferentes tipos de horas extras, para evitar conflitos no cálculo e garantir a integridade dos dados.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099511253)  
  
**5 - Eventos**  
Como citado acima, os **IDs de Ponto** que tratam do **Adicional Noturno** e **Adicional Noturno sobre Horas Extras** são: **003N, 004A, 027N e 028A**. É importante que exista evento vinculado a cada um desses IDs para a correta apuração.  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como alterar a Regra de Apontamento de um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18869900945687-RH-Linha-Protheus-PON-Como-alterar-a-Regra-de-Apontamento-de-um-Funcion%C3%A1rio)
