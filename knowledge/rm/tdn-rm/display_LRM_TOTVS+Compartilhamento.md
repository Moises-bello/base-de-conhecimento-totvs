---
content_hash: 7efa8533ffc58eb44dbbb3bd53b8d3f59d92d676c54d20b3e2f925fce51635fc
fetched_at: '2026-06-29T00:08:55.367127+00:00'
page_id: '348297816'
product: rm
source: tdn-rm
title: TOTVS Compartilhamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento
version: 14
---

# Índice

---

.\*ndice

# Objetivo

---

       O TOTVS Compartilhamento é um recurso disponibilizado no RM, onde os clientes podem baixar objetos gerenciais, padrão, fornecidos pela TOTVS.

       Neste documento será explicado como baixar e importar para o sistema esses objetos gerenciais, como por exemplo, relatórios, gráficos, cubos, consultas SQL, planilhas e outros.

       Para utilizar esse recurso, é necessário , nos parâmetros globais do sistema.

Apenas arquivos fornecidos pela TOTVS são disponibilizados no TOTVS Compartilhamento.

# Localizando um objeto gerencial no TOTVS Compartilhamento

---

**1º)** Após fazer login no sistema, a funcionalidade**"TOTVS Compartilhamento"** estará disponível na lateral direita da tela, conforme mostrado na imagem abaixo:

Importante

Esta primeira pesquisa é executada na base de dados local e lista os objetos dos tipos: Consultas SQL, Gráficos, Cubos, Relatórios e Planilhas.

Caso a busca não encontre o termo especificado, você pode utilizar a busca Online para importar um novo objeto gerencial, conforme descrito nos demais passos.

         **2****º)**Para abrir a tela do TOTVS Compartilhamento com mais opções de filtros de busca, clique em "Não Encontrou? Pesquise na TOTVS":

**3****º)**Utilize os filtros Bucar, Tipo e Produto para localizar o objeto gerencial desejado. Neste exemplo, mostraremos como buscar relatórios da Folha de Pagamento:

* Selecione o Tipo: Relatório;
* Selecione o Produto: Folha de Pagamento;
* Clique no botão Pesquisar.

Para localizar outros objetos gerenciais, basta alterar os filtros. Para pesquisar um relatório específico, por exemplo, basta informar o seu código:

# Download de objeto gerencial no TOTVS Compartilhamento

---

**1º)** Selecione o(s) objeto(s) gerenciais que deseja fazer o baixar e clique no botão "Download". 

**2******º)****Existem duas opções ao fazer o download:

* Salvar o arquivo em um diretório do seu computador;
* Importar o arquivo direto na base de dados do RM;

Endereços à serem liberados 

Para o funcionamento do TOTVS Compartilhamento, devem ser liberados alguns endereços no proxy/firewall de sua rede: 

Veja mais detalhes aqui: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409626038551-Framework-Linha-RM-Frame-Endere%C3%A7os-TOTVS-Compartilhamento>

# Nova opção de acesso ao TOTVS Compartilhamento

---

     Criamos uma nova opção de acesso ao TOTVS Compartilhamento através de um botão na aba **Gestão | Utilitários.** Por padrão este acesso é bloqueado e é preciso realizar a liberação do mesmo em **"Acesso a Menus"** na visão de cadastro de perfil;

Importante

O acesso pela aba lateral, já existente até então, continua da mesma forma. Não sendo necessária nenhuma intervenção/liberação. Caso não queira mais utilizar esta forma antiga de acesso, basta desabilitá-la nos parâmetros globais do sistema [Habilitar o painel de pesquisa no Fluig](https://tdn.totvs.com/display/LRM/Habilitando+painel+de+pesquisa+no+Fluig).

Versões:

Disponível a partir das versões 12.1.31.273. 12.1.32.219, 12.1.33.146 e 12.1.34

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.x

false

**Processo:** TOTVS Compartilhamento

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
