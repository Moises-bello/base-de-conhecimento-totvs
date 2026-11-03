---
content_hash: ca707bc29a9b84814be54500edeb1fe239cae88ceb56fb7229a6034030b67c2f
fetched_at: '2026-06-29T00:11:10.258525+00:00'
page_id: '642951420'
product: rm
source: tdn-rm
title: 03 - Tela inicial do portal
type: documentation
url: https://tdn.totvs.com/display/LRM/03+-+Tela+inicial+do+portal
version: 5
---

Esta tela será a exposição de vendas online, onde estão dispostos processos seletivos e áreas ofertadas em cards permitindo ao usuário ver detalhes e adicionar o curso que deseja adquirir. Também será possível filtrar os processos por categoria a partir de botões embutidos na própria página e filtros por URL cujo os parâmetros serão: Coligada, Filial, IdPS, CodCategoria e AgruparPS. Nesta página também haverá disponibilidade de banner em destaque no topo em slider, que poderão ser definidos em cada um dos processos cadastrados, nestes será possível definir um link de redirecionamento, prazo de validade e se está ativo ou não.

Verifique as configurações no RM:

***Portal E-commerce de cursos:***

**Banner**

Aqui será o resultado de tudo que foi parametrizado acima em "**TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Venda Online de Cursos | Anexo | Banner**", os banners que foram definidos lá serão exibidos desta forma na página do portal.

**Filtro por Categoria**

As categorias apresentadas como campo de seleção, serão de acordo com a categoria vinculada ao processo seletivo.

**Processo Seletivo e Áreas de interesse ofertadas**

Assim será exibido as áreas ofertadas dentro de cada processo seletivo de acordo com a parametrização feita em "**TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Venda Online de Cursos | Anexo | Área de Interesse Ofertada",** observe que a imagem é a mesma que foi cadastrada em **"Portal | Imagem"**

Quando clicar em **"Mais Detalhes"** será exibido um modal de acordo com a parametrização feita em **"Portal | Resumo"**

**Filtro por parâmetro URL**

A coligada e filial são obrigatórias, já os outros parâmetros (IdPS, CodCategoria e NivelEnsino) são opcionais, os parâmetros serão passados via URL:

Exemplo: [http://](http://xn--local_de_instalao-nqb9e/FrameHTML/web/app/Edu/PortalGestaoEducacional/)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web/app/Edu/PortalEcommerceCurso/#/home?c=1&f=1](http://xn--local_de_instalao-nqb9e/FrameHTML/web/app/Edu/PortalGestaoEducacional/)  (aqui está parametrizado coligada = 1 e filial = 1)

Caso queira por exemplo filtrar por CodCategoria ficaria desta forma: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/app/edu/](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)[PortalEcommerceCurso/#/home](http://xn--local_de_instalao-nqb9e/FrameHTML/web/app/Edu/PortalGestaoEducacional/)[?c=1&f=1&ct=2](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)

Caso queira por exemplo filtrar por NivelEnsino ('es' para Ensino Superior e 'eb' para Ensino Básico) ficaria desta forma: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/app/edu/](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)[PortalEcommerceCurso/#/home](http://xn--local_de_instalao-nqb9e/FrameHTML/web/app/Edu/PortalGestaoEducacional/)[?c=1&f=1&ne=e](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)s

Também é possível utilizar os filtros combinados, por exemplo, para visualizar todos os processos seletivos com categoria 1 e nível de ensino "Ensino Superior" da Coligada 1 e Filial 1: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/app/edu/](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)[PortalEcommerceCurso/#/home](http://xn--local_de_instalao-nqb9e/FrameHTML/web/app/Edu/PortalGestaoEducacional/)[?c=1&f=1&ct=1&ne=e](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)s

**Os parâmetros**

- Coligada e Filial: ?f=1&c=1 **(Obrigatório)**  
- IdPS: &ps=136  
- CodCategoria: &ct=2  
- NivelEnsino: &ne=eb
