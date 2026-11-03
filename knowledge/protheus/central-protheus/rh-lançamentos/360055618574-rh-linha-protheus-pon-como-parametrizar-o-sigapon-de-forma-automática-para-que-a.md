---
article_id: 360055618574
category: RH - Lançamentos
content_hash: 2c8a7a3fa67118d252c1aa06102156e44414216cbbbb312b4a608ffc6e76b8f3
fetched_at: '2026-06-28T22:44:46.832880+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Como parametrizar o SIGAPON de forma automática
  para que alguns funcionários trabalhem com BH e outros com Folha
type: support-article
updated_at: '2026-06-02T13:56:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055618574-RH-Linha-Protheus-PON-Como-parametrizar-o-SIGAPON-de-forma-autom%C3%A1tica-para-que-alguns-funcion%C3%A1rios-trabalhem-com-BH-e-outros-com-Folha
---

**Dúvida**  
Como parametrizar o SIGAPON de forma automática para que alguns funcionários trabalhem com Banco de horas (BH) e outros com Folha de Pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando existe o cenário de na mesma filial existirem funcionários que trabalham a**penas com Banco de Horas** e outros **apenas com Folha de Pagamento**, orientamos a criação de **duas** Regras de Apontamentos para que seja possível fazer a parametrização dos Eventos e Tipos de Horas Extras de forma separada.  
Existem alguns campos da Regra de Apontamento: **Atualizações>Cadastro do Ponto>Regra de Apontamento** que nos possibilitam saber quais eventos serão calculados e são eles:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096347593)  
  
Estes campos não determinam se os eventos serão ou não apurados, mas se serão gerados eventos [**Autorizados ou Não Autorizados**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406010444567-RH-Linha-Protheus-PON-Como-gerar-eventos-Autorizados-ou-N%C3%A3o-Autorizados)**.**  
Para os campos **Pg. Hora Ext.** e **Pg. He. Dia Nt.**, se deixamos as batidas/dias **marcados**, o sistema entende que deve gerar **Horas Extras Autorizadas**, se deixarmos **desmarcados**, os eventos gerados serão os **Não Autorizados**. A parametrização de eventos Autorizados/Não Autorizados é feita no cadastro de [**Tipos de Horas Extras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras).  
Para os campos **Desc. DSR**, **Desc. Faltas**, **Desc. Atrasos**, **Desc. S. Antec** e **Desc. S. Exped**, se deixarmos como **Sim**, o sistema entende que deve gerar os eventos de desconto que possuem ID de Ponto **A = Autorizados**, como **010A para Falta Autorizada**, **012A para Atraso Autorizado** e assim sucessivamente. Se deixarmos como **Não**, os eventos gerados serão os que possuem ID de Ponto **N = Não Autorizados**, como **009N para Falta Não Autorizada, 011N para Atraso Não Autorizado** e assim sucessivamente.  
  
Sabendo da funcionalidade dos campos, devemos **criar uma Regra deApontamento** onde vamos deixar os campos que tratam das **Horas Extras marcados e os de desconto como Sim** e na outra Regra **o inverso**:  
  
- Regra de Apontamento Banco de Horas:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096348593)  
  
- Regra Folha de Pagamento:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096348693)  
  
No cadastro dos **Tipos de Horas Extras**, na coluna de **Código Autorizado** é necessário associar os **eventos** parametrizados **para Banco de Horas** e na coluna de Código **Não Autorizado** associar os **eventos** para **Folha de Pagamento**.  
  
Lembrando que a nomenclatura dos eventos não precisa estar necessariamente como Autorizado/Não Autorizado, quem determina isso é o cliente. Usamos estas nomenclaturas para nos basear através das colunas de cadastro dos Tipos de Horas Extras e IDs de Ponto.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096350433)  
  
Segue um exemplo utilizando o tipo de hora Normal, onde meu evento 100 é o que deve ir pra Folha e o 101 para Banco de Horas:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096351473)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094083054)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096351553)  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096351573)  
  
Importante ressaltar: eventos de horas extras NÃO possuem ID de Ponto.  
  
No cadastro dos Eventos de desconto que possuem ID, parametrizei os que possuem ID A para Banco de Horas e os eventos com ID N para Folha de Pagamento, segue exemplo com os eventos de Falta, onde o 009 deve ser descontado em Folha e o 010 em Banco de Horas:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094083514)  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094083554)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096352033)  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094083674)  
  
Depois de alterar todos estes cadastros, farei uma troca de turno para dois funcionários. No meu exemplo, o funcionário 000008 é o que terá vínculo com a Regra de Banco de Horas e o 000009 terá vínculo com a Regra de Folha:  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096352473)  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094084034)  
  
Dentro do período, o funcionário 000008 teve uma falta, um atraso e horas extras que devem ir para o Banco de Horas:  
![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094084334)  
  
O funcionário 000009 também teve uma falta, um atraso e horas extras, mas neste caso, os apontamentos devem ser pagos/descontados em Folha:  
![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094084434)  
  
É necessário realizar o Cálculo Mensal de todo o período, pois esta rotina é a responsável por definir para onde deve ir cada um dos apontamentos:  
![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096353213)  
![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094084674)  
![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096353253)  
![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094084794)  
  
Após o Cálculo Mensal, verificando os Lançamentos de Banco de Horas para o funcionário 000008, tudo foi lançado corretamente:  
![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094084994)  
  
Verificando os Lançamentos de Resultados para o funcionário 000009, tudo foi lançado corretamente também:  
![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094085174)  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
