---
content_hash: 15435abbf7fac3c17dc5656f8d5bea7692fdd55ee55fc25af3cb07d5415afb9b
fetched_at: '2026-06-29T00:10:25.866515+00:00'
page_id: '506144561'
product: rm
source: tdn-rm
title: Comportamento do RM em relação ao License Server - Cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506144561
version: 57
---

**ÍNDICE**

## **01. VISÃO GERAL**

       Documentação criada no intuito de demonstrar como o RM (MDI, Portal Corpore.Net, Novos Portais,Serviços SOAP/REST e APIs) se comporta em relação ao License Server e o consumo de licenças.

## **02. MDI**

       Cada MDI aberta do RM, em uma determinada máquina e autenticada com um determinado usuário, representa para o License Server um usuário concorrente. O consumo de licenças se dá de acordo com o Módulo e as Rotinas que vão sendo abertas. Cada módulo possui uma licença específica.

**Exemplo:**

* **Maquina A, usuário Mestre:**

             Ao acessar o módulo "Folha de Pagamento" e abrir o cadastro de funcionário, uma licença do módulo utilizado será consumida, identificado através do "Id Licença" (podendo ser escalada para TOTVS FULL) na aba "Conexões" do monitor, como mostra exemplo abaixo.

             Ao abrir uma outra rotina do mesmo módulo, com o mesmo usuário, na mesma máquina, a licença será mostrada no Monitor do License Server, mas não descontará do total de licenças disponíveis, apresentando o status "Abonada".

Algumas rotinas de configuração do sistema (Exemplo: "Cadastro de Usuário"), não consomem nenhuma licença, mas notificam o seu uso à TOTVS para fins estatísticos.

**Atualização**

A partir da versão 12.1.2310 houve mudança da forma de montagem do nome da rotina. A Partir de agora será feita como o exemplo abaixo:

* wsDataServer - GlbColigadaData

* **Abertura de telas HTML pela MDI**

            Atualmente, está sendo desenvolvido um novo padrão de telas HTML que podem ser abertas pela MDI e alguns produtos já estão implementando. Apesar dessas telas serem construídas com estruturas de APIs, quando elas são abertas por dentro da MDI, as licenças TOTVS I consumidas seguirão o mesmo padrão de abono citado acima.

            É importante saber que essa mesma tela quando aberta por fora da MDI terá o consumo da licença TOTVS I e se comportará da mesma forma explicada no tópico "Novos Portais, Serviços SOAP/REST e APIs" deste documento.

* **Abertura de telas através da funcionalidade de "Anexos / Processos / Outras informações" da MDI**

             Até a versão 12.1.2205, todas as telas chamadas pelos menus de "Anexos / Processos / Outras informações" na MDI, solicitam consumo de licença no LS. Nesse caso, o LS decide se aquela solicitação consumirá uma licença ou a mesma será abonada.

Exemplo

Ao chamar a tela "Batidas de Refeições" a partir do anexo do cadastro de funcionários, o RM fará duas chamadas para o LS de solicitação de consumo de licença. Porém no LS apenas uma licença será consumida (no caso do cadastro de funcionários) e uma licença será abonada (no caso do cadastro de refeições).

**Podemos perceber que o consumo da action principal é realizado através do comando GetLicense, e logo em seguida ao abrir uma action anexa, também é realizado o GetLicense.**

             A partir da versão 12.1.2209, as telas chamadas pelo menu de "Anexos / Processo / Outras informações" não solicitam mais consumo de licença no LS. Foi criado no RM um mecanismo para "descobrir" se aquela chamada de tela feita através de um Anexo/Processo, irá consumir ou abonar a licença. Caso seja percebido que aquela chamada poderá consumir uma licença, nesse caso será feita uma solicitação de consumo de licença para o LS. Caso contrário, essa comunicação com o LS não será mais realizada. Sendo assim, não aparecerá mais informação no LS de abono de licença para esses casos em específico. Nesse caso o RM fará uma notificação para a TOTVS para fins estatísticos.

Exemplo

Ao chamar a tela "Batidas de Refeições" a partir do anexo do cadastro de funcionários, o RM fará apenas uma chamada para o LS de solicitação de consumo de licença. Nesse caso, no LS apenas uma licença será consumida (no caso do cadastro de funcionários) e não terá mais no LS a informação de licença abonada para o cadastro de refeições.

**Podemos perceber que o consumo da action principal é realizado através do comando GetLicense, e logo em seguida ao abrir uma action anexa, agora um LS006\_Local é realizado, onde não é mais consumida a licença e somente um SetInfo será enviado para o License Server informando que a action foi aberta.**

             Com essa implementação pretendemos ter um ganho de performance tanto no momento da abertura das telas pelo RM quanto no próprio mecanismo do LS, pois menos requisições serão enviadas.

Segue abaixo alguns prints de telas demonstrando o momento na MDI que essa funcionalidade será utilizada:

a) - Chamada via anexo

|  |
| --- |

b) - Chamada via processo

|  |
| --- |

c) - Chamada via action estendida

|  |
| --- |

c) - Chamadas de actions isoladas( ex: click de um botão em uma tela qualquer).

No link abaixo, disponibilizamos as melhores práticas para criação de código de chamada de action  RM.

<https://tdn.totvs.com/x/uA4SKQ>

## **03. Portal Corpore.Net, Novos Portais, Serviços SOAP/REST e APIs**

            Os portais e serviços expostos pelo Servidor de Aplicação da Linha RM (RM.Host) tem o seu consumo independente de máquina e usuário. O seu consumo é dado por requisição e durante o tempo de vida de cada uma. Eles utilizam a licença TOTVS I ou similar, conforme a modalidade do contrato.

* **Portal Corpore.Net**

            Cada abertura de página gera um consumo de licença TOTVS I ou equivalente durante o processamento da página até sua exibição, ou seja, ao clicar no link da rotina, enquanto a página é "desenhada" a licença é consumida no License Server.

            Após o término de processamento, a licença é liberada. Isso ocorre o tempo todo durante a navegação no Portal Corpore.Net.

* **Novos Portais, Serviços SOAP/REST e APIs**

            Um processamento semelhante ao Portal Corpore.Net acontece com os novos portais e qualquer outra aplicação que faça consumo de serviços expostos pelo Servidor de Aplicação. Durante o processamento da requisição até a sua resposta, a licença é consumida no License Server. Ao término da requisição, a licença é liberada.

Como as requisições nos portais e WebServices tendem a serem muitas, existe um mecanismo que reaproveita uma licença consumida durante 30 segundos, desde que as requisições não concorram entre si.

A licença liberada, caso ainda tenha algum tempo de vida (limite 30 segundos) é colocada em uma fila para ser reutilizada.

* Requisição 1 → Consumo L1 → Processamento → Resposta → Liberação L1
* Requisição 2 → Consumo L1 → Processamento → Resposta → Liberação L1
* Requisição 3.1 → Consumo L2 → Processamento → Resposta → Liberação L2
* Requisição 3.2 → Consumo L3 → Processamento → Resposta → Liberação L3

Logo, é possível que diferentes acessos em web services ou portais consumam a mesma licença que é exibida no monitor, desde que os acessos não concorram e aconteçam dentro de um período de 30 segundos.

Obs.: As APIs de: menus, troca de senha e geração de token não consomem licença.  Veja mais sobre as APIs: .

## **04. API Gateway / Middleware**

            O consumo de API pode ser feito por um Middleware (API Gateway), caso seja contratado e configurado o Middleware será responsável pelo gerenciamento de autorização e verificação de bilhetagem dessa chamada, que poderá ser consumida por qualquer client (apps, portais, MDI, aplicações externas). Dado essa verificação, o Servidor de Aplicação da Linha RM (RM.Host) fará o registro da utilização dessa requisição no LicenseServer, consumindo ou abonando a mesma, de acordo com o plano contratado no Middleware.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** License Server

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**

falseFerramenta Auxiliar

Para auxiliar na análise dos log's do License Server foi criado o Licence Log Analyser, onde a ferramenta carrega todos os arquivos de Log do License server e transforma os log's em dados que serão visualizados em um grid totalmente customizável.
