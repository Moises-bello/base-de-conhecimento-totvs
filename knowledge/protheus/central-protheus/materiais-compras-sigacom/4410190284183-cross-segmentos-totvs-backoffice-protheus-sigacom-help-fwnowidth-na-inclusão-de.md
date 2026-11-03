---
article_id: 4410190284183
category: Materiais - Compras (SIGACOM)
content_hash: 0dd23bcdf81e44127d88831572f25947084976b9e58c4a278a4b6b2745e0a294
fetched_at: '2026-06-28T22:41:12.933129+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - HELP FWNOWIDTH na
  inclusão de Cadastro de Grupo de Compras ( COMA086 )
type: support-article
updated_at: '2024-08-29T13:21:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410190284183-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-FWNOWIDTH-na-inclus%C3%A3o-de-Cadastro-de-Grupo-de-Compras-COMA086
---

**Ocorrência**

Ao realizar a inclusão de um Cadastro de Grupo de Compras ( COMA086 ) ocorre o Help "FWNOWIDTH Valor atribuído difere do tamanho do campo (Usuário)"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410195899287)  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Causa**O help é disparado quando há diferença entre tamanho de campos utilizados na rotina e a tentativa de inserção de uma informação em um campo, sendo que essa informação tem um tamanho maior do que o tamanho do campo comporta.  
  
**Solução**Foi necessário a realização de uma modelagem de dados na tabela **SAJ,**habilitando a edição de tamanho do campo **AJ\_US2NAME.**

E neste caso, se necessário, deve-se ajustar os campos abaixo conforme cada cadastro utilizado, no CFG para o maior tamanho de uso no sistema (**40**), de acordo com o tamanho do campo de "nome completo" (USR\_NOME) do cadastro de Usuários que possui **Tamanho 40**:

AJ\_US2NAME (Cadastro Grupo Compras)

AI\_USRNAME (Cadastro Solicitantes)

Y1\_NOME (Cadastro Compradores)

***Obs:***

Quanto a alteração/aumento do tamanho dos campos, orienta-se a checagem se o aumento do campo  realizado foi efetivado tanto no Dicionário de Dados do Protheus quanto também no Banco de Dados.

***Saiba Mais :***

[6735236 DMANMAT02-21090 DT Help FWNOWIDTH no grupo de compras](https://tdn.totvs.com/x/xaKpHg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035929453)
