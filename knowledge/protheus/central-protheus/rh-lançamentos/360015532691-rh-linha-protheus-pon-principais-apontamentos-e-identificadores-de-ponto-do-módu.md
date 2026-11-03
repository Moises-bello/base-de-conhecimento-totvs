---
article_id: 360015532691
category: RH - Lançamentos
content_hash: 6875f912f79eb59323a7a322c3ab6229f9f8b8a00fc8da58fa7e8c98bddc5007
fetched_at: '2026-06-28T22:44:46.882564+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Principais Apontamentos e Identificadores de Ponto
  do Módulo de Ponto Eletrônico
type: support-article
updated_at: '2025-06-04T19:13:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015532691-RH-Linha-Protheus-PON-Principais-Apontamentos-e-Identificadores-de-Ponto-do-M%C3%B3dulo-de-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31901668448023) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Quais são os principais Apontamentos e Identificadores de Ponto do Módulo de Ponto Eletrônico?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**

No modulo do ponto eletrônico, acessar em **Atualizações > Cadastro do Ponto > Eventos**, e realizar o cadastro do principais identificadores abaixo:

**1. Horas Normais**  
Cadastrar o evento de Horas Normais relacionado ao Identificador de Ponto **001A.**- No campo **Classificação** deve ser preenchido como **ZZ - Outros**: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154404913047)**No **Cadastro de Regra de Apontamento** o campo **Pg Hrs. Norm**. (PA\_HRNORM) deve ser configurado com “**Sim**”:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154623048215)  
  
**2. Adicional Noturno**:   
Cadastrar o evento de Adicional Noturno relacionados aos Identificadores de Ponto **003N** e **004A.**- No campo **Classificação** deve ser preenchido como **ZZ - Outros**:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221528340759)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221528341143)**No **Cadastro de Regra de Apontamento, em Atualizações-Cadastro do ponto-Regra Apontamento,** o campo **Pg.Ad.Not** (PA\_ADNOT) estiver preenchido com "**Não",** será gerado o evento vinculado ao Identificador de Ponto **003N,** e se estiver preenchido com **Sim,** será gerado o evento vinculado ao Identificador de Ponto **004A:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221502001047)  
  
3. Adicional Noturno sobre Hora Extra:**Cadastrar os eventos de Adicional Noturno Sobre Hora Extra relacionados aos Identificadores de Ponto **027N** e **028A.**- No campo **Classificação** deve ser preenchido como **ZZ - Outros:** **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221528344215)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221502004631)**No **Cadastro de Regra de Apontamento** na aba Apontamentos se o campo **Pg.Ad.Not.Ex.**(PA\_ADNOTEX) estiver preenchido com **Não** será gerado o evento vinculado ao Identificador de Ponto **027N,** se estiver preenchido com **Sim**, será gerado o evento vinculado ao Identificador de Ponto **028A:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221502006807)  
  
4. Hora Extra:**Cadastrar os eventos de Hora Extra **sem vinculo** a qualquer **Identificador de Ponto.**- No campo **Classificação** deve ser preenchido como **01 - Hora Extra:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154405013527)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154405019543)**No **Cadastro de Regra de Apontamento** para definir se a Hora Extra a ser apontada será **Autorizada** ou **Não Autorizada,** é necessário verificar o preenchimento dos campos **Pg. Hora Ext.** e **Pg. He. Dia Nt.** Para mais destelhes sobre a horas "Autorizada" e "Não Autorizada" [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004053911-RH-Linha-Protheus-PON-Como-funcionam-as-horas-extras-autorizadas-e-n%C3%A3o-autorizadas). **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154594999447)  
  
IMPORTANTE**: Será necessário informar no cadastro de **Tipos de Horas Extras** os eventos de Horas Extras **Autorizado** e **Não Autorizado**. Para mais informações [**clique aqui**.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras)  
  
**5. Faltas**:   
Cadastrar os eventos de **Faltas** relacionados aos Identificadores de Ponto **009N** e **010A.**- No campo **Classificação** deve ser preenchido como **02 - Falta:** **![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154413540887)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154413542551)**No **Cadastro de Regra de Apontamento** se o campo **Desc Faltas** (PA\_FALTAS) estiver preenchido com **Não**, será gerado o evento vinculado ao Identificador de Ponto **009N**, se estiver preenchido com **Sim,** será gerado o evento vinculado ao Identificador de Ponto **010A:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154594987031)  
  
**6. Atrasos**:  
Cadastrar os eventos de **Atrasos** relacionados aos Identificadores de Ponto **011N** e **012A.**- No campo **Classificação** deve ser preenchido como **03 -** **Atraso:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154413549335)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154413552663)**  
No **Cadastro de Regra de Apontamento** se o campo **Desc Atrasos** (PA\_Atrasos) estiver preenchido com **Não**, será gerado o evento vinculado ao Identificador de Ponto **011N**, se estiver preenchido com **Sim,** será gerado o evento vinculado ao Identificador de Ponto **012A:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154623061655)** **7. Saída Antecipada**:   
Cadastrar os eventos de Saída Antecipada relacionados aos Identificadores de Ponto **013N** e **014A.**  
- No campo **Classificação** deve ser preenchido como **05 - Saída Antecipada:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154413554583)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154413561111)  
  
No **Cadastro de Regra de Apontamento** se o campo **Desc S. Antec** (PA\_SAIANT) estiver preenchido com **Não**, será gerado o evento vinculado ao Identificador de Ponto **013N**, se estiver preenchido com **Sim,** será gerado o evento vinculado ao Identificador de Ponto **014A:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19154594994711)  
  
8. Saída Expediente**Cadastrar os eventos de Saída Expediente relacionados aos Identificadores de Ponto **019N** e **020A**.  
- No campo **Classificação** deve ser preenchido como **04 - Saída Expediente**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221501986967)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221501991575)  
  
No **Cadastro de Regra de Apontamento** se o campo **Desc S. Exped** (PA\_SAIEXPE) estiver preenchido com **Não**, será gerado o evento vinculado ao Identificador de Ponto **019N**, se estiver preenchido com **Sim,** será gerado o evento vinculado ao Identificador de Ponto **020A:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19221528339351)  
 **Obs.:** Os prints acima são somente exemplos de eventos cadastrados com os identificadores de Ponto. Referente ao campo código quem defini é o usuário, que poderá criar o código que esteja disponível no ambiente.  
  
**Saiba mais:**[RH - Linha Protheus - PON - Como funcionam as horas extras autorizadas e não autorizadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004053911-RH-Linha-Protheus-PON-Como-funcionam-as-horas-extras-autorizadas-e-n%C3%A3o-autorizadas)  
[RH - Linha Protheus - PON - Como gerar eventos Autorizados ou Não Autorizados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406010444567-RH-Linha-Protheus-PON-Como-gerar-eventos-Autorizados-ou-N%C3%A3o-Autorizados)  
[RH - Linha Protheus - PON - Regras importantes para o cadastro dos Tipos de Horas Extras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060489314-RH-Linha-Protheus-PON-Regras-importantes-para-o-cadastro-dos-Tipos-de-Horas-Extras)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
