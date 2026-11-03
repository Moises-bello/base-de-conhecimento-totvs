---
article_id: 4408434877591
category: RH - Cadastros
content_hash: c061b104a8b9b72bdd8ce38e622bf351cb5372db8a4f82f6f2a7fe668b3f4e68
fetched_at: '2026-06-28T22:44:52.989794+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Escalonamento de Horas Extras
type: support-article
updated_at: '2026-06-25T14:47:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408434877591-RH-Linha-Protheus-PON-Escalonamento-de-Horas-Extras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32617456549655) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como escalonar as horas extras do Ponto Eletrônico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O **Escalonamento de Horas Extra** basicamente funciona para que seja possível **remunerar** um **mesmo Tipo de Hora Extra** com **percentuais diferentes.**  
  
No **Protheus**, podemos trabalhar com o **Escalonamento** de **duas formas:**  
- com o parâmetro **MV\_ACMHEXT = N**  
- com o parâmetro **MV\_ACMHEXT = S**

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Exemplo de utilização** |
| **MV\_ACMHEXT** | Acumular Todas as Horas Extras do Dia de forma que essas possam ser escalonadas. "S"=Sim ; "N"=Nao | S |

Primeiro, falaremos sobre o cenário tendo o **parâmetro MV\_ACMHEXT = N**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15000979524503)**

**Cadastro de Evento**  
É necessário **cadastrar os eventos de hora extra** para que o sistema faça corretamente seu apontamento. Por exemplo, no cadastro de **eventos,** precisa existir **um evento** de **hora extra normal autorizada** e **outro evento** referente a **hora extra não autorizada**. Dessa maneira, no **apontamento** quando o funcionário realizar uma **hora extra,** a mesma será exibida no **evento** cadastrado. Para que o **evento** cadastrado seja **reconhecido como hora extra**, será necessário informar no campo **"Classific."** como **"01 - Hora Extra".**  
Para acessar a rotina de cadastro de **evento**, acesse o módulo SIGAPON do Protheus, **Atualizações → Cadastro do Ponto → Eventos.**  
  
**Exemplo** de cadastro **Hora Extra Normal 55%**![](https://tdn.totvs.com/download/attachments/557344882/image2020-8-6_17-7-3.png?version=1&modificationDate=1596746265750&api=v2&effects=drop-shadow)

Será **necessário** ter **mais eventos** para um **único tipo de hora extra**, por exemplo: **Hora Extra Normal Autorizada 55%, 75%, 100% e etc**, ou seja, teremos que **cadastrar** **6 eventos no total** para as **Horas Extras Normais de 55%, 75% e 100% autorizadas e não autorizadas**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15000666934167)

- É **necessário** realizar o **cadastro** de **eventos** de **todos os tipo de hora extra**, por exemplo, **Hora Extra Normal, Hora Extra Noturna, Hora Extra DSR e etc**.  
- Para que os **eventos** de **horas extras** sejam **integrados com a folha**, será necessário vincular uma **verba** no campo **Cod.p/ Folha**  
- Após aplicar todos os **escalonamentos**, o sistema irá **transferir o resultado de cada evento** para sua respectiva **verba**. Por este motivo **cada evento** utilizado na faixa terá que possuir o vínculo de uma **verba única**, **não podendo ser utilizado uma verba para mais de um evento do ponto**, visto que o **escalonamento** é feito para **cada faixa** de **cada Tipo de Hora Extra,** e não por verba.  
  
**Cadastro Tipo de Hora Extra**  
Após cadastrarmos todos os eventos iremos realizar o cadastro de **Tipo de Hora Extra**. Esse cadastro tem como função **identificar** **qual evento será utilizado no momento do apontamento**. Se houver o lançamento de uma **Hora Extra Normal**, o sistema irá verificar, através do **cadastro** de **Tipo de Hora Extra**, qual **evento** deverá ser **exibido**, podendo ser o **evento** de **Hora Extra Autorizada ou não**.   
  
Para que o sistema **aponte** corretamente todos os **eventos,** será necessário **cadastrar** no mínimo **08 tipos de hora extra**, que são: **Normal, D.S.R, Compensado, Feriado, Noturna Normal, Noturna DSR, Noturna Compensada e Noturna Normal.**  
  
Para acessar a rotina de **cadastro de tipos de horas extras**, acesse o módulo **SIGAPON do Protheus**, **Atualizações → Cadastro do Ponto → Tipos Hora Extra.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408434707479)

Para **cadastrar o escalonamento,** teremos que definir sua **porcentagem**, o **limite** de uma **hora extra** para aquela **porcentagem** e **quais eventos** serão utilizados, conforme a imagem abaixo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408429615767)

De **1 minuto até 1 hora** será considerada **Hora Extra de 55%**  
De **1:01 até 2 horas** será considerada **Hora Extra de 75%**  
De **2:01 até 999,99** horas será considerada **Hora Extra de 100%**

Caso o parâmetro **MV\_ACMHEXT** **não** **esteja ativo**, não será **necessário** realizar o **cadastro dos Tipos de Horas Extras em pares**, ou seja, **faixas de Escalonamento**, porém, é **obrigatório** que existam os **08 tipos de horas extras cadastradas,** por exemplo:  
**- cadastro do Tipo de Hora Extra Normal**:  
**Faixa 1 =** 0,01 à 50,00  
**Faixa 2 =** 50,01 à 999,99  
  
**- cadastro do** **Tipo de Hora Extra Noturna Normal**:  
**Faixa 1 (única) =** 0,01 à 999,99  
  
Veja que **não** foram cadastradas **duas faixas** **de escalonamento** para o tipo **Noturna Normal**, porém, ele foi **cadastrado** com uma **faixa única** de apuração.  
  
Agora, falaremos sobre o cenário tendo o **MV\_ACMHEXT = S**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15001277678103)  
  
Será **necessário seguir todos os passos cadastrais citados anteriormente**, ou seja: cadastrar **Eventos** e **Tipos de Horas Extras**, porém, temos **particularidades** neste caso:  
- Para o **escalonamento** quando o **MV\_ACMHEXT = S**, os **Tipos de Hora Extra deverão ser pares**, por exemplo, se forem cadastradas duas **faixas** do **Tipo de Hora Extra Normal,** deverão existir **duas faixas também** para o **Tipo de Hora Extra Noturna Normal** conforme exemplo abaixo:  
**- cadastro do Tipo de Hora Extra Normal**:  
**Faixa 1 =** 0,01 à 50,00  
**Faixa 2 =** 50,01 à 999,99  
  
**- cadastro do** **Tipo de Hora Extra Noturna Normal**:  
**Faixa 1 =** 0,01 à 50,00  
**Faixa 2 =** 50,01 à 999,99  
  
Veja que neste caso, existem **duas faixas exatamente iguais para ambos Tipos de Horas Extras**.

**AEJ**  
Para a **geração do arquivo AEJ**, o sistema irá **validar** se os **eventos** cadastrados nos **Tipos de Hora Extra** estão em **duplicidade**. Por este motivo, verifique se um **evento** está sendo **utilizado em mais de um Tipo de Hora Extra**, pois **não será possível gerar o arquivo** se isso acontecer.  
Caso isso ocorra, será **exibido** um ***log*** em **tela** para o usuário.

**Apontamentos**  
Após realizar o **cadastro** de **Eventos** e **Tipo de Hora Extra**, podemos verificar como o sistema gerou os **eventos** de acordo com o **tipo de apuração da hora extra**, que nos **exemplos** abaixo são **Diária e Mensal para exemplificar a diferença entre eles**.

* [Apuração Diária](https://tdn.totvs.com/display/public/PROT/Escalonamento+Horas+Extras#tabs-diaria)
* [Apuração Mensal](https://tdn.totvs.com/display/public/PROT/Escalonamento+Horas+Extras#tabs-mensal)

**\*\*Importante: O escalonamento de Horas Extras é acatado somente para apontamentos de eventos AUTORIZADOS**  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
