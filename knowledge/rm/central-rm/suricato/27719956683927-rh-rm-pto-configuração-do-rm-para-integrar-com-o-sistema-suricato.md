---
article_id: 27719956683927
category: Suricato
content_hash: ea83edd95d754246acb172e6dce34033c4b85e1fdf5d2d8db2ddbd524de31779
fetched_at: '2026-06-28T22:46:26.381173+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Configuração do RM para integrar com o sistema Suricato
type: support-article
updated_at: '2025-03-06T14:29:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27719956683927-RH-RM-PTO-Configura%C3%A7%C3%A3o-do-RM-para-integrar-com-o-sistema-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27719971830551) Tempo aproximado para leitura: **00:10:00 min****Dúvida**

Como configurar o RM para integrar com o sistema Suricato?  
  
  
**Ambiente**

TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1  
  
  
**Solução**

1. Acessar o módulo RM Automação de Ponto | guia Configurações | Parametrizador | Avançar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956618647)

2. Selecionar o Processo 08.01 - Iniciais e avance

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719971834135)

3. Avance até a Etapa 5 - Integração e marque o parâmetro “Utilizar integração com o TSA”

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956622359)

4. Avance até concluir o processo

5. Acesse o módulo Integração | guia Ferramentas | Parâmetros | Avance

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956626711)

6. Selecione o processo 50.01 - Configurações gerais ByYouESB e avance

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719971838231)

7. Nos campos Nº. de tentativas para Envio, Diagrama Síncrono e Diagrama Assíncrono informe o valor padrão 1

8. No campo URL do Webservice informe a URL do Webservice RM. [Clique aqui para informações sobre a instalação do Webservice RM](RH%20-%20RM%20-%20PTO%20-%20Instala%C3%A7%C3%A3o%20e%20configura%C3%A7%C3%A3o%20do%20Webservice%20RM%20para%20integra%C3%A7%C3%A3o%20com%20o%20Suricato)

A URL será composta da seguinte forma:

* Protocolo http ou https de acordo com as configurações do IIS
* IP do Servidor ou o nome do Servidor onde foi instalado o Webservice RM
* Nome do aplicativo/site criado no IIS após a instalação do Webservice RM (nome padrão TSA)
* Arquivo TSService.asmx

Exemplo de URL: http://Localhost/TSA/TSService.asmx

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719971842455)

9. Avance até concluir o processo

E para concluir a configuração do RM, importe as fórmulas visuais referentes a integração com o Suricato

1. Através do TOTVS Compartilhamento (guia Gestão) baixe o arquivo

PTOWKF0002 -Formulas\_Visuais\_Integracao\_RM\_TSA.TotvsWF

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956634263)

2. Na guia Gestão clique em Fórmula Visual | Categorias

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956638231)

3. Crie um novo registro e na aba Perfis da Categoria da Fórmula Visual inclua Perfis dos seguintes sistemas que estejam vinculados ao usuário que irá realizar a importação das fórmulas visuais:

* A - Automação de Ponto
* G - Serviços Globais
* P - Folha de Pagamento
* V - Gestão de Pessoas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956640663)

4. Ainda na guia Gestão clique em Fórmula Visual | Fórmula Visual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956646551)

5. No cadastro de fórmula visual clique em Processos | Importação de Fórmula Visual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956650007)

6. Clique no botão Adicionar Objetos e selecione o arquivo baixado no passo 1 da importação de fórmula visual

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719956651543)

7. Para as fórmulas que possuem gatilhos clique no sinal de mais (+) e marque e selecione a caixa do gatilho. E para todas as fórmulas clique na aba Parâmetros e informe a categoria criada nos passos 2 e 3. Selecione o gatilho e informe a categoria para TODAS a fórmulas visuais, EXCETO para a fórmula HISTÓRICO DE FUNÇÃO. Essa fórmula foi descontinuada e não precisa ser importada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27719971867671)

8. Após marcar os gatilhos e informar a categoria, execute o processo
