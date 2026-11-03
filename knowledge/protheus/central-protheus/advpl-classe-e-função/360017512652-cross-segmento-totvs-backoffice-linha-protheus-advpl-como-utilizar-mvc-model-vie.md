---
article_id: 360017512652
category: ADVPL - Classe e Função
content_hash: 3a50ce2014c63b1c711b65361c8f8d5abab9d17ed7952a9422224e598002fa93
fetched_at: '2026-06-28T22:40:15.589576+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como utilizar MVC
  (Model View Controller)
type: support-article
updated_at: '2021-12-07T14:35:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017512652-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-MVC-Model-View-Controller
---

**Dúvida**Como utilizar **MVC** (*Model View Controller*)em **ADVPL?****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**A arquitetura *MVC* possui três componentes básicos:

***Model o*****u modelo de dados:** representa as informações do domínio do aplicativo e fornece funções para operar os dados, isto é, ele contém as funcionalidades do aplicativo. Nele definimos as regras de negócio: tabelas, campos, estruturas, relacionamentos etc.. O modelo de dados *(Model)* também é responsável por notificar a *interface* (*View)* quando os dados forem alterados.

***View*** **ou** ***interface:*** responsável por renderizar o modelo de dados *(Model)* e possibilitar a interação do usuário, ou seja, é o responsável por exibir os dados.

***Controller***: responde às ações dos usuários, possibilita mudanças no Modelo de dados *(Model)* e seleciona a *View* correspondente.

![Screenshot_8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013091632/Screenshot_8.png)

**Principai****s funções da aplicação em** ***AdvPL*** **utilizando o** ***MVC***

***ModelDef***: Contem a construção e a definição do *Model*, lembrando que o Modelo de dados *(Model)* contém as regras de negócio;

***ViewDef***: Contem a construção e definição da View, ou seja, será a construção da *interface*;

***MenuDef***: Contem a definição das operações disponíveis para o modelo de dados *(Model)**.*

Cada fonte em *MVC* (PRW) só pode conter uma de cada dessas funções. Só pode ter uma ***ModelDef***, uma ***ViewDef*** e uma ***MenuDef***.

Ao se fazer uma aplicação em *AdvPL* utilizando *MVC*, automaticamente ao final, esta aplicação já terá disponível:

* · **Pontos de Entradas** já disponíveis;
* · Um ***Web*** ***Service*** para sua utilização;
* · **Importação ou exportação** mensagens XML.

Poderá ser utilizada, similarmente ao que é a rotina automática das aplicações sem *MVC**.*

**Saiba mais**[AdvPl utilizando MVC](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)  
[MVC (Model View Controller)](http://tdn.totvs.com.br/pages/viewpage.action?pageId=28574107)
