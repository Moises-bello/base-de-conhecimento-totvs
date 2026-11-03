---
article_id: 34510407623703
category: eSocial - Gerar XML/ Integração Evento
content_hash: 64daf5aea01e8e9909ac1e63021013aea590b1bf84c87af2d58d34a02ad04bd3
fetched_at: '2026-06-28T22:47:12.997871+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ORA-01843: not a valid month / não é um mês
  válido ao executar rotinas do eSocial'
type: support-article
updated_at: '2025-08-28T15:35:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34510407623703-RH-RM-FOP-eSocial-Erro-ORA-01843-not-a-valid-month-n%C3%A3o-%C3%A9-um-m%C3%AAs-v%C3%A1lido-ao-executar-rotinas-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34510407601047) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao executar determinado processo no módulo do **eSocial**, o sistema apresenta a seguinte inconsistência, erro:  
**ORA-01843:**not a valid month.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34510401991575)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**  
A parametrização do ***Language*** do Oracle não corresponde as definições recomendadas para o CorporeRM.  
  
**Solução 1:**  
Para que o erro seja solucionado, recomendamos que os passos abaixo sejam aplicados pelo DBA ou responsável pelo Banco de Dados da empresa:  
  
1. Acessar o **redegit**;  
2. Localizar a **home do Oracle:**  
  
HKEY\_LOCAL\_MACHINE\SOFTWARE\ORACLE\KEY\_OraDb\_home1  
HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Oracle\KEY\_OraDb\_home1  
  
3. Incluir a chave ***NLS\_DATE\_FORMAT*** com o valor **DD/MM/YYYY**.  
4. Acertar o parâmetro***NLS\_LANG*** para **AMERICAN\_AMERICA.WE8ISO8859P1**;

A exceção do Oracle **ORA-01843** normalmente é apresentada no CorporeRM, quando a parametrização de Formato de Data ou Linguagem está fora do padrão recomendado pela Totvs.  
  
**Solução 2:**

**ORACLELANGUAGE**

O idioma da sessão de conexão do RM com uma base Oracle pode ser alterar através da *tag* de configuração chamara **OracleLanguage** no arquivo **RM.exe.config.**  
O valor padrão desta chave é **PT-BR**. O sistema deve considerar a linguagem **EN-US** do banco Oracle para na configuração do Server utilizando a *tag* **ORACLELANGUAGE**:

```
<add key="OracleLanguage" value="en-US"/>
```

Após inserir a *tag*, reinicie o serviço de *host*, reabra a aplicação e execute o processo novamente.

**Importante:**

* Caso utilize ambiente 3 camadas, a alteração deve ser realizada no Servidor de APP.
* Só devem ser alterados os parâmetros **NLS\_LANG** listados que tiverem com o valor *Brazilian*, os registros que estiverem com N/A não devem ser alterados.
* Essa inconsistência pode ser apresentada por outros motivos, sendo assim, caso a inconsistência persista, recomendamos um contato com o suporte do módulo onde o erro foi apresentado.

Saiba Mais:  
[Framework - Framework RM - BD - ERRO ORA-01843: NÃO É UM MÊS VÁLIDO / NOT A VALID MONTH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003110012--Framework-Framework-RM-BD-ERRO-ORA-01843-N%C3%83O-%C3%89-UM-M%C3%8AS-V%C3%81LIDO-NOT-A-VALID-MONTH)
