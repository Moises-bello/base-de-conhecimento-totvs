---
content_hash: 80604c3105e2ff6d52a815aad05f46fb3a131ce1691d8bf367dcc7decd560d6e
fetched_at: '2026-06-29T00:08:19.202307+00:00'
page_id: '266979020'
product: rm
source: tdn-rm
title: RPT00018.1.1 - Opção Nome do Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266979020
version: 9
---

# Índice:

---

.\*ndice:

# Introdução:

---

       Com o advento da migração do **TOTVS Reports** da **versão 11.8x** para as versões **superiores a versão 12.1.4**, muitas alterações foram feitas principalmente **na geração sobre demanda dos dados** vinculados a cada componente presente no relatório.

Em relatórios da versão **11.8x**, por exemplo, **a geração sobre demanda dos dados** era realizada no momento da impressão de cada componente, ao contrário dos das versões mais atuais **(12.1.5 ou superiores)**, onde a geração dos dados é feita através de apenas uma consulta SQL **(Fase de Preparação)**, que é gerada a partir das tabelas e consultas SQL vinculadas ao relatório.

Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

# Como Executar:

---

     O componente **InformaçõesdaPagina** tem uma opção **(Nome do Usuário)** que apresenta o nome do usuário, **Dono** da **Thread** corrente.

* Executando o Relatório pelo **RM.exe**, o dono da **Thread** corrente é o usuário de rede. **Exemplo: carlos.farias.**

* Executando o Relatório pelo **Portal**, o dono da **Thread** corrente é o **IIS App Pool Identity**. **Exemplo: DefaultAppPool**.

Tanto na versão **10.1** dos componentes **Devexpress** utilizada na versão **11.8x** do **RM**, quanto na versão **14.1** dos componentes da **Devexpress** utilizada na versão **12.1.x** do **RM**, esse componente funciona dessa mesma maneira.

Existem diversas respostas do suporte da **Devexpress**, que respaldam esse comportamento, inclusive em outros componentes, outras **"suites"**, dessa mesma empresa.

**TÓPICO 1 : [Authentication Active Directory always IIS App Pool Identity (Autenticação Active Directory retorna sempre o IIS App Pool Identity)](https://www.devexpress.com/Support/Center/Question/Details/T404719)**

falseTradução

**[...]**

Nosso AuthenticationActiveDirectory funciona de forma bem simples - ele recebe o nome de usuário retornado pelo método **WindowsIdentity.GetCurrent()**.

**[...]**

**[...]**

Então, a aplicação irá autenticar com o usuário retornado pelo método **WindowsIdentity.GetCurrent()**.Preenche a propriedade. Nos não modificamos esse comportamento em nosso código.  

**[...]**

Da mesma forma, foi buscado uma solução para que pudéssemos modificar esse comportamento, porém sem sucesso, como respaldado pela resposta abaixo:

**TÓPICO 2 : [How to set the DevExpress.XtraPrinting.PageInfo.UserName when printing? (Como modificar a propriedade DevExpress.XtraPrinting.PageInfo.UserName na impressão?)](https://www.devexpress.com/Support/Center/Question/Details/CQ63200)**

falseTradução

**[...]**

Infelizmente, é impossível modificar o texto . Ele é recuperado através da configuração do sistema.

**[...]**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Opção Nome do Usuário

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
