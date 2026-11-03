---
content_hash: 38e9c184952b294798aa76ee2206f5b69d5365b3d996f8bab282ae985f0e4378
fetched_at: '2026-07-02T19:24:25.984825+00:00'
page_id: '519702867'
product: protheus
source: tdn-tec
title: DBAccess - Processos de Conexão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519702867
version: 3
---

Processos de Conexão

O true possui um mecanismo de controle dos Processos de Conexão.

Através do true, na guia **Configurações >** sub-guia **Avançado**, é possível configurar a quantidade inicial e máxima de *threads* que o true tratará.

Além disso, considerando os limites configurados, é possível determinar o valor incremental de *threads* que devem ser adicionadas ao "pool de conexões".

Essa configuração é útil para ambientes em que o número de conexões ativas e simultâneas é alto, e a rotatividade de conexões e desconexões também é alta.

**Por exemplo:** se temos uma média diária de 500 conexões simultâneas com o true e uma alta rotatividade de conexões e desconexões, onde mais de 10 conexões ocorrem ao mesmo tempo, podemos configurar o número de *threads* inicial para 400 e o número de *threads* em espera para 20.

Com isto, após iniciar o true, se 200 novas conexões forem realizadas ao mesmo tempo, haverá *threads* suficientes aguardando para receber todas essas requisições, e a partir de 400 conexões simultâneas, sempre serão mantidas 20 *threads* adicionais em espera e prontas para aceitar novas conexões.

  

---

## Caso de uso

Com o objetivo de elucidar seu uso e função, vejamos o case a seguir.

Para o case, vamos assumir os valores:

|  |  |
| --- | --- |
| Inicial | 50 |
| Máximo | 1000 |
| Em espera | 5 |

Com esta configuração, ao iniciar o serviço do true, 50 *threads* serão instanciadas e ficarão disponíveis para aceitar conexões.

Todas estas *threads* estão inicialmente "em espera" e somente quando uma conexão com true for realizada é que uma delas será utilizada e passará a atender exclusivamente àquela conexão, diminuindo o número de *threads* em espera.

A cada nova conexão realizada com o true, ele verifica se a quantidade de *threads* em espera está dentro do parâmetro configurado e, caso esteja abaixo desta configuração, ele vai automaticamente instanciar novas *threads*, para sempre manter 10 *threads* livres e em espera.

O número total de *threads* utilizadas, mais o número de *threads* em espera, nunca ultrapassará o número máximo configurado.

Supondo que já existem 990 conexões ativas com o true e existem 10 *threads* em espera, já temos o total de 1000 *threads*. Caso mais uma conexão seja estabelecida, uma thread em espera será alocada, restando apenas 9 *threads* em espera.

Como a soma de *threads* ativas (991) mais o número de *threads* em espera (9) já atingiu o limite configurado de 1000 *threads*, o true não vai instanciar mais *threads* e colocá-las em espera.

Se 1000 conexões forem estabelecidas com o true, não haverá mais *threads* em espera e não será possível estabelecer novas conexões com ele.

Importante

Caso o limite de conexões seja atingido, a seguinte mensagem será observada no log do true:

---

## Observações

* Conforme as conexões vão sendo encerradas, as *threads* em uso também serão "fechadas" e voltarão ao estado de "em espera"
* O true sempre tentará manter disponível o valor configurado em  *threads* sempre (que disponível) 10 threads "em espera".
* Quando o número de *threads* ativas, mais o número de *threads* em espera, for menor que o número de *threads* inicial, o true alocará automaticamente mais *threads* para o estado de "em espera", sempre considerando o limite máximo definido.

---

## Veja também
