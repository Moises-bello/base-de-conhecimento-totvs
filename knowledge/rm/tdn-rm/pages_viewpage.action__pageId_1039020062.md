---
content_hash: 626a9bd2151650740fee2c87deaaa854e85b86ca2bf4ec905f7e14bebead2632
fetched_at: '2026-06-29T00:05:49.244292+00:00'
page_id: '1039020062'
product: rm
source: tdn-rm
title: Ativar/Desativar Dados Bancários Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039020062
version: 5
---

Disponibilização do Recurso

Esse processo está disponível a partir da **release 12.1.2602**.

---

**IMPORTANTE**

Nas versões **anteriores** a ela, a ativação ou desativação do uso dos **Dados Bancários Global** é realizada exclusivamente por meio do parâmetro: **Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar (ou Contas a Receber) | Manutenção de Lançamento | Lançamento | Cliente/Fornecedor**  
Opção: **“Usar Dados Bancários Global do Cliente/Fornecedor”**

Processo responsável pela ativação ou desativação do uso dos **Dados Bancários Globais de Cliente/Fornecedor (coligada zero)**. Este processo érecomendado para usuários que já utilizam ou que pretendem utilizar os cadastros de Dados Bancários de forma Global. E está acessível através do menu **Utilitários | Outros | Mais | Ativar/Desativar Dados Bancários Global**.

Pré-Requisito

Para que o processo possa ser executado, a coligada deve estar parametrizada com a opção **“Permitir Globais”** habilitada (disponível em Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar (ou Contas a Receber) | Manutenção de Lançamento | Lançamento | Cliente/Fornecedor). Caso contrário, o sistema não permitirá sua execução.

A partir da release **12.1.2602**, o parâmetro **“Usar Dados Bancários Global do Cliente/Fornecedor”** passou a ser disponível **apenas para consulta**, refletindo seu estado:

* **Ativo**: quando marcado
* **Inativo**: quando desmarcado

Ao executar o processo:

* A **coligada do contexto** e **todas as demais coligadas** que possuírem o parâmetro **“Permitir Globais”** ativado (disponível em Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Pagar (ou Contas a Receber) | Manutenção de Lançamento | Lançamento | Cliente/Fornecedor) passarão a **usar os Dados Bancários de Cliente/Fornecedor de forma global**.
* A **coligada informada na tela do processo** será definida como **coligada de referência**.
* Todos os dados bancários dessa coligada de referência serão **transformados em dados globais (coligada zero)**.

Em seguida, o processo:

* Atualiza **todos os boletos e lançamentos financeiros** de fornecedores globais para que passem a **referenciar os dados bancários globais**.
* Essa atualização é realizada **automaticamente em todas as demais coligadas** que permitem dados globais na base de dados.

Para garantir a integridade dos dados, recomendamos que o processo seja executado e validado em ambiente de homologação antes de executá-lo em produção. Ressaltamos que a execução em ambiente real sem backup prévio é de responsabilidade exclusiva do usuário.

**Permissão**

Para ter acesso ao processo é necessário que o perfil do usuário no **TOTVS Gestão Financeira** tenha permissão à funcionalidade **"Ativar/Desativar Dados Bancários Global"** que fica na árvore de permissões em **Gestão Financeira | Utilitários | Outros | Mais...** .

Importante

Para que o processo seja executado corretamente, é necessário que:

* A **coligada de referência** possua os **dados de pagamento de todos os fornecedores globais** existentes em **todas as coligadas**.
* As **formas de pagamento** de cada fornecedor respeitem a **mesma sequência (IDPGTO)** nas diferentes coligadas.

**Atenção:**  
Caso exista qualquer lançamento ou boleto, em qualquer coligada, de um fornecedor global **não configurado** nos dados bancários da coligada de referência, o banco de dados retornará **erro**, impedindo a conclusão do processo.
