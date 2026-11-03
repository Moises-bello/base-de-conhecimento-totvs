---
content_hash: 38d8a33596b9339c1c66719964fdb1bd983fb9ff64306bed971d3c2f1b586e04
fetched_at: '2026-06-29T00:11:06.176203+00:00'
page_id: '63277377'
product: rm
source: tdn-rm
title: Visualizador de Eventos do Windows
type: documentation
url: https://tdn.totvs.com/display/LRM/Visualizador+de+Eventos+do+Windows
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**10.80, 11.x |
| **Processo** | **:** | Windows |
| **Subprocesso** | **:** | Visualizador de Eventos do Windows |
| **Data da publicação** | **:** | 21/06/2013 |

|  |
| --- |
|  |
| **Sintoma**  Os logs de eventos são armazenados em arquivos do Windows, que podem crescer consideravelmente à medida que o Windows captura os eventos do sistema ou aplicativos.  Com isso o sistema além de perder um pouco o desempenho, pode gerar mensagens de erro ao acessar o sistema ou em sua utilização. |
|  |
| **Causas**  Em determinadas situações, o Log de eventos pode retornar alguns erros devido ao tamanho máximo do arquivo de Log configurado. |

**Solução**

É de extrema importância, gerenciar corretamente as propriedades de Log, definindo um tamanho adequado para seu sistema e marcando a opção para que quando o tamanho máximo do Log for atingido, o Windows possa gerenciá-lo de forma adequada.

Para acessar o Visualizador de Eventos, entre em Painel de Controle -> Ferramentas Administrativas -> Visualizador de Eventos.

Ou pelo Iniciar - > Executar -> eventvwr.msc

No Windows XP, dentro das Propriedades dos Logs de Aplicativos, é possível configurar o tamanho máximo do Log e também a ação que o Windows Irá tomar quando esse tamanho for atingido.

Configure o Log para que sejam armazenados os últimos 7 dias dos eventos.

|  |
| --- |
| **Solução**  É de extrema importância, gerenciar corretamente as propriedades de Log, definindo um tamanho adequado para seu sistema e marcando a opção para que quando o tamanho máximo do Log for atingido, o Windows possa gerenciá-lo de forma adequada.  Para acessar o Visualizador de Eventos, entre em Painel de Controle -> Ferramentas Administrativas -> Visualizador de Eventos.  Ou pelo Iniciar - > Executar -> eventvwr.msc  No Windows XP, dentro das Propriedades dos Logs de Aplicativos, é possível configurar o tamanho máximo do Log e também a ação que o Windows Irá tomar quando esse tamanho for atingido.  Configure o Log para que sejam armazenados os últimos 7 dias dos eventos.    Figura 1 - Windows XP  No Windows Vista, a opção para substituir, só ocorre quando o tamanho máximo do arquivo for atingido.    Figura 2 - Windows Vista |
|  |
| **Informações Adicionais**  Visualizar Eventos é um snap-in do Console de Gerenciamento Microsoft (MMC) que permite procurar e gerenciar os logs de eventos. É uma ferramenta indispensável para monitorar a saúde dos sistemas e solucionar problemas quando eles surgem.  Quando você usa Visualizar Eventos para solucionar um problema, precisa localizar os eventos relacionados ao problema, independente do log de eventos no qual eles aparecem.  O log Aplicativo contém eventos registrados por aplicativos ou programas. Por exemplo, um programa de banco de dados pode registrar um erro de arquivo no log do aplicativo. Os desenvolvedores de programa decidem quais eventos registrar em log.  O log Sistema contém eventos registrados pelos componentes de sistema do Windows. Por exemplo, se um driver ou outro componente do sistema não for carregado durante a inicialização, essa falha será registrada no log do sistema. Os tipos de eventos registrados pelos componentes do sistema são determinados previamente pelo Windows.   Para maiores informações:    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha); |
