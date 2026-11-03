---
content_hash: 10232d3334dfcc13d652d15c883836ec5be18226e83b45ed2c71982fc26a8789
fetched_at: '2026-06-29T00:09:58.321608+00:00'
page_id: '452690269'
product: rm
source: tdn-rm
title: Integração com base ORCECERTO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452690269
version: 19
---

---

Ao lidar com uma obra é preciso buscar formas de conectar o que acontece em campo ao escritório, controlando a distribuição de tarefas, prazos, orçamentos e a evolução das etapas de construção para que ela seja entregue dentro dos custos e prazos esperados.

Neste contexto, a integração da base ORCECERTO com o ERP TOTVS Obras e Projetos é uma evolução que trouxe lucratividade e otimização do desempenho para empresas. A ORCECERTO é uma empresa 100% focada em Engenharia de Custos e possui Praças onde permite que o usuário tenha acesso a preços médios atualizados de insumos, captados nas 27 capitais brasileiras, para garantir orçamentos mais precisos em qualquer região do País.

A **ORCECERTO** fornece 3 conjuntos de Bases para Composições, Insumos e Preços. São elas: BASE **ORCECERTO**, BASE **SINAPI** e BASE **SICRO**.

* **ORCECERTO -** É a mais completa base para Edificações do mercado e conta com equipe especializada para atualizações constantes. A solução possibilita a realização de orçamentos mais eficientes de forma rápida, utilizando as bases de referências da Tabela de Composição ORCECERTO.
* **SICRO -**  É a base para obras de infraestrutura (SICRO é a sigla de Sistema de Custos Referenciais de Obras), criado pelo Departamento Nacional de Infraestrutura de Transportes (DNIT), que em sua essência são insumos e composições usadas como referência para obras de infraestrutura de transportes, porém pode ser utilizada em qualquer obra, pública ou privada, de infraestrutura.
* **SINAPI -** É a base voltada para edificações financiadas pela Caixa Econômica Federal (CEF). Através do serviço ORCECERTO você receberá de forma simples e rápida todos os dados desta base, além das opções para escolha do período referência de Importação, atualização de preços, composições, insumos e recursos.

A integração com a ORCECERTO agiliza o processo de importação destas informações, levando mais agilidade e facilidade ao escolher o período de referência (Mês / Ano) desejado e o que se deseja importar, poupando tempo e recursos para tratar estas informações antes de importa-las.

* **Relação Natureza ORCECERTO x Grupo de Custo:** Associação das naturezas dos recursos da base ORCECERTO com os Grupos de Custo do projeto. Ao realizar a importação dos recursos, eles serão associados aos grupos de custo correspondentes.

* **Insumos**
  + **Importar Insumos:**Realiza a importação dos insumos de acordo com a Versão e a Praça escolhida.
  + **Atualizar Código do Insumo:** Caso o usuário já tenha feito alguma importação de insumo, essa opção atualiza o código dos insumos que sofreram alteração para os códigos originais de acordo com a Versão e a Praça escolhida.
  + **Atualizar descrição:**Caso o usuário já tenha feito alguma importação de insumo, essa opção atualiza a descrição dos insumos que sofreram alteração para as descrições originais de acordo com a Versão e a Praça escolhida.
  + **Atualizar unidade:**Caso o usuário já tenha feito alguma importação de insumo, essa opção atualiza a unidade dos insumos que sofreram alteração para as unidades originais de acordo com a Versão e a Praça escolhida.
  + **Atualizar Grupo de Custo:**Caso o usuário já tenha feito alguma importação de insumo, essa opção atualiza o grupo de custo dos insumos que sofreram alteração para os grupos de custo originais de acordo com a Versão e a Praça escolhida.

* **Preços**
  + **Importar preços:**Realiza a importação de preços de acordo com a Versão e a Praça escolhida.
  + **Ativar preço importado:**Após realizar a importação de preços, os preços serão ativados automaticamente.
  + **Calcular preços dos insumos:**Após realizar a importação de preços, os insumos serão calculados automaticamente.
  + **Importar preço desonerado:** “A base ORCECERTO publica as composições unitárias de custo sem encargos sociais,  
     Pode-se colocar os encargos que desejar, sendo os que o Sinapi Publica ou a ORCECERTO ou os próprios encargos calculados pela empresa ou seja se são onerados ou não é prerrogativa do usuário”.

**Obs:** Somente para a base ORCECERTO não esta disponível esta opção "Importar preço desonerado".

* **Utilizar código ORCECERTO da Integração:**Ao realizar a importação, os recursos importados serão importados com códigos da base ORCECERTO independente da máscara do projeto.

* **Composições**
  + **Importar Composições:**Realiza a importação de preços de acordo com a Versão e a Praça escolhida.
  + **Código ORCECERTO como Código Composições:**As composições importadas pelo processo serão importadas com códigos da base ORCECERTO independente da máscara do projeto.
  + **Atualizar descrição:**Caso o usuário já tenha feito alguma importação de composição, essa opção atualiza a descrição das composições que sofreram alteração para as descrições originais de acordo com a Versão e a Praça escolhida.
  + **Atualizar unidade:**Caso o usuário já tenha feito alguma importação de composição, essa opção atualiza a unidade das composições que sofreram alteração para as unidades originais de acordo com a Versão e a Praça escolhida.

* **Importar Recursos:**Realiza a importação dos recursos e recursos vinculados da composição.
* **Recalcular o projeto:**Após executar o processo de importação, o projeto é recalculado.
