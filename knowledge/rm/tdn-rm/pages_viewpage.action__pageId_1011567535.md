---
content_hash: cf1804d3c6c581a8b444c68ffa8c7c7ea206d11ec4402b0297a8769c42af7d36
fetched_at: '2026-06-29T00:05:47.373302+00:00'
page_id: '1011567535'
product: rm
source: tdn-rm
title: Tabela CST e Classificação Tributária (IBS e CBS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1011567535
version: 19
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Informamos que para a **inclusão manual de NOVOS** indicadores na **Tabela de CST**, é necessário que o processo de importação já tenha sido executado previamente. Isso permite ao sistema identificar os indicadores ativos na tabela oficial.

# Conteúdo

2Conteúdonone

# 1. Visão Geral

A tabela de classificação de situação tributária (CST) é uma lista de indicadores para habilitar ou não regras de um determinado **CST** ou **Classificação Tributária** (cClassTrib)

# 2. Como acessar

O cadastro da **Tabela CST** está disponível a partir da versão **12.1.2502** do TOTVS Gestão Fiscal.

IMPORTANTE!

**Mantenha o sistema sempre atualizado para o último patch disponibilizado.** Esta prática assegura que todos os ajustes e melhorias mais recentes estejam aplicados ao seu ambiente.

Para acessá-lo:

**Permissões**

* Acesse o perfil vinculado ao usuário no módulo TOTVS Gestão Fiscal.
* Vá até a aba **Acesso a Menus** e siga o caminho:  
  `[01] Cadastros` → `[01.01] Específicos` → `[01.01.11] Mais...` → `[01.01.11.22] → selecione Tabela CST / cClassTrib` e clique em **Permitir Acesso**.

  

**Menu de Acesso**

* **TOTVS Gestão Fiscal** → **Cadastros** → **Específicos** → **Mais** → **Tabela CST / cClassTrib**

**Observação:**O menu de acesso para a **Tabela CST / cClassTrib** também está disponível através do TOTVS Gestão de Compras, Estoque e Faturamento no caminho:

* **TOTVS Gestão de Compras, Estoque e Faturamento** → **Cadastros → Fiscais** → **Tabela CST / cClassTrib**

# 3. Importação da Tabela

Importação de CST/Classificações Tributárias

O **Cadastro de CST/Classificações Tributárias** (denominado internamente como **“Tabelas CST/ClassTrib”**) é utilizado para definir como determinados grupos e comportamentos de valores serão tratados nas Notas Fiscais (NF-e/NFS-e).

O **Fisco** disponibiliza uma lista oficial de **CST's e Classificações Tributárias** já contendo os indicadores e parâmetros padronizados que devem ser utilizados pelos sistemas emissores. Embora o sistema permita que o cliente crie ou altere seus próprios registros, recomenda-se que o cadastro siga as informações fornecidas pelo Fisco para garantir conformidade fiscal.

Para facilitar esse processo, o sistema disponibiliza uma funcionalidade que permite duas formas de importação:

Fluxo Realizar Consultaleft11 - Integração via API (Certificado Digital)

Funcionalidade responsável por **consultar automaticamente o serviço do Fisco e importar a lista de CSTs e Classificações Tributárias** para o cadastro interno. 

O consumo do serviço do Fisco exige o uso de um **certificado digital**, que deve estar previamente cadastrado no módulo de Certificados do sistema.

Ao executar o processo, o usuário deverá informar:

1. **URL/Endereço do serviço** – o campo já é exibido preenchido com o endereço padrão do serviço que fornece a lista de CST/Classificações Tributárias;
2. **Certificado digital** – o usuário deve selecionar, entre os certificados cadastrados no sistema, aquele que será utilizado para acessar o serviço do Fisco.

Após a execução, o sistema realiza a importação e atualização dos registros, garantindo que o cadastro esteja sempre alinhado às definições oficiais do Fisco.

IMPORTANTE!

Caso já exista o registro de CST/Classificação tributária ele será substituído pelo importado.

 

 

22 - Importação de arquivo 

Funcionalidade responsável por **importar um arquivo no formato json e incluir a lista de CSTs e Classificações Tributárias** para o cadastro interno. 

O arquivo está disponível para download por meio do link fornecido pelo **Fisco** (mesmo endereço utilizado para importação via API), acessível em: <https://cff.svrs.rs.gov.br/api/v1/consultas/classTrib>

Acesse o link em qualquer máquina e qualquer navegador, bastando apenas que o Certificado Digital esteja importado previamente no Windows, e utilize o botão direito do mouse para selecionar a opção ‘Salvar como’, salvando o conteúdo como arquivo no formato .json:

 

Em seguida, clique no ícone de pasta para abrir o *Explorador de Arquivos*, onde será possível localizar e selecionar o arquivo para importação.

Por fim, clique em *Executar* para iniciar o processo. O sistema realizará a importação do arquivo informado e atualizará os dados conforme especificado no arquivo, garantindo que o cadastro permaneça alinhado às definições oficiais do Fisco.

IMPORTANTE!

Caso já exista o registro de CST/Classificação tributária ele será substituído pelo importado.

Quando os campos *Certificado Digital* e *Arquivo de Importação* estiverem preenchidos, o sistema realizará a importação do arquivo informado. Para importação via API, o campo *Arquivo de Importação* não deve ser preenchido.

# 4. Campos do Cadastro

Os campos do cadastro são dinâmicos de acordo com a [especificação da SEFAZ](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria).

Exemplo de indicadores existentes na data de
