---
content_hash: 50e3bcca8c72b9fa9b7e4341028cce5d93bbe5097b4845be7d5ab7dcf76ccefe
fetched_at: '2026-06-29T00:12:09.202081+00:00'
page_id: '942063818'
product: rm
source: tdn-rm
title: Tela de Classificação de Ambiente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=942063818
version: 12
---

# Índice

---

Índice

## **01. Introdução**

---

O objetivo desta página é apresentar como funciona o mecanismo de Classificação do ambiente.

## **02. Descrição do Banco de Dados**

---

Em alguns casos, será exibido o endereço da base de dados na tela de classificação para correta analise do ambiente. A montagem do endereço da base de dados é realizada dinamicamente com base nas propriedades de infraestrutura resgatadas diretamente do servidor de banco de dados.

Para concatenar essas informações, o sistema utiliza o caractere especial **"■"** como delimitador.

A estrutura do endereço gerado segue a anatomia detalhada abaixo:

1. **Tipo do Banco de Dados:** Identifica a tecnologia utilizada, retornando **SQL** (para ambientes Microsoft SQL Server) ou **ORA** (para ambientes Oracle).
2. **Arquitetura/Nome do Cluster:** Identifica o modelo de alta disponibilidade (High Availability).

   * Em ambientes convencionais (sem HA), o valor padrão retornado será **"standalone"**.
   * Em ambientes com Alta Disponibilidade ativa, o valor corresponderá ao nome do Cluster do Windows (WSFC).
3. **Nome Virtual do Servidor:** Exibe o nome do servidor virtualizado que está respondendo pela instância do banco de dados.
4. **Identificador Único (ID):** Código numérico gerado internamente que identifica de forma exclusiva aquela instância ou base de dados específica.
5. **Nome da Base de Dados:** Exibe o nome físico do banco de dados utilizado pela aplicação.

#### Exemplo Prático:

O endereço: `ora■standalone■tfdbprod■715524218■frame_oidc` Significa que o cliente usa banco **Oracle (ora)**, em um servidor **comum (standalone)**, o servidor virtual se chama **tfdbprod**, o código da base é **715524218** e o nome do banco é **frame\_oidc**.

## **03. Exibição da tela via menu**

---

Ao selecionar a **Aba Serviços→ Tipo de Ambiente**, será apresentada a tela para selecionar a finalidade e tipo de ambiente da base de dados.  
Após a confirmação o tipo selecionado será gravado.

A descrição exibida na tela é definida com base na consistência do ambiente.

#### **03.01 - Ambiente Inconsistente**

Quando o ambiente possui os Tipos de inconsistência detalhados no item 05:

* Classificação do ambiente não foi definida no RM
* Houve alguma atualização na integração com o Smartlink
* Houve uma restauração da base de dados.
* CRC Inválido da tabela GSMARTLINKCONFIG

#### **03.02 - Ambiente Consistente**

Quando a classificação do ambiente ja foi definida e o ambiente não possui os Tipos de inconsistência listados no item 04.

#### **03.03 - Credencial Helper está gerando credenciais**

Quando for identificado que o Credential Helper está em processo de geração de novas credenciais

#### **03.04 - Base desatualizada**

Quando a base de dados não possui os scripts necessários para a abertura da tela

#### **03.05 - Base de Teste**

Quando a base de dados utilizada foi convertida como base de teste

## **04. Exibição da Tela via Login**

---

Funcionalidade disponível a partir da versão 12.1.2406

Quando um usuário com privilégio de Supervisor entra no sistema, pelo login via MDI, são realizadas validações de consistência, caso alguma inconsistência seja detectada o usuário deverá confirmar a Classificação do ambiente.

## **05. Tipos de Inconsistência**

---

#### **04.01 - Quando a Classificação do Ambiente não foi definida no RM**

* **Será apresentada a tela abaixo para que o usuário confirme a finalidade correta do sistema.**

**O que deve ser feito:**Neste caso, significa que a Classificação de Ambiente não foi definida, esta vazia ou nula, dessa forma será necessário selecionar uma opção!  
Após a confirmação a classificação selecionada será gravada.

#### **04.02 - Quando for identificado que houve alguma atualização na integração com o Smartlink**

* **Será apresentada a tela abaixo para que o usuário confirme os dados e selecione novamente a classificação do ambiente.**

**O que deve ser feito:**Confirmar ou alterar a Classificação do sistema.

**O que deve ser feito:**Neste caso, significa que a Classificação de Ambiente não foi definida, esta vazia ou nula, dessa forma será necessário selecionar uma opção!  
Após a confirmação a classificação selecionada será gravada.

* + Caso a classificação do ambiente seja mantida e exista uma integração ligada com o License Serve um Wizard do Credential Helper poderá ser aberto e apresentado ao usuário para que um novo ambiente seja integrado. O Wizard poderá decidir conforme as configurações do License Server se as credenciais serão geradas no momento sendo necessário aguardar, ou se serão geradas por uma tarefa automática.

#### **04.03 Quando houver uma restauração da base de dados.**

* **Será apresentada a tela para que o usuário confirme o Endereço e Classificação antigos e selecione um novo.**

**O que deve ser feito:**Confirmar ou alterar a Classificação do sistema e a alteração para um **Novo** Endereço Base de Dados.

* + Caso a classificação do ambiente seja mantida e exista uma integração ligada com o License Serve um Wizard do Credential Helper poderá ser aberto e apresentado ao usuário para que um novo ambiente seja integrado. O Wizard poderá decidir conforme as configurações do License Server se as credenciais serão geradas no momento sendo necessário aguardar, ou se serão geradas por uma tarefa automática.

#### **04.04** **CRC Inválido da tabela GSMARTLINKCONFIG**

* **Será apresentada a tela abaixo para que o usuário confirme a finalidade correta do sistema.**

**O que deve ser feito:**Neste caso, significa que a houve alguma alteração indevida na tabela GSMARTLINKCONFIG,  dessa forma será necessário selecionar uma opção!  
Após a confirmação a classificação selecionada será gravada e tabela será limpa.

Importante saber: Sobre Alias e Nome da Base de Dados

Em ambientes com servidores Multi-Host, ou até mesmo quando existem Hosts nas maquinas Client sendo executados, é importante haver uma padronização nas configurações do Banco de Dados feitas no Alias Manager, essa informação deve estar bem definida para execução e para as validações nos processos do Credential Helper.

O que isso quer dizer?

Usar a mesma configuração Servidor/Base para todos os Hosts. Utilizando DNS ou IP para identificar o servidor da base de dados, mas somente um deles para todos os hosts utilizados. Isso deve evitar que o sistema entenda que cada Host está configurado para uma base diferente do outro.
