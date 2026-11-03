---
article_id: 16597326326039
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 5a82a99fc8a3bc22e6f95e8c3529ad4986751c40aecfac73017c1a13ee12a682
fetched_at: '2026-06-28T22:39:08.224303+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - EICA130 - Inclusão
  da rotina de Manutenção de Cadastro de NCM ( Clientes que não utilizam o módulo
  SIGAEIC )
type: support-article
updated_at: '2023-08-07T20:48:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16597326326039-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-EICA130-Inclus%C3%A3o-da-rotina-de-Manuten%C3%A7%C3%A3o-de-Cadastro-de-NCM-Clientes-que-n%C3%A3o-utilizam-o-m%C3%B3dulo-SIGAEIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16597320406423) Tempo aproximado para leitura: **00:06:12 min**

**Dúvida**Como adicionar a rotina de Manutenção de NCM (EICA130) se não tenho o módulo SIGAEIC?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

NCM significa "Nomenclatura Comum do Mercosul" e trata-se de um código de oito dígitos estabelecido pelo Governo Brasileiro para identificar a natureza das mercadorias e promover o desenvolvimento do comércio internacional, além de facilitar a coleta e análise das estatísticas do comércio exterior.

Este cadastro e amplamente utilizado por diversos produtos do Microsiga Protheus (ex. SIGAEIC, SIGACOM, SIGAFIS e etc.)

Os dados ficam armazenados na tabela SYD. A tabela SYD ao ser dropada / recriada, traz uma carga inicial de registros (facilitador de cadastro - Somente informações básicas). Se o cliente precisar adicionar novos registros e/ou atualizar os dados da tabela, mesmo não utilizando o modulo SIGAEIC deve seguir os passos abaixo.

1 - No **Configurador (SIGACFG)** acesse**Ambientes / Cadastro / Menu (CFGX013)**. Informe a opção de menu do que deseja efetuar a inclusão da rotina, exemplo: SIGAEST, SIGACOM...

**Obs:** No exemplo abaixo estaremos utilizando a SIGACOM.

**Menu:** SIGACOM.XNU

**Submenu:** Cadastros

**Nome da Rotina:** N.C.M.

**Programa:** MVC\_EICA130

**Módulo:** Compras

**Tipo:** Função Protheus

Imagem da Seleção do modulo

![](http://tdn.totvs.com/download/attachments/271157597/image2017-1-16%2016%3A25%3A32.png?version=1&modificationDate=1484591216000&api=v2)

Imagem da inclusão do cadastro de N.C.M

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16597349570327)

Caso seja o primeiro acesso ao cadastro de N.C.M (Tabela SYD) será realizada a carga inicial da tabela com a lista de código (imagem abaixo), mas vale ressaltar que a responsabilidade de manutenção/atualização do cadastro é do cliente.

**Observação:** Essa primeira carga só ocorrera no primeiro acesso a tabela (CRIAÇÃO), caso já tenha informação essa carga não irá acontecer.

Segue abaixo o exemplo do Browser da rotina:

![](http://tdn.totvs.com/download/attachments/271157597/image2017-1-16%2016%3A11%3A22.png?version=1&modificationDate=1484590437000&api=v2)

![(aviso)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/warning.png) **Importante**: Recentemente tivemos algumas alterações no cadastro de N.C.M, por isso recomendamos a consulta as entidades abaixo:

1. 1. **Problemas na Transmissão da NFE**  
      Caso esteja com problemas na transmissão da NFE, consulte o documento contido no link abaixo.  
      <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AyYR5yk6KUQ=>
   2. **Portal da Receita Federal, onde o Governo disponibiliza informações sobre as NCM´s**  
      <http://www.receita.fazenda.gov.br/publico/tipi/TIPI.doc>
   3. **Entrar em contato com o Serpro** (Serviço Federal de Processamento de Dados) e verificar se ele disponibiliza os dados de NCM´s para serem importados.   
      O Serpro é o órgão responsável pelo Siscomex (sistema do Governo para controle do comércio exterior no Brasil).  
      Portal do Serpro : <https://www.serpro.gov.br/>
   4. **Segunda Unidade de Medida -****TAG Utrib** de acordo com o NCM  
      <http://tdn.totvs.com/display/public/PROT/NFE0114_Segunda_unidade_de_medida_Ucom_Utrib_2016.001_817>

|  |  |
| --- | --- |
| **Observações:** | Caso no seu cadastro não contenha um código desejado ou esteja desatualizada a descrição, devera ser realiza a manutenção manualmente nas opções de "Alterar" ou "Incluir" |

***Observação sobre unidade de medida:***

A unidade de medida da carga padrão da tabela é numérico (11).  
Para as NCM's a serem atualizadas manualmente será necessário informar a unidade como UN, PC, KG 

**Possível atualização automática do cadastro de NCM para clientes que não possuem os módulos do SIGAEIC**

Temos uma ferramenta chamada Totvs Comex, conforme documento abaixo, porém será necessário entrar em contato com o seu ESN da Totvs para obter mais informações sobre essa ferramenta.

<https://tdn.totvs.com/pages/releaseview.action?pageId=224119853>

***Saiba Mais :***

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
