---
content_hash: 9542bd3eee523b69458d23df90b733c0a453d672cf68b36185a97d5458b2480c
fetched_at: '2026-06-29T00:11:45.088702+00:00'
page_id: '819495410'
product: rm
source: tdn-rm
title: Plano de Manutenção - TCOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819495410
version: 5
---

Os Planos de Manutenção são conjuntos de serviços e produtos a serem executados e aplicados periodicamente a uma unidade ou a um grupo de Objetos de Manutenção do mesmo tipo. Através  
do Plano de Manutenção é possível Planejar e controlar a execução da manutenção periódica. Estes devem ser executados em intervalos que variam em função dos Indicadores de Uso Cadastrados no  
Tipo de Objeto de Manutenção. É possível que Objetos de Manutenção pertencentes ao mesmo grupo (Tipo, Modelo e Submodelo) façam parte de Planos de Manutenção diferentes. O vencimento dos Planos de Manutenção poderá ser por marco ou cíclico em função do indicador de uso. E o vencimento será calculado em função da média atual do indicador de uso do Objeto de Manutenção. Para cadastrar um plano de manutenção acesse o menu Tabelas  / Manutenção / Plano de Manutenção.

**Identificação**  
Informe o Tipo de Objeto, Modelo e Submodelo do grupo de Objetos de Manutenção que o plano se aplica.

* Se segmentado apenas para um Tipo de Objeto o plano se aplica a todos os Modelos e Submodelos do Tipo.
* Se segmentado para um Tipo de Objeto e Modelo o plano de aplica a todos os Submodelos do modelo.
* Se segmentado para um Tipo de Objeto, Modelo e Submodelo o plano se aplica somente ao grupo de objetos determinados.

**Tipo de Execucão:**

**Marco: Plano de Manutenção baseado em Marco**

O Plano de Manutenção por Marco é acionado quando o Objeto de Manutenção atinge ou ultrapassa o valor do indicador de uso especificado no plano.

**Exemplo:**

* **Plano:** Troca da Correia Dentada
* **Frequência de Quilometragem:** 10.000 km

Se, ao iniciar o Plano de Manutenção por "Marco", o indicador de uso do Objeto de Manutenção for registrado como 0 km, a próxima execução do plano ocorrerá aos 10.000 km, com uma quilometragem remanescente de 10.000 km.

Caso o indicador de uso seja inserido como 1.000 km, a próxima execução ocorrerá aos 10.000 km, com uma quilometragem remanescente de 9.000 km.

**Cíclico: Plano de Manutenção Cíclico**

O Plano de Manutenção por Cíclico é executado quando o Objeto de Manutenção ultrapassa o valor do Indicador de Uso estabelecido no plano.

**Exemplo:**

* **Plano:** Troca da Correia Dentada
* **Frequência de Quilometragem:** 10.000 km

Se, ao iniciar o Plano de Manutenção Cíclico, o indicador de uso do Objeto de Manutenção for registrado como 0 km, a próxima execução ocorrerá aos 10.000 km, com uma quilometragem remanescente de 10.000 km.

Se o indicador de uso for inserido como 1.000 km, a próxima execução ocorrerá aos 11.000 km, com uma quilometragem remanescente de 10.000 km.

**Anexo – Itens do Plano de Manutenção**  
São os Produtos e serviços e que irão compor a ordem de serviço para a execução do Plano de Manutenção.

Para associar um produto através do anexo de Itens do plano de manutenção, é necessário ativar a opção "Disponível para Manutenção/Locação" na tela de configuração do produto, que faz parte do módulo de Gestão de Estoque, Compras e Faturamento. No entanto, essa opção só estará disponível após a conclusão bem-sucedida da integração entre o módulo Obras e Projetos e o módulo de Gestão de Estoque. Para mais informações sobre como realizar esta integração Clique aqui.

**Anexo – Inicialização de Plano de Manutenção**  
Após compor o plano é necessário iniciá-lo para cada objeto de manutenção contemplado pelo mesmo. Isto significa incluir o objeto no plano informando qual a última vez que o mesmo realizou o plano e qual era o indicador de uso. A partir desta informação o sistema passa a gerar as informações necessárias ao gerenciamento do plano para o referido objeto.

**Processos – Cópia de Planos de Manutenção**  
Permite criar cópias dos Planos de Manutenção selecionados. Para fazê-lo, selecione o(s) plano(s) que deseja copiar, e defina o Tipo de Objeto, Modelo e SubModelo que a cópia do(s) plano(s) terá(ao). Os planos copiados terão os mesmos itens do(s) plano(s) selecionado(s) para fazer(em) a(s) cópia(s).

**Processos – Inclusão de Vários Itens**

Esta funcionalidade permite ao usuário incluir vários itens ao Plano de Manutenção de uma única vez.  
Para acessar essa funcionalidade o usuário terá que clicar em Processos | Inclusão de Vários Itens e selecionar os itens que deseja incluir ao Plano de Manutenção.
