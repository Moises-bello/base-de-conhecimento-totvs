---
content_hash: 29d6a2d748ed72fa9a33273510f8864689f7e49320576d6a212bf845de8b5da6
fetched_at: '2026-06-29T00:08:32.415663+00:00'
page_id: '273985377'
product: rm
source: tdn-rm
title: DT Relatório RM Reports Para o Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273985377
version: 3
---

# RELATÓRIO RM REPORTS PARA O PORTAL

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | **Folha de Pagamento** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Envelope de Pagamento Portal* | *Envelope de Pagamento Portal* | | | |
| **Chamado/Ticket:** | [FOPROTINAS01-75](http://jiraproducao.totvs.com.br/browse/FOPROTINAS01-75) | | |
| **Requisito/Story/Issue:** | [FOPCALCULO01-48](http://jiraproducao.totvs.com.br/browse/FOPCALCULO01-48 "View this issue in JIRA") | | |
| **País:** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Informações Iniciais

Foram criados relatórios no RM Reports para serem utilizados como envelope de pagamento no Portal RH, com o intuito de ser possível de personalizar as informações que deseja adicionar ao envelope do portal.

Com isso, criamos 3 relatórios, sendo eles:

**FOPREL00176 - Envelope Pgto Portal Padrão - Onde não é possível de se aplicar Filtros (Para eventos do tipo B, Base de Cálculo, no envelope de pagamento aparecerá a referencia como "BASE", e não mostrará valores.**

**FOPREL00177 - Envelope Pgto Portal Personalizado ORACLE - Onde é possível filtrar os eventos, ou algum outro dado, através da edição das sentenças SQLs devidas, esse funcionando apenas em bases ORACLE.**

**FOPREL00178 - Envelope Pgto Portal Personalizado SQL - Onde é possível filtrar os eventos, ou algum outro dado, através da edição das sentenças SQLs devidas, esse funcionando apenas em bases SQL.**

# Importar Layout

Para importar o layout desejado, siga os passos abaixo;

Acesse em **RH | Folha de Pagamento | Gestão | RM Reports**:

Clique em Processos e depois Importar Estrutura de Relatório e localize o relatório desejado.

Os Relatórios se encontram em: ...\CorporeRM\ObjetosGerenciais\Relatórios

# Parametrizar o Portal

Para parametrizar o portal corretamente, de modo que ele gere o relatório que foi importado, acesse;

**RH | Folha de Pagamento | Configurações | Parametrizador**

Marque o 06.05 - RM Portal e avance

Selecione o grupo e clique em Parametrizar;

Marque os flags **Gera Envelope via Gerador de Relatórios** e **Relatórios do RM Reports**. Após feito isso, selecione o relatório, avance e confirme as mudanças;

# Gerar o Relatório no Portal

Após isso, basta entrar no portal, acessar **Folha de Pagamento | Envelope Pgto**, e selecionar o Mês e Ano que deseja gerar o relatório.

As informações do Envelope virão conforme os dados estavam no mês e ano selecionado do usuário logado no portal;

# Personalizar o Relatório

Para isso, basta ir em**RH | Folha de Pagamento | Gestão | RM Reports**, selecione o relatório, clique em **Processos | Editar Estrutura**;

Após isso, moderá fazer a modificação que desejar.

Se o relatório for do tipo Personalizado (FOPREL00177 e FOPREL00178), você pode aplicar filtros através das sentenças SQL, para isso clique em Editar Sentença, e selecione onde quer aplicar;

# Criar Novas Consultas

Para criar novas consultas para o relatório, ou utilizar um relatório do tipo “Genérico” no Envelope de Pagamento do portal, é necessário que ele atenda as seguintes condições:

* Ao criar um novo relatório genérico, adicione os seguintes parâmetros do tipo “sequência de caracteres” (a nomenclatura é importante):
  + CHAPA
  + CODCOLIGADA
  + NROPERIODO
  + MESCOMP
  + ANOCOMP

Utilize os parâmetros em consultas SQL para buscar as informações pertinentes ao envelope de pagamento:

Em seguida basta adicionar os campos da consulta SQL ao relatório conforme desejado
