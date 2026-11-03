---
content_hash: a722dbf2cd36a4d68305284ec83bed7bbe7df50bc8a78d60ec23b8ec1a7f8d56
fetched_at: '2026-06-29T00:11:49.557509+00:00'
page_id: '834825593'
product: rm
source: tdn-rm
title: TGM - Visualização do parque de máquinas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834825593
version: 7
---

# 

# **VISÃO GERAL**

A partir da versão 12.1.2406 do RM, é possível visualizar o parque de máquinas vinculado ao TGM acessando a seguinte rota: **http://HOSTDOTGM:PORTADOSERVICO/app**  
Por exemplo, se seu TGM está em **localhost** e a Porta de Serviço está configurada para **8040**, acesse [http://localhost:8040/app](http://localhost:8041/app)

Essa visão traz uma representação gráfica em forma de grafos para facilitar a visualização da infraestrutura envolvendo o TGM.

# **GUIA BÁSICO**

**Para utilizar as funcionalidades da API CLOUD, é necessário adicionar no .config de todos os hosts ativos a tag API\_KEYVALUE. [Mais informações clicando aqui](#)**

Página: **Gestão de Ambiente**

No seletor de Alias, informe o Alias que deseja visualizar no mapa.

O mapa de grafos será atualizado automaticamente no tempo de polling determinado na página de Configuração.

Página: **Configuração**

Nessa página é possível configurar alguns parâmetros da aplicação, como **Porta de serviço do TGM**e **Tempo de Polling (segundos).**

Dica: A Porta de Serviço pode ser verificada no **ManagerService** na aba **Totvs Gateway Manager**:
