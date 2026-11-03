---
content_hash: 435eca9ffcb360875f1e82c7f3a574624b9cb311cf2d3b7e88259675f165d768
fetched_at: '2026-06-29T00:09:46.412263+00:00'
page_id: '435104778'
product: rm
source: tdn-rm
title: Área do Imóvel - Anexo - Histórico de Locação de Área
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104778
version: 3
---

Nesta tela (Anexo de Área do Imóvel) será exibido o histórico de alterações da Área do Imóvel. Sempre que houver alguma alteração de metragem (M² locado, reservado, disponível e total) no cadastro de área, o histórico será preenchido.

**Procedimentos que geram histórico:**

* Cadastro e alteração de área;
* Inclusão de área no contrato de locação: atualizará o M² reservado e gerará o histórico;
* Exclusão de imóveis do contrato;
* Efetivação do contrato de locação;
* Reabrir contrato de locação;
* Aditivo de alteração de imóveis:
  + Ao aumentar a ocupação de uma área já inclusa no contrato, ou incluir uma nova área será atualizado o M² reservado e o histórico será gerado. (Aditivo em preparação);
  + Ao efetivar o aditivo, o M² reservado e o M² locado serão atualizados e o histórico será gerado;

* Aditivo de exclusão de imóveis: ao efetivar o aditivo, serão atualizados M² locado e M² disponível e o histórico será gerado;
* Encerramento do contrato: atualizará o histórico ao efetivar e ao desfazer;
* Exclusão do contrato;
* A exclusão da área ou do imóvel deve excluir o histórico.

**Campos mostrados na tela de histórico:**

* Id Histórico;
* Código da Coligada do Imóvel;
* Código do Imóvel;
* Código da Área;
* Data Referência: pode ser a data de execução do procedimento que deu origem à linha de histórico ou, no caso de aditivos, a data do aditivo, ou, no caso de contratos, a data de início de vigência do contrato, ou, no caso de encerramentos, a data de encerramento;
* Data de Criação: será sempre a data de execução do procedimento que originou a linha de histórico, independente de qual procedimento foi executado;
* Processo de Origem: indica qual procedimento (processo ou cadastro) originou a linha de histórico em questão;
* Compõe saldo de área para locação;
* Núm. Contrato Locação;
* Desc. Localização;
* Desc. Tipo de Área do Imóvel;
* M² Total;
* M² Disponível;
* M² Locado;
* M² Reservado;
* Código do Tipo de Área;
* Código da Localização da Área;
