---
content_hash: 9971196a61b355a67c04d80bb1bb5bb82733b8a8e0e48087ff3928dd0af500a1
fetched_at: '2026-06-29T00:10:25.377361+00:00'
page_id: '504792560'
product: rm
source: tdn-rm
title: Venda Online Área de interesse ofertada (Portal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504792560
version: 16
---

Atenção

Esta funcionalidade está disponível a partir da versão 12.1.25

A partir dessa versão haverá uma funcionalidade para exposição de vendas online, onde dispostos processos seletivos e áreas ofertadas em cards permitindo ao usuário ver detalhes e acessar a página de inscrição da área selecionada, também será possível filtrar os processos por categoria a partir de botões embutidos na própria página e filtros por URL cujo os parâmetros serão: Coligada, Filial, IdPS, CodCategoria e AgruparPS. Nesta página também haverá disponibilidade de banner em destaque no topo em slider, que poderão ser definidos em cada um dos processos cadastrados, nestes será possível definir um título, um link de redirecionamento, prazo de validade e se está ativo ou não.

Informação

Esta nova funcionalidade é exibida em uma página separada do portal de inscrições, que será visualizada a partir da url [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1), esta funcionalidade serve exclusivamente para deixar os cursos ofertados em exibição para os candidatos, que assim que clicarem em "Inscrever", serão redirecionados automaticamente para a inscrição naquele processo seletivo e área de interesse escolhida. Ao final desta documentação é informada a configuração para utilização de filtros de exibição dos processos seletivos de venda online.

**Parametrização:**

Para habilitar a funcionalidade e configurar as áreas ofertadas o usuário do sistema deverá acessar o Processo Seletivo.

**TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Venda Online de Cursos | Anexo | Área de Interesse Ofertada**

Figura 1 – Áreas de interesse ofertadas

Ao acessar o menu citado acima, selecione uma das Áreas de interesse ofertadas e dê um duplo clique. ***(Figura 1)***

Figura 2 - Seleção de Área de interesse ofertada: EM - 1ª Série (M)

Em seguida acesse a aba **“Venda online de cursos” e “Portal”. *(Figura 2)***

**Portal | Resumo**

Figura 3 - Resumo: detalhes da área de interesse ofertada

Dentro de resumo será cadastrado os detalhes da área de interesse ofertada, é possível utilizar todos os recursos de formatação disponibilizado conforme destaque na ***Figura 3.***

**Portal | Imagem**

Figura 4 -  imagem definida para exibição de área de interesse ofertada no portal.

Dentro da aba **Imagem** será cadastrado a imagem de exibição para a área de interesse ofertada, para cadastrar a imagem clique no botão em destaque na *Figura 4* e em seguida selecione a imagem desejada, é importante ressaltar que todas as imagens cadastradas para cada área de interesse ofertada devem manter a mesma proporção de tamanho para cada processo seletivo (exemplo: 240x135 pixels).  ***Este tamanho reflete diretamente à aparência e alinhamento das opções de áreas de interesse ofertada.***

**TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Venda Online de Cursos | Anexo | Banner**

Figura 5 - Selecionado Processo Seletivo > Anexo > Banner

Pode ser cadastrado um ou mais banners para cada processo seletivo, para cadastrar o banner basta clicar no botão em destaque na *Figura 5.* Importante ressaltar que todos os banner cadastrados devem manter a mesma proporção de tamanho (exemplo: 1650x528 pixels)*.*

***Este tamanho reflete diretamente à aparência e alinhamento da disposição do banner no portal.***

Figura 6 - Parametrização Banner

Este banner aparece de acordo com o Checkbox ATIVO, quando está marcado será exibido no portal desde que o “Processo Seletivo” também esteja ATIVO, poderá ser cadastrado um título que será exibido também no portal, defina um link para que quando clicado seja redirecionado, é possível também definir um período datado para exibição do banner e suas respectivas ordens que serão determinadas em ordem crescente, ambas parametrizações podem ser vistas na *Figura 6.*

***Vendas Online Portal Processo Seletivo:***

Figura 7 - Portal Processo Seletivo Venda Online

**Banner**

Figura 8 - Banner

Aqui será o resultado de tudo que foi parametrizado acima em "**TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Venda Online de Cursos | Anexo | Banner**", os banners que foram definidos lá serão exibidos desta forma na página do portal.

**Botões de Filtro por Categoria**

Figura 9 - Botões de Filtro por Categoria

As categorias apresentadas como botão de filtro serão de acordo com a categoria vinculada ao processo seletivo.

**Processo Seletivo e Áreas de interesse ofertadas**

Figura 10 - Processo Seletivo e Áreas de interesse ofertadas

Assim será exibido as áreas ofertadas dentro de cada processo seletivo de acordo com a parametrização feita em "**TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Venda Online de Cursos | Anexo | Área de Interesse Ofertada",** ao clicar em **"Inscrever"** será redirecionado a página de inscrição da área de interesse ofertada selecionada, observe que a imagem é a mesma que foi cadastrada em **"Portal | Imagem"**

Quando clicar em **"Detalhes"** será exibido um modal de acordo com a parametrização feita em **"Portal | Resumo"** *(Figura 11)*

Figura 11 - Detalhes **[Portal | Resumo]**

**Filtro por parâmetro URL**

A coligada e filial são obrigatórias, já os outros parâmetros (IdPS, CodCategoria e AgruparPS) são opcionais, os parâmetros serão passados via URL:

Exemplo: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)  (aqui está parametrizado coligada = 1 e filial = 1)

Caso queira por exemplo filtrar por CodCategoria ficaria desta forma: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2) (onde o ct = 2)

Caso queira por exemplo filtrar por AgruparPS (nivel de ensino) ficaria desta forma: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ne=2](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2) (onde o ne = 2)

Também é possível utilizar todos os filtros de uma só vez: [http://](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[dominio.com.br](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/web](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1)[/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ps=136&ct=2&ne=2](http://localhost:8026/web_src/app/edu/PortalProcessoSeletivo/cursos/?c=1&f=1&ct=2)

**Os parâmetros**

- Coligada e Filial: ?f=1&c=1 (Obrigatório)  
- IdPS: &ps=136  
- CodCategoria: &ct=2  
- AgruparPS: &ne=eb
