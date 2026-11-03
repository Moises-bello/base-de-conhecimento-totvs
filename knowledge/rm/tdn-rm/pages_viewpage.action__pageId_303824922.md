---
content_hash: b97bed5f176d8771bfbdb8aa450e47e5f2cef7837b525e2ddb3dc7ab7444a656
fetched_at: '2026-06-29T00:08:43.581647+00:00'
page_id: '303824922'
product: rm
source: tdn-rm
title: RPT00018.2 - Propriedade Seção Corrente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=303824922
version: 25
---

# Índice

---

.\*ndice

# Objetivo

---

          O objetivo deste documento é exemplificar como utilizar o componente “Informações da Página” para contabilizar as páginas reiniciando a contagem após quebra em cabeçalho do detalhe escolhido.

          Como exemplo: Configurar um relatório de “Registro de Funcionário” para que a contagem de páginas reinicie sempre que houver quebra associada ao funcionário.

          Desta forma será possível gerar o relatório para vários registos e a cada funcionário diferente a contagem de páginas seja reiniciada.

# Introdução

---

          Esta configuração atende as situações onde a contagem das páginas será reiniciada assim que uma quebra for realizada. Para realizar essa configuração siga os passos seguintes.

falsePasso a PassoPasso 1Passo 1Passo 1

          Acesse a “Caixa de Ferramentas” e inclua na estrutura do relatório o controle "Informações da Página".

Selecione o controle e mantenha pressionado o botão esquerdo do mouse. Arraste o controle e posicione-o no relatório onde a informação será impressa. No exemplo arrastamos o controle para o grupo “Rodapé da Página”.

false

          O menu “Caixa de Ferramentas” fica localizado na visão direita da edição do RM Reports. Caso esteja desabilitado, acesse o menu “Exibição | Janelas | Ferramentas”.

Passo 2Passo 2Passo 2

Configure a quebra no seu relatório. Selecione o grupo onde será incluso o “Cabeçalho do Detalhe” e no cabeçalho do detalhe configure a quebra. No exemplo abaixo incluímos no grupo “Detalhe1” o “Cabeçalho do Detalhe12”

Configure a quebra no “Cabeçalho do Detalhe”. Para configurar a quebra, clique no grupo “Cabeçalho do Detalhe” e tecle F4 (ou acesse suas propriedades). Na barra de propriedades do controle clique em “Ordenação / Quebra”.

Será apresentado uma visão para que seja configurado o campo que será realizado a quebra do relatório.

Para incluir o campo clique no botão “Adicionar”. Habilitará ao lado uma opção onde será possível procurar pelo campo designado para quebra. No exemplo selecionamos a coluna CHAPA da tabela de funcionários (PFUNC).

false

          Os campos disponíveis para quebra são pertencentes a tabela máster do grupo.

Definido a quebra, clique no controle “Informações da Página” e tecle F4 (ou acesse as propriedades do controle).

Na propriedade “Seção Corrente” do controle selecione o grupo onde foi configurado a quebra do relatório.

Passo 3Passo 3Passo 3

Depois de feitas as configurações geramos o relatório para confirmarmos a contagem de página reiniciando conforme a quebra definida.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.5 ou superiores

false

**Processo:** Totvs Reports

false

**Subprocesso:** Reiniciar contagem de páginas

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
