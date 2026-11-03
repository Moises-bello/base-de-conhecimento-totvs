---
content_hash: 925c6f4309d8dcd879dc4007c7964d577a6193b9acba4a1333b40519241f289c
fetched_at: '2026-06-29T00:12:07.441385+00:00'
page_id: '925361487'
product: rm
source: tdn-rm
title: Guia de manutenção para Banco de Dados Oracle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925361487
version: 12
---

Para garantirmos mais qualidade em nossos produtos implementamos a execução de testes automatizados com bases Oracle.

Isto foi possível a partir da versão 12c na qual foi implementado o conceito de *Pluggable Database* (PDB). O Oracle passou a trabalhar com um container no qual podem existir várias bases plugáveis. Nestas bases é possível a execução de várias operações e maneira muito fácil e rápida:

* Criação
* Clonagem (duplicação)
* Deleção
* Renomear

## **Como funciona o processo de Restauração de Bases Oracle no TOTVS Automação de Testes - Linha RM**

O que é necessário?

* Um Servidor com Oracle Server na versão 12c ou superior.
* Um Projeto de testes que possua uma Atividade de Restauração de Base Oracle.
* Um backup de base Oracle.

O backup da base Oracle é restaurado no Servidor e fica sempre em estado de somente leitura (READ ONLY).

Ao executar o Projeto, a Atividade de Restauração de Banco clona esta base e este clone fica com o estado de leitura e escrita (READ WRITE).

O TOTVS Automação de Testes executa todas as Atividades contidas no Projeto e posteriormente deleta este clone.

## **Atualização de Scripts na Base Modelo**

Este processo é essencial para garantir que as bases estejam alinhadas com os requisitos da aplicação e atualizadas com os últimos recursos e patches.

### Etapas do Processo:

1. **Clone sua base modelo:**

   * Gere uma cópia da base modelo existente.
   * Exemplo de comando: `CREATE PLUGGABLE DATABASE CLONEMODELO FROM MODELO;`
2. **Coloque o clone em modo READ WRITE:**

   * Por padrão, os clones podem ser criados como somente leitura. Habilite o modo de escrita com:

     ```
     ALTER PLUGGABLE DATABASE CLONEMODELO OPEN READ WRITE;
     ```
3. **Aplique os scripts de atualização:**

   * Utilize uma ferramenta de gerenciamento de scripts ou execute os scripts diretamente no Oracle SQL Developer.
4. **Certifique-se de que a base está funcional:**

   * Execute testes específicos para garantir que as tabelas, dados e funcionalidades estão como esperado.
5. **Substitua a base original pelo clone atualizado:**

   * Delete a base original.
   * Renomeie o clone atualizado para o nome original da base.

## **Deleção de Bases no Servidor Oracle**

Deletar bases antigas ou não utilizadas é essencial para manter o servidor organizado e otimizar o uso de recursos.

### Etapas do Processo:

1. **Identifique a base a ser deletada:**

   * Liste as bases existentes para confirmar o nome correto da base a ser removida.
   * Exemplo de comando: `SHOW PDBS;`
2. **Desconecte a base do container:**

   * Certifique-se de que não há sessões conectadas:

     ```
     ALTER PLUGGABLE DATABASE NOMEDABASE CLOSE IMMEDIATE;
     ```
3. **Delete a base:**

   * Use o comando abaixo para remover a base e seus arquivos:

     ```
     DROP PLUGGABLE DATABASE NOMEDABASE INCLUDING DATAFILES;
     ```
4. **Verifique a remoção:**

   * Confirme que a base foi removida da lista:

     ```
     SHOW PDBS;
     ```

## **Informações Importantes**

* **Padrão de nomes:** Use nomes claros e consistentes, como `MODELO1212402` para identificar versões.
* **Conexões:** Certifique-se de usar o domínio completo ao referenciar bases.
* **Usuários e permissões:** As operações descritas requerem permissões de administrador no Oracle. Garanta que o usuário possui as credenciais adequadas.
* **Backup:** Sempre mantenha backups antes de realizar operações críticas para evitar perda de dados.
