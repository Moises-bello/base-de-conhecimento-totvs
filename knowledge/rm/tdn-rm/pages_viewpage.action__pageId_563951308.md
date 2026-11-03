---
content_hash: bcfc0481f0c78cc74bc61628e6dcf0a267017f2ab50d32968e5db6fb5f9000e3
fetched_at: '2026-06-29T00:10:51.268544+00:00'
page_id: '563951308'
product: rm
source: tdn-rm
title: Batidas fora do Perímetro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563951308
version: 16
---

Neste documento iremos demonstrar as configurações para visualizar as batidas fora do Perímetro integrados com a Carol.

**Rm.exe**

A configuração básica para visualização das batidas fora do perímetro através da Carol, consiste em informar no parametrizador, que o sistema irá utilizar a integração.

Será necessário também informar os servidores de API/APP.

[Servidores e Portas API-APP](https://tdn.totvs.com/pages/viewpage.action?pageId=721733078)

Para isso, basta acessar o menu **Configurações | Parametrizador**, no processo 08.01 - Iniciais, avance até a Etapa 5 - Integração, aba Integração Carol/TSA e selecione o parâmetro **"Considera integração com as batidas da Carol"**

**Segurança-Perfis**

Para acessar o menu "Batidas fora do perímetro "  será necessário permitir acesso.Vá em Serviços globais -Segurança-perfis-selecione o perfil  Acesso a menus- item 04-Processos-04.01-Aprovações-**04.01.03-Batidas Fora do Perímetro.**

Após concluir a permissão será possível acessar o menu.

Menu Processos-Aprovações-**Batidas fora do perímetro**.

**Como visualizar as Batidas fora do Perímetro**

Será necessário realizar a importação das batidas através do menu Entrada de dados -Importar , selecionando a opção ["Utilizar integração com a Carol"](https://tdn.totvs.com/pages/releaseview.action?pageId=441821303) .

Ao executar o processo, as batidas serão recuperadas através da plataforma Carol. Dentro do período de importação definido.

Será criados registros de importação para todos os dispositivos cadastrados nas tabelas AHSTIMPORTACAO e APORTARIA373, e será visualizada apenas as batidas que estiverem fora da Cerca.

Na tabela APORTARIA373,  será gravada  na coluna DENTROPERIM as informações da Carol com os valores 0-Não utiliza cerca , 1-Batida dentro da cerca , 2-Batida fora da cerca .

O usuário poderá: Pesquisar por nome, Alterar situação De: D-Desconsiderada Para: C-Considerada  , Atualizar página e carregar mais resultados.

**Observação :**

* É visualizado 20 registros por página e se necessário utilize o Carregar mais resultados.

* Caso apresente o erro **"Servidor não está respondendo"** será necessário reservar as portas utilizadas **conforme o item 1**da documentação: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4496031752343-RH-RM-Meu-RH-Erro-ao-logar-no-APP-Meu-RH-Ops-algo-deu-errado)
