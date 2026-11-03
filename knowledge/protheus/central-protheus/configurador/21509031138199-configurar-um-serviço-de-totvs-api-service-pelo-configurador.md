---
article_id: 21509031138199
category: Configurador
content_hash: 5a70283303233b147d51ef3483bc307e3bfdde76d702eba0c7c04d914aec31e3
fetched_at: '2026-06-28T22:42:18.863265+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Configurar  um serviço de Totvs Api Service pelo Configurador
type: support-article
updated_at: '2024-02-22T14:06:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21509031138199-Configurar-um-servi%C3%A7o-de-Totvs-Api-Service-pelo-Configurador
---

Exemplo de configuração de um serviço Totvs Api Service:

- Acesse o Configurador  
- Entre no menu Ambiente / Cadastros / Totvs Api Service  
- Clique em Incluir  
- Clique em Outras Ações, Totvs Api Service  
- Selecione o serviço do Totvs Api Service desejado (Correios - Pesquisa de CEP, por exemplo), e clique em Salvar  
- Em "Alias", selecione a tabela que irá utilizar este Totvs Api Service  
- Clique novamente em Outras Ações, e clique em Parâmetros  
- Nesta tela, serão configurados os Parâmetros Enviados (informações que serão enviadas para o serviço do Totvs Api Service) e os Retornos Esperados (os campos da tabela que receberão informações do serviço do Totvs Api Service baseado nos parâmetros enviados)  
- No exemplo do Totvs Api Service dos Correios - Pesquisa de CEP, o parâmetro de envio obrigatório é apenas o CEP, que poderá retornar informações como endereço, bairro, cidade, estado, etc.   
  
Parâmetros Enviados:  
Abaixo da coluna Origem, clique 2 vezes no campo, onde abrirá um combo com as opções "1- Sistema" e "2 - Usuário". A opção Sistema serve para que o parâmetro de envio seja lido diretamente do campo preenchido na tabela, indicado em "Campo". A opção Usuário serve para que o parâmetro de envio seja solicitado "manualmente" no momento de execução do Totvs Api Service, indicando em "Tipo Objeto" qual objeto enviará a informação, se será um objeto do tipo "Get" (campo de digitação de texto) ou um objeto do tipo "Combo" (uma lista de opções).  
  
Retornos Esperados:  
Nessa área são exibidos os retornos possíveis do serviço do Totvs Api Service escolhidos. Os parâmetros estão listados na coluna "Parâmetro". Você pode definir quais deles quer importar para a tabela, bastando clicar 2 vezes na coluna "Campo" do parâmetro correspondente, e selecionando o campo da tabela que receberá a informação (por exemplo, na tabela SA1, selecionar o campo A1\_END para o parâmetro ENDERECO)  
  
- Após concluir, clique em Salvar, depois em Salvar/Confirmar novamente. O serviço do Totvs Api Service estará criado. Para utilizar o mesmo, basta acessar a rotina que utiliza esta tabela, e clicar em Outras Ações / Ações Relacionadas, e selecionar Totvs Api Service.
