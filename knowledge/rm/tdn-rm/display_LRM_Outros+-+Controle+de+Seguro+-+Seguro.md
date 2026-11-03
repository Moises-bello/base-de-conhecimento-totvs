---
content_hash: 430707802416a628929e5c08e9a55160959788da559a8303152d810d757d796f
fetched_at: '2026-06-29T00:09:49.568317+00:00'
page_id: '435105321'
product: rm
source: tdn-rm
title: Outros - Controle de Seguro - Seguro
type: documentation
url: https://tdn.totvs.com/display/LRM/Outros+-+Controle+de+Seguro+-+Seguro
version: 17
---

O cadastro de apólice de seguro foi desenvolvido para o usuário informar os dados da apólice do seguro para ser utilizado no módulo Gestão de Controle de Seguro do TOTVS Incorporação.

São os seguintes dados que constam este cadastro:

* **Código**: Identificador único gerado automaticamente pelo sistema para controle interno;
* **Seguro anterior**: Informa a apólice do seguro anterior em caso de renovação da apólice do seguro;
* **Status**: Campo que define o status do seguro. Pode ter o seguintes valores: Em Preparação/Efetivado/Encerrado/Endossado.
* **Responsável**: Define o responsável pela apólice do seguro como por exemplo locador ou locatário;
* **Número da apólice**: Campo destinado a indicar o número da apólice gerada pela empresa seguradora, portanto trata-se de um campo informado pelo usuário.
* **Número SUSEP**: Número de registro do processo na Superintendência de Seguros Privados.
* **Data de emissão**: Data de emissão da apólice de seguro;
* **Data de início de vigência**: Data inicial de vigência do seguro;
* **Data de fim de vigência**: Data final de vigência do seguro;
* **Modalidade**: Associação da apólice do seguro ao cadastro de modalidade, como por exemplo, Seguro Predial, Seguro de Responsabilidade Civil, Seguro de Condomínio, etc
* **Prêmio total**: Valor do prêmio total pago pelo seguro.
* **Valor da cobertura**: Valor total da cobertura do seguro, o sistema informa por default o somatório das coberturas, porém o usuário pode alterar este valor;
* **Moeda da apólice**: Informa qual a moeda utilizada para os valores da apólice de seguro;
* **Corretora**: Empresa que fez as cotações dos seguros e negocia os valores, intermediando a relação entre a seguradora e o segurado;
* **Seguradora**: Empresa responsável pela emissão e registro da apólice junto a SUSEP
* **Descrição**: Campo de texto livre para o usuário informar qualquer informação referente a apólice do seguro;
* **Beneficiários**: Campo de texto livre para o usuário informar quais são os beneficiários do seguro;
* **Cobertura:** Nessa grid pode ser realizada o controle das coberturas, possibilitando a inclusão, edição e exclusão. O sistema disponibiliza o botão "**Somar Coberturas**" para calcular a soma do prêmio de todas as coberturas e salvar no campo Prêmio total do seguro. Ao incluir uma nova cobertura, será exibida uma tela com os seguintes campos:
  + **Descrição:** Campo de texto livre para o usuário informar qualquer informação referente a cobertura do seguro;
  + **Franquia:** Campo no qual permite informar o valor da franquia da cobertura do seguro;
  + **Limite máximo de indenização:** Campo no qual permite informar o valor de limite máximo de indenização da cobertura do seguro;
  + **Prêmio:** Campo no qual permite informar o valor do prêmio da cobertura do seguro;
  + **Observação:** Campo de texto livre para o usuário informar qualquer observação referente a cobertura do seguro.

* **Origem:** Campo para informar qual a origem da apólice de seguros:
  + **Imóvel:** Caso seja uma apólice se seguros vinculada a imóvel.
  + **Contrato de locação:** Caso seja uma apólice se seguros vinculada a contrato de locação.

O sistema ainda possibilita ao usuário a criação de campos complementares para este cadastro.  
Após a criação do registro de apólice do seguro, o usuário pode:

* Associar o seguro a uma documentação do módulo de  do Totvs Incorporação. Esta associação é feita no cadastro de documentação.
* Associar o seguro a uma despesa, através do anexo Despesa do Seguro.

Anexos





Processos
