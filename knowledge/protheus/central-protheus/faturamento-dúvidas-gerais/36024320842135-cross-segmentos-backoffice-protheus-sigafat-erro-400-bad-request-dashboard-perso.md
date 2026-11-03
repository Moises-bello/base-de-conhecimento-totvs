---
article_id: 36024320842135
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 20000ab63898afeead6fc1b06e310137f9276d57351f80b3031dd94e19b06e4d
fetched_at: '2026-06-28T22:38:33.041703+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Erro 400 - Bad Request "Dashboard
  Personalizado"
type: support-article
updated_at: '2025-10-31T20:14:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36024320842135-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Erro-400-Bad-Request-Dashboard-Personalizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36024340245655) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Na rotina Manutenção de Itens Customizados (Dashboard), ao realizar a validação da URL do serviço, apresenta o erro "400 - Bad Request - Ocorreu um erro na requisição do endpoint "**WSRESTFUL**/cards/**Serviço - 404 NotFound".**

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões;  
  
**Causa**  
Esse incidente ocorre, pois as informações incluídas na URL de Serviço, difere das informações gravadas no fonte compilado (Coredash).  
  
**Solução**  
  
Para solucionar essa ocorrência, realize os seguintes passos:

**1. Localização da função no fonte.**  
Acesse o **fonte** onde está sendo compilado o serviço e localize a chamada da função `WSRESTFUL`.  
Logo após essa chamada, será exibido o **nome da função** que deverá ser utilizada na **URL do serviço**.

> **Exemplo:** `WSRESTFUL CardsCustomer`  
> Nesse caso, o nome da função a ser utilizada na URL será **CardsCustomer**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36024340246167)

**2. Configuração no Dashboard (Manutenção de Itens Customizados)**  
Na tela de **Manutenção de Itens Customizados (Dashboard)**, realize o preenchimento dos campos conforme os serviços desejados.  
É importante que a URL sempre contenha uma **barra ( / )** no início e no final, seguida pelo **nome da função** e o **complemento da rota**.

> **Exemplo de URL:**  
> `/CardsCustomer/cards/cardInfo/`

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36024320824343)

**3. Validação das Configurações**  
Após realizar todas as configurações, acesse a opção ****Validar****.  
Caso as informações estejam corretas, o sistema exibirá a mensagem:

> **"Endpoints validados com sucesso"**

Essa confirmação indica que a configuração do serviço foi concluída corretamente e que os endpoints estão prontos para utilização.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36024340247319)

**Fontes de Exemplo do Card e Gráficos:**

[Serviço Cards](https://tdn.totvs.com/x/mvwpIQ)

[Serviço Gráficos de Barra/Linha](https://tdn.totvs.com/x/mvwpIQ)

[Serviço Gráficos de Pizza/Polar](https://tdn.totvs.com/x/4QAxIQ)

**Saiba Mais:**

[Home DashBoard](https://tdn.totvs.com/display/PROT/Home+Dashboard)

[Customização de Cards Dashboard (Coredash)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7811846584471-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Customiza%C3%A7%C3%A3o-de-Cards-Dashboard-Coredash)
