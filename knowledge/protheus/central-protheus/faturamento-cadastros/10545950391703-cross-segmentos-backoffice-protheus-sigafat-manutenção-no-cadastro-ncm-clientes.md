---
article_id: 10545950391703
category: Faturamento - Cadastros
content_hash: c1e4a8a39498a94fdce332ba1ad6ff8be5870da1c2c08c693fef373896c34f7c
fetched_at: '2026-06-28T22:38:36.803897+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Manutenção no Cadastro NCM  (Clientes
  que não utilizam o módulo SIGAEIC)
type: support-article
updated_at: '2022-12-01T13:07:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10545950391703-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Manuten%C3%A7%C3%A3o-no-Cadastro-NCM-Clientes-que-n%C3%A3o-utilizam-o-m%C3%B3dulo-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como efetuar a Manutenção no cadastro NCM (Clientes que não utilizam o SIGAEIC) ?

**Ambiente**Protheus – Faturamento – A partir da versão 11.80

**Solução**

NCM significa "Nomenclatura Comum do Mercosul" e trata-se de um código de oito dígitos estabelecido pelo Governo Brasileiro para identificar a natureza das mercadorias e promover o desenvolvimento do comércio internacional, além de facilitar a coleta e análise das estatísticas do comércio exterior.

Este cadastro e amplamente utilizado por diversos produtos do Microsiga Protheus (ex. SIGAEIC, SIGACOM, SIGAFIS, SIGAFAT etc.)

Os dados ficam armazenados na tabela SYD. A tabela SYD ao ser dropada/recriada, traz uma carga inicial de registros (facilitador de cadastro - Somente informações básicas). Se o cliente precisar adicionar novos registros e/ou atualizar os dados da tabela, mesmo não utilizando o modulo SIGAEIC deve seguir os passos abaixo.

1 - No **Configurador (SIGACFG)** acesse**Ambientes / Cadastro / Menu (CFGX013)**. Informe a opção de menu do que deseja efetuar a inclusão da rotina, exemplo: SIGAEST, SIGAFAT..

**Obs:** No exemplo abaixo estaremos utilizando a SIGACOM.

**Menu:** SIGAFAT.XNU

**Submenu:** Cadastros

**Nome da Rotina:** N.C.M.

**Programa:**MVC\_EICA130

**Módulo:** Faturamento

**Tipo:** Função Protheus

Imagem da inclusão do cadastro de N.C.M

![faturamento.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10545870232599)

Caso seja o primeiro acesso ao cadastro de N.C.M (Tabela SYD) será realizada a carga inicial da tabela com a lista de código (imagem abaixo), mas vale ressaltar que a responsabilidade de manutenção/atualização do cadastro é do cliente.

**Observação:** Essa primeira carga só ocorrera no primeiro acesso a tabela (CRIAÇÃO), caso já tenha informação essa carga não irá acontecer.

Segue abaixo o exemplo do Browser da rotina:

![](http://tdn.totvs.com/download/attachments/271157597/image2017-1-16%2016%3A11%3A22.png?version=1&modificationDate=1484590437000&api=v2)

![(aviso)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/warning.png) **IMPORTANTE**: Recentemente tivemos algumas alterações no cadastro de N.C.M, por isso recomendamos a consulta as entidades abaixo:

* **Problemas na Transmissão da NFE**  
  Caso esteja com problemas na transmissão da NFE, consulte o documento contido no link abaixo.  
  <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AyYR5yk6KUQ=>
* **Portal da Receita Federal, onde o Governo disponibiliza informações sobre as NCM´s**  
  <http://www.receita.fazenda.gov.br/publico/tipi/TIPI.doc>
* **Entrar em contato com o Serpro** (Serviço Federal de Processamento de Dados) e verificar se ele disponibiliza os dados de NCM´s para serem importados.   
  O Serpro é o órgão responsável pelo Siscomex (sistema do Governo para controle do comércio exterior no Brasil).  
  Portal do Serpro : <https://www.serpro.gov.br/>
* **Segunda Unidade de Medida -****TAG Utrib** de acordo com o NCM  
  <http://tdn.totvs.com/display/public/PROT/NFE0114_Segunda_unidade_de_medida_Ucom_Utrib_2016.001_817>

**OBS 1:** Caso no seu cadastro não contenha um código desejado ou esteja desatualizada a descrição, devera ser realiza a manutenção manualmente nas opções de "Alterar" ou "Incluir"

**OBS 2:** A unidade de medida da carga padrão da tabela é numérico (11).  
Para as NCM's a serem atualizadas manualmente será necessário informar a unidade como UN, PC, KG 

**OBS 3: Possível atualização automática do cadastro de NCM para clientes que não possuem os módulos do SIGAEIC:**

Temos uma ferramenta chamada Totvs Comex, conforme documento abaixo, porém será necessário entrar em contato com o seu ESN da Totvs para obter mais informações sobre essa ferramenta.

<https://tdn.totvs.com/pages/releaseview.action?pageId=224119853>
