---
content_hash: d7310a3333dad6cb2106ebcafbfc97eeb8963ae20ad39ec5fa1362de5de4c665
fetched_at: '2026-06-29T00:08:06.942775+00:00'
page_id: '236597253'
product: rm
source: tdn-rm
title: TOTVS Business Connector - Novo Conceito
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Business+Connector+-+Novo+Conceito
version: 21
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        O objetivo deste documento é trazer as melhorias e novidades realizadas no Novo Conceito.

# Introdução:

---

       O Conceito é a estrutura responsável por armazenar os dados de conexões (de vários tipos) dos sistemas de origem e destino.

# Melhorias:

---

* Novo designer mais simples, com funcionamento baseado em drag & drop;

* Leitura e geração de arquivos texto em memória ou direto no disco;

* Leitura de dados de origem em lotes podendo quebrar por intervalos de data e números (o que permite a leitura dos dados de origem quebrando por data ou coligada por exemplo);

* Permitir a atualização dos dados de origem do processamento;

* Log de validação estrutural do conceito para não permitir a execução de conceitos montados de forma errada;

* Log detalhado de erros de processamento integrado com o Monitor da integração;

* Permitir a utilização de múltiplas conexões de origem ou destino;

* Permitir a utilização de Lookup nas conexões de Data Server e Banco de Dados;

* Permitir a criação de parâmetros para execução do conceito;

* Criação de arquivo do conceito (ICP) simplificado;

* Otimização do uso de memória trabalhando diretamente com os objetos específicos da conexão ao invés de trabalhar somente com Datasets;

* Otimização da rotina de geração percorrendo os dados de origem o menor número de vezes possível;

* Novo operador do tipo “Expressão”;

* Conexão Web Services com suporte para leitura e escrita.

# Processo:

---

**Processo do Novo Conceito****:**

* O processo do Novo Conceito é composto de conexões, operações, parâmetros, expressões e valores fixos, que juntos formam as ligações para a conexão de saída.

# Conexões:

---

Conexão Data Server**:**

**Novidades:**

* Novo designer;

* Utilização de um contexto padrão ou um contexto fixo;

* Permite a utilização de lookups;

* Permite continuar a operação de salvamento mesmo que ocorra erros ao salvar algum registro;

* Permite a atualização da origem;

**Conexão Banco de Dados:**

**Novidades:**

* Configuração simplificada

* Permite a utilização de tabelas ou consultas SQL

**Conexão TXT:**

**Novidades:**

* Configuração Simplificada
* Gravação Parcial
* Não trabalha mais com Datasets

**Conexão WBS WEBSERVICES:**

**Novidades:**

* Designer simplificado
* Permite ser utilizado como conexão de entrada e de saída
* Ele só funciona com WebServices que retorna uma tabela. ([Segue exemplo](http://tdn.totvs.com/x/tpKZH))

# Operadores:

---

**Novidades:**

* Novos designers especializados
* Cache e reaproveitamento de operadores

# Parâmetros:

---

**Novidades:**

* Possibilidade de criação de diversos tipos de parâmetros para utilização em filtros ou no próprio conceito.

# Filtros:

---

**Novidades:**

* Novo mecanismo de filtro com suporte a parâmetros da execução do conceito.
* Suporte a filtros definidos pelo usuário.

# Log de Execução Resumido:

---

**Novidades:**

* Possibilidade de informar se um determinado conceito irá apresentar um log resumido ao final de sua execução.
* O valor padrão deste novo campo é desmarcado, ou seja, caso o mesmo não seja marcado será gerado o log completo normalmente.

Este recurso estará disponível apenas a partir da versão 12.1.34.

# Permissões / Perfil

---

**Permissão unificadas**

* Ao acessar a aba **Acesso a Menus** na tela de um determinado **Perfil**, será possível habilitar ou desabilitar o acesso aos menus de forma unificada, ou seja, ou habilita os dois menus (Processar Antigo e Novo Conceito) ou desabilita os dois:

# Codificação de Caracteres do Arquivo:

---

Quando trabalhamos com uma conexão de destino do tipo Texto podemos escolher um tipo de codificação para os caracteres do texto que será gerado, como por exemplo ASCII e UTF8. Abaixo seguem alguns exemplos:

ASCII

Configuração:

Texto gerado:

UTF8

Configuração:

Texto gerado:

UTF7

Configuração:

Texto gerado:

Importante

É importante frisar que devemos verificar se o conteúdo do arquivo está na codificação escolhida e não a informação que é exibida ao abrir o arquivo no Bloco de Notas ou similares.

No exemplo abaixo o arquivo foi exportado na codificação ASCII e seu conteúdo está corretamente na codificação escolhida, mesmo apresentando a informação de UTF-8 no rodapé do Bloco de Notas.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** TOTVS Business Connector Novo Conceito

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
