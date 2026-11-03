---
content_hash: fdea6d6c30e84bba367a0281fbf93e41867cbf3e44b3f2b56d7873bc20fa1816
fetched_at: '2026-06-29T00:10:04.067231+00:00'
page_id: '452719192'
product: rm
source: tdn-rm
title: Catálogo de EPI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719192
version: 13
---

Por este menu, serão cadastrados os **Equipamentos de Proteção Individual (EPI's)** que a empresa disponibilizará para seus funcionários.

# **Cadastro de EPI**

Neste cadastro, é possível incluir informações importantes sobre os EPI's. **Três campos são de preenchimento obrigatório:**

* + **Código:** gerado automaticamente pelo sistema;
  + **Nome:** nome do EPI;
  + **Grupo de EPI's:** para que o sistema carregue as informações corretas, é necessário, antes do cadastro do EPI, acessar o menu **EPI/EPC | Grupos** e incluir os grupos de EPI's desejados.

Além disso, o usuário poderá:

* + Informar se o EPI é descartável;
  + Definir se está ativo ou inativo;
  + Incluir uma descrição detalhada do EPI;
  + Adicionar uma foto do EPI.

O cadastro de EPI pode ser utilizado de quatro formas, de acordo com o tipo de integração do sistema:

1. * Sem Integração (Sem controle de estoque);
   * Sem Integração (Com controle de estoque);
   * Integração com o Totvs Gestão de Estoques, Compras e Faturamento;
   * Integração com um sistema externo.

🚨 **Atenção:**

* + Na visão do catálogo de EPI's a coluna quantidade de EPI's permite visualizar os equipamentos que estão **emprestados, mas estão inválidos e/ou vencidos**.

    Essa informação é apenas para consulta e **não influencia na quantidade total de EPI's disponíveis**.
  + O campo **Identificador do Lote**  presente na edição e na visão do catálogo de EPIS é um número disponível apenas para consulta. Essa informação é gerado automaticamente pelo sistema por se tratar de um identificador no momento do cadastro de lotes de EPI's.Não pode ser alterado garantindo assim a integridade dos dados, permitindo arastreabilidade dos EPI's.

## **Sem Integração (Sem controle de estoque)**

Neste modo, o sistema **não está integrado** a um controle de estoque externo e **não utiliza o controle de estoque interno** do Totvs Segurança e Medicina do Trabalho.

**Anexos disponíveis:**

* + **Utilização de EPI's por Função:** lista todos os EPI's fornecidos, agrupados por **Cargo, Função, Local de Trabalho** e o nome da pessoa responsável pelo EPI (pode ser um funcionário ou um local de trabalho).
  + **Utilização de EPI's por Seção:** exibe os EPI's agrupados por **Filial, Departamento, Seção**, e o nome do responsável.
  + **Lote:** permite cadastrar lotes para o EPI selecionado, incluindo informações como:
    - Certificado de Aprovação (CA), Data de Aquisição, Data de Validade, Durabilidade, entre outros;
    - Nome do Fabricante, Certificados de Registro do Importador/Fabricante;
    - Situação do EPI (higienizado, inválido), Filial e Seção de origem;
    - **Identificador do Lote** (campo chave, não editável).

**EPI do Catálogo:**

* + **Histórico de Fornecimento:** datas de fornecimento e devolução, destinatário, validade e motivo da devolução.
  + **Histórico de Higienização:** registros das datas de higienização do EPI.
  + **Processos:**
    - Enviar/retornar EPI para higienização;
    - Definir a periodicidade de higienização;
    - Invalidar o EPI.

## **Sem Integração (Com controle de estoque)**

Neste modo, o sistema **não está integrado** a um sistema externo, mas **utiliza o controle de estoque interno** do Totvs Segurança e Medicina do Trabalho.

### **Anexos e processos** (iguais ao modo anterior, com o controle de estoque ativo):

* + Utilização de EPI's por Função e por Seção;
  + Lote (com o **Identificador do Lote** bloqueado para edição);
  + EPI do Catálogo, incluindo histórico de fornecimento e higienização;
  + Processos de envio para higienização, definição de periodicidade e invalidação de EPI's.

🚩 **Importante:** Após o cadastro do lote, o processo **"Gerar Itens do EPI"** deve ser executado para que o sistema possa realizar o fornecimento de EPI's aos funcionários.

## **Integrado com o Totvs Gestão de Estoques, Compras e Faturamento**

Neste caso, o controle de estoque é realizado **integralmente pelo Totvs Gestão de Estoques, Compras e Faturamento**.  
Todos os movimentos de entrada, saída, empréstimo e devolução de EPI's são gerenciados por essa integração.

### **Anexos disponíveis:**

* + Utilização de EPI's por Função e por Seção;
  + EPI do Catálogo (com histórico de fornecimento, higienização e processos de gestão);
  + Lotes a serem lançados (importados do sistema Totvs).

🚩 **Atenção:** O processo **"Gerar Itens do EPI"** é essencial para o fornecimento correto dos EPI's.

## **Integrado com um Sistema Externo**

Aqui, o controle de estoque é realizado **por um sistema externo**, que gerencia todos os movimentos de entrada, saída e devolução dos EPI's.

### **Anexos disponíveis:**

* + Utilização de EPI's por Função e por Seção;
  + EPI do Catálogo (com histórico e processos de higienização e invalidação);
  + **Importação de Lote:** realizada via arquivo XML, através do processo **"Importar Arquivo de Lote"**.
    - Se o arquivo estiver inválido, o sistema exibirá uma mensagem de erro.

🚩 **Importante:** Após a importação, é necessário executar o processo **"Gerar Itens do EPI"** para que o fornecimento de EPI's funcione corretamente.

**Considerações Finais**

Para **todos os tipos de integração**, o sistema permite o processo de **cópia de dados entre coligadas**.

O **correto cadastro dos lotes** e a **imutabilidade do Identificador do Lote** são fundamentais para garantir a segurança, integridade dos dados e o bom funcionamento do sistema.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Exemplo Arquivo XML Estrutura do Arquivo XML

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Como Fazer](http://totvsconnect.blogspot.com/2012/01/como-fazer-controle-de-estoque-de-epi)  
Acerto Local de Estoque
