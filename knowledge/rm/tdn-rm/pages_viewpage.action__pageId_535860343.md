---
content_hash: 2b7c8c247c0b819e08817af93b82ad640f2d94bdcb75ebba17c757264e7bcd0a
fetched_at: '2026-06-29T00:10:37.135056+00:00'
page_id: '535860343'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Atendimento ( Antigo PDC )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535860343
version: 17
---

Essa funcionalidade é responsável por gerenciar os atendimentos com base nas coberturas e garantias relacionadas à SubUnidade.

Integração com Agilis:

Parametrização necessária para a execução do processo:   
**Importante:** É Obrigatório que seja informado o **Cliente Online** nos parâmetros do Agilis, este cadastro será utilizado como default para as solicitações que serão abertas no APP Meu Imóvel ou PDC.  O Cliente Online deve ser informado na **Coligada do Agilis** parametrizada para execução do processo de .

* **Caminho para os parâmetros do Agilis:**

Gestão do Relacionamento com o Cliente >> Ambiente >> Parâmetros >> CRM >> 51.14 - Cliente Online) Prencha o campo "Atendente Cliente Online".

**Abertura do Atendimento:**

1. Deve ser selecionado a Subunidade que necessita do Atendimento.
2. Será possível acionar uma Garantia ou Pular a Etapa
3. Informar o Título da Solicitação
4. Descrição da Solicitação
5. É possível informar um Anexo.

**Os Atendimentos são sempre associados ao Comprador Principal da Venda. Caso um Comprador Secundário abra o Atendimento, ele não irá aparecer na visão deste Comprador, apenas na visão daquele.**

---

**Importante**

A partir da versão **12.1.33**, o usuário poderá informar os dias da semana que terá disponibilidade para receber suas visitas, bem como o período do dia que poderá receber a visita como mostra a imagem abaixo:

Abertura de Atendimento PDC - ( Tipo de Atendimento ).

**Versão 12.1.34 em Diante !!!**

No PDC, será apresentado para o usuário , opção para  escolher o tipo de atendimento. Lembrando que serão apresentados todos os tipos de atendimentos visíveis no Portal em seu parâmetro.

Caso o tipo de atendimento escolhido for de garantia, gerar Atendimento de garantia no PDC para o novo modelo de atendimento, seguindo a mesma regra de atendimento antigo

Tipos de Atendimentos cadastrados no TCGI , parametrizados para uso no Portal.

Abertura de Atendimento no PDC , mostrando todos os Tipos de Atendimentos cadastrados no TCGI e configurados para uso do Portal.

Exemplo do Tipo de Atendimento parametrizado no PDC.

1 - Exibir Tipo de Atendimento no Portal

Entrega de Chaves Vendas - Mostrando no Portal

2 -  Exibir Preferência do Período de Visitas no Atendimento.

3 - Exigir anexo no Portal do Cliente.

# **Garantia de Atendimento** ( Garantias secundárias visualizadas no PDC - Versão 12.1.2302 e Posteriores ).

Garantia de Atendimento possui cadastros secundários e o PDC mostra a opção de escolher as Garantias secundárias também.

Abrir uma Solicitação

Selecionar o Tipo de Garantia.

Clicar na Seta ao lado da Garantia

Garantias Secundárias sendo visualizadas no PDC.

Abertura de Atendimento - Aluguel.

Além de ser possível abrir atendimentos para o contrato de venda, o cliente da locação tem  a opção de abrir um atendimento para o contrato de locação.

Entrar no parametro - 22.08

Habilitar o uso do Contrato de Locação para portal e aplicativo.

Clicar em Alterar empreendimento / Contrato

Ai fica o Aluguel na visão de atendimento no Portal.

Veja mais

---

* [Parâmetros - Contrato - Turno de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=616226405)
* [TCGI - Solicitação de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105224)
