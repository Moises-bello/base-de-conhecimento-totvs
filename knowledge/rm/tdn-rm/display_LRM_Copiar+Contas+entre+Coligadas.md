---
content_hash: 85015e2edc5acfa8f4dce96e3882741f007f9eaeea93762372ca48eaae0dd31a
fetched_at: '2026-06-29T00:09:28.467826+00:00'
page_id: '423938678'
product: rm
source: tdn-rm
title: Copiar Contas entre Coligadas
type: documentation
url: https://tdn.totvs.com/display/LRM/Copiar+Contas+entre+Coligadas
version: 15
---

Para agilizar e facilitar o cadastro uma Conta Contábil ou Gerencial já cadastrada em uma coligada poderá ser copiada de uma coligada para outra utilizando o processo de copia de contas. Selecione as contas desejadas e execute o processo marcando para quais coligadas deseja efetuar a cópia das contas.

#### Plano de Contas Contábil

* As **máscaras** entre as coligadas origem e destino devem, obrigatoriamente, serem iguais para que a cópia seja efetuada.
* Contas **globais** não poderão ser copiadas.
* A opção **'Substituir registros no destino se eles já existirem'** não está disponível para esta visão. Isso ocorre porque campos como Rateio, Distribuição Gerencial, Natureza (Analítica/Sintética) e Status (Ativa/Inativa), Data Conciliação exigem validações obrigatórias, presentes nos processos específicos de alteração do Plano de Contas.
* Toda a hierarquia de contas sintéticas (todos os níveis anteriores, ou seja, os pais da conta que está sendo copiada) deve existir na coligada destino, caso contrário, a conta não será copiada.
* Se para a cópia for selecionada, por exemplo, a conta sintética 1, será copiada apenas a conta sintética 1. Não será copiado todo o grupo 1 (as contas filhas do grupo 1 não serão copiadas).
* Se a conta origem exigir **rateio**, a conta copiada também exigirá rateio, porém os rateios default da conta origem não serão copiados. A conta destino (cópia) ficará com rateio default vazio
* Os campos **complementares** não serão copiados.
* Os dados da aba Ativo Imobilizado, disponível somente no cadastro do Plano de Contas Contábil no Totvs Gestão Patrimonial, não serão copiados.

#### Plano de Contas Gerencial

* As máscaras entre as coligadas origem e destino devem, obrigatoriamente, serem iguais para que a cópia seja efetuada.
* Contas globais não poderão ser copiadas.
* Possui a opção "Substitui registros no destino se eles já existirem": Com essa opção marcada o sistema consiste se a coligada destino possui alguma conta (seja global ou não) com mesmo código da que está sendo copiada. Se existir a cópia será efetuada com as seguintes ressalvas.  
  - Os campos "Analítica/Sintética" e "Inativa" não são alterados na coligada de destino, pois precisam passar por validações existentes nos processos "Alteração do Tipo de Conta Gerencial (Analítica/Sintética)" e "Alteração de Múltiplos Registros de Conta Gerencial" respectivamente.  
  - O campo "Data de Inclusão" é adicionado no destino com a data corrente, porém, não é modificado.
* Toda a hierarquia de contas sintéticas (todos os níveis anteriores, ou seja, os pais da conta que está sendo copiada) deve existir na coligada destino, caso contrário, a conta não será copiada.
* Se para a cópia for selecionada, por exemplo, a conta sintética 1, será copiada apenas a conta sintética 1. Não será copiado todo o grupo 1 (as contas filhas do grupo 1 não serão copiadas).
* Os campos complementares não serão copiados.

Todas essas regras se aplicam também a cópia de contas utilizando o processo de "Cópia de dados" via **template** no módulo Serviços Globais.
