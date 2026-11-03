---
content_hash: bf82615d45ff36b979ef48a8ee6a6cb52dac0d3a647599dad0d676ee6ffe9c92
fetched_at: '2026-06-29T00:05:56.333448+00:00'
page_id: '149881506'
product: rm
source: tdn-rm
title: Utilizando a atividade "Ler Visão"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881506
version: 24
---

# Índice:

---

* Objetivo:
* Configuração:

# Objetivo:

---

     Este documento tem como finalidade, demonstrar o uso da atividade **"Ler Visão"**.

falseConfiguração

Esse tópico serve para apresentar as informações de como utilizar a atividade "Ler Visão" e apresentar um exemplo prático bastante útil, afim de facilitar o uso da atividade.

falseInformações Gerais

Objetivo: A finalidade da atividade "Ler Visão" é permitir que o usuário recupere dados de uma visão vinculada à um DataServer específico.

Passo a Passo: Primeiramente é necessário arrastar a atividade "Atualizar Registros Localizando na Tabela" para o "Fluxo de Trabalho Sequencial" em sua fórmula visual.

Após atividade ter sido adicionada ao fluxo de trabalho, é necessário configurar as propriedades da atividade.

No exemplo acima, as propriedades foram preenchidas da seguinte maneira

Após preencher as propriedades, salve e execute a <strong>Fórmula Visual</strong>. Verifique o resultado do processo. A <strong>Fórmula Visual</strong> deverá executar com sucesso. Com isso poderemos seguir para o exemplo de utilização real da atividade.

# EXEMPLO PRÁTICO

Vamos agora ver um exemplo prático do uso da atividade "Ler Visão".

Iremos acrescentar a atividade de Enviar E-mail e configurá-la adequadamente.

OBS

Lembre-se de preencher corretamente o assunto do e-mail,os destinatários, remetente e testo do e-mail. Como exemplo colocamos a informação obtida pela atividade "Ler Visão" como texto do e-mail.

OBS

[Mais de "Atividade Enviar E-mail"](http://www.tdn.totvs.com/pages/releaseview.action?pageId=146184224)

Salve e execute e veja o resultado

```

```

```

```

Segurança na Atividade

A partir das versões **12.2302.104**,  **12.1.2209.176**, **12.1.2205.230** para que a atividade valide as permissões do Usuário que está executando a Formula visual e aplique a mesma segurança do **Data Server** é necessário habilitar a propriedade 'Aplicar segurança nas atividades do fluxo de trabalho'.

falseParâmetros da AtividadefalseFiltroDetalhes da Propriedade Filtro

**Descrição:** Filtro do DataServer escolhido na propriedade "Nome do DataServer". Permite filtrar a tabela resultante.  
**Tipo:** String (Cadeia de caracteres)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o filtro do DataServer escolhido na propriedade "Nome do DataServer".  
**Valor Utilizado na Requisição:** CODCOLIGADA = 6

falseNome do DataServerDetalhes da Propriedade Nome do DataServer

**Descrição:** Nome do DataServer que será utilizado para recuperar os dados da visão.  
**Tipo:** String (Cadeia de caracteres)  
**Como Usar:** Esse parâmetro é do tipo **Cadeia de Caracteres**, ou seja, deve-se utilizar um valor alfanumérico que represente o nome do DataServer que será utilizado para recuperar os dados da visão.  
**Valor Utilizado na Requisição:** GlbColigadaDataBR

falseRetorno da AtividadefalseDados da LeituraDetalhes da Propriedade Dados da Leitura

**Descrição:** Fonte de Dados resultante da leitura da visão.  
**Tipo:** DataSet (Conjunto de Tabelas em Memória)  
**Como Usar:** Esse parâmetro é do tipo **Conjunto de Tabelas em Memória**, e representa a fonte de dados responsável por preencher as informações na visão.  
**Valor Utilizado na Requisição:** CODCOLIGADA;CODFILIAL

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
