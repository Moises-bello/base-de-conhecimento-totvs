---
article_id: 360028448132
category: Portal de Gestão de Capital Humano
content_hash: f2e221ad4fe8fb20aabd3d303dce604f114970ea1de8afed8ee5083188d78a36
fetched_at: '2026-06-28T22:42:59.081221+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Ao consultar a tabela horário padrão no
  portal apresenta a mensagem GetScheduleChart - Funcionário sem tabela de horário
  cadastrada
type: support-article
updated_at: '2021-04-07T12:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028448132-RH-Linha-Protheus-PORTAL-GCH-Ao-consultar-a-tabela-hor%C3%A1rio-padr%C3%A3o-no-portal-apresenta-a-mensagem-GetScheduleChart-Funcion%C3%A1rio-sem-tabela-de-hor%C3%A1rio-cadastrada
---

**Dúvida**Ao acessar o Portal Gestão Capital Humano, na opção Consulta > Tabela de Horário padrão, apresenta a mensagem **GetScheduleChart**. **Funcionário sem tabela de horário cadastrada**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**1- Verifique se o compartilhamento das tabelas SPJ e SR6 estão iguais. Caso exista alguma diferença deverá ser ajustada via configurador, com os devidos backups.

**Importante:**  
Sempre que for alterado o modo de compartilhamento de uma tabela deve ser atualizado o campo de filial na base de dados conforme orientação abaixo:  
Tabela Exclusiva --> Passa a ser Compartilhada --> Todos os registros da tabela deverão ficar com o campo filial em branco (deve ser observado se vai duplicar o registro ao fazer esta mudança).  
  
Tabela Compartilhada --> Passa a ser Exclusiva --> Todos os registros da tabela deverão ficar com o campo filial preenchido.  
  
2- Avalie o compartilhamento da tabela SPO se esta compatível com o campo filial dos parâmetros MV\_PONMES e MV\_PAPONTA.

Seguindo a regra abaixo:  
A tabela SPO deve ser Compartilhada (C C C) ou Exclusiva (E E E), não podendo ter compartilhamento diferente de um desses dois.  
  
Se a SPO for Compartilhada (C C C), no cadastro de parâmetros através do configurador (ambiente > cadastro > parâmetros) deverá ter apenas um parâmetro **MV\_PAPONTA** e um **MV\_PONMES** com filial em branco.  
  
Porém, se a SPO for Exclusiva (E E E), no cadastro de parâmetros através do configurador (ambiente > cadastro > parâmetros) deverá ter **um** parâmetro (MV\_PAPONTA e MV\_PONMES) para cada filial, sendo necessário preencher o campo filial.

3- Avalie se existe registro para a matricula na rotina troca de turno (tabela SPF).

Realizando a conferencia acima o erro é sanado, sendo possível realizar a consulta da tabela de horário padrão no portal.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029250571/mceclip0.png)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
