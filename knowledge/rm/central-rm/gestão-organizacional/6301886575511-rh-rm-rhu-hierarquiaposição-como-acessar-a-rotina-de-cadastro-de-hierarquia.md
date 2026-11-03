---
article_id: 6301886575511
category: Gestão organizacional
content_hash: 1bf3bbcc08da77ab7cac56eaadab8c90c88026f8fd84e670a03a705d0bae4e50
fetched_at: '2026-06-28T22:47:22.310300+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Hierarquia/Posição: Como acessar a rotina de cadastro de Hierarquia'
type: support-article
updated_at: '2026-01-16T21:50:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6301886575511-RH-RM-RHU-Hierarquia-Posi%C3%A7%C3%A3o-Como-acessar-a-rotina-de-cadastro-de-Hierarquia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15869469208471) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como habilitar e configurar a Gestão por hierarquia?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.34 e superiores  
  
**Solução**

Para habilitar a gestão por hierarquia, siga os passos abaixo.

- Parametrizador: Quando estamos configurando a gestão de hierarquia em **Gestão de Pessoas** | **Configuração** | **Parametrizador** | **Gerenciamento de Hierarquia**, o primeiro ponto é marcar a flag "***Habilita Funcionalidade de Hierarquia**”*. Ao marcar este parâmetro será considerada a gestão por hierarquia nas demais rotinas do sistema e será liberado os demais parâmetros para sua configuração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31718672430487)

**Parâmetros Referente ao Funcionário**: Este parâmetro irá controlar em qual cadastro é possível manipular os cadastros abaixo. Quando selecionada a opção por Posição, somente será possível manipula-los dentro do cadastro de posição, se marcado por Funcionário, será liberado no funcionário a manipulação dos dados e se marcado em ambos, em ambos os cadastros é possível manipular os dados abaixo.

* Seção
* Função
* Nível salarial
* Faixa salarial
* Sindicato
* Salário mensal
* Carga horária mensal
* Horário
* Letra

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31718617587607)

**Calendário utilizado no cálculo do ponto**: Como o nome indica, neste parâmetro será selecionado de qual cadastro deve ser utilizado o Calendário do ponto, se é da seção ou da Hierarquia.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31718617592983)

**Habilita uso nas Requisições**: Para habilitar este parâmetro é necessário concluir ou cancelar as requisições em andamento, aprovadas ou suspensa. Isto se deve, pois após marcar este parâmetro será alterado também o comportamento do produto na aprovação de requisição, onde anteriormente era validado os chefes e as suas seções pais, mas após marcar o parâmetro é possível configurar um novo fluxo de atendimento ou usar o padrão, o qual vai buscar as hierarquias e a pessoa responsável por cada nível.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31718617595415)

Após habilitada a rotina, a mesma poderá ser encontrada em Gestão Organizacional | Hierarquia.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37738406576151)

**Importante**

Caso os menus estejam desabilitados, deverão realizar a permissão dos mesmos ao perfil atrelado ao usuário no módulo Serviços Globais | Segurança | Perfis. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37738406577047)

**Saiba mais**  
Para maiores informações, acesse:

- [Ativação da Hierarquia Por Posição](https://tdn.totvs.com/pages/releaseview.action?pageId=653572529)
