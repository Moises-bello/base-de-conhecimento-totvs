---
article_id: 360026986932
category: ADVPL - Classe e Função
content_hash: a9db87bb0bd66cffbdbdb7fb1d7993bde046b4ef02a8a5207d984933a1d61f40
fetched_at: '2026-06-28T22:40:14.334545+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Acesso aos submodelos
  disponíveis em uma rotina MVC
type: support-article
updated_at: '2022-01-03T20:45:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026986932-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Acesso-aos-submodelos-dispon%C3%ADveis-em-uma-rotina-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Estou implementando um ponto de entrada MVC na rotina de liquidação do contas a receber, porém preciso saber o nome dos modelos de dados envolvidos para fazer algumas validações.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Os submodelos disponíveis em uma rotina MVC podem ser consultados através da propriedade **ADEPENDENCY**, esta propriedade armazena em um array todos os seus submodelos.  
No ponto de entrada padrão MVC, é possível instanciar o objeto do modelo ativo através do método [FwModelActive](http://tdn.totvs.com/display/framework/FWModelActive), neste objeto estará contida a propriedade conforme exemplo a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026790612/mceclip0.png)

Utilizando como exemplo o ponto de entrada MVC da rotina **FINA460**, atribuímos a um objeto o modelo ativo retornado pela [FwModelActive](http://tdn.totvs.com/display/framework/FWModelActive), no caso este objeto, que está sendo avaliado pelo 'Expressões', temos o array na propriedade **ADEPENDENCY**acima. Portanto, no caso da rotina **FINA460**, os submodelos disponíveis são "MASTERFO0", "TITSELFO1" e "TITSELFO1".

**Saiba mais**[AdvPl utilizando MVC Página não encontrada](http://tdn.totvs.com/display/PROT/AdvPl+utilizando+MVC)  
[DT\_FINA460A\_Ponto\_Entrada\_Principal](http://tdn.totvs.com/display/PROT/DT_FINA460A_Ponto_Entrada_Principal)
