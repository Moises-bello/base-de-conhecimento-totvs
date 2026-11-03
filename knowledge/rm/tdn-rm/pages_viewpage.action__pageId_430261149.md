---
content_hash: 71c1992bc0cb77c1eda6220941e8b4e4ad66569fd3da48019a6ebac2218b152b
fetched_at: '2026-06-29T00:09:38.739049+00:00'
page_id: '430261149'
product: rm
source: tdn-rm
title: Exportação e Importação de Códigos Fontes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=430261149
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer uma visão do funcionamento do processo de exportação e importação de códigos fontes (SourceCode), para serem editados fora do RM

# Introdução:

---

Importante

A partir da versão 12.1.31 (e superiores), é possível realizar alterações em códigos-fonte diretamente pelo RM em ambientes SmartClient ou 3 camadas (Client). Para informações acerca deste comportamento, acesse a documentação: ["Executar Código Fonte" em ambientes SmartClient / 3 Camadas](https://tdn.totvs.com/x/a80pJw), para compreender as limitações e informações importantes.

Uma vez que o editor de códigos fontes (SourceCode) necessita de todas as DLLs (camada cliente e servidor) para compilar um código fonte cadastrado, em ambientes SmartClient ou na camada Client para ambientes 3 camadas, uma das formas para editar o código é seguinte:

***Passo a passo para realização do processo:***

false111° Passo

Na tela de cadastro de códigos fontes, clique no menu processos e escolha a opção exportação do código fonte para xml.

22° Passo

Após a solicitação ser processada, salve o arquivo e em seguida edite-o com um editor de sua preferência.

Recomendamos que seja feito um backup deste arquivo xml antes da edição, pois os mesmos não possuem controle de versão.

Caso tenha o RM instalado em um ambiente local, o arquivo poderá ser editado no próprio editor do RM.

33° Passo

Após concluir a edição do código fonte, para que as alterações tenham efeito, o mesmo deve ser importado. Para isso, acesse a tela de cadastro de códigos fontes, clique no menu processos e escolha a opção importação do código fonte para xml.

44° Passo

Selecione o arquivo que acabou de editar

55° Passo

Após selecionado será dado início ao processo de importação, onde o código fonte será compilado.

Caso seu código fonte seja compilado com sucesso, o mesmo será atualizado em sua base de dados substituindo o código anterior.

A compilação com sucesso não garante que a regra de negócio esteja de acordo. Após a importação efetue as devidas validações.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superiores

false

**Processo:** Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2018

false

**Autores:**
