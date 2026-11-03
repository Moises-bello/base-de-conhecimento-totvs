---
content_hash: 14f62e8b34c65d57efd169a2e8b49a947ccff857c0c3c8e7bcb144487f02d5f5
fetched_at: '2026-06-29T00:05:47.849803+00:00'
page_id: '1018567236'
product: rm
source: tdn-rm
title: Acelerador de implantação PDC - Dados Cadastrais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1018567236
version: 3
---

## Visão Geral

Esta funcionalidade permite a configuração granular das permissões de edição dos dados cadastrais do comprador no Portal, sendo parte do Acelerador de Implantação do PDC (Portal do Comprador).

## Objetivo

Permitir que o usuário administrador defina quais campos de dados cadastrais poderão ser alterados pelos clientes através do Portal, oferecendo controle total sobre a edição de informações pessoais, endereços e contatos.

## Versão Mínima Requerida

**12.1.2510**

## Informações Técnicas

* **Tabela de Armazenamento:** `XCOMPRADORDADOSCADASTRAIS`
* **Tipo de Configuração:** Ligar/Desligar (toggle) por campo
* **Contexto:** Wizard do Acelerador de Implantação do PDC e Portal do Cliente(PDC)

## Campos Configuráveis

### Dados Pessoais

| Campo | Descrição |
| --- | --- |
| Nome | Nome completo do comprador |
| Nome Social / Fantasia | Nome social (PF) ou nome fantasia (PJ) |
| CPF / CNPJ | Documento de identificação fiscal |
| Inscrição Estadual | Número de inscrição estadual (PJ) |
| Inscrição Municipal | Número de inscrição municipal (PJ) |
| Data de nascimento | Data de nascimento do comprador |
| Estado Civil | Estado civil do comprador |
| Identidade (CI) | Número da carteira de identidade |
| Órgão emissor (CI) | Órgão que emitiu a identidade |
| Estado emissor (CI) | UF do órgão emissor |

---

### Endereço Principal

| Campo | Descrição |
| --- | --- |
| Rua | Logradouro do endereço principal |
| Número | Número do endereço |
| Complemento | Complemento do endereço |
| Bairro | Bairro do endereço |
| Cidade | Município do endereço |
| Estado | Unidade Federativa |
| CEP | Código de Endereçamento Postal |
| País | País do endereço |

---

### Contato

| Campo | Descrição |
| --- | --- |
| Telefone | Telefone residencial |
| E-mail | Endereço de e-mail principal |
| Telefone comercial | Telefone comercial |
| Celular | Número de celular |
| Contato | Nome do contato |

---

### Endereço de Pagamento

| Campo | Descrição |
| --- | --- |
| Rua | Logradouro do endereço de pagamento |
| Número | Número do endereço |
| Complemento | Complemento do endereço |
| Bairro | Bairro do endereço |
| Cidade | Município do endereço |
| Estado | Unidade Federativa |
| CEP | Código de Endereçamento Postal |
| País | País do endereço |

---

### Contato de Pagamento

| **Nome** | **Descrição** |
| --- | --- |
| Telefone | Habilita contato por telefone. |
| E-mail | Habilita contato por e-mail. |
| Contato | Habilita contato geral. |
| Fax | Habilita contato por fax. |

---

## Funcionamento

### Configuração dos Campos

1. Para cada campo listado, o usuário poderá **ativar ou desativar** a permissão de edição
2. A configuração é feita através de um controle de **toggle (ligar/desligar)**

As configurações são armazenadas na tabela `XCOMPRADORDADOSCADASTRAIS`

### Comportamento no Portal

**Campo Ativado (Ligado):** O cliente poderá editar o campo através do Portal

* **Campo Desativado (Desligado):** O campo será exibido como somente leitura no Portal

## Casos de Uso

### Caso de Uso 1: Restrição de Dados Fiscais

Uma empresa deseja que clientes possam atualizar dados de contato, mas não deseja permitir alterações em CPF/CNPJ e Inscrições Estadual/Municipal.

**Configuração:**

* Desativar: CPF/CNPJ, Inscrição Estadual, Inscrição Municipal
* Ativar: Telefone, E-mail, Celular

### Caso de Uso 2: Liberação Total de Dados de Contato

Permitir que o cliente atualize todos os dados de contato e endereços, mas manter dados pessoais protegidos.

**Configuração:**

* Desativar: Seção completa de Dados Pessoais
* Ativar: Seções de Endereço Principal, Contato, Endereço de Pagamento

## Observações Importantes

1. As configurações são aplicadas por portal configurado
2. A configuração não afeta os dados existentes, apenas a permissão de edição
3. Alterações nas configurações não requerem reinicialização do sistema
4. É recomendável documentar as políticas de privacidade da empresa antes de configurar

## Recursos Relacionados

* Acelerador de Implantação do PDC
* Portal do Comprador (PDC)
* Gestão de Cadastro de Compradores
