---
content_hash: 37aa1d3e3afe3071227a1a6a6226667398d79c0d7ad447d956b0636198b1bc0d
fetched_at: '2026-06-29T00:10:43.935859+00:00'
page_id: '551432669'
product: rm
source: tdn-rm
title: 'Módulo: Processo Seletivo - SGE'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551432669
version: 11
---

|  |  |
| --- | --- |
| Descrição | Novidades do Template por Módulo: Processo Seletivo |
| Observações | Aplicável para SESI/SENAI. |

---

# **Módulo: Processo Seletivo**

## **LGPD****Termo de Consentimento do Processo Seletivo.**

Aplicável para SESI/SENAI.

**Objetivo**

Gravação do termo de aceite na inscrição do candidato.

**Parametrização**

O termo de aceite é definido na área ofertada do processo seletivo, conforme abaixo:

Se o termo da área ofertada não estiver preenchido, será exibido o termo de aceite padrão:

***Ao inscrever-me, estou ciente da importância das informações aqui descritas. Sei também que devo manter meus dados sempre atualizados, através deles poderei receber notícias durante e após o término das inscrições******.***

**Como o termo de aceite será exibido****?**

O termo de aceite será exibido ao final da inscrição do candidato pelo portal. Quando o candidato puder selecionar mais de uma opção de curso (Área ofertada), será considerado apenas o termo de aceite da 1ª opção selecionada na inscrição.

## **LGPD****Anonimização de Candidato.**

Aplicável para SESI/SENAI.

**Objetivo**

Possibilitar anonimizar o candidato do processo seletivo

**Situação / Requisito**

Para atender a Lei Nº 13.709/18 foi criado o processo "anonimizar usuários", este processo irá verificar se o usuário do processo seletivo possui algum vínculo com algum processo seletivo, se não possuir o processo irá excluir o usuário, caso este possua algum vínculo o sistema irá verificar algumas regras e se o usuário for elegível para anonimizar o sistema irá alterar os campos permitidos e definidos para um valor fictício

(ex: 000).

## **Venda Online****Área de Interesse Ofertada.**

Aplicável para SESI/SENAI.

**Objetivo**

A partir desta versão, haverá uma funcionalidade para exposição de vendas online, onde serão dispostos os processos seletivos e áreas ofertadas em cards, permitindo ao usuário ver detalhes e acessar a página de inscrição da área selecionada. Também será possível filtrar os processos por categoria a partir de botões embutidos na própria página e filtros por URL cujo os parâmetros serão: Coligada, Filial, IdPS, CodCategoria e AgruparPS. Nesta página também haverá disponibilidade de banner em destaque no topo em slider, que poderão ser definidos em cada um dos processos cadastrados. Nestes, será possível definir um título, um link de redirecionamento, prazo de validade e se está ativo ou não.

Esta nova funcionalidade é exibida em uma página separada do portal de inscrições, que será visualizada a partir da url [http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?](http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[c=1&f=1](http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1). Esta funcionalidade serve exclusivamente para deixar os cursos ofertados em exibição para os candidatos, que assim que clicarem em "Inscrever", serão redirecionados automaticamente para a inscrição naquele processo seletivo e área de interesse escolhida. Ao final desta documentação, é informada a configuração para utilização de filtros de exibição dos processos seletivos de venda online.

**Parametrização**

Para habilitar a funcionalidade e configurar as áreas ofertadas o usuário do sistema deverá acessar o Processo Seletivo.

***TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Oferta Online de Cursos | Anexo | Área de Interesse Of****ertad****a***

VS Portal do  cesso Seletivo

Dentro de Resumo serão cadastrados os detalhes da área de interesse ofertada.

Dentro da aba Imagem será cadastrada a imagem de exibição para a área de interesse ofertada. É importante ressaltar que todas as imagens cadastradas para cada área de interesse ofertada devem manter a mesma proporção de tamanho para cada processo seletivo (exemplo: 240x135 pixels).  
Este tamanho reflete diretamente à aparência e alinhamento das opções de áreas de interesse ofertada.

**Nova visão no Portal de Inscrição do Processo Seletivo por Venda Online**

**Filtro por parâmetro URL**

A coligada e filial são obrigatórias, já os outros parâmetros (IdPS, CodCategoria e AgruparPS) são opcionais, os parâmetros serão passados via URL:

Exemplo: <http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1>  (**aqui está parametrizado coligada = 1 e filial = 1)**

Caso queira por exemplo filtrar por CodCategoria ficaria desta forma:

<http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2> (onde o ct = 2)

Caso queira por exemplo filtrar por AgruparPS (nivel de ensino) ficaria desta forma:

<http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ne=2> (onde o ne = 2)

Também é possível utilizar todos os filtros de uma só vez:

<http://dominio.com.br/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ps=136&ct=2&ne=2>

Os parâmetros

-Coligada e Filial: ?f=1&c=1 (Obrigatório)

-IdPS: &ps=136

-CodCategoria: &ct=2

-AgruparPS: &ne=eb

Após realizadas as devidas parametrizações no sistema, o processo seletivo parametrizado estará pronto para utilização no portal.

## Inscrição no Processo Seletivo com Questionário Sócio-Econômico

Aplicável para SESI/SENAI.

[Questionário Sócio Econômico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025945054-RM-PS-Inscri%C3%A7%C3%A3o-com-Question%C3%A1rio-S%C3%B3cio-Econ%C3%B4mico-Novo-portal-de-inscri%C3%A7%C3%B5es)

**Objetivo**

Disponibilização de um questionário sócio-econômico que o candidato deve preecher para se inscrever no processo seletivo.

**Parametrização**

Para utilizar o questionário socioeconômico no novo portal de inscrições, basta vincular um questionário criado no TOTVS Avaliação e Pesquisa, no cadastro do processo seletivo.

TOTVS Processo Seletivo| Cadastros| Processo seletivo| Aba Informações Complementares

Ao acessar o portal de inscrições, será criado um novo passo na inscrição permitindo que o candidato responda o questionário.

Atenção
