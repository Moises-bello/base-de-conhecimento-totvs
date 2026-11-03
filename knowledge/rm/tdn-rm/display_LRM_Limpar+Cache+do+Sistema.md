---
content_hash: 1684247dea60520f7eb7151dbedcc1710319ebc1c949ca8d78b92197e42ef412
fetched_at: '2026-06-29T00:08:41.305269+00:00'
page_id: '286523370'
product: rm
source: tdn-rm
title: Limpar Cache do Sistema
type: documentation
url: https://tdn.totvs.com/display/LRM/Limpar+Cache+do+Sistema
version: 3
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     Este documento tem por objetivo especificar a atividade “Limpar Cache do Sistema” disponível no Cockpit.

# Especificação:

---

     Foi implementada uma nova funcionalidade no Cockpit do sistema que permite que o Cache de cada servidor seja esvaziado.

     Localizada na parte superior de cada servidor, está funcionalidade busca limpar o cache das configurações criadas pelo parametrizador de cada produto.

     Esta limpeza é uma funcionalidade importante, principalmente quando se utilizado em um ambiente Cloud ou em situações em que o host não pode ser parado. Imagine a seguinte situação:

     Um client que utiliza múltiplos hosts, como no da imagem acima. Ao executar o parametrizador de algum produto (o da Folha de Pagamento por exemplo), as configurações realizadas serão salvas no cache do host em que a parametrizador foi executado. Os outros hosts permanecerão com o cache antigo antes do parametrizador ser executado.

     Para que se tenha um melhor desempenho, é recomendado que ao realizar a parametrização dos produtos, utilize-se a funcionalidade de “Limpar Cache do Sistema” presente no Cockpit. Com isso, o sistema ganhará em performance, diminuindo a quantidade de memória utilizada pelos hosts sem a necessidade de que os mesmos sejam reiniciados além de alinhar os parâmetros configurados para os múltiplos hosts utilizados.

     Por default, a limpeza do cache de parâmetro já vem habilitada no sistema com intervalo de 60 segundos a cada execução de limpeza. Entretanto, esses parâmetros podem ser alterados no arquivo de configuração “RM.Host.Service.exe.config” utilizando as tags abaixo:

**<add key="CacheParamsCheckInterval" value="60" />**Tag responsável por definir o intervalo de tempo em segundos em que o cache será limpo.

Importante

Para um maior ganho de performance, é recomendado que o intervalo de tempo de cada execução seja de no mínimo 60 segundos.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.16 ou Superior

false

**Processo:** Atividade "Limpar Cache do Sistema" disponível no Cockpit do sistema

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
