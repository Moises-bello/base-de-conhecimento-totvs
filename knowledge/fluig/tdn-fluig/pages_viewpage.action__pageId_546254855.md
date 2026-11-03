---
content_hash: d7554d6e2de19d7e08f3efecef082f92d651e86d915ac9c4b750b511c385e194
fetched_at: '2026-06-28T21:35:27.401250+00:00'
page_id: '546254855'
product: fluig
source: tdn-fluig
title: ARQ - Prevenção de ataques Slow post e Slow headers
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546254855
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.6.x ou superiores

# Ocorrência

Como prevenir os ataques Http Slow Post & Http Slow Headers na plataforma?

# Solução

A natureza desse tipo de ataque DDoS é tentar bloquear os serviços, ocupando o servidor com o uso de poucos recursos do atacante. Isso é realizado atrasando o tempo total da requisição: os cabeçalhos ou dados são enviados em blocos e se camuflam de uma requisição lenta. Mesmo que esta seja inválida, somente quando estiver completa é que será feita a validação e a liberação dos recursos. Infelizmente, esse tipo de ataque ainda é muito eficaz, porque além de utilizar poucos recursos do atacante, ele é difícil de filtrar por parecer de fato uma requisição lenta.

O ideal para prevenir esse tipo de ataque é reduzir o limite de tempo das requisições lentas, que é bem grande por padrão. Isso é realizado nas configurações do Load Balancer (servidor de aplicação). Realizamos testes específicos utilizando o Load Balancer Ngix na frente das requisições, e constatamos que a arquitetura da própria ferramenta reduz a eficácia desse tipo de ataque. Veja mais detalhes sobre a a recomendação de configuração da própria ferramenta no [site oficial](https://www.nginx.com/blog/mitigating-ddos-attacks-with-nginx-and-nginx-plus/), na seção **Closing Slow Connections**.

Importante!

Somente é possível utilizar o NGINX **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.

## Testes efetuados com o Nginx

Em testes realizados no ambiente local, com a configuração recomendada, é possível verificar que, após o tempo determinado, as conexões são encerradas. A configuração equivalente no *undertow(read-)* não limita o tempo total do envio dos headers, somente o tempo entre cada requisição, o que permite manter a conexão aberta por bastante tempo.

Abaixo os resultados dos testes com a configuração ativa:

falseTestesc1Configuração do NGINX

Importante notar que os valores configurados não representam uma situação de uso real, portanto devem ser ajustados para uso.

c2Verificação das portas em uso

A contagem de portas em uso está duplicada porque o cliente e servidor são locais.

c3Comportamento da ferramenta de simulação de ataque

É possível visualizar que, após o tempo definido, as conexões existentes foram encerradas.
