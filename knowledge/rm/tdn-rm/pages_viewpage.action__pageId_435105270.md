---
content_hash: ca334c781e6a29cbda31b056e1f81fa199d9e2394b6fec0e1ba69a5ad67f9a97
fetched_at: '2026-06-29T00:09:49.255040+00:00'
page_id: '435105270'
product: rm
source: tdn-rm
title: Parâmetros - Contrato - Atendimento ao cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105270
version: 18
---

Importante!

A partir da conversão para o novo [Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309), as Etapas *Atendimento ao cliente* e de *Integração com o Agilis*, não estão mais disponíveis porque estas configurações serão realizadas diretamente nos cadastros desta funcionalidade.

**Etapa 1 - Atendimento ao cliente**

* **Modelo de descrição para atendimento**: Nesse campo é possível criar um texto default para os atendimentos, esse texto será utilizado após ser gerado um agendamento de Inspeção ou atendimento. A partir da conversão para o novo [Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309), esta opção não está mais disponível porque esta configuração será realizada diretamente nos cadastros desta funcionalidade.  
  + Observação: Nesse campo podem ser utilizados Mnemônicos.
    - Mnemônicos: São palavras reservadas que substituem os dados que podem ser utilizados em relatórios, históricos entre outros.
      * Os seguintes Mnemônicos estão disponíveis no TOTVS Incorporação:

1. 1. 1. 1. 1. 1. **[BRR]: Bairro (Endereço do Empreendimento).**
               2. **[CPL]: Complemento (Endereço do Empreendimento).**
               3. **[DSCSUB]: Descrição da Sub Unidade.**
               4. **[DSCUNI]: Descrição da Unidade.**
               5. **[LGR]: Logradouro (Endereço do Empreendimento).**
               6. **[CLI]: Nome do Cliente.**
               7. **[NOM]: Nome do Empreendimento.**
               8. **[NRO]: Número (Endereço do Empreendimento).**
               9. **[SUB]: Número da Sub Unidade.**
               10. **[UNI]: Número da Unidade.**
               11. **[VND]: Número da Venda.**
               12. **[CONT]: Número do Contrato.**
               13. **[EMP]: Número do Empreendimento.**
               14. **[TEL]: Telefone do Cliente.**
               15. **[TLG]: Tipo do Logradouro.**

**Etapa 2 - Turno de Atendimento**

* **Turnos de atendimento ao cliente:** Insira a descrição mais adequada ao à atuação da Incorporadora para descrever os turnos de atendimento aos clientes, que será apresentada no cadastro dos Atendimentos. Por padrão as opções são:
  + Manhã
  + Tarde
  + Noite
* **Permitir ao usuário selecionar mais de um turno:** Marque esta opção caso o usuário possar marcar mais de um turno para agendar os atendimentos que serão realizados;
* **Permitir ao usuário selecionar finais de semana:** Marque esta opção caso o usuário possa solicitar o agendamento do atendimento para os finais de semana.

**Etapa 3 - Garantia**

* **Máscara do código da Cobertura**: Informe como será a máscara para criar uma nova cobertura, como será o código de identificação de cada cobertura criada;
* **Permitir cadastrar atendimento de garantia sem Cobertura de Garantia vinculada a venda:** Esta opção permite que qualquer tipo de Cobertura válida cadastrada no sistema seja associado à venda. Utilize esta opção também para associar as variações de um [Tipo de Cobertura](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Tipos+de+Cobertura) mais específicos ao associado ao contrato de venda, caso se tenha feito uma especialização deste Tipo de Cobertura que foi inicialmente associado a um contrato de venda;
* **Primeira etapa da Solicitação:** Esse campo é responsável por determinar qual será a etapa em que a solicitação se iniciará. Essa etapa define qual o status do atendimento e as permissões por perfil de quem pode utilizar essa etapa. A partir da conversão para o novo [Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309), esta opção não está mais disponível porque esta configuração será realizada diretamente nos cadastros desta funcionalidade.

**Etapa 4 - Integração com Agilis**

* **Tipo de Atendimento de TCGI Entrega de Chaves:** Informe o tipo de atendimento padronizado no TCGI para a os atendimentos de entrega de chaves.
* **Tipo de Atendimento de TCGI Aprovação de Efetivação da Venda:** Informe o tipo de atendimento padronizado no TCGI para os atendimentos de aprovação da Venda dos contratos de vendas utilizando o TAA.
* **Tipo de Atendimento de TCGI Aprovação de Efetivação do Aditivo:** Informe o tipo de atendimento padronizado no TCGI para os atendimentos de aprovação do Aditivo aos contratos de vendas utilizando o TAA.
* **Tipo de Atendimento de TCGI Aprovação de Efetivação do Distrato:** Informe o tipo de atendimento padronizado no TCGI para a os atendimentos de aprovação do Distrato aos contratos de vendas utilizando o TAA.

**Integração com o Agilis**: A partir da conversão para o novo [Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309), esta opção não está mais disponível porque esta configuração será realizada diretamente nos cadastros desta funcionalidade.

* **Criar automaticamente um Atendimento no Agilis ao criar uma Solicitação**: Indica ao sistema que deverá ser feito integração com o Agilis, ao se criar uma Solicitação de Garantia. Ao marcar o parâmetro são habilitados os campos abaixo:
  + **Coligada do Agilis:** Indica qual a coligada que será criado os atendimentos do Agilis *(Campo obrigatório);*
  + **Grupo de Atendimento:** Indica qual o Grupo de atendimento será utilizado para a criação do atendimento, será exibido somente os Grupos de Atendimento da Coligada selecionada *(Campo obrigatório);*
  + **Tipo de Atendimento:** Indica qual o Tipo de Atendimento será utilizado para a criação do atendimento, será exibido somente os Tipos de Atendimento do Grupo de Atendimento selecionado *(Campo obrigatório).*

 

Veja Também

---

Para maiores informações sobre as Etapas do TIN, acesse o link: Etapas  
Para maiores informações sobre Grupo de Atendimento, acesse o link:   
Para maiores informações sobre Tipo de Atendimento, acesse o link:
