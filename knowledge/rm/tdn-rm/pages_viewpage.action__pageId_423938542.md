---
content_hash: 82f287f7c865f9b96b7f49bc1534c7151fbe43db5496bfee479b626a56a63854
fetched_at: '2026-06-29T00:09:27.551625+00:00'
page_id: '423938542'
product: rm
source: tdn-rm
title: Criação de Estruturas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938542
version: 2
---

Estruturas são como esboços dos lançamentos periódicos. Elas serão criadas uma única vez, embora possam ser alteradas a qualquer tempo. Em uma estrutura haverá as informações que comporão dos lançamentos periódicos.  
Crie uma estrutura para cada tipo de lançamento. A Descrição informada para a estrutura será a mesma usada para a descrição do lançamento contábil gerado por esta estrutura.

A informação do lote contábil, indicando onde o lançamento a ser gerado por esta estrutura será incluído não é obrigatória, pois no momento da geração automática dos lançamentos será solicitado, caso não tenha sido informado na estrutura.

A data para o lançamento contábil gerado por esta estrutura poderá ser definida de 4 maneiras. Na geração automática dos lançamentos, o tipo de data aqui selecionado será sugerido como data para o lançamento, podendo ser alterada conforme desejado.

**Fixar Data:**   
Na própria estrutura deverá ser informada uma data fixa que será sugerida como data para os lançamentos gerados por esta estrutura.

**Variável de Data:**   
A data para os lançamentos gerados por esta estrutura será solicitada no momento da geração automática dos lançamentos.

**Data do Dia:**   
A data do dia em que os lançamentos estiverem sendo gerados por esta estrutura, será sugerida como data para os lançamentos.

**Compor Data (DIA/MÊS/ANO):** Este tipo de data permite criar estruturas que possibilitam uma maior flexibilização para a data dos lançamentos que serão gerados, pois permite que na estrutura o preenchimento do DIA, do MÊS e do ANO que irão compor a data dos lançamentos sejam independentes. Os campos correspondentes respectivamente ao DIA/MÊS/ANO que não forem informados ficarão preenchidos com 0 (zero). Isto indica ao sistema que estes campos zerados serão preenchidos com informações da data de execução do processo de Geração de Lançamentos Periódicos.

**Exemplo:** Estrutura parametrizada com DIA=5, MÊS=0 e ANO=0 No dia 30/10/2011, por exemplo, execute o processo de geração de lançamentos para esta estrutura. O lançamento gerado por esta estrutura receberá a data = 05/10/2011, sendo o DIA 05 igual ao dia informado na estrutura e o MÊS/ANO igual ao mês/ano da execução do processo.

**OBS:** Este tipo de parametrização é muito utilizado quando se deseja **Agendar** a execução do processo de Geração de Lançamentos Periódicos, criando recorrências ou repetições para os mesmos.
