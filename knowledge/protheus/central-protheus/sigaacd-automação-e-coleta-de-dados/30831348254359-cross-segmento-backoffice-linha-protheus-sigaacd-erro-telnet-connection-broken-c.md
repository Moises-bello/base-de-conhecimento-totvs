---
article_id: 30831348254359
category: SIGAACD - Automação e Coleta de Dados
content_hash: e153f04d79c31679a8204be54cc939c47dc1e109eb1153e3f72a949b064df522
fetched_at: '2026-06-28T22:39:11.072673+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD  - Erro Telnet Connection
  Broken - Causas e Detalhamentos
type: support-article
updated_at: '2026-02-12T13:50:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30831348254359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Erro-Telnet-Connection-Broken-Causas-e-Detalhamentos
---

O erro "Telnet Connection Broken" no Protheus ACD ocorre por perda de conexão entre coletores e antenas de rádio frequência, causada por áreas de sombra, falhas de bateria, interferências ou problemas de infraestrutura. Recomenda-se revisar a instalação das antenas e considerar o uso do aplicativo Meu Coletor de Dados, que oferece maior estabilidade.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30831348222615) Tempo aproximado para leitura: **00:04:37 min**  
  
**Dúvida**  
O que pode causar o erro Telnet Connection Broker? Qual a solução para este problema não acontecer?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

**1. Explicando o que é a Tecnologia Rádio Frequência**

A Tecnologia de Radio Frequência, que é usada no Telnet do Protheus ACD, é compreendida por uma ou várias antenas distribuídas em um armazém que estão conectadas a um modulo que comunica via rede no protocolo Telnet com o servidor Protheus. Os Coletores VT100, são coletores portáteis à bateria e dispõem de uma antena onde o coletor se comunica com as antenas do armazém.

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30831348228247)

**2. Recomendações para Instalação das Antenas:**

* **Cobertura Adequada:** Assegure que as antenas estejam posicionadas de forma a cobrir todas as áreas onde os coletores serão utilizados, evitando zonas de sombra;
* **Altura e Posicionamento:** Instale as antenas em locais elevados e livres de obstruções físicas, como paredes metálicas ou estruturas que possam interferir no sinal;
* **Interferências:** Evite instalar antenas próximas a equipamentos que possam causar interferência, como motores elétricos ou outros dispositivos emissores de RF;
* **Teste de Sinal:** Após a instalação, realize testes de sinal em diferentes pontos do armazém para identificar e corrigir possíveis áreas com sinal fraco;
* **Outros fatores:** Além disso, é importante considerar que fatores como a presença de estruturas metálicas, equipamentos eletrônicos e até mesmo a movimentação de pessoas podem afetar a qualidade do sinal. Portanto, é recomendável realizar um estudo de site antes da instalação para mapear as melhores posições para as antenas.

**3. Fatores que causam a queda e mensagem "*****Telnet Connection Broken*****" (traduzindo, queda de conexão com o Telnet):**

Qualquer interrupção de sinal entre o coletor e as antenas podem gerar o erro "*Telnet Connection Broken*", onde o servidor identifica que havia um coletor usando uma aplicação e não está mais visível.

Estes fatores que podem causar uma interrupção podem ser por vários motivos, como:

* O coletor estar numa área de sombra da antena e não conseguir se comunicar;
* Pela descarga de baterias do coletor;
* Por confinamento do coletor dentro de um local metálico que bloqueia seu sinal;
* Por uma antena do armazém naquele local com defeito;
* Por problemas com o modulo das antenas;
* Falta de energia no modulo das antenas;
* Desligamento do coletor no meio do uso sem sair do sistema.

As camadas do Protheus que administram o coletor são realizadas pelo Framework do Protheus (do login à navegação nos menus, onde existem regras de permissões de acessos de usuários). Já a aplicação, onde é possível acionar os atalhos CTRL+A e CTRL+Z e saber o nome da aplicação, bem como usabilidades, são realizadas pela camada do SIGAACD.

Quando ocorre a queda do Coletor, a aplicação avisa por meio da mensagem "Telnet Connection Broken" que havia uma conexão e que ela não está mais presente **e o responsável pela Infraestrutura física onde os coletores operam** **deve investigar a causa e os fatores que podem interromper a comunicação dos coletores.**

**4. Diferenciando a conectividade Rádio Frequência (coletor de dados) da conectividade Wi-Fi (aplicativo "meu coletor de dados")**

Os coletores não usam inteligência de uso em áreas de sombra como o App Meu Coletor de Dados, pois a aplicação é executada no servidor, diferentemente do App Meu Coletor de Dados que tem uma aplicação executando no celular e pode coletar dados mesmo sem comunicação de WI-FI (Esta é outra tecnologia de comunicação) e ao se encontrar dentro da área de sinal novamente, conseguem restabelecer a comunicação e fazer a transferência dos dados coletados enquanto estava fora de área.

**5. Como solucionar o problema então?**

Sabendo que a mensagem vai ocorrer por conta da perda de conexão entre o coletor e o modulo de antenas, deve-se, junto ao responsável pela infraestrutura onde os coletores operam, avaliar os pontos destacados na Documentação.

Outra possibilidade, pensando em novas soluções que a TOTVS têm projetado para melhor autonomia e efetividade nos processos de estoque, a migração para o uso do Aplicativo Meu Coletor de Dados torna-se uma solução interessante, por se tratar de uma conectividade mais atual e estável, contendo diversas rotinas similares à de um coletor de dados físico. Todos os detalhes sobre o App Meu Coletor de Dados estão descritos nestes Guias abaixo:

[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como configurar o App Meu Coletor de Dados?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30317999783703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-App-Meu-Coletor-de-Dados)

**6. No coletor de dados há alguma distancia mínima recomenda para as antenas?**

A TOTVS não homologa nenhum equipamento de hardware para comunicação com rede com fio e sem fio.

Recomendamos verificar junto ao seu fabricante do coletor, a usabilidade de sua rede em qualquer ponto físico na qual está sendo utilizado as conexões  com o servidor Protheus, visto que o SIGAACD não trabalha de forma Off-line, e por tanto exige uma conexão com a rede.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
