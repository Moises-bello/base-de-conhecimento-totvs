---
content_hash: a3d01c7424a6ee8bd9b20932c4a070e7da9d7f7a99b8f95302378349742efece
fetched_at: '2026-06-29T00:05:47.099458+00:00'
page_id: '1005900251'
product: rm
source: tdn-rm
title: Processar Artefatos Sensíveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005900251
version: 2
---

## 📘 Visão Geral

O processo consiste em verificar dentre os **artefatos** (*Consulta SQL, Planilha Net e/ou RM Reports*) quais contém dados que são configurados como **sensíveis** baseado no cadastro de proteção de dados.

---

## 🗃️ Estrutura da Tabela `GARTEFATOSENSIVEL`

|  |  |  |
| --- | --- | --- |
| **ID** | UNIQUEIDENTIFIER | Identificador único (GUID) do acesso registrado |
| **CODCOLIGADA** | INT | Código da coligada associada ao artefato sensível |
| **TIPOARTEFATO** | CHAR(1) | Tipo de artefato sensível acessado: • **C** → Consulta SQL • **R** → RM Reports • **P** → Planilha .NET |
| **APLICACAO** | CHAR(1) | Código da aplicação onde o artefato está localizado |
| **CODARTEFATO** | VARCHAR(150) | Código identificador do artefato sensível |
| **TABELA** | VARCHAR(255) | Nome da tabela de banco de dados acessada |
| **COLUNA** | VARCHAR(255) | Nome da coluna acessada |
| **ATIVO** | SMALLINT | Status de situação do artefato  • **0** → Ativo • **1** → Inativo |
| **RECCREATEDBY** | VARCHAR(50) | Usuário que executou o processo |
| **RECCREATEDON** | DATETIME | Data e hora em que o processo foi executado |

Todos os registros são identificados unicamente pelo campo `ID` (GUID), permitindo auditorias completas e sem risco de duplicidade.

## 🗃️ Estrutura da Tabela `GHSTARTEFATOSENSIVEL`

|  |  |  |
| --- | --- | --- |
| **ID** | UNIQUEIDENTIFIER | Identificador único (GUID) relacional a tabela de GARTEFATOSENSIVEL |
| **DATA** | DATETIME | Data de movimentação do artefato |
| **TIPOREGISTRO** | CHAR(1) | Tipo da movimentação do artefato **• I** → Inclusão  • **E** → Exclusão |

---

## 🧠 Funcionamento Geral

Ao ser executado, o processo percorre todos os artefatos registrados no ecossistema TOTVS RM, avaliando se há a presença de dados sensíveis.  
Quando um dado sensível é identificado, o artefato e o respectivo campo são registrados na tabela **GARTEFATOSENSIVEL**.

O sistema mantém um **histórico de inclusões e exclusões** desses artefatos na tabela **GHSTARTEFATOSENSIVEL**, permitindo o rastreamento completo das alterações.

Uma vez registrado na tabela **GARTEFATOSENSIVEL**, **o artefato não poderá ser excluído**, apenas **inativado**.  
Todas as movimentações entre inclusão e exclusão são registradas no histórico mantido em **GHSTARTEFATOSENSIVEL**.

Caso o dado deixe de ser considerado sensível em função de alterações no **cadastro de proteção de dados**, o processo, ao ser executado novamente, realizará automaticamente a **inativação do registro**, preservando integralmente seu histórico.

Apenas os artefatos Consulta Sql, Planilha Net e RM Reports serão verificados na execução deste processo.

Não está previsto o processamento de dados dos Relatório do Smart View.

Todos os artefatos deverão estar funcionando corretamente para serem validados.

Os artefatos somente serão classificados como sensíveis após a execução do processo.

Em caso de inclusão de novos artefatos no ecossistema, o processo deverá ser executado novamente, garantindo a atualização e consistência dos dados.

---

## 🔄 Fluxo Resumido do Processo

trueDiagrama de Fluxofalseautotoptrue7812

### 🧠 **Resumo textual do fluxo**

1. O processo é iniciado.
2. O sistema busca os dados sensíveis cadastrados em base.
3. Para cada artefato encontrado, verifica se ele contém algum desses dados sensíveis.
4. Se possuir:

   * Verifica se já existe na base:

     + Se sim → atualiza o histórico ou reativa o registro, caso esteja inativo.
     + Se não → insere o novo artefato sensível.
5. Caso algum dado anteriormente sensível tenha deixado de ser considerado sensível, o sistema atualiza o cadastro, desativando o registro e mantendo o histórico.
6. O processo se repete para todos os artefatos e, ao final, é encerrado.

---

## 🧭 Localização no Totvs RM

No **Totvs RM**, no módulo de **Serviços Globais**. O Processo estará disponível na Aba Segurança, no menu Proteção de Dados - Configurar Proteção de Dados:

cssConfluence

Caso o processo não esteja visível, é provável que o usuário não possua permissão para acessá-lo.  
Veja a seção abaixo sobre **liberação de acesso ao perfil**.

---

## 🔐 Liberação de Acesso ao Objeto de Negócio

Para disponibilizar o Objeto de Negócio de Artefatos Sensíveis a um perfil de usuário, siga os passos abaixo:

1️⃣ **Acesse o módulo:** `Serviços Globais`

2️⃣ **Abra a aba:** `Segurança e Perfis`

3️⃣ **Filtre pelo perfil desejado** e clique em **Editar**

4️⃣ **Selecione a aba:** `Acesso a Menus`

5️⃣ **Libere a permissão:**

cssConfluence

Após a liberação, o processo ficará visível no Menu Processos da Visão de Configurar Visão de Dados.

Liberação de Fracionamento

Para otimizar o desempenho e a eficiência do sistema o processo foi construído utilizando-se do recurso de fracionamento de jobs. Logo, para seu correto funcionamento deverá ser realizado o cadastramento através do Menu de **Segurança de Jobs Fracionáveis.**

Para mais informações:
