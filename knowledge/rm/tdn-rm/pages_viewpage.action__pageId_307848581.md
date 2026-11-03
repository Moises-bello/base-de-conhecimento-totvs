---
content_hash: 399fda50be85ba91491427adfc853eaa84d9161db93a625fce78dd635ea633a4
fetched_at: '2026-06-29T00:08:44.376217+00:00'
page_id: '307848581'
product: rm
source: tdn-rm
title: Configuração do parâmetro Habilitar Painel Social
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307848581
version: 8
---

# Índice

---

.\*ndice

# Introdução

---

        A configuração do parâmetro global **Habilitar Painel Social**, quando habilitada, tem como função exibir o usuário que criou e o último usuário quem editou um registro de cadastro.

Exemplo:

        As fotos são buscadas do cadastro do funcionário. Assim, apenas o usuário associado à um funcionário com foto terá sua imagem exibida na visão. Caso contrário, será exibido a imagem padrão do sistema; mas é possível ver o nome do usuário ao passar o mouse sobre a imagem.

        O Painel Social será exibido apenas em telas que possuem os campos "RECCREATEDBY" e "RECMODIFIEDBY" no método ReadRecord da visão. Para o exemplo deste documento, alteramos a tela de cadastro de usuário apenas para teste. Se o cliente desejar usar tal funcionalidade em alguma tela que não possua tais campos, o suporte da totvs deve ser acionado para análise de viabilidade.

# Exemplo

---

      Veja como utilizar o painel social:

false.1° Passo:

Acesse o menu Ambiente > Parâmetros > Parâmetros Globais > Aba Comunicação com redes sociais e marque a configuração **Habilitar painel social**;

2° Passo:

Faça o login no sistema com um usuário que esteja associado à um funcionário.

Depois acesse o cadastro de usuário em Serviços Globais > Segurança > Usuários.

Obs.: O cadastro de usuários está sendo usado apenas para exemplificar a funcionalidade, pois a mesma não apresenta os campos "RECCREATEDBY e RECMODIFIEDBY" na visualização. Esses foram inseridos manualmente pelo desenvolvimento para testes.

Crie um novo usuário - no rodapé da tela será exibida a imagem e o nome do usuário que fez o cadastro:

3° Passo:

Faça login no sistema com outro usuário, que não tenha seu cadastro associado à um funcionário.

Depois acesse a tela de usuário e edite o cadastro feito no passo anterior.

A imagem do usuário será exibida como a padrão do sistema, mas ao passar o mouse sobre o ícone é possível ver o nome.

É possível expandir o histórico e visualizar todos os registros que o usuário editou ou criou.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.19 ou superiores

false

**Processo:** Configuração do parâmetro Habilitar Painel Social

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
