---
content_hash: 1c88696ebde08be48e407b82c241ee35fd97b2460915a12a99cdbe78881d18a1
fetched_at: '2026-06-29T00:06:10.663811+00:00'
page_id: '203765976'
product: rm
source: tdn-rm
title: ER_PCREC-5243_upgrade_importar_precos_suprimentos_faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREC-5243_upgrade_importar_precos_suprimentos_faturamento
version: 61
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Obras e Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-5242 |
| **Requisito1** | PCREQ-5243 | **Subtarefa1** | PDR\_CP\_TOP008-50 |
| **Chamado2** | - | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Permitir a importação de preços/custos do suprimento/faturamento para o produto principal dos insumos.

## Definição da Regra de Negócio

 

1. A importação de preços do suprimento/faturamento será feita através do processo disponível na visão principal de insumos   
   "**Importar Preços de Suprimento/Faturamento**", conforme ***protótipo 01***.
2. Ao selecionar um preço no campo “Opções de Valores Habilitados”, o TOP irá recuperar o produto principal associado ao insumo   
   e buscará seu valor cadastrado no Suprimento/Faturamento, conforme parametrizado.

## Tela do Processo

O processo terá as seguintes opções: 

1. Opções de Valores Habilitados:
   1. Os preços a serem exibidos serão conforme parametrizados no Suprimentos/Faturamento.  
      Os preços serão exibidos se estiverem habilitados, e a descrição será conforme estiver parametrizada.
   2. Ex.:   
      * Preço à Vista;
      * Preço à Prazo;
      * Preço em Promoção;
      * Preço em Dólar;
      * Preço em Oferta;
      * Custo Unitário;
      * Custo Médio;
   3. As opções Custo Unitário e Custo Médio são fixas.
   4. Caso seja selecionada uma das opções 'Custo Unitário' ou 'Custo Médio', a opção 2 será habilitada;
2. Filial e/ou Local de Estoque:
   * Esta opção será habilita se o 'Custo Unitário' ou 'Custo Médio' (da opção 1), for selecionado.
   * Se estiver parametrizado como Filial, apenas a opção de Filial será habilitada;
     + Por padrão o processo irá sugerir a Filial do Projeto na opção de Filial, porém será possível editar;
   * Se estiver parametrizado como Local de Estoque, a opção Local de Estoque será habilitada;
   * Se o processo for executado, sem nenhum valor informado, será retornado o custo referentes ao produto;
3. Opções de Conversão dos Preços:  
   * Converter preço para moeda do projeto sem manter a indexação:
     + O TOP irá gerar o preço convertendo para a moeda do projeto, e setar a moeda indexadora  igual  a do projeto;
   * Converter preço para moeda do projeto e manter a indexação:
     + O TOP irá gerar o preço convertendo para a moeda do projeto, e setar a moeda indexadora  igual  a de origem;
   * Manter moeda do preço:
     + O TOP irá gerar o preço sem converter para a moeda do projeto, mantendo a moeda de origem;
4. Descrição do Preço Importado:
   1. A descrição por padrão será conforme layout abaixo, porém poderá ser editada conforme necessidade;
   2. A descrição obedecerá o layout: "descrição da opção 1 selecionada" de Suprimentos/Faturamento em "data atual";
      1. Ex.: Preço à Vista Importado de Suprimentos/Faturamento em 07/10/2015;
5. Sobrepor preço com a mesma descrição;
   1. Por padrão esta opção irá aparecer marcada;
6. Ativar preço importado;
   1. Por padrão esta opção irá aparecer marcada
   2. O preço selecionado irá substituir o preço ativo no TOP.
7. Utilizar tabelas de preço;
   1. Por padrão esta opção irá aparecer desmarcada;
   2. Caso esta opção seja marcada, será exibido o próximo passo, com:
      1. O Cronograma de aplicação da vigência.  
         (O cálculo do cronograma do TOP utilizará o preço de acordo com os cronogramas selecionados);
      2. As tabelas de prioridade de consulta das tabelas de preços.   
         (Um produto pode estar associado a mais de uma tabela na mesma vigência,   
         sendo necessário definir uma prioridade no movimento para determinar o preço a ser utilizado);  
         As tabelas de preços têm como principal objetivo proporcionar ao usuário uma flexibilidade no preço do produto através de suas variáveis:  
         Filial, Condição de Pagamento, Município ou Estado. É permitido utilizar várias tabelas de preços em cada produto, sendo suas atualizações   
         baseadas em critérios pré-definidos conforme parametrização; O Suprimento/Faturamento possui tabelas de preço associadas a mais de um   
         produto e um produto pode estar associado a mais de uma tabela, possibilitando maior diversificação de preços.   
         Um produto pode estar associado a mais de uma tabela na mesma vigência, sendo   
         necessário definir uma prioridade no movimento para determinar o preço a ser utilizado;
      3. Quando selecionada a opção “Utilizar tabelas de preço” não será possível sobrescrever preço pela descrição, pois o TOP poderá  
         inserir vários preços com a mesma descrição, de acordo com as vigências dos produtos cadastrados nas tabelas de preço;

* Parâmetros:
  + Se o parâmetro de projeto Vigência de Preço, estiver como 'Não utiliza', a opção 7 'Utilizar tabelas de preço' será desabilitada;
  + Se o parâmetro de projeto Vigência de Preço, estiver marcada a opção 'Aplicar preços em percentual',   
    os preços já existentes do insumo, poderão ser recalculados.
  + Acesso: Parâmetros de Projeto (F6) >> Cálculo >> BDI >> Vigência de preço
* Integração:
  + O processo é compatível com a integração TOP x Protheus, uma vez que a integração já atualiza as entidades utilizadas por este processo.

 

 

## Protótipo de Tela

**Protótipo 01 - Processo Importar Preços de Suprimentos/Faturamento**

**Protótipo 02 - Passo 01 e Passo 02**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
