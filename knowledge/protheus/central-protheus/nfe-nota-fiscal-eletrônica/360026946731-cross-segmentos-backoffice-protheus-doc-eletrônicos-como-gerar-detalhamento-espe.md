---
article_id: 360026946731
category: NFe - Nota Fiscal Eletrônica
content_hash: 6678dba18688223d2b70782680415133c475a0b585c72d8a3a3823d9c27be2a2
fetched_at: '2026-06-28T22:39:59.952330+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar Detalhamento
  Específico de Veículos novos no XML'
type: support-article
updated_at: '2022-05-04T20:29:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026946731--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-Detalhamento-Espec%C3%ADfico-de-Ve%C3%ADculos-novos-no-XML
---

**Dúvida**

Como gerar Detalhamento Específico de Veículos novos no XML ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **editar.** Preencher o parâmetro ***MV\_VEICNV no configurador o parâmetro*** com o grupo de produto de ***Veículos novos:***

**![MV_VEICNV.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414750781719/MV_VEICNV.gif)**

2. Preencher no cadastro de produto no campo ***Grupo "B1\_GRUPO"***  informado no parâmetro ***MV\_VEICNV.***

![B1_GRUPO.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414751382295/B1_GRUPO.gif)

3. Acesse a rotina de ***Livros Fiscais -> Atualizações -> Movimentos -> NF-e Manual de Entrada / Saída > Complementos.***

![20220504_172710.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5876577236119/20220504_172710.gif)

4. Selecione opção ***Veículos automotores.***

![veiculo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414744947607/veiculo.gif)

5. Preencher no ***complemento de veículo os campos abaixo:***

***![20211202_112902.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414758194967/20211202_112902.gif)***

***CD9\_TPOPER, CD9\_CHASSI, CD9\_CODCOR, CD9\_DSCCOR, CD9\_POTENC, CD9\_CM3POT, CD9\_PESOLI, CD9\_CODCOR, CD9\_DSCCOR, CD9\_POTENC, CD9\_CM3POT, CD9\_PESOLI, CD9\_PESOBR, CD9\_SERIAL, CD9\_TPCOMB, CD9\_NMOTOR, CD9\_CMKG, CD9\_DISTEI, CD9\_RENAVA, CD9\_ANOMOD, CD9\_ANOFAB, CD9\_TPPINT, CD9\_TPVEIC, CD9\_ESPVEI, CD9\_CONVIN, CD9\_CONVEI, CD9\_CODMOD***

* **Saiba mais:**

![20211202_112159.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414758109975/20211202_112159.gif)

***2=**Faturamento direto para consumidor final  
**3=**Venda direta para grandes consumidores (frotista, governo, ...)  
**0=**Outros*

* Tipo Oper. "CD9\_TPOPER" = ***03 para gerar tpOp = 1***
* Tipo Oper. "CD9\_TPOPER" = ***1 para gerar tpOp = 2***
* Tipo Oper. "CD9\_TPOPER" = ***2 para gerar tpOp = 3***
* Tipo Oper. "CD9\_TPOPER" = ***9 para gerar tpOp = 0***

* ***Exemplo do XML:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026296032/mceclip0.png)
