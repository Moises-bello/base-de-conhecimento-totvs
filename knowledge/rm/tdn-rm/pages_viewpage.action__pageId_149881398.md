---
content_hash: 7bfa9fa2af24e090782b72852a08b3b4d2d5512e10da8be74a15dfcdbda98f82
fetched_at: '2026-06-29T00:05:56.279917+00:00'
page_id: '149881398'
product: rm
source: tdn-rm
title: Utilizando a atividade "Consultar Parâmetros do Processo"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881398
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso das atividades Consultar Parâmetros do Processo e Transformar Registro/Tabela em XML.

# Configuração:

---

false.1) Atividade Consultar Parâmetros do Processo

* Nesta atividade devemos informar o nome do Processo que devemos utilizar na execução da fórmula visual, conforme print abaixo:

* Informe o nome do processo, na tela de pesquisa.

2) Atividade Transformar Registro/Tabela em XML

* Nas propriedades da atividade informe os valores abaixo:

**Modo XML** – IgnoreSchema

**Tabela** – Clicar no "Cilindro Amarelo (Localizado ao lado da escrita tabela, veja no exemplo abaixo)" e aponte para a atividade de Consultar Parâmetros do Processo criada no passo anterior. Deve-se atentar que devemos selecionar a opção Tables[0] e a opção DataTable, conforme print abaixo:

    

3) Atividade Gerar Exceção

         Podemos através desta opções obter quais são os parâmetros que o processo disponibiliza utilizando algumas atividades, como Gravar Log, Gerar Exceção, expressão, etc.

* Esta atividade tem a finalidade de interromper um determinado processo ou ação de salvar um cadastro, por exemplo, e informar uma determinada mensagem ao usuário.

    

* Para exibir o XML com os parâmetros do processo, nas propriedades desta atividade, clicamos no botão  no campo MENSAGEM, apontamos para a atividade Transformar Registro/Tabela em XML, e selecionamos a opção XML, ficando conforme prints abaixo:

   

* Ao executarmos o processo será exibida uma mensagem de "erro" para o usuário com um XML contendo os parâmetros que existem no processo. Neste exemplo utilizamos o processo de Associação de Itens ao Contrato e o XML exibido é conforme o print abaixo:

     

falsefalse

**Produto:** Framework

false

**Versão:** 11.50.XX e 11.80.XX

false

**Processo:** Fórmula Visual - Consultar Parâmetros do Processo

falsefalse

**Status:** Finalizado

false

**Data:** 10/05/2016

false

**Autores:**
