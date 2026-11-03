---
article_id: 7465292499735
category: MDT - Atendimento Médico
content_hash: ff73e23ffc5a42099e79d6623032b1287fef9c1236705157f5a64702ff6256fa
fetched_at: '2026-06-28T22:44:21.462151+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Quais as rotinas do SIGAMDT estão relacionadas
  com o  parâmetro MV_MDTGPE?
type: support-article
updated_at: '2025-09-02T16:56:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7465292499735-RH-Linha-Protheus-MDT-Quais-as-rotinas-do-SIGAMDT-est%C3%A3o-relacionadas-com-o-par%C3%A2metro-MV-MDTGPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25655805378839) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Quais as rotinas do SIGAMDT estão relacionadas com o  parâmetro MV\_MDTGPE?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Quando existe integração do módulo de Medicina e Segurança do Trabalho com o Gestão de Pessoas, as rotinas abaixo sofrem alteração/atualização:

* **Ficha Médica (MDTA005)**
* **Sesmt/Usuar.atend (MDTA070)**
* **Diagnóstico Médico (MDTA155)**
* **Riscos (MDTA180)**
* **Atestado ASO (MDTA200)**
* **Candidatos (MDTA645)**
* **Componentes (MDTA660)**
* **Atestado Médico (MDTA685)**
* **Licença Maternidade (MDTA920)**
* **Ficha Médica (MDTA005)**

Faz a atualização do campo de **Cota Def. (****TM0\_CTPCD)** para o campo **Cota Def (RA\_CTPCD)** e **Tipo Defic. (TM0\_TIPDEF)**para o campo **Tp.Deficien (RA\_TPDEFFI)**. Os campos de **Data de Nascimento**, **Função**, **CPF**, **Centro de Custo** e **Sexo** ficam disponíveis para edição quando não existir integração entre os módulos.

Caso o parâmetro **MV\_NG2FICH**esteja habilitado, ao incluir um funcionário e o mesmo possuir um CPF, o sistema gerará uma ficha médica.  
  
**Importante!**   
**MV\_NG2FICH -** Indica se deverá incluir uma Ficha Médica para o Funcionário. 1-Sim; 2-Não. 

* **Sesmt/Usuar.atend (MDTA070)**

Ao incluir um conteúdo no campo **Ent.Cl. (TMK\_NUMENT)** o sistema não permite que seja colocado conteúdo com caracteres especiais e não deve ultrapassar a quantidade de 10 caracteres. O conteúdo deve ser de acordo com o CAGED utilizando caracteres alfanuméricos.

* **Diagnóstico Médico (MDTA155)**

Faz a atualização do campo de **Tipo Defic. (TMT\_TIPDEF)**para o campo **Tp.Deficien (RA\_TPDEFFI)**.

* **Riscos (MDTA180)**

Através do parâmetro **MV\_MDTADIC** é possível definir de onde vai ser integrado a insalubridade/periculosidade. Para maiores informações do processo, pode ser consultada a FAQ: [MDT0044\_Periculosidade\_Insalubridade\_Cadastro\_do\_Funcionario](https://tdn.totvs.com/display/PROT/MDT0044_Periculosidade_Insalubridade_Cadastro_do_Funcionario).

Importante! MV\_MDTADIC - Percentual de insalubridade/periculosidade virá do módulo SIGAMDT?    

* **Atestado ASO (MDTA200)**

Se o ASO for do tipo **4 - Retorno ao trabalho**e se o funcionário estava afastado mais dias do que o conteúdo do parâmetro **MV\_NG2TOAF,** ao confirmar o cadastro do ASO, o sistema gera um período de estabilidadepara o funcionário **(RFX)**de acordo com o parâmetro **MV\_NG2AUXD**, se o parecer do ASO for **2 - Inapto**. Para maiores informações do processo, pode ser consultada a documentação: 

[Atestado ASO (MDTA200 - SIGAMDT)](https://tdn.totvs.com/pages/viewpage.action?pageId=463817116).  
  
  
**Importante!**   
**MV\_NG2AUXD-** Indica se gera estabilidade no retorno ao trabalho após o termino do auxílio-doença acidentário. Opções 1=Gera, 2=Não gera ou 3=Pergunta se gera ou não.          
  
**MV\_NG2TOAF-** Indica a quantidade de dias que a empresa deverá pagar, referente ao afastamentos do trabalho. Valor padrão 15 dias.      

* **Candidatos (MDTA645)**

Ao gerar um conteúdo no campo **Data Estab. (TNO\_DTESTB)** o sistema atualiza o campo da rotina de **Funcionários (GPEA010)** **Dt.Vto.Estab (RA\_DTVTEST)**. Para maiores informações do processo, pode ser consultada a FAQ: [Atualização de Remoção da Estabilidade de Funcionários da CIPA](https://tdn.totvs.com/pages/viewpage.action?pageId=621598834).

* **Componentes (MDTA660)**

Ao gerar um conteúdo no campo **Data Estab. (TNQ\_DTESTB)** o sistema atualiza o campo da rotina de **Funcionários (GPEA010)** **Dt.Vto.Estab (RA\_DTVTEST)**. Para maiores informações do processo, pode ser consultada a FAQ: [Atualização de Remoção da Estabilidade de Funcionários da CIPA](https://tdn.totvs.com/pages/viewpage.action?pageId=621598834).

* **Atestado Médico (MDTA685)**

Ao realizar a inclusão de um atestado médico e informar na pasta Afastamento um período de afastamento, a mesma gravará na rotina de**Afastamento (GPEA240)**. Para maiores informações do processo, podem ser consultadas as FAQs:  [Preenchimento dos Campos de Atestado Medico](https://tdn.totvs.com/display/PROT/MDT0015+Preenchimento+dos+Campos+de+Atestado+Medico), [Atestado\_medico\_horario\_noturno](https://tdn.totvs.com/display/PROT/MDT0018_Atestado_medico_horario_noturno) e [Atestado de Falta de Trabalho Dias/Horas](https://tdn.totvs.com/pages/viewpage.action?pageId=234615426).  
  
**Importante!**  
**MV\_NGMDTAF-** Indica se o funcionário devera ser afastado do trabalho após o Atestado Medico. 

* **Licença Maternidade (MDTA920)**

Ao incluir uma licença maternidade, o sistema gera um afastamento na rotina de **Afastamento (GPEA240)**, de acordo com o campo**Cod. Ausência (TOF\_CODAFA)** atualizando o campo **Cod. Ausência (R8\_TIPOAFA)**.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
