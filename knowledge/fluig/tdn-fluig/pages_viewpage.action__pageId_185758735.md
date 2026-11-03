---
content_hash: 6991c1a5559c807f4b160f37371cba97a726ad661c85fd954edd7cec328f1339
fetched_at: '2026-06-28T21:35:18.970351+00:00'
page_id: '185758735'
product: fluig
source: tdn-fluig
title: Análise inicial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185758735
version: 14
---

# Índice

4true.\*ndicenone

## Monitoramento

---

A primeira meta é identificar o ponto de lentidão no sistema e levantar os tempos aproximados.

Com base no cenário de lentidão reportado, pode-se monitorar os tempos de resposta do servidor usando as ferramentas de desenvolvimento do navegador (tecla F12). O monitoramento dos tempos de resposta é feito pela ferramenta de rede (*Network*).

**Tabela Geral para tempo de resposta**

| Tempo | Percepção | Reação |
| --- | --- | --- |
| menor que 1 segundo | Instantâneo | Feliz |
| até 3 segundos | Rápido | Indiferente |
| de 3 a 5 segundos | Aceitável | Desconforto |
| de 5 a 10 segundos | Lento | Irritação |
| maior que 10 segundos | Travado | Reenvio da solicitação |

**Tempos esperados para algumas operações do fluig**

| Operação | 1 usuário | 30 usuários | 100 usuários |
| --- | --- | --- | --- |
| Carregar pagina | < 3 segundos | < 5 segundos | 12 segundos |
| Movimentação de processos | < 5 segundos | < 8 segundos | 20 segundos |
| Publicar documento | < 3 segundos | < 5 segundos | 10 segundos |

## Análise

---

Após levantar o recurso e os tempos é possível fazer uma rápida análise para identificar alguns pontos que costumam interferir na resposta do servidor:

#### Páginas

###### Tamanho das páginas

Ainda na aba de *Network* da ferramenta de desenvolvimento, verificar a quantidade de *bytes* transferidos para montar a página.

As páginas padrão da plataforma Fluig não ultrapassam o tamanho de 1100 *bytes*. Tamanhos acima de 2 MB podem prejudicar a performance, dependendo da infraestrutura de rede.

###### Widgets síncronas

Em alguns casos*, widgets*demorados "travam" o carregamento de toda página. Retire o *widget* em questão da página e efetue um novo teste. Caso o tempo de resposta seja aceitável, verificar a possibilidade do *widget* ser convertido para assíncrono.

#### Banco de Dados

Solicite um relatório de *queries* lentas ao DBA da empresa (ou à equipe que monitora o banco de dados do Fluig) e peça para verificarem se não existem *locks* muito demorados ou *deadlocks*.

#### Configurações

O Fluig na instalação padrão sai com apenas 20 conexões com o banco. Recomenda-se ajustar a quantidade de conexões para um valor próximo à quantidade de usuários concorrentes esperada.

Atenção

Um número muito alto de conexões ao banco de dados gera gasto no gerenciamento do *pool*.

Para identificar se o sistema está sofrendo com falta de conexões, é necessário habilitar o console de gerenciamento do WildFly.

1. No prompt de comando do Windows ou no *shell* do Linux, navegue até o diretório bin do WildFly ([Instalação do fluig]/appserver/bin);
2. Executar o *script* add-user.bat ou add-user.sh;
3. Na primeira pergunta exibida, apenas digite ENTER;
4. Informe o nome do usuário na segunda pergunta;
5. Escolha uma senha e digite-a na terceira e quarta perguntas;
6. Após a confirmação da senha, digite ENTER na quinta pergunta;
7. Na sexta e sétima perguntas é necessário digitar "Sim" (ou *"Yes",* se o console estiver em inglês) e confirmar com a tecla *Enter*.

Após o cadastro do usuário acesse o console de monitoramento http://[IP ou hostname]:9990.

* A métrica *Available* indica quantas conexões estão livres para serem usadas.

* O *Active Count* informa a quantidade de conexões com o banco sendo usadas no momento.

* O *Max Used* é o registro do numero máximo de conexões usadas desde que o servidor foi iniciado. Se o percentual do *Max Used* estiver em 100% em algum momento o cliente sofreu com falta de conexões com o banco. Para verificar o percentual Max Used, acesse **Runtime > Hosts > master > fluig1 > Subsystems > Datasources** e acione **View**.

Ainda no console de monitoramento é possível acompanhar o uso de memória do WildFly. Para verificar o uso de memória, acesse **Runtime > Hosts > master > fluig1 > JVM** e acione **View**.

Caso o percentual do uso de memória fique variando na casa dos 90% por um longo período é possível que o servidor precise mais memória.

A última avaliação a ser feita no console é o acumulo de mensagens nas filas e tópicos. Para isso, acesse **Hosts > master > fluig1 > Subsystems > Messaging - ActiveMQ** e acione **View**.

Avaliar todas as filas e tópicos. Caso algum tenha a informação *In Delivery* maior que 30 provavelmente algum componente do Fluig precise ser revisto.
