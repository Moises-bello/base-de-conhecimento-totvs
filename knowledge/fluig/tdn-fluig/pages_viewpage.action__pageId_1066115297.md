---
content_hash: dda0be19eca561dd5a51ac0c14a1e2154af74f11a425e3fabaae345a140c7ebf
fetched_at: '2026-06-28T21:35:17.453074+00:00'
page_id: '1066115297'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Finalizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1066115297
version: 9
---

Consulte a documentação correta:

Esta documentação refere-se ao Editor de processo atual da plataforma. Caso esteja utilizando o Editor de processo clássico, acesse .

5.\*ndice

# Falando de evento Finalizado...

---

O evento **Finalizado** indica a conclusão global do processo, ou seja, quando o fluxo chega nesse evento, todos os demais caminhos possíveis que o fluxo do processo poderia seguir também são finalizados, bem como todas as atividades pendentes da solicitação, interrompendo inclusive subprocessos vinculados. Ou seja, ele representa uma interrupção abrupta do processo.

Por padrão, não ocorre nenhum tipo de compensação ou pós processamento depois que o fluxo do processo atinge esse evento. Somente é possível realizar pós processamento com desenvolvimentos sobre a plataforma.

Quando há algum desenvolvimento utilizando o *script **afterProcessFinish***, ele será executado imediatamente à chegada do fluxo do processo nesse evento, independentemente de haver outros caminhos do fluxo abertos.

trueGreenIndicação de uso  
Esse tipo de evento de fim normalmente é utilizado em situações de inconsistência crítica, cancelamento pelo solicitante ou quando uma decisão em um caminho paralelo torna todos os outros caminhos irrelevantes ou obsoletos.

#ebecf0

trueExemplo de uso  
Em um processo de **Tratamento de incidente de segurança**, depois que o alerta de possível incidente é emitido, existem algumas etapas paralelas para analisar os servidores, investigar os *logs* para validar a autenticidade do incidente*,* preparar comunicado interno e iniciar o *backup* dos dados. Porém, se ao analisar os dados for constatado que o incidente não é real, ou seja, foi um falso positivo, todas as etapas podem ser encerradas por completo, para evitar desperdício operacional. Por isso, é possível utilizar o evento **Finalizado** logo após a constatação de que o incidente não é real para que todo o restante do processo seja interrompido.

## Diferença entre o Fim e o Finalizado

---

Os eventos  e Finalizado são utilizados para finalizar o processo, porém, eles atuam de formas diferentes:

* **Fim**: finaliza apenas o fluxo do caminho que chegou até ele. Se o processo possuir ramificações – atividades paralelas – o evento Fim finaliza apenas o caminho que o atingiu. As demais atividades de caminhos paralelos permanecem abertas e ativas. A solicitação é considerada finalizada apenas quando o último caminho ativo chegar em um evento Fim.

* **Finalizado**: finaliza o processo de forma global imediatamente, ou seja, quando um único caminho do processo chega até ele, ele finaliza todas as atividades pendentes de todos os caminhos possíveis que estão ativos, inclusive subprocessos vinculados ao processo principal.

## Configurar evento Finalizado

---

**100%true5%**

**01.** No  do processo, clique no evento **Finalizado**  que deseja configurar.

#f2f2f2#f2f2f2

As configurações disponíveis são exibidas na lateral direita.

**02.** Defina as informações desejadas para o evento que representa o fim global do processo, ou seja, tudo o que estiver pendente ou ativo será finalizado.

#f2f2f2#f2f2f2

**Título**  
Nome para identificar o fim global do processo.

#ebecf0

trueExemplo de uso  
Em um processo de **Solicitação de reembolso**, onde existem as etapas **Análise financeira** e **Conferência de documentos** paralelas, em uma certa direção do fluxo, a solicitação pode ser cancelada pelo próprio solicitante. Neste ponto poderia existir um evento Finalizado com o nome **Cancelado pelo solicitante**.

**Acompanhamento**  
Quem deve ser notificado quando a solicitação chegar nesse evento e o processo for encerrado de forma global. As opções disponíveis são:

* **Notificar solicitante**: quando assinalada, determina que uma notificação sobre a finalização global do processo será enviada ao solicitante.

* **Notificar gestor**: quando assinalada, determina que uma notificação sobre a finalização global do processo será enviada ao gestor do processo.

Importante!

Independentemente das opções assinaladas, a notificação não é enviada para quem realizou a ação.

#ebecf0

trueExemplo 1  
Uma pessoa movimenta a solicitação para uma etapa na qual ela mesma é a responsável. Mesmo que a opção **Notificar responsável** esteja assinalada, ela não receberá a notificação, visto que a ação foi feita por ela mesma.

#ebecf0

trueExemplo 2  
O gestor do processo movimenta a solicitação (como responsável ou gestor) para uma etapa na qual a opção **Notificar gestor** está assinalada. Neste caso, ele não receberá a notificação, apenas os outros gestores do processo receberão.

O mesmo ocorre para todos os tipos de notificação, incluindo a de substituto.

#ebecf0

trueExemplo  
Se a pessoa A é substituta da pessoa B e movimenta a solicitação para uma etapa onde a pessoa B é responsável, a pessoa A (substituta) não será notificada. Apenas a pessoa B e outras pessoas substitutas dela serão notificadas.

Nota:

As notificações podem ser enviadas na  ou por *e-mail*, dependendo de como foi feita a  das opções de envio no perfil pessoal, bem como quais opções estão disponíveis para uso na empresa, que podem ter sido configuradas de forma  – para todas as empresas – ou por .

**03.** Clique em **Salvar rascunho** – localizado no lado direito da barra superior – para salvar as configurações feitas no evento **Finalizado**.

**04.** Na mensagem exibida, clique em **Ok, entendi**.

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.

]]>
