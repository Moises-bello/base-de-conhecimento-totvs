---
content_hash: ed2b9e8bb1c525a802dc53ce9beb3eaa0be535f8b764ca420d3d9ade75040c7c
fetched_at: '2026-06-29T00:05:53.893427+00:00'
page_id: '1072001117'
product: rm
source: tdn-rm
title: TestFlow - Virada de Versão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1072001117
version: 8
---

## 1. Preparação de Arquivos (Servidor de Bases)

Nesta etapa, preparamos a estrutura física dos arquivos da nova versão.

1. Aceda ao diretório: `\\BH-AUTBDCP\BasesAutomacao\v1200\1212606`
2. Copie todo o conteúdo da pasta **1212606**
3. Crie a pasta **1212610** no mesmo nível.
4. Cole o conteúdo na pasta `\\BH-AUTBDCP\BasesAutomacao\v1200\1212610`.

## 2. Conversão de Bases de Dados

### 2a) SQL Server

* Converter os bancos da pasta **12.1.2610** para a versão **12.1.2610**.
* **Atenção:** Se a versão já estiver no restore, utilize o **atualizador manual**.
* **Importante:** Garanta o apontamento correto para a pasta `12.1.2610`.
* **Configuração de Backup:** Marcar sempre `Compactar backup` e `Substituir arquivos`.

### 2b) Oracle (Instância PDB)

Clonagem da base `REALESTATEV1212606` para `REALESTATEV1212610`.

**Comandos de Execução:**

SQL

```
-- Conectar como SYSDBA
sqlplus sys/totvs@BH-AUT-ORA-CONS.SP01.LOCAL/ORA190PDB.SP01.LOCAL as sysdba   
  
-- Criar o clone da base
CREATE PLUGGABLE DATABASE REALESTATEV1212610 FROM REALESTATEV1212606;

-- Abrir em modo Read-Write para atualização
ALTER PLUGGABLE DATABASE REALESTATEV1212610 OPEN;
```

> **Ação Manual:** Execute o atualizador da versão **12.1.2610** usando o domínio: `BH-AUT-ORA-CONS.SP01.LOCAL/REALESTATEV1212610.SP01.LOCAL`

**Finalização (Modo Read-Only):**SQL

```
ALTER PLUGGABLE DATABASE REALESTATEV1212610 CLOSE IMMEDIATE;
ALTER PLUGGABLE DATABASE REALESTATEV1212610 OPEN READ ONLY;
ALTER PLUGGABLE DATABASE REALESTATEV1212610 SAVE STATE;
```

## 3. Preparação das VMs (AUTTIN01, AUTTIN02, AUTTINPR)

Realize as seguintes limpezas em cada VM:

* **Shift + Del** na pasta da versão `12.1.2506`.
* **Shift + Del** na pasta da versão `Atual` antiga.
* **Agendamentos:**

  + **Desabilitar:** Desmarque "Executar diariamente" nos AGENDAMENTOS da Versão Atual (evita conflitos entre 2606 e 2610), DESMARCAR  a flag: Repetir Tarefa  a cada minuto
  + **Eliminar:** Exclua todos os agendamentos da versão `12.1.2506`.

## 4. Configuração no Testflow

Assim que o ambiente **Versão Atual 12.1.2610** estiver disponível no TestFlow

Verifique aqui se já está disponível:  
  
<http://testflow/testflow/productversions>

1. **Planilha Engenharia:** Validar apenas após concluir as etapas 1 e 2.
2. **Versão de Agendamentos:** Gerar versão manual (12.1.2606 -> 12.1.2610) para:

   * `ATUALIZA AMBIENTE AUTTIN02 NOVO TOTVS RESTORE`
   * `IMBALG_RECURSOALGRECURSOATUALIZABASES` (Modelo, Populada, Conv)
   * `IMBALG_RECURSOORACLEATUALIZASCRIPTS`
   * Projetos Oracle: `RestauraOracle_Script`, `RestauraOracle`, `SubstituirBaseOficial`, `CriarCenarios`.

### Ajuste Técnico JSON

Nos projetos `SubstituirBaseOficial` e `CriarCenarios`, da versaoAtual, altere o JSON na atividade C#:

De:SON

```
{
  "pdbInstance": "ORA190PDB.SP01.LOCAL",
  "dbSource": "REALESTATEV1212606",
  "oraServer": "BH-AUT-ORA-CONS.SP01.LOCAL",
  "user": "sys",
  "passWord": "totvs"
}
```

```
Para:  
{
  "pdbInstance": "ORA190PDB.SP01.LOCAL",
  "dbSource": "REALESTATEV1212610",
  "oraServer": "BH-AUT-ORA-CONS.SP01.LOCAL",
  "user": "sys",
  "passWord": "totvs"
}
```

## 5. Reativação de Agendamentos

1. **Habilitação:** Ativar a opção "Executar diariamente" nos agendamentos da **Nova Versão Atual (12.1.2610)**.   
   **Marcar** a flag: Repetir Tarefa  a cada minuto

## 6. Ajustes de Website (IIS)

**Projeto:** `ImbAlg_RecursoAlgConfiguraWebsitenoIIS`

Ajuste na versão **12.1.2606**:

JSON

```
{
  "WebSiteName": "FrameHTML",
  "PhysicalPath": "C:\\RM\\Legado\\12.1.2606\\FrameHTML",
  "HttpPort": "8080"
}
```

*Dica: Caso ocorram erros em outras atividades, verifique se existem caminhos físicos (PhysicalPath) estáticos que ainda apontam para a pasta "Atual" antiga.*
