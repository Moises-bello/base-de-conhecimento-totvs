---
content_hash: 9b6e610ba21fb184d991559befc5aa6a6948b6fe254d7a27bd9dc0f77380283d
fetched_at: '2026-06-29T00:09:49.240358+00:00'
page_id: '435105266'
product: rm
source: tdn-rm
title: Seguro - Processo - Gerar Endosso
type: documentation
url: https://tdn.totvs.com/display/LRM/Seguro+-+Processo+-+Gerar+Endosso
version: 5
---

Esse processo é utilizado quando se tem a necessidade da realização de alguma alteração de uma Apólice de Seguro, que já se encontra com o status "Efetivado".   
   
**Pré-requisitos:**

* Permissão de acesso ao processo;
* Seguro cadastrado com o status igual à "Efetivado";
* Caso exista despesa associada ao seguro, ela não pode ter parcelas de despesa e/ou parcelas de reembolso de despesa cujo vencimento seja posterior a data do endosso e estejam integradas,

**Como executar**

Acesse a visão de Seguros, através do caminho: TOTVS Incorporação >> Outros >> Seguro;  
Selecione o Seguro desejado com status de Efetivado e em Processos escolha a opção "Gerar endosso";

Será exibida a tela abaixo:  
  
**Campos presentes na tela do processo de Gerar endosso:**

* **Código:** Identificador único gerado automaticamente pelo sistema para controle interno.
* **Número do endosso:** Campo utilizado para informar o número do endosso que está sendo realizado. Este campo é editável.
* **Data do endosso:** Neste campo o usuário informa a data em que o endosso está sendo realizado. Este campo é editável.
* **Motivo do endosso:** Campo usado para o usuário informar uma breve descrição do endosso que está sendo realizado. Este campo é editável.
* **Corretora:** Empresa que fez as cotações dos seguros e negocia os valores, intermediando a relação entre a seguradora e o segurado.
* **Status:** Campo que define o status do seguro. Pode ter os seguintes valores: Em Preparação/Efetivado/Encerrado/Endossado.
* **Seguradora:** Empresa responsável pela emissão e registro da apólice junto a SUSEP.
* **Modalidade:** Associação da apólice do seguro ao cadastro de modalidade, como por exemplo, Seguro Predial, Seguro de Responsabilidade Civil, Seguro de Condomínio, etc.
* **Origem:** Campo para informar qual a origem da apólice de seguros.
* **N° apólice:** Campo para informar o novo número da apólice.
* **N° SUSEP:** Número de registro do processo na Superintendência de Seguros Privados.
* **Seguro anterior:** Informa a apólice do seguro anterior em caso de renovação da apólice do seguro.
* **Responsável:** Define o responsável pela apólice do seguro como por exemplo locador ou locatário.
* **Data de início de vigência:** Data inicial de vigência do seguro que está sendo endossado.
* **Data de fim de vigência:** Data final de vigência do seguro que está sendo endossado.
* **Data de emissão:** Data de emissão da apólice de seguro que está sendo endossado.
* **Moeda da apólice:** Informa qual a moeda utilizada para os valores da apólice de seguro.
* **Descrição:** Campo de texto livre para o usuário informar qualquer informação referente a apólice do seguro.
* **Beneficiários:** Campo de texto livre para o usuário informar quais são os beneficiários do seguro.
* **Cobertura:** Nessa grid pode ser realizada o controle das coberturas, possibilitando a inclusão, edição e exclusão. Ao incluir uma nova cobertura, será exibida uma tela com os seguintes campos:

* + **Descrição:** Campo de texto livre para o usuário informar qualquer informação referente a cobertura do seguro;
  + **Franquia:** Campo no qual permite informar o valor da franquia da cobertura do seguro.
  + **Limite máximo de indenização:** Campo no qual permite informar o valor de limite máximo de indenização da cobertura do seguro. **-**
  + **Prêmio:** Campo no qual permite informar o valor do prêmio da cobertura do seguro.
  + **Observação:** Campo de texto livre para o usuário informar qualquer observação referente a cobertura do seguro.

* **Resíduo financeiro:** Neste grupo, serão exibidos os valores das despesas em aberto do seguro que está sendo endossado. São considerados apenas os valores de parcelas com vencimento posterior à data do endosso. Os valores serão exibidos em campos separados para valores a pagar e valores a receber (parcelas de reembolso).
* **Prêmio total:** Campo usado para o usuário informar o prêmio total do seguro que está sendo endossado.
* **Valor da cobertura:** Campo usado para o usuário informar o valor da cobertura do seguro que está sendo endossado.

Após a execução do processo, será gerada uma nova Apólice de Seguro com status igual à "Em Preparação", no qual poderá ser realizado alterações. Esta apólice de seguro, terá o campo "Seguro Anterior" preenchido com o código da apólice endossada. A sua data final será a mesma da apólice original.   
A apólice no qual foi executado o processo, terá o seu status alterado para "Endossado" e o seus campos permaneceram bloqueados.  O motivo informado no processo, será visualizado na apólice original.

Observações

O Processo poderá ser feito somente com um cadastro de seguro.

Caso exista despesa associada ao seguro e esta contenha parcelas de despesa e/ou parcelas de reembolso integradas cujo vencimento seja posterior a data do endosso, ao gravar o endosso, será exibida uma mensagem de erro apontando este fato e informando que a integração destas parcelas precisa ser cancelada

Veja Também

* [Cadastro de apólice de seguro](http://tdn.totvs.com/display/LRM/Outros+-+Controle+de+Seguro+-+Seguro)
