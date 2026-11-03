---
content_hash: 363d0086177832ee9e45f7a40f1938786343c2c470ad3af4472d847f444d99dd
fetched_at: '2026-06-29T00:06:13.779575+00:00'
page_id: '208346425'
product: rm
source: tdn-rm
title: Parametrização de Mapas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208346425
version: 64
---

# Índice

---

# Parametrizando a API do Google.

---

• 1 - Acesse o site <https://developers.google.com/maps/>

• 2 - No canto direito superior da tela efetue o login com sua conta Google

• 3 - Após fazer login, acesse seu Console:

• 4 - Clique em "Criar" e crie um novo projeto para sua conta:

• 5 - Defina o nome do seu novo projeto:

• 6 - No menu superior, você poderá selecionar o seu novo projeto:

• 7 - Clique no seu projeto para seleciona-lo:

• 8 - Vá no menu do seu projeto e selecione "API e Serviços / Painel " para gerenciar as API's do seu projeto:

• 9 - Acesse "Ativar API's e Serviços" para adicionar a API do Google Maps em seu projeto:

• 10 - Filtre os módulos para exibição apenas das API's de "Mapas":

• 11 - Agora você deve ativar em seu projeto, selecionando um à um e ativando:  
• Directions API  
• Geocoding API  
• Geolocation API  
• Maps Embed API  
• Maps JavaScript API

**Obs.: O serviço de APIs do Google Maps não é gratuito!**

Verifique as condições de valores para cada serviço, como por exemplo:

Para o correto funcionamento desta API dentro do RM, é necessário que a conta do Google esteja de acordo com os requisitos do contrato da Cloud Platform, com números de requisições disponíveis de acordo com a demanda do seu ambiente RM.

• 12 - Feito isso, confira em seu Painel de API's se todos estão ativos:

• 13 - Agora basta você acessar "Credenciais" / "Chave de API" para criar sua chave:

• 14 - Com sua chave criada, ela estará disponível para cópia e inserção nas parametrizações do RM.

• 15 - Parâmetro Global URL de Acesso ao Portal RM

Um dos pré-requisitos para utilização do Maps no RM é possuir o Portal RM Configurado.  
Para isso, certifique-se de que o caminho do seu portal está disponível em:

Serviços Globais | Ambiente | Parâmetros | Parâmetros Globais | Gerais

• 16 - Agora adicione a sua Chave da API em

Serviços Globais | Ambiente | Parâmetros | Parâmetros Globais | Google | Google Maps

Caso seu ambiente possua proxy, preencha as configurações do proxy.

Após inserir a chave de identificação o sistema está configurado para utilizar o recurso de Mapas.

# Observações

---

Para configurar o Maps em seu RM, é necessário:

• Possuir o RM Portal instalado e configurado  
• Possuir uma conta Google

Veja como configurar um Mapa em Anexo no RM em: 

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Parametrização de Mapas

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
